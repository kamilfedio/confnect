from pydantic import BaseModel


class Base(BaseModel):
    """
    base model
    """

    class Config:
        from_attributes = True
