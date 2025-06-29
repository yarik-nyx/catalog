from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from typing import List




class AppConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000
    

class EnvConfig(BaseSettings):
    DB_URL: str
    ALLOWED_IPS: List[str]
    model_config = SettingsConfigDict(env_file=".env")

class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    prices: str = "/prices"
    collections: str = "/collections"
    products: str = "/products"

class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

class DbConfig(BaseModel):
    DB_URL: str = ""

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow:int = 10
    
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }


  

class Settings(BaseModel):
    run: AppConfig = AppConfig()
    env: EnvConfig = EnvConfig()
    api: ApiPrefix = ApiPrefix()
    db: DbConfig = DbConfig()
    db.DB_URL = env.DB_URL

    




settings = Settings()

    