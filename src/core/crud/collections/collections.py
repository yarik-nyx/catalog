from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from sqlalchemy.orm import joinedload, selectinload
from core.models.models import CatalogCollection, CatalogProduct, ClassificationSubcategory, ClassificationCategory
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
    ):
    stmt_get_collection = (
        select(CatalogCollection)
        .where(CatalogCollection.id == collection_id)
    )
    executed_stmt_collection = await session.execute(stmt_get_collection)
    result_collection = executed_stmt_collection.scalars().all()

    if not result_collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    
    # stmt_get_category = (
    #     select(ClassificationCategory)
    #     .where(ClassificationCategory.id == category_id)
    # )
    # executed_stmt_category = await session.execute(stmt_get_category)
    # result_category = executed_stmt_category.scalars().all()

    # if not result_category:
    #     raise HTTPException(status_code=404, detail="Category not found")
    
    stmt_product = (
        select(CatalogProduct)
        .where(CatalogProduct.collection_id == collection_id)
        # .options(joinedload(CatalogProduct.collection))

    )
    executed_stmt_product = await session.execute(stmt_product)
    result_product = executed_stmt_product.scalars().all()
    
    return result_product

async def get_all_categories_by_collection_id(
        session: AsyncSession,
        collection_id: int,
    ):
    stmt_get_collection = (
        select(CatalogCollection)
        .where(CatalogCollection.id == collection_id)
    )
    executed_stmt_collection = await session.execute(stmt_get_collection)
    result_collection = executed_stmt_collection.scalars().all()

    if not result_collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    
    stmt_collection_with_categories = (
        select(CatalogCollection)
        .where(CatalogCollection.id == collection_id)
        .options(joinedload(CatalogCollection.category)
        .load_only(ClassificationCategory.label))
    )
    executed_col_w_cat = await session.execute(stmt_collection_with_categories)
    result_col_w_cat = executed_col_w_cat.scalars().all()

    return result_col_w_cat