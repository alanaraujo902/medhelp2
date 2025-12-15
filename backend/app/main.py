"""
Medical Evolution System - Backend API
Sistema de Evolução Médica com IA

Aplicação FastAPI principal que configura e executa o servidor.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from app.core.config import settings
from app.api.v1.router import api_router
from app.schemas.evolution import HealthCheckResponse


def create_application() -> FastAPI:
    """
    Factory function para criar a aplicação FastAPI.
    Configura middlewares, routers e handlers.
    """
    application = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    
    # Configuração de CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Inclui router da API v1
    application.include_router(
        api_router,
        prefix=settings.API_V1_PREFIX,
    )
    
    return application


app = create_application()


@app.get("/", tags=["Root"])
async def root():
    """
    Endpoint raiz da API.
    Retorna informações básicas sobre o sistema.
    """
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "description": settings.APP_DESCRIPTION,
        "docs": "/docs",
        "api": settings.API_V1_PREFIX,
    }


@app.get("/health", response_model=HealthCheckResponse, tags=["Health"])
async def health_check():
    """
    Verifica o status de saúde da aplicação.
    Útil para monitoramento e load balancers.
    """
    # Verifica status dos serviços
    services = {
        "api": "healthy",
        "perplexity": "configured" if settings.PERPLEXITY_API_KEY else "not_configured",
        "supabase": "not_configured",  # Preparado para implementação futura
    }
    
    return HealthCheckResponse(
        status="healthy",
        version=settings.APP_VERSION,
        timestamp=datetime.now(),
        services=services,
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
