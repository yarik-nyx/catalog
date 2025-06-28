from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from sqlalchemy.orm import joinedload
from core.models.models import CatalogCollection, CatalogProduct, ClassificationSubcategory
from typing import Sequence
from fastapi import HTTPException

async def get_all_collections(
        session: AsyncSession,
        sort_by_field: str,
        order_direction: str
    ) -> Sequence[CatalogCollection]:
    stmt = (select(CatalogCollection)
    .options(joinedload(CatalogCollection.category))
    .options(joinedload(CatalogCollection.pricing_strategy))
    .options(joinedload(CatalogCollection.template))
    .order_by(text(f"{sort_by_field} {order_direction}"))
    )
    
    executed = await session.execute(stmt)
    result = executed.scalars().all()

    return result

async def get_all_products_by_collection_id(
        session: AsyncSession,
        collection_id: int,
        subcategory_id: int
    ):
    stmt_get_collection = (
        select(CatalogCollection)
        .where(CatalogCollection.id == collection_id)
    )
    executed_stmt_collection = await session.execute(stmt_get_collection)
    result_collection = executed_stmt_collection.scalars().all()

    if not result_collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    
    stmt_get_subcategory = (
        select(ClassificationSubcategory)
        .where(ClassificationSubcategory.id == subcategory_id)
    )
    executed_stmt_subcategory = await session.execute(stmt_get_subcategory)
    result_subcategory = executed_stmt_subcategory.scalars().all()

    if not result_subcategory:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    
    stmt_product = (
        select(CatalogProduct)
        .where(CatalogProduct.collection_id == collection_id)
        .where(CatalogProduct.subcategory_id == subcategory_id)
        .options(joinedload(CatalogProduct.subcategory))

    )
    executed_stmt_product = await session.execute(stmt_product)
    result_product = executed_stmt_product.scalars().all()
    
    return result_product