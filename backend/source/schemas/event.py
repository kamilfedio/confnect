from datetime import datetime

from pydantic import Field
from source.schemas.base import Base
from source.schemas.feedback import FeedbackRead
from source.utils.enums import EventStatus


class Event(Base):
    """
    event object base
    """

    name: str
    description: str
    place: str
    status: EventStatus = Field(default=EventStatus.INCOMING)
    date: datetime | None
    optional_info: str | None


class EventCreate(Event):
    """
    create form object
    """

    pass

class EventChangeStatus(Base):
    """
    change event status object
    """

    status: EventStatus

class EventUpdate(Base):
    """
    update event data object
    """

    name: str | None = None
    description: str | None = None
    place: str | None = None
    date: datetime | None = None
    status: EventStatus | None = None
    optional_info: str | None = None


class EventRead(Event):
    """
    stores shortcut data object
    """

    user_id: int
    id: int
    status: EventStatus
    created_at: datetime
    updated_at: datetime | None


class EventReadFull(EventRead):
    """
    stores all data object
    """

    feedbacks: list[FeedbackRead]
