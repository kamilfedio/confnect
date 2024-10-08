from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, ForeignKey, Text, DateTime, func, Enum
from datetime import datetime

from source.models.base import Base
from source.models.feedback import Feedback
from source.utils.enums import EventStatus


class Event(Base):
    """
    event database schema
    """

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    place: Mapped[str] = mapped_column(String(255), nullable=False)
    optional_info: Mapped[str | None] = mapped_column(String(255), nullable=True)
    status: Mapped[EventStatus] = mapped_column(
        Enum(EventStatus), nullable=False, default=EventStatus.INCOMING
    )
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, onupdate=func.now())

    feedbacks: Mapped[list["Feedback"]] = relationship(
        "Feedback", back_populates="event", lazy="selectin"
    )
