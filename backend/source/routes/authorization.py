from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc

from source.models.token import Tokens
from source.database import get_async_session
from source.schemas.user import UserRead, UserCreate
from source.utils.authenticate import auth
from source.models.user import User
from source.crud.user import user_crud
from source.utils.enums import TokenType


router = APIRouter()

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def register(user_create: UserCreate, session: AsyncSession = Depends(get_async_session)) -> User:
    hashed_pass = auth.get_password_hash(user_create.password)

    user = User(**user_create.model_dump(exclude={'password'}), hashed_password=hashed_pass)
    try:
        await user_crud.create(user, session)
    except exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists')
    
    user = UserRead.model_validate(user)
    return user

@router.post('/token')
async def create_token(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    session: AsyncSession = Depends(get_async_session)
) -> dict[str, str]:
    user: UserRead | bool = await auth.authenticate_user(form_data.username, form_data.password, session)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect email or password')

    access_token: str = await auth.create_token(user.id, type=TokenType.ACCESS, session=session)
    refresh_token: str = await auth.create_token(user.id, type=TokenType.REFRESH, session=session)

    return {'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'}

@router.post('/refresh')
async def refresh_token(refresh_token: str, session: AsyncSession = Depends(get_async_session)) -> dict[str, str]:
    if not await auth.verify_refresh_token(refresh_token, session):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid refresh token')
    
    token: Tokens | None = await auth.get_token(refresh_token, session, token_type=TokenType.REFRESH)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid refresh token')
    
    access_token: str = await auth.create_token(token.user_id, type=TokenType.ACCESS, session=session)

    return {'access_token': access_token, 'token_type': 'bearer'}
