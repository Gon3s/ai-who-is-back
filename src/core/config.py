from pydantic_settings import BaseSettings
from pydantic import Field

class LLMConfig(BaseSettings):
    api_key: str = Field(..., description="Groq API Key")
    model_name: str = "llama-3.1-8b-instant"
    temperature: float = 0.3
    max_tokens: int = 50
    
    class Config:
        env_prefix = "AIWHO_"
        env_file = ".env"
