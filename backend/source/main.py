from contextlib import asynccontextmanager
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from source.config.config import Config, ConfigMiddleware
from source.config.routes import routes_config

from source.routes.forms import router as forms_router
from source.routes.authorization import router as auth_router
from source.routes.test import router as test_router
from source.routes.users import router as users_router
from source.routes.events import router as events_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    creating lifespan for fastapi
    Args:
        app (FastAPI): FastAPI
    """
    yield

app = FastAPI(
    title=Config.title,
    description=Config.description,
    version=Config.version,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ConfigMiddleware.allow_origins,
    allow_credentials=ConfigMiddleware.allow_credentials,
    allow_methods=ConfigMiddleware.allow_methods,
    allow_headers=ConfigMiddleware.allow_headers,
)

routes = [
    (forms_router, routes_config.forms),
    (auth_router, routes_config.auth),
    (test_router, routes_config.test),
    (users_router, routes_config.users),
    (events_router, routes_config.events),
]

for route in routes:
    app.include_router(route[0], prefix=f'{routes_config.version}/{route[1]}', tags=[route[1]])

@app.get("/")
async def root() -> Response:
    return Response(status_code=status.HTTP_200_OK, content=f'{Config.title} - {Config.version} is running')
