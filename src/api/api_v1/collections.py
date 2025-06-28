from fastapi import APIRouter
from core.config import settings
from core.crud.collections.collections import get_all_collections, get_all_products_by_collection_id
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Query
from core.models.db_helper import db_helper
from core.schemas.collections.collections_query_schema import CatalogCollectionQueryParamsSortByOrder, CatalogCollectionQueryParamsSubcategoryId
from typing import List

collections_router = APIRouter(
    prefix = settings.api.v1.collections,
    tags = ["Collections"]
)


@collections_router.get("", description="Get all products by query paramss")
async def get_collections(
    query_params: CatalogCollectionQueryParamsSortByOrder = Query(...),
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

@collections_router.get("/{collection_id}/products", description="Get all products by collection id")
async def get_products_by_collection_id(
    collection_id: int,
    query_params: CatalogCollectionQueryParamsSubcategoryId = Query(...),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    products = await get_all_products_by_collection_id(session=session, collection_id=collection_id, subcategory_id=query_params.subcategory_id)
    return products