from source.schemas.base import Base
from datetime import datetime

class User(Base):
    email: str
    name: str

class UserCreate(User):
    password: str

class UserRead(User):
    id: int
    created_at: datetime
    updated_at: datetime | None
