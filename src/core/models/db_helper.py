from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from core.config import settings

class DatabaseHelper:
    def __init__(
            self,
            url: str,
            echo: bool = False, #Вывод логов запросов в консоль
            echo_pool: bool = False, #Вывод логов соединения с бд в консоль
            pool_size: int = 5, #Макс кол-во постоянных соединений, которые будут поддерживаться в пуле
            max_overflow: int = 10, #Макс кол-во временных соединений
        ) -> None:
            self.engine: AsyncEngine = create_async_engine(
                url = url,
                echo = echo,
                echo_pool = echo_pool,
                pool_size = pool_size,
                max_overflow = max_overflow,
            )

            self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
                  bind = self.engine,
                  autoflush = False,
                  autocommit = False,
                  expire_on_commit = False
            )

    async def dispose(self) -> None:
        await self.engine.dispose()
    
    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
         async with self.session_factory() as session:
             yield session


db_helper = DatabaseHelper(
     url = settings.db.DB_URL,
     echo = settings.db.echo,
     echo_pool = settings.db.echo_pool,
     pool_size = settings.db.pool_size,
     max_overflow = settings.db.max_overflow
)
    
