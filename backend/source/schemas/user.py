from source.schemas.base import Base
from datetime import datetime

class User(Base):
    email: str
    name: str

class UserCreate(User):
    picture_url: str

class UserRead(User):
    id: int
    picture_url: str
    created_at: datetime
    updated_at: datetime
