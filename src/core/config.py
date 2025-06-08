from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn

class AppConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    prices: str = "/prices"

class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

class DbConfig(BaseSettings):
    DB_URL: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow:int = 10
    model_config = SettingsConfigDict(env_file=".env")

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
    
    

class Settings(BaseSettings):
    run: AppConfig = AppConfig()
    api: ApiPrefix = ApiPrefix()
    db: DbConfig = DbConfig()
    
    




settings = Settings()

    