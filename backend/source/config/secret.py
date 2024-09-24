import os
from dotenv import load_dotenv
from pydantic.dataclasses import dataclass

env_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_path=env_path)


@dataclass
class SecretConfig:
    """
    secret app config
    """

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "bcrypt"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    INVITATION_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    RESET_PASSWORD_EXPIRE_MINUTES: int = 60


secret_config = SecretConfig()
