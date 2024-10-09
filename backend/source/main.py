from contextlib import asynccontextmanager
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from source.config.config import config, config_middleware
from source.config.routes import routes_config

from source.routes.forms import router as forms_router
from source.routes.authorization import router as auth_router
from source.routes.test import router as test_router
from source.routes.users import router as users_router
from source.routes.events import router as events_router

from source.utils.connection_manager import broadcast


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    creating lifespan for fastapi
    Args:
        app (FastAPI): FastAPI
    """
    await broadcast.connect()
    yield
    await broadcast.disconnect()


app = FastAPI(
    title=config.title,
    description=config.description,
    version=config.version,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config_middleware.allow_origins,
    allow_credentials=config_middleware.allow_credentials,
    allow_methods=config_middleware.allow_methods,
    allow_headers=config_middleware.allow_headers,
)

routes = [
    (forms_router, routes_config.forms),
    (test_router, routes_config.test),
    (users_router, routes_config.users),
    (events_router, routes_config.events),
]

# adding routes with prefix and tags
for route in routes:
    app.include_router(
        route[0], prefix=f"{routes_config.version}/{route[1]}", tags=[route[1]]
    )

# add other routers
app.include_router(auth_router, tags=[routes_config.auth])


@app.get("/")
async def root() -> Response:
    """
        return default root response
    Returns:
        Response: information about version
    """
    return Response(
        status_code=status.HTTP_200_OK,
        content=f"{config.title} - {config.version} is running",
    )
