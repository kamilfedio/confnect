from datetime import datetime
from source.schemas.base import Base

class Event(Base):
    name: str
    description: str
    place: str
    date: datetime | None
    optional_info: str | None

class EventCreate(Event):
    pass

class EventUpdate(Base):
    name: str | None = None
    description: str | None = None
    place: str | None = None
    date: datetime | None = None
    optional_info: str | None = None

class EventRead(Event):
    user_id: int
    id: int
    created_at: datetime
    updated_at: datetime | None