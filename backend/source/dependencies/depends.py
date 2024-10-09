from fastapi import Depends, Query, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.token import Token
from source.models.user import User
from source.database import get_async_session
from source.utils.authenticate import get_token


def pagination(
    skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)
) -> tuple[int, int]:
    """
        count pagination
    Args:
        skip (int, optional): skip. Defaults to Query(0, ge=0).
        limit (int, optional): skip. Defaults to Query(10, ge=0).

    Returns:
        tuple[int, int]: skip, offset tuple
    """
    capped_limit = min(100, limit)
    return skip, capped_limit


async def get_current_user(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/login")),
    session: AsyncSession = Depends(get_async_session),
) -> User:
    """
    return current user by access token
    Args:
        token (str, optional): access token. Defaults to Depends(OAuth2PasswordBearer(tokenUrl="/login")).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if invalid token

    Returns:
        User: current user
    """

    access_token: Token | None = await get_token(token, session)
    if access_token is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return access_token.user
