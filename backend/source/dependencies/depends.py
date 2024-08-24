from fastapi import Depends, Query, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from source.database import get_async_session
from source.schemas.user import UserRead
from source.utils.authenticate import auth
from source.crud.user import user_crud


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

class Dependencies:
    def pagination(self, skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> tuple[int, int]:
        capped_limit = min(100, limit)
        return skip, capped_limit
    
    async def get_current_user(self, token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_async_session)) -> UserRead:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
            )
        payload = await auth.encode_access_token(token)
        if not payload:
            raise credentials_exception
        
        user: UserRead | None = await user_crud.get_by_id(payload.get("user_id"), session)
        if not user:
            raise credentials_exception
        
        return user

dependencies = Dependencies()
