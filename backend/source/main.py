from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from source.config.config import Config, ConfigMiddleware
from source.config.routes import routes_config
from source.config.authorization import google_auth_config

from source.routes.forms import router as forms_router
from source.routes.authorization import router as auth_router


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

app.add_middleware(SessionMiddleware, secret_key=google_auth_config.secret_key)

routes = [
    (forms_router, routes_config.forms),
    (auth_router, routes_config.auth),
]

for route in routes:
    app.include_router(route[0], prefix=route[1], tags=[route[1][1:]])

@app.get("/")
async def root() -> Response:
    return Response(status_code=status.HTTP_200_OK, content=f'{Config.title} - {Config.version} is running')
