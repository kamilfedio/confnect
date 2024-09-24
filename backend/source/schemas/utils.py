from source.utils.enums import EmailType
from source.schemas.base import Base
from pydantic import EmailStr


class ResetPassword(Base):
    """
    reset password schema
    """

    reset_token: str
    new_password: str
    confirm_password: str


class ResetPasswordRequest(Base):
    """
    Reset password request schema
    """

    email: EmailStr


class EmailSchema(Base):
    """
    email schema
    """

    type: EmailType
    to: EmailStr
    subject: str
    content: dict[str, str]
