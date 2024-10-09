from datetime import datetime
from pydantic import BaseModel


class Base(BaseModel):
    """
    base model
    """

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda v: v.isoformat()}
