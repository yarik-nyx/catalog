from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models.models import PricingPricingstrategy
from core.schemas.prices_schema import PriceJsonSchema, PriceJsonSchemaSum, PriceJsonSchemaSumWithName
from typing import List


async def get_all_prices(session: AsyncSession) -> List[PriceJsonSchemaSumWithName]:
    stmt = select(PricingPricingstrategy)
    executed = await session.execute(stmt)
    result = executed.scalars().all()
    output: List[PriceJsonSchemaSumWithName] = []
    for idx, value in enumerate(result):
        param = value.parameters["parameters"]
        res = PriceJsonSchema(parameters=dict(param))
        sum = (
            
            res.parameters.pricePerMeter * ((res.parameters.marginPct + 100) / 100) + 
                (
                    res.parameters.extras.ottomanFlat.count * res.parameters.extras.ottomanFlat.price + 
                    res.parameters.extras.mechanismFlat.count * res.parameters.extras.mechanismFlat.price
                )
        ) * ((res.parameters.fabricPct.category + 100) / 100)
        res = PriceJsonSchemaSumWithName(engine=value.engine,parameters=dict(res.parameters), sum=round(sum, 2))
        output.append(res)
    return output

async def sum_price(session: AsyncSession, body: PriceJsonSchema) -> PriceJsonSchemaSum:
    param = body.parameters
    
    sum = (
        param.pricePerMeter * ((param.marginPct + 100) / 100) + 
            (
                param.extras.ottomanFlat.count * param.extras.ottomanFlat.price + 
                param.extras.mechanismFlat.count * param.extras.mechanismFlat.price
            )
    ) * ((param.fabricPct.category + 100) / 100)
    print(type(body.parameters))
    output = PriceJsonSchemaSum(parameters=dict(body.parameters), sum=sum)
    return output