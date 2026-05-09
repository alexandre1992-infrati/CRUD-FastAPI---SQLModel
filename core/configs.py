from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configuração da API"""
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/escola"
    class Config:
        case_sensitive = True


settings: Settings = Settings()       
