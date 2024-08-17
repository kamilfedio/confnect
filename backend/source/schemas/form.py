from pydantic import EmailStr
from source.schemas.base import Base
from datetime import datetime

class Form(Base):
    email: EmailStr
    name: str
    content: str

class FormCreate(Form):
    pass

class FormRead(Form):
    id: int
    created_at: datetime
