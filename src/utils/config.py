from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""

    # App settings
    app_name: str = "AI Who Is"
    app_description: str = "A game to guess the AI who generated a text."
    version: str = "1.0.0"
    debug: bool = False
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # LLM settings
    api_key: str
    model_name: str = "llama-3.1-8b-instant"
    temperature: float = 0.3
    max_tokens: int = 50

    class Config:
        env_file = ".env"
        env_prefix = "AIWHO_"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
