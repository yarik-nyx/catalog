from pydantic import BaseModel


class ottomanFlat(BaseModel):
    count: int
    price: int

class mechanismFlat(BaseModel):
    count: int
    price: int

class fabricPct(BaseModel):
    category: int


class extras(BaseModel):
    ottomanFlat: ottomanFlat
    mechanismFlat: mechanismFlat

class parameters(BaseModel):
    extras: extras
    fabricPct: fabricPct
    marginPct: int
    pricePerMeter: int

class PriceJsonSchema(BaseModel):
    parameters: parameters

class PriceSchema(BaseModel):
    engine: str
    parameters: PriceJsonSchema


class PriceCreateSchema(PriceSchema):
    pass

class PriceReadSchema(PriceSchema):
    id: str