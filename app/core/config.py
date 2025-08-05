# from pydantic import BaseSettings
from pydantic_settings import BaseSettings , SettingsConfigDict


class Settings(BaseSettings):
    mongo_uri: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    # qdrant_host: str
    # qdrant_port: int

    model_config = SettingsConfigDict(extra="allow", env_file=".env")
    
    
settings = Settings()
