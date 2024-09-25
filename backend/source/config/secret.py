from source.config.base import BaseConfig

class SecretConfig(BaseConfig):
    """
    secret app config
    """

    SECRET_KEY: str
    ALGORITHM: str = "bcrypt"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    INVITATION_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    RESET_PASSWORD_EXPIRE_MINUTES: int = 60


secret_config = SecretConfig()
