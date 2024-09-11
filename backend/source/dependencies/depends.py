from fastapi import Depends, Query, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.token import Token
from source.models.user import User
from source.database import get_async_session
from source.utils.authenticate import get_token



def pagination(self, skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return skip, capped_limit

async def get_current_user(
        self,
        token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/token")),
        session: AsyncSession = Depends(get_async_session),
) -> User:
    print(token)
    access_token: Token | None = await get_token(token, session)
    if access_token is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    return access_token.user
