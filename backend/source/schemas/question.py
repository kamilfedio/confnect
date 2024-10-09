from source.schemas.base import Base
from pydantic import Field
from datetime import datetime


class Question(Base):
    """
    Question schema
    """

    code: str
    content: str
    created_at: datetime = Field(default_factory=datetime.now)

    def model_dump_iso(self) -> dict:
        """
        conver model to json
        """
        return {
            "code": self.code,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
        }


class QuestionRead(Question):
    """
    question read schema
    """

    id: int
    event_id: int

    def model_dump_iso(self) -> dict:
        """
        conver model to json
        """
        return {
            "id": self.id,
            "event_id": self.event_id,
            "code": self.code,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
        }
