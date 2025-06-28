from enum import Enum
from typing import Optional, ClassVar
from fastapi import Query
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.models.db_helper import db_helper
from core.models.models import ClassificationSubcategory
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import asyncio





class OrderEnum(str, Enum):
    asc = "asc"
    desc = "desc"

class CatalogCollectionSortEnum(str, Enum):
    created_at = "created_at"
    updated_at = "updated_at"
    label = "label"
    defaults = "defaults"
    id = "id"
    pricing_strategy_id = "pricing_strategy_id"
    category_id = "category_id"
    template_id = "template_id"

class CatalogCollectionQueryParamsSortByOrder(BaseModel):
    sort_by: Optional[CatalogCollectionSortEnum] = Query("id", description="Поле для сортировки. Допустимые значения: label, id, defaults.")
    order: Optional[OrderEnum] = Query("asc", description="Направление сортировки: 'asc' (возрастание) или 'desc' (убывание).")

class CatalogCollectionQueryParamsSubcategoryId(BaseModel):

    # subcategories:Optional[Enum] = None

    # @classmethod
    # async def get_subcategory_labels(cls, session: AsyncSession = Depends(db_helper.session_getter)):
    #     stmt = (select(ClassificationSubcategory.label))
        

        
    #     executed = session.execute(stmt)

    #     resx = executed.scalars().all()

    #     return resx 
    
    # @classmethod
    # async def run_in_class(cls):
    #     res = await cls.get_subcategory_labels()
    #     print(res)
    #     subcategoryEnum = Enum("SubcategoryType", {value for value in res}, type = str)
    #     cls.subcategories: Optional[subcategoryEnum] = Query(None, description="Фильтрация по типу продукта")


    subcategory_id: int = Query(description="Фильтрация по типу продукта")