from pydantic import EmailStr
from source.schemas.base import Base
from datetime import datetime


class Form(Base):
    """
    form base
    """

    email: EmailStr
    name: str
    content: str


class FormCreate(Form):
    """
    create form object
    """

    pass


class FormRead(Form):
    """
    stores all form data
    """

    id: int
    created_at: datetime
