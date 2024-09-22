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


db_config = DatabaseConfig()
