from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.form import FormRead, FormCreate
from source.database import get_async_session
from source.dependencies.depends import dependencies
from source.crud.forms import crud
router = APIRouter()

@router.get('/', response_model=list[FormRead])
async def get_all_forms(pagination: tuple[int, int] = Depends(dependencies.pagination), session: AsyncSession = Depends(get_async_session)) -> Sequence[FormRead]:
    res = await crud.get_all(pagination, session)
    return res

@router.post('/', response_model=FormRead)
async def create_form(model: FormCreate, session: AsyncSession = Depends(get_async_session)) -> FormRead:
    res = await crud.create(model, session)
    return res

@router.get('/{id}', response_model=FormRead)
async def get_form_by_id(id: int, session: AsyncSession = Depends(get_async_session)) -> FormRead:
    res = await crud.get_by_id(id, session)
    if res is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Form not found')
    
    return res