class Config:
    """
    app config
    """

    title: str = "convnect"
    description: str = "..."
    version: str = "0.0.1"
    debug: bool = True


class ConfigMiddleware:
    """
    middleware config
    """

    allow_origins: list[str] = ["*"]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
