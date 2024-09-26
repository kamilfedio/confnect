import json
from broadcaster import Broadcast
from fastapi import WebSocket
from pydantic_core import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.websockets import WebSocketState

from source.config.env_config import redis_config
from source.schemas.question import Question
from source.models.invitation_code import InvitationCode
import source.crud.invitation_codes as codes_crud

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


async def receive_message(websocket: WebSocket, event_id: int) -> None:
    """
    Receive message from the broadcast channel and send it to the websocket
    Args:
        websocket (WebSocket): websocket
        event_id (int): event id
    """
    async with broadcast.subscribe(channel=str(event_id)) as subscriber:
        async for event in subscriber:
            try:
                data_dict = json.loads(event.message)
                question_msg: Question = Question(**data_dict)

                await websocket.send_json(question_msg.model_dump())
            except json.JSONDecodeError as e:
                await websocket.send_json({"error": "Invalid json format"})
            except ValidationError as e:
                await websocket.send_json(
                    {"error": "validation error", "details": str(e)}
                )
            except Exception as e:
                await websocket.send_json(
                    {"error": "Unexcepted error", "details": str(e)}
                )


async def send_message(websocket: WebSocket, event_id: int) -> None:
    """
    Send message to the broadcast channel
    Args:
        websocket (WebSocket): websocket
        event_id (int): event_id
    """
    try:
        if websocket.application_state != WebSocketState.CONNECTED:
            await websocket.send_json({"error": "Websocket is not connected"})
        data = await websocket.receive_text()
        data_dict = json.loads(data)
        question: Question = Question.model_validate_strings(data_dict)
        await broadcast.publish(
            channel=str(event_id), message=question.model_dump_json()
        )

    except json.JSONDecodeError as e:
        await websocket.send_json({"error": "Invalid json format"})
    except ValidationError as e:
        await websocket.send_json({"error": "validation error", "details": str(e)})
    except Exception as e:
        await websocket.send_json({"error": "Unexcepted error", "details": str(e)})
