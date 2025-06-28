from fastapi import FastAPI
import uvicorn
from api import api_router
from core.config import settings
from contextlib import asynccontextmanager
from core.models import db_helper
from fastapi.responses import ORJSONResponse
from core.utils.errors_handlers import register_errors_handlers




@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.db_helper.dispose()

app = FastAPI(
    default_response_class = ORJSONResponse,
    lifespan = lifespan,
    docs_url= "/docs"
)

register_errors_handlers(app = app)

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