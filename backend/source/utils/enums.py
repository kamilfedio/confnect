from enum import Enum


class TokenType(Enum):
    """
    token types
    """

    ACCESS: str = "access"
    REFRESH: str = "refresh"
    RESET_PASSWORD: str = "reset-password"


class EventStatus(Enum):
    """
    event status
    """

    ENDED: str = "ended"
    ONGOING: str = "ongoing"
    INCOMING: str = "incoming"


class EmailType(Enum):
    """
    email types
    """

    RESET_PASSWORD: str = "reset_password"
