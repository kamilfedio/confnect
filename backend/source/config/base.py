from pydantic_settings import BaseSettings
import os


class BaseConfig(BaseSettings):
    """
    base config settings
    """

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "../../.env")
        env_file_encoding = "utf-8"
        extra = "allow"
