from fastapi import APIRouter

from core.config import settings

from api.api_v1.prices import prices_router

api_v1_router = APIRouter(
    prefix = settings.api.v1.prefix
)

api_v1_router.include_router(
    router = prices_router
)
