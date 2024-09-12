from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc

from source.models.token import Token
from source.database import get_async_session
from source.schemas.user import UserRead, UserCreate
from source.utils.authenticate import (
    get_password_hash,
    create_token,
    authenticate_user,
    verify_refresh_token,
    get_token,
)
from source.models.user import User
import source.crud.user as user_crud
from source.utils.enums import TokenType


router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_create: UserCreate, session: AsyncSession = Depends(get_async_session)
) -> dict[str, str]:
    """
        register user in db
    Args:
        user_create (UserCreate): user data object
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if user already exists

    Returns:
        dict[str, str]: refresh and access tokens
    """
    hashed_pass = get_password_hash(user_create.password)

    user = User(
        **user_create.model_dump(exclude={"password"}), hashed_password=hashed_pass
    )
    try:
        await user_crud.create(user, session)
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )

    access_token: str = await create_token(
        user.id, type=TokenType.ACCESS, session=session
    )
    refresh_token: str = await create_token(
        user.id, type=TokenType.REFRESH, session=session
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    session: AsyncSession = Depends(get_async_session),
) -> dict[str, str]:
    """
        create access token
    Args:
        form_data (OAuth2PasswordRequestForm, optional): login form data. Defaults to Depends(OAuth2PasswordRequestForm).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if incorrected data

    Returns:
        dict[str, str]: refresh and access tokens
    """
    user: UserRead | bool = await authenticate_user(
        form_data.username, form_data.password, session
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token: str = await create_token(
        user.id, type=TokenType.ACCESS, session=session
    )
    refresh_token: str = await create_token(
        user.id, type=TokenType.REFRESH, session=session
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/refresh")
async def refresh_token(
    refresh_token: str, session: AsyncSession = Depends(get_async_session)
) -> dict[str, str]:
    """
        refresh access token
    Args:
        refresh_token (str): refresh token
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if invalid refresh token

    Returns:
        dict[str, str]: access token
    """
    if not await verify_refresh_token(refresh_token, session):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
        )

    token: Token | None = await get_token(
        refresh_token, session, token_type=TokenType.REFRESH
    )
    access_token: str = await create_token(
        token.user_id, type=TokenType.ACCESS, session=session
    )

    return {"access_token": access_token, "token_type": "bearer"}
