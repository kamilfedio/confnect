from pydantic import EmailStr
from source.schemas.base import Base
from datetime import datetime


class User(Base):
    """
    user base
    """

    email: EmailStr
    name: str


class UserCreate(User):
    """
    creating user object inherit from User
    """

    password: str


class UserUpdate(Base):
    """
    update user object
    """

    email: EmailStr | None = None
    name: str | None = None


class UserPasswordUpdate(Base):
    """
    update user password object
    """

    old_password: str
    password: str


class UserRead(User):
    """
    stores user all data
    """

    id: int
    created_at: datetime
    updated_at: datetime | None
