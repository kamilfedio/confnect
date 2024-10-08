import json
from broadcaster import Broadcast
from fastapi import WebSocket
from pydantic_core import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.websockets import WebSocketState

from source.config.env_config import redis_config
from source.schemas.question import Question, QuestionRead
from source.models.questions import Question as QuestionModel
from source.models.invitation_code import InvitationCode
import source.crud.invitation_codes as codes_crud
import source.crud.events as events_crud
from source.models.event import Event
import source.crud.questions as questions_crud
from source.utils.enums import EventStatus

broadcast = Broadcast(redis_config.REDIS_URL)


async def check_event_code(code: str, event_id: int, session: AsyncSession) -> bool:
    """
    check if the code is valid for the event
    Args:
        code (str): invitation code
        event_id (int): event id
        session (AsyncSession): current session

    Returns:
        bool: if is valid or not
    """
    code: InvitationCode | None = await codes_crud.get_by_code(code, session)
    if not code:
        return False
    if not code.event_id == event_id:
        return False
    return True


async def check_if_event_is_ongoing(event_id: int, session: AsyncSession) -> bool:
    """
    check if event status is ongoing
    Args:
        event_id (int): event id
        session (AsyncSession): current session

    Returns:
        bool: if is ongoing or not
    """

    event: Event = await events_crud.get_by_id(event_id, session)
    return event.status == EventStatus.ONGOING


async def send_message(
    websocket: WebSocket, event_id: int, session: AsyncSession
) -> None:
    """
    Send message to the broadcast channel and return the saved QuestionRead object
    Args:
        websocket (WebSocket): websocket
        event_id (int): event_id
        session (AsyncSession): current session
    """
    try:
        if websocket.application_state != WebSocketState.CONNECTED:
            await websocket.send_json({"error": "Websocket is not connected"})
            return

        data = await websocket.receive_text()
        data_dict = json.loads(data)

        question: Question = Question(**data_dict)

        question_model: QuestionModel = QuestionModel(
            **question.model_dump(), event_id=event_id
        )

        saved_question: QuestionModel = await questions_crud.create(
            question_model, session
        )

        question_response: QuestionRead = QuestionRead.model_validate(saved_question)

        await broadcast.publish(
            channel=str(event_id), message=question_response.model_dump_json()
        )

        await websocket.send_json(question_response.model_dump_iso())

    except json.JSONDecodeError:
        await websocket.send_json({"error": "Invalid json format"})
    except ValidationError as e:
        await websocket.send_json({"error": "Validation error", "details": str(e)})
    except Exception as e:
        await websocket.send_json({"error": "Unexpected error", "details": str(e)})


async def receive_message(websocket: WebSocket, event_id: int) -> None:
    """
    Receive message from the broadcast channel and send it to the websocket.
    Args:
        websocket (WebSocket): websocket
        event_id (int): event id
        session (AsyncSession): current session
    """
    async with broadcast.subscribe(channel=str(event_id)) as subscriber:
        async for event in subscriber:
            try:
                data_dict = json.loads(event.message)

                question_response: QuestionRead = QuestionRead(**data_dict)

                await websocket.send_json(question_response.model_dump_iso())

            except json.JSONDecodeError:
                await websocket.send_json({"error": "Invalid json format"})
            except ValidationError as e:
                await websocket.send_json(
                    {"error": "Validation error", "details": str(e)}
                )
            except Exception as e:
                await websocket.send_json(
                    {"error": "Unexpected error", "details": str(e)}
                )
