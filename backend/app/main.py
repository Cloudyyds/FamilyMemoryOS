from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.persons import router as persons_router
from app.core.config import get_settings
from app.core.database import init_db

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    debug=settings.app_debug,
    lifespan=lifespan,
)


app.include_router(health_router, prefix=settings.api_prefix)
app.include_router(persons_router, prefix=settings.api_prefix)
