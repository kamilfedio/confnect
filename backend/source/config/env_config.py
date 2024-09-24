import os
from dotenv import load_dotenv
from pydantic.dataclasses import dataclass

env_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_path=env_path)


@dataclass
class DatabaseConfig:
    """
    database config
    """

    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_HOST: str = os.getenv("DB_HOST")

    @property
    def database_url(self) -> str:
        """
            generate database url
        Returns:
            str: database url
        """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


@dataclass
class EmailConfig:
    """
    Email config
    """

    EMAIL_PASSWORD: str = os.getenv("EMAIL_PASS")
    EMAIL: str = os.getenv("EMAIL")
    EMAIL_PORT: int = os.getenv("EMAIL_PORT")
    EMAIL_SERVER: str = os.getenv("EMAIL_SERVER")


@dataclass
class HostConfig:
    """
    Base information about host
    """

    BASE_URL: str = "http://localhost:5173"


@dataclass
class RedisConfig:
    """
    redis config
    """

    REDIS_URL = os.getenv("REDIS_URL")


db_config = DatabaseConfig()
email_config = EmailConfig()
host_config = HostConfig()
redis_config = RedisConfig()
