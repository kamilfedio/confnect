from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import DateTime, String, Integer, func, ForeignKey
from datetime import datetime

from source.models.base import Base


class Question(Base):
    """
    question database schema
    """

    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    event_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("events.id"), nullable=False
    )
    code: Mapped[str] = mapped_column(String(9), nullable=False)
    content: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )

    event: Mapped["Event"] = relationship("Event", lazy="selectin")
