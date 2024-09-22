from pydantic.dataclasses import dataclass
from dataclasses import field


@dataclass
class Config:
    """
    app config
    """

    title: str = "convnect"
    description: str = "..."
    version: str = "0.0.1"
    debug: bool = True


@dataclass
class ConfigMiddleware:
    """
    middleware config
    """

    allow_origins: list[str] = field(default_factory=lambda: ["*"])
    allow_credentials: bool = True
    allow_methods: list[str] = field(default_factory=lambda: ["*"])
    allow_headers: list[str] = field(default_factory=lambda: ["*"])


config = Config()
config_middleware = ConfigMiddleware()
