from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from core.config import settings

class Base(DeclarativeBase):

    meatadata = MetaData(
        naming_convention = settings.db.naming_convention
    )

    # id: Mapped[int] = mapped_column(primary_key=True)

