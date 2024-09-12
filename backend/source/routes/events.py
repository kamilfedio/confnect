import io
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import StreamingResponse
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.feedback import Feedback
from source.schemas.feedback import FeedbackRead, FeedbackCreate
from source.database import get_async_session
from source.models.user import User
from source.models.invitation_code import InvitationCode
from source.schemas.event import EventRead, EventUpdate, EventCreate
from source.dependencies.depends import pagination, get_current_user
import source.crud.events as event_crud
import source.crud.invitation_codes as codes_crud
import source.crud.feedback as feedback_crud
from source.models.event import Event
from source.utils.codes import create_codes, create_qr_code

router = APIRouter()


@router.get("/", response_model=list[EventRead])
async def get_all_user_events(
    user: User = Depends(get_current_user),
    pagination: tuple[int, int] = Depends(pagination),
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
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> EventRead:
    new_event = Event(**event.model_dump(), user_id=user.id)
    return await event_crud.create(new_event, session)


@router.patch("/{id}", response_model=EventRead)
async def update_event(
    id: int,
    event: EventUpdate,
    user: User = Depends(get_current_user),
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


@router.delete("/{id}")
async def delete_event(
    id: int,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    await event_crud.delete(id, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/{id}/invite")
async def generate_invitation_codes(
    id: int,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> str:
    event = await event_crud.get_by_id(id, session)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )

    code: str = await create_codes(event.id, session)

    return code


@router.get("/generate_qr/{code}")
async def get_qr_image(
    code: str,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    qr_code: io.BytesIO = await create_qr_code(code, session)

    return StreamingResponse(qr_code, media_type="image/png")


@router.get("/join/{code}", response_model=EventRead)
async def join_event(
    code: str, session: AsyncSession = Depends(get_async_session)
) -> Response:
    invitation_code: InvitationCode | None = await codes_crud.get_by_code(code, session)
    if not invitation_code:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Code not found"
        )

    event: Event = invitation_code.event
    return event


@router.get("/feedback", response_model=list[FeedbackRead])
async def get_user_feedbacks(
    user: User = Depends(get_current_user),
    pagination: tuple[int, int] = Depends(pagination),
    session: AsyncSession = Depends(get_async_session),
) -> list[FeedbackRead]:
    return await feedback_crud.get_all(user.id, pagination, session)


@router.get("/{event_id}/feedback", response_model=list[FeedbackRead])
async def get_event_feedbacks(
    event_id: int,
    pagination: tuple[int, int] = Depends(pagination),
    session: AsyncSession = Depends(get_async_session),
) -> list[FeedbackRead]:
    return await feedback_crud.get_all(event_id, pagination, session)


@router.get("/feedback/{id}", response_model=FeedbackRead)
async def get_feedback_by_id(
    id: int, session: AsyncSession = Depends(get_async_session)
) -> FeedbackRead:
    feedback: Feedback | None = await feedback_crud.get_by_id(id, session)
    if not feedback:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feedback not found"
        )

    return feedback


@router.post("/{event_id}/feedback", response_model=FeedbackRead)
async def create_feedback(
    event_id: int,
    feedback: FeedbackCreate,
    session: AsyncSession = Depends(get_async_session),
) -> FeedbackRead:
    feedback = FeedbackRead(**feedback.model_dump(), event_id=event_id)
    return await feedback_crud.create(feedback, session)


@router.delete("/feedback/{id}")
async def delete_feedback_by_id(
    id: int,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    await feedback_crud.delete_by_id(id, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
