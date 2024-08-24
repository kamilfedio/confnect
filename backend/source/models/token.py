from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Enum, Text, DateTime, func, Integer, ForeignKey
from datetime import datetime
from source.models.base import Base
from source.utils.enums import TokenType

class Tokens(Base):
    __tablename__ = 'tokens'

    token: Mapped[str] = mapped_column(Text, primary_key=True, unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    type: Mapped[TokenType] = mapped_column(Enum(TokenType), nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    user: Mapped['User'] = relationship('User', lazy='joined')
