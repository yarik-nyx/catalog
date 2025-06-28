from fastapi import APIRouter
from core.config import settings
from core.crud.collections.collections import get_all_collections
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Query
from core.models.db_helper import db_helper
from core.schemas.collections.collections_query_schema import CatalogCollectionQueryParams
from pydantic import ValidationError

collections_router = APIRouter(
    prefix = settings.api.v1.collections,
    tags = ["Collections"]
)

# response_model = list[PriceJsonSchema]
@collections_router.get("")
async def get_collections(
    query_params: CatalogCollectionQueryParams = Query(...),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    sort_by_field = query_params.sort_by.value
    order_direction = query_params.order.value
    collections = await get_all_collections(
        session = session,
        sort_by_field = sort_by_field,
        order_direction = order_direction
    )
    return collections