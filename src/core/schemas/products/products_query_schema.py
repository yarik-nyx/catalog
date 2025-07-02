from fastapi import Query
from pydantic import BaseModel





class ProductsQueryParamsSubcategoryId(BaseModel):

    subcategory_id: int = Query(description="Фильтрация по подкатегории продукта")