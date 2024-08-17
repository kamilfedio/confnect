from contextlib import asynccontextmanager
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from source.config.config import Config, ConfigMiddleware
from source.routes.forms import router as forms_router
from source.config.routes import RoutesConfig

routes_config = RoutesConfig()

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
    version=Config.description,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ConfigMiddleware.allow_origins,
    allow_credentials=ConfigMiddleware.allow_credentials,
    allow_methods=ConfigMiddleware.allow_methods,
    allow_headers=ConfigMiddleware.allow_headers,
)

@app.get("/")
async def read_root() -> Response:
    return Response(status_code=status.HTTP_200_OK, content=f'{Config.title} - {Config.version} is running')

app.include_router(forms_router, prefix=routes_config.forms, tags=[routes_config.forms])
