from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel




class AppConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

class EnvConfig(BaseSettings):
    DB_URL: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    prices: str = "/prices"
    collections: str = "/collections"

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

class AdminViewConfig(BaseModel):
    SECRET_KEY: str = ""
    admin_db_url: str = ""
    track_events: bool = True
    allowed_ips: list[str] = ["10.0.0.1"],
    allowed_networks: list[str] = ["192.168.1.0/24"],
    secure_cookies:bool = False,
    enforce_https:bool = False,
    initial_admin:bool = True
    max_sessions_per_user:int = 3,
    session_timeout_minutes:int = 15,

    track_events:bool = True,
    track_sessions_in_db: bool = True,

    initial_username: str = "admin",
    initial_password: str = "tTRm+eAA9hM.A7"

    mount_path:str = "/admin"
    

    

class Settings(BaseModel):
    run: AppConfig = AppConfig()
    env: EnvConfig = EnvConfig()
    api: ApiPrefix = ApiPrefix()
    db: DbConfig = DbConfig()
    db.DB_URL = env.DB_URL
    AdminConfig: AdminViewConfig = AdminViewConfig()
    AdminConfig.admin_db_url = env.DB_URL
    AdminConfig.SECRET_KEY = env.SECRET_KEY

    




settings = Settings()

    