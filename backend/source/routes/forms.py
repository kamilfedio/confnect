from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.form import FormRead, FormCreate
from source.database import get_async_session
from source.dependencies.depends import pagination
import source.crud.forms as forms_crud

router = APIRouter()


@router.get("/", response_model=list[FormRead])
async def get_all_forms(
    pagination: tuple[int, int] = Depends(pagination),
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[FormRead]:
    """
        get all forms
    Args:
        pagination (tuple[int, int], optional): pagination - limit&offset. Defaults to Depends(pagination).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        Sequence[FormRead]: list of forms objects
    """
    res = await forms_crud.get_all(pagination, session)
    return res


@router.post("/", response_model=FormRead)
async def create_form(
    model: FormCreate, session: AsyncSession = Depends(get_async_session)
) -> FormRead:
    """
        create form
    Args:
        model (FormCreate): form data object
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        FormRead: form data object
    """
    res = await forms_crud.create(model, session)
    return res


@router.get("/{id}", response_model=FormRead)
async def get_form_by_id(
    id: int, session: AsyncSession = Depends(get_async_session)
) -> FormRead:
    """
        returns form by given id
    Args:
        id (int): form id
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if form doesn't exists

    Returns:
        FormRead: form data object
    """
    res = await forms_crud.get_by_id(id, session)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Form not found"
        )

    return res
