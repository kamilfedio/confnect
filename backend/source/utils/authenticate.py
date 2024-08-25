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
from source.models.token import Tokens
from source.utils.enums import TokenType

class Authenticate:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)
    
    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.pwd_context.hash(password)
    
    @classmethod
    async def authenticate_user(cls, email: str, password: str, session: AsyncSession) -> UserRead | bool:
        user: User | None = await user_crud.get_by_email(email, session)
        if not user:
            return False
        if not cls.verify_password(password, user.hashed_password):
            return False
        
        return user
    
    @classmethod
    async def create_token(cls, user_id: int,  session: AsyncSession, type: str = TokenType.ACCESS) -> str:
        match type:
            case TokenType.ACCESS:
                expirates = secret_config.ACCESS_TOKEN_EXPIRE_MINUTES
            case TokenType.REFRESH:
                expirates = secret_config.REFRESH_TOKEN_EXPIRE_MINUTES
            case _:  
                raise ValueError('Invalid token type')
        expire = datetime.now() + timedelta(minutes=expirates)
        token_data = secrets.token_urlsafe(32)
        token = Tokens(token=token_data, user_id=user_id, type=type, expiration_date=expire)
        await tokens_crud.create(token, session)
        
        return token_data
    
    @staticmethod
    async def get_token(token: str, session: AsyncSession, token_type: TokenType = TokenType.ACCESS) -> Tokens | None:
        return await tokens_crud.get_by_id(id=token, session=session, token_type=token_type)

    @classmethod
    async def verify_refresh_token(cls, token: str, session: AsyncSession) -> bool:
        new_token: Tokens | None = await cls.get_token(token, session, token_type=TokenType.REFRESH)
        if new_token is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        
        return True
    

auth = Authenticate()
