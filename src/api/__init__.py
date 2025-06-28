from fastapi import APIRouter
from core.config import settings
from api.api_v1 import api_v1_router

api_router = APIRouter(  
    prefix = settings.api.prefix
)

api_router.include_router(
    router = api_v1_router
)