"""Endpoints module - rotas da API v1."""
from .templates import router as templates_router
from .evolution import router as evolution_router
from .options import router as options_router

__all__ = ["templates_router", "evolution_router", "options_router"]
