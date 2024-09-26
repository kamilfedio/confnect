import asyncio
import io
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    WebSocket,
    WebSocketDisconnect,
    status,
    Response,
)
from fastapi.responses import StreamingResponse
from fastapi.websockets import WebSocketState
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.question import QuestionRead
from source.utils.connection_manager import (
    check_event_code,
    check_if_event_is_ongoing,
    receive_message,
    send_message,
)
from source.models.feedback import Feedback
from source.schemas.feedback import FeedbackRead, FeedbackCreate
from source.database import get_async_session
from source.models.user import User
from source.models.invitation_code import InvitationCode
from source.schemas.event import EventRead, EventUpdate, EventCreate, EventChangeStatus
from source.dependencies.depends import pagination, get_current_user
import source.crud.events as event_crud
import source.crud.invitation_codes as codes_crud
import source.crud.questions as questions_crud
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
    """
        returns all user events
    Args:
        user (User, optional): current user. Defaults to Depends(get_current_user).
        pagination (tuple[int, int], optional): pagination - offset&limit. Defaults to Depends(pagination).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        Sequence[EventRead]: list of events objects
    """
    return await event_crud.get_all(user.id, pagination, session)


@router.get("/{id}", response_model=EventRead)
async def get_event_by_id(
    id: int, session: AsyncSession = Depends(get_async_session)
) -> EventRead:
    """
        returns event object by id
    Args:
        id (int): event id
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if event doesn't exists

    Returns:
        EventRead: event data object
    """
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
    """
        create event
    Args:
        event (EventCreate): event object
        user (User, optional): current user. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        EventRead: event data object
    """
    new_event = Event(**event.model_dump(), user_id=user.id)
    return await event_crud.create(new_event, session)


@router.patch("/{id}", response_model=EventRead)
async def update_event(
    id: int,
    event: EventUpdate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> EventRead:
    """
        update event data
    Args:
        id (int): event id
        event (EventUpdate): event data object
        user (User, optional): current user. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if event doesn't exists

    Returns:
        EventRead: event data object
    """
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
    """
        delete event by id
    Args:
        id (int): event id
        user (User, optional): current id. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        Response: status code
    """
    await event_crud.delete(id, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/{id}/invite")
async def generate_invitation_codes(
    id: int,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> str:
    """
        return invitation code
    Args:
        id (int): event id
        user (User, optional): current user. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if event doesn't exists

    Returns:
        str: invitation code
    """
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
    """
        returns qr code
    Args:
        code (str): code
        user (User, optional): current user. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        _type_: streming response with qr code image
    """
    qr_code: io.BytesIO = await create_qr_code(code, session)

    return StreamingResponse(qr_code, media_type="image/png")


@router.get("/join/{code}", response_model=EventRead)
async def join_event(
    code: str, session: AsyncSession = Depends(get_async_session)
) -> Response:
    """
        join event by invitation code
    Args:
        code (str): code
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if code doesn't exists

    Returns:
        Response: event data object
    """
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
) -> Sequence[FeedbackRead]:
    """
        get all user events
    Args:
        user (User, optional): current user. Defaults to Depends(get_current_user).
        pagination (tuple[int, int], optional): paginatino - offset&limit. Defaults to Depends(pagination).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        Sequence[FeedbackRead]: list of feedbacks data object
    """
    return await feedback_crud.get_all_user(user.id, pagination, session)


@router.get("/{event_id}/feedback", response_model=list[FeedbackRead])
async def get_event_feedbacks(
    event_id: int,
    pagination: tuple[int, int] = Depends(pagination),
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[FeedbackRead]:
    """
        return all event feedbacks
    Args:
        event_id (int): event id
        pagination (tuple[int, int], optional): pagination - offset&limit. Defaults to Depends(pagination).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        Sequence[FeedbackRead]: list of feedbacks data object
    """
    return await feedback_crud.get_all(event_id, pagination, session)


@router.get("/feedback/{id}", response_model=FeedbackRead)
async def get_feedback_by_id(
    id: int, session: AsyncSession = Depends(get_async_session)
) -> FeedbackRead:
    """
        get feedback by id
    Args:
        id (int): feedback id
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if feedback doesn't exists

    Returns:
        FeedbackRead: feedback data object
    """
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
    """
        create feedback
    Args:
        event_id (int): event id
        feedback (FeedbackCreate): feedback object data
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        FeedbackRead: feedback data object
    """
    feedback = FeedbackRead(**feedback.model_dump(), event_id=event_id)
    return await feedback_crud.create(feedback, session)


@router.delete("/feedback/{id}")
async def delete_feedback_by_id(
    id: int,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    """
        delete feedback by id
    Args:
        id (int): feedback id
        user (User, optional): current user. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        Response: status code
    """
    await feedback_crud.delete_by_id(id, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{event_id}/status", response_model=EventRead)
async def update_event_status(
    event_id: int,
    event_status: EventChangeStatus,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> EventRead:
    """
    change status of the event
    Args:
        event_id (int): event id
        event_status (EventChangeStatus): event new status
        user (User, optional): current user. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        EventRead: _description_
    """
    new_event = event_status.model_dump()
    event: Event | None = await event_crud.get_by_id(event_id, session)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    event.status = new_event["status"]

    return await event_crud.update(event, session)


@router.get("/{event_id}/questions", response_model=list[QuestionRead])
async def get_event_question(
    event_id: int, session: AsyncSession = Depends(get_async_session)
) -> Sequence[QuestionRead]:
    """
    get event questions
    Args:
        event_id (int): event id
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        QuestionRead: question data object
    """
    return await questions_crud.get_by_event(event_id, session)


@router.websocket("/{event_id}/questions")
async def websocket_endpoint(
    websocket: WebSocket,
    event_id: int,
    session=Depends(get_async_session),
):
    """
    websocket endpoint to manage live questions
    Args:
        websocket (WebSocket): websocket connection
        event_id (int): event id
        session (_type_, optional): current session. Defaults to Depends(get_async_session).
    """
    code: str = websocket.query_params.get("code")
    if not await check_event_code(code=code, event_id=event_id, session=session):
        await websocket.close(code=1008)
        return
    if not await check_if_event_is_ongoing(event_id=event_id, session=session):
        await websocket.close(code=1008)
        return

    await websocket.accept()
    try:
        while True:
            receive_task = asyncio.create_task(
                receive_message(websocket, event_id)
            )
            send_task = asyncio.create_task(send_message(websocket, event_id, session))
            done, pending = await asyncio.wait(
                {receive_task, send_task},
                return_when=asyncio.FIRST_COMPLETED,
            )
            for task in pending:
                task.cancel()

            for task in done:
                try:
                    task.result()
                except WebSocketDisconnect:
                    for task in pending:
                        task.cancel()
                    return

    except WebSocketDisconnect:
        pass
    finally:
        if websocket.client_state == WebSocketState.CONNECTED:
            await websocket.close()
