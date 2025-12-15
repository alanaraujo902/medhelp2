"""
Configuração central do aplicativo.
Gerencia variáveis de ambiente e configurações globais.
"""
from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache


class Settings(BaseSettings):
    """Configurações do aplicativo carregadas de variáveis de ambiente."""
    
    # Informações do App
    APP_NAME: str = "Medical Evolution System"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Sistema de Evolução Médica com IA"
    DEBUG: bool = True
    
    # API
    API_V1_PREFIX: str = "/api/v1"
    
    # CORS - Origens permitidas
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "*",  # Permitir todas as origens em desenvolvimento
    ]
    
    # Perplexity API
    PERPLEXITY_API_KEY: str = ""
    PERPLEXITY_API_URL: str = "https://api.perplexity.ai/chat/completions"
    PERPLEXITY_MODEL: str = "llama-3.1-sonar-small-128k-online"
    
    # Supabase (preparado para implementação futura)
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Retorna instância cacheada das configurações."""
    return Settings()


settings = get_settings()
