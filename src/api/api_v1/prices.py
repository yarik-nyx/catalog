from fastapi import APIRouter
from core.config import settings
from core.crud.prices import get_all_prices
from core.schemas.prices_schema import PriceJsonSchema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.models.db_helper import db_helper
from pydantic import ValidationError

prices_router = APIRouter(
    prefix = settings.api.v1.prices,
    tags = ["Prices"]
)

# response_model = list[PriceJsonSchema]
@prices_router.get("")
async def get_prices(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    
    users = await get_all_prices(session = session)
    return users