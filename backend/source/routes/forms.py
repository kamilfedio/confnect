from fastapi import APIRouter, Depends
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.form import FormRead, FormCreate
from source.database import get_async_session
from source.dependencies.depends import Dependencies
from source.crud.forms import FormsCrud

Dependencies = Dependencies()
router = APIRouter()
crud = FormsCrud()

@router.get('/', response_model=list[FormRead])
async def get_all_forms(pagination: tuple[int, int] = Depends(Dependencies.pagination), session: AsyncSession = Depends(get_async_session)) -> Sequence[FormRead]:
    res = await crud.get_all(pagination, session)
    return res

@router.post('/', response_model=FormRead)
async def create_form(model: FormCreate, session: AsyncSession = Depends(get_async_session)) -> FormRead:
    res = await crud.create(model, session)
    return res
