from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from sqlalchemy.orm import joinedload
from core.models.models import CatalogCollection
from typing import Sequence

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