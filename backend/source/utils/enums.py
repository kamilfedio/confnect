from enum import Enum


class TokenType(Enum):
    """
    token types
    """

    ACCESS: str = "access"
    REFRESH: str = "refresh"


class EventStatus(Enum):
    """
    event status
    """

    ENDED: str = "ended"
    PENDING: str = "pending"
    INCOMING: str = "incoming"
