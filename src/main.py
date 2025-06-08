from fastapi import FastAPI
import uvicorn
from api import api_router
from core.config import settings
from contextlib import asynccontextmanager
from core.models import db_helper
from fastapi.responses import ORJSONResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.db_helper.dispose()

app = FastAPI(
    default_response_class = ORJSONResponse,
    lifespan = lifespan
)

app.include_router(
    router = api_router,
)

if __name__ == "__main__":
    uvicorn.run(
        app = "main:app", 
        host = settings.run.host,
        port = settings.run.port,
        reload = True
    )