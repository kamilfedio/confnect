from fastapi import HTTPException
from passlib.context import CryptContext
import secrets
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.user import User
from source.schemas.user import UserRead
from source.config.secret import secret_config
import source.crud.user as user_crud
import source.crud.tokens as tokens_crud
from source.models.token import Token
from source.utils.enums import TokenType

pwd_context = CryptContext(schemes=[secret_config.ALGORITHM], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
        verify given password with hashed password
    Args:
        plain_password (str): user input password
        hashed_password (str): user hashed db password

    Returns:
        bool: if plain and hashed are equal
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
        hash given password
    Args:
        password (str): user input password

    Returns:
        str: hashed password
    """
    return pwd_context.hash(password)


async def authenticate_user(
    email: str, password: str, session: AsyncSession
) -> UserRead | bool:
    """
        check if user is in db and if password is correct
    Args:
        email (str): user email
        password (str): user password
        session (AsyncSession): async session

    Returns:
        UserRead | bool: return user if data is correct or False if not
    """
    user: User | None = await user_crud.get_by_email(email, session)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user


async def create_token(
    user_id: int, session: AsyncSession, type: str = TokenType.ACCESS
) -> str:
    """
        create user access or refresh token and save in database
    Args:
        user_id (int): user id
        session (AsyncSession): async session
        type (str, optional): token type. Defaults to TokenType.ACCESS.

    Returns:
        str: token data
    """

    async def _disable_old_access_token(user_id: int, session: AsyncSession) -> None:
        """
            disable each active access token for user
        Args:
            user_id (int): user id
            session (AsyncSession): async session
        """
        available_access_tokens: list[Token] = await tokens_crud.get_user_tokens_by_id(
            user_id, TokenType.ACCESS, session
        )
        for token in available_access_tokens:
            await tokens_crud.disable_token(token.token, session)

    match type:
        case TokenType.ACCESS:
            expirates: int = secret_config.ACCESS_TOKEN_EXPIRE_MINUTES
            await _disable_old_access_token(user_id, session)
        case TokenType.REFRESH:
            expirates: int = secret_config.REFRESH_TOKEN_EXPIRE_MINUTES
        case TokenType.RESET_PASSWORD:
            expirates: int = secret_config.RESET_PASSWORD_EXPIRE_MINUTES
        case _:
            raise ValueError("Invalid token type")

    expire = datetime.now() + timedelta(minutes=expirates)
    token_data = secrets.token_urlsafe(32)
    token = Token(token=token_data, user_id=user_id, type=type, expiration_date=expire)
    await tokens_crud.create(token, session)

    return token_data


async def get_token(
    token: str, session: AsyncSession, token_type: TokenType = TokenType.ACCESS
) -> Token | None:
    """
        search in database for token by id
    Args:
        token (str): token string
        session (AsyncSession): async session
        token_type (TokenType, optional): token type. Defaults to TokenType.ACCESS.

    Returns:
        Token | None: token data or None
    """
    return await tokens_crud.get_by_id(token_id=token, session=session, token_type=token_type)


async def verify_refresh_token(token: str, session: AsyncSession) -> bool:
    """
        verify if given refresh token exists and is valid
    Args:
        token (str): token
        session (AsyncSession): async session

    Raises:
        HTTPException: if token doens't exists
        HTTPException: if refresh token is expired

    Returns:
        bool: if is valid
    """
    new_token: Token | None = await get_token(
        token, session, token_type=TokenType.REFRESH
    )
    if new_token is None:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    if new_token.expirated:
        raise HTTPException(status_code=401, detail="Refresh token expired")

    return True
