from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models.models import CatalogProduct, CatalogConfiguration
from fastapi import HTTPException

async def get_configuration_by_productid(session: AsyncSession, product_id:int):
    stmt_product = (
        select(CatalogProduct)
        .where(CatalogProduct.id == product_id)
    )
    executed_product = await session.execute(stmt_product)
    result_product = executed_product.scalars().all()

    if not result_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    stmt_configuration = (
        select(CatalogConfiguration)
        .where(CatalogConfiguration.product_id == product_id)
    )

    executed_configuration = await session.execute(stmt_configuration)
    result_configuration = executed_configuration.scalars().all()

    if not result_configuration:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    return result_configuration

    