from datetime import datetime

from source.schemas.base import Base


class Feedback(Base):
    """
    feedback base
    """

    content: str
    event_id: int


class FeedbackCreate(Base):
    """
    create feedback object
    """

    content: str


class FeedbackRead(Feedback):
    """
    stores all feedback data
    """

    id: int
    created_at: datetime
