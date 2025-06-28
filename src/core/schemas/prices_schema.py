from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass
        


class ottomanFlat(BaseSchema):
    count: int = 0
    price: int = 0

class mechanismFlat(BaseSchema):
    count: int = 0
    price: int = 0

class fabricPct(BaseSchema):
    category: int = 0


class extras(BaseSchema):
    ottomanFlat: ottomanFlat
    mechanismFlat: mechanismFlat

class parameters(BaseSchema):
    extras: extras
    fabricPct: fabricPct
    marginPct: int = 0
    pricePerMeter: int = 0

class PriceJsonSchema(BaseSchema):
    parameters: parameters

class PriceJsonSchemaSum(BaseSchema):
    parameters: parameters
    sum: int
    

class PriceSchema(BaseSchema):
    engine: str 
    parameters: PriceJsonSchema

    model_config = {"exclude": {"created_at", "updated_at"}}




class PriceCreateSchema(PriceSchema):
    pass

class PriceUpdateSchema(PriceSchema):
    pass

class PriceReadSchema(PriceSchema):
    id: str