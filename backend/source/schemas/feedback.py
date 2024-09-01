from datetime import datetime

from source.schemas.base import Base

class Feedback(Base):
    content: str
    event_id: int

class FeedbackCreate(Base):
    content: str

class FeedbackRead(Feedback):
    id: int
    created_at: datetime