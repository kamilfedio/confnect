from pydantic import EmailStr
from source.schemas.base import Base
from datetime import datetime

class User(Base):
    email: EmailStr
    name: str

class UserCreate(User):
    password: str

class UserUpdate(Base):
    email: EmailStr | None = None
    name: str | None = None

class UserPasswordUpdate(Base):
    old_password: str
    password: str

class UserRead(User):
    id: int
    created_at: datetime
    updated_at: datetime | None
