from source.config.base import BaseConfig


class DatabaseConfig(BaseConfig):
    """
    database config
    """

    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str

    @property
    def database_url(self) -> str:
        """
            generate database url
        Returns:
            str: database url
        """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class EmailConfig(BaseConfig):
    """
    Email config
    """

    EMAIL_PASS: str
    EMAIL: str
    EMAIL_PORT: int
    EMAIL_SERVER: str


class HostConfig(BaseConfig):
    """
    Base information about host
    """

    BASE_URL: str = "http://localhost:5173"


class RedisConfig(BaseConfig):
    """
    redis config
    """

    REDIS_URL: str


db_config = DatabaseConfig()
email_config = EmailConfig()
host_config = HostConfig()
redis_config = RedisConfig()
