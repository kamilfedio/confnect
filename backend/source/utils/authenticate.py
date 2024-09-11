from fastapi import HTTPException
from passlib.context import CryptContext
import secrets
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.user import User
from source.schemas.user import UserRead
from source.config.secret import secret_config
from source.crud.user import user_crud
from source.crud.tokens import tokens_crud
from source.models.token import Token
from source.utils.enums import TokenType

pwd_context = CryptContext(schemes=[secret_config.ALGORITHM], deprecated="auto")

@classmethod
def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
    return cls.pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def authenticate_user(email: str, password: str, session: AsyncSession) -> UserRead | bool:
    user: User | None = await user_crud.get_by_email(email, session)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    
    return user

async def create_token(user_id: int,  session: AsyncSession, type: str = TokenType.ACCESS) -> str:
    async def _disable_old_access_token(user_id: int, session: AsyncSession) -> None:
        available_access_tokens: list[Token] = await tokens_crud.get_user_tokens_by_id(user_id, TokenType.ACCESS, session)
        for token in available_access_tokens:
            await tokens_crud.disable_token(token.token, session)

    match type:
        case TokenType.ACCESS:
            expirates = secret_config.ACCESS_TOKEN_EXPIRE_MINUTES
            await _disable_old_access_token(user_id, session)
        case TokenType.REFRESH:
            expirates = secret_config.REFRESH_TOKEN_EXPIRE_MINUTES
        case _:  
            raise ValueError('Invalid token type')
    expire = datetime.now() + timedelta(minutes=expirates)
    token_data = secrets.token_urlsafe(32)
    token = Token(token=token_data, user_id=user_id, type=type, expiration_date=expire)
    await tokens_crud.create(token, session)
    
    return token_data

async def get_token(token: str, session: AsyncSession, token_type: TokenType = TokenType.ACCESS) -> Token | None:
    return await tokens_crud.get_by_id(id=token, session=session, token_type=token_type)

async def verify_refresh_token(token: str, session: AsyncSession) -> bool:
    new_token: Token | None = await get_token(token, session, token_type=TokenType.REFRESH)
    if new_token is None:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    if new_token.expirated:
        raise HTTPException(status_code=401, detail="Refresh token expired")
    
    return True
    