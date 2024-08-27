from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from source.database import get_async_session
from source.models.user import User
from source.schemas.event import EventRead, EventUpdate, EventCreate
from source.dependencies.depends import dependencies
from source.crud.events import event_crud
from source.models.event import Event


router = APIRouter()


@router.get("/", response_model=list[EventRead])
async def get_all_user_events(
    user: User = Depends(dependencies.get_current_user),
    pagination: tuple[int, int] = Depends(dependencies.pagination),
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[EventRead]:
    return await event_crud.get_all(user.id, pagination, session)


@router.get("/{id}", response_model=EventRead)
async def get_event_by_id(
    id: int, session: AsyncSession = Depends(get_async_session)
) -> EventRead:
    event = await event_crud.get_by_id(id, session)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )

    return event


@router.post("/", response_model=EventRead)
async def create_event(
    event: EventCreate,
    user: User = Depends(dependencies.get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> EventRead:
    new_event = Event(**event.model_dump(), user_id=user.id)
    return await event_crud.create(new_event, session)


@router.patch("/{id}", response_model=EventRead)
async def update_event(
    id: int,
    event: EventUpdate,
    user: User = Depends(dependencies.get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> EventRead:
    new_event = event.model_dump(exclude_unset=True)
    event: Event | None = await event_crud.get_by_id(id, session)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    
    for field, value in new_event.items():
        setattr(event, field, value)

    return await event_crud.update(event, session)

@router.delete('/{id}')
async def delete_event(
    id: int,
    user: User = Depends(dependencies.get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    await event_crud.delete(id, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
