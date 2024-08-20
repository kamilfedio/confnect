from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from source.database import get_async_session
from backend.source.schemas.user import UserCreate, UserRead
from backend.source.crud.user import user_crud

router = APIRouter()

@router.get('/{id}')
async def get_user_by_id(id: int):
    pass

@router.post('/', response_model=UserRead)
async def create_user(model: UserCreate, session: AsyncSession = Depends(get_async_session)) -> UserRead:
    pass