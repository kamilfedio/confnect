from source.config.base import BaseConfig


class RoutesConfig(BaseConfig):
    """
    routes config
    """

    version: str = "/api/v1"
    forms: str = "forms"
    auth: str = "auth"
    test: str = "test"
    users: str = "users"
    events: str = "events"


routes_config = RoutesConfig()
