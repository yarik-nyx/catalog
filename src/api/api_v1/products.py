from fastapi import APIRouter, Depends, Query
from core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper
from core.crud.products.products import get_configuration_by_productid
from core.schemas.products.products_query_schema import ProductsQueryParamsSubcategoryId

products_router = APIRouter(
    prefix = settings.api.v1.products,
    tags = ["Products"]
)

@products_router.get("/{product_id}/configurations", description="Get configuration by product id and subcategory id")
async def get_configuration_of_product(
    product_id: int,
    query_params: ProductsQueryParamsSubcategoryId = Query(...),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await  get_configuration_by_productid(product_id = product_id, session = session, subcategory_id = query_params.subcategory_id)
    return result