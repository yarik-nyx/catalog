from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models.models import PricingPricingstrategy
from core.schemas.prices_schema import PriceJsonSchema




async def get_all_prices(session: AsyncSession):
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