class RoutesConfig:
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
