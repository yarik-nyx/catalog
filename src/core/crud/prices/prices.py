from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models.models import PricingPricingstrategy
from core.schemas.prices_schema import PriceJsonSchema, PriceJsonSchemaSum
from typing import List


async def get_all_prices(session: AsyncSession) -> List[PriceJsonSchema]:
    stmt = select(PricingPricingstrategy)
    executed = await session.execute(stmt)
    result = executed.scalars().all()
    for idx, value in enumerate(result):
        res: PriceJsonSchema = value.parameters
        PriceJsonSchema.model_validate(res)
        sum = (
            res["parameters"]["pricePerMeter"] * ((res["parameters"]["marginPct"] + 100) / 100) + 
                (
                    res["parameters"]["extras"]["ottomanFlat"]["count"] * res["parameters"]["extras"]["ottomanFlat"]["price"] + 
                    res["parameters"]["extras"]["mechanismFlat"]["count"] * res["parameters"]["extras"]["mechanismFlat"]["price"]
                )
        ) * ((res["parameters"]["fabricPct"]["category"] + 100) / 100)
        res["sum"] = round(sum, 2)
    return result

async def sum_price(session: AsyncSession, body: PriceJsonSchema):
    param = body.parameters
    
    sum = (
        param.pricePerMeter * ((param.marginPct + 100) / 100) + 
            (
                param.extras.ottomanFlat.count * param.extras.ottomanFlat.price + 
                param.extras.mechanismFlat.count * param.extras.mechanismFlat.price
            )
    ) * ((param.fabricPct.category + 100) / 100)

    output = PriceJsonSchemaSum(parameters=dict(body.parameters), sum=sum)
    return output