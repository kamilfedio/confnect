from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime, Text, String, Integer, func
from datetime import datetime

from source.models.base import Base

class Form(Base):

    __tablename__ = 'forms'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    