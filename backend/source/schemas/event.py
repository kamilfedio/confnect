from datetime import datetime
from source.schemas.base import BaseSchema

class Event(BaseSchema):
    name: str
    description: str
    place: str
    date: datetime
    optional_info: str
    user_id: int

class EventCreate(Event):
    pass

class EventRead(Event):
    id: int
    created_at: datetime
    updated_at: datetime | None