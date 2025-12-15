"""
Router principal da API v1.
Agrega todos os endpoints da versão 1 da API.
"""
from fastapi import APIRouter

from app.api.v1.endpoints import templates_router, evolution_router, options_router

api_router = APIRouter()

# Inclui todos os routers de endpoints
api_router.include_router(templates_router)
api_router.include_router(evolution_router)
api_router.include_router(options_router)
