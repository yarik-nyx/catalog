from enum import Enum
from typing import Optional
from fastapi import Query
from pydantic import BaseModel


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

class CatalogCollectionQueryParams(BaseModel):
    sort_by: Optional[CatalogCollectionSortEnum] = Query("id", description="Поле для сортировки. Допустимые значения: label, id, defaults.")
    order: Optional[OrderEnum] = Query("asc", description="Направление сортировки: 'asc' (возрастание) или 'desc' (убывание).")