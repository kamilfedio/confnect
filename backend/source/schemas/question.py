from source.schemas.base import Base
from pydantic import Field
from datetime import datetime


class Question(Base):
    """
    Question schema
    """

    event_id: int
    invitation_code: str
    content: str
    created_at: datetime = Field(default_factory=datetime.now)

    def model_dump(self) -> dict:
        """
        conver model to json
        """
        return {
            "event_id": self.event_id,
            "invitation_code": self.invitation_code,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
        }
