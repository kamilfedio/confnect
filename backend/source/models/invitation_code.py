from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import DateTime, String, Integer, func
from datetime import datetime

from source.models.base import Base

class InvitationCode(Base):

    __tablename__ = 'invitation_codes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    event_id: Mapped[int] = mapped_column(Integer, nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    code: Mapped[str] = mapped_column(String(9), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    event: Mapped['Event'] = relationship('Event', back_populates='invitation_codes')
