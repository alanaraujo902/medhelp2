"""
Endpoints para gerenciamento de templates de evolução médica.
"""
from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.evolution import (
    TemplateCreateRequest,
    TemplateUpdateRequest,
    TemplateResponse,
    TemplateListResponse,
    PresetTemplate,
    PresetTemplatesResponse,
)
from app.services.template_service import template_service

router = APIRouter(prefix="/templates", tags=["Templates"])


@router.get("", response_model=TemplateListResponse)
async def list_templates():
    """
    Lista todos os templates disponíveis.
    Inclui templates pré-configurados e criados pelo usuário.
    """
    templates = template_service.get_all_templates()
    
    response_templates = [
        TemplateResponse(
            id=t.id,
            name=t.name,
            is_default=t.is_default,
            primary_context=t.primary_context,
            emergency_type=t.emergency_type,
            outpatient_specialty=t.outpatient_specialty,
            icu_type=t.icu_type,
            hospitalization_type=t.hospitalization_type,
            header_config=t.header_config,
            sections_config=t.sections_config,
            formatting_config=t.formatting_config,
            created_at=t.created_at,
            updated_at=t.updated_at,
        )
        for t in templates
    ]
    
    return TemplateListResponse(
        templates=response_templates,
        total=len(response_templates)
    )


@router.get("/presets", response_model=PresetTemplatesResponse)
async def list_preset_templates():
    """
    Lista apenas os templates pré-configurados do sistema.
    """
    presets = template_service.get_preset_templates()
    
    preset_responses = [
        PresetTemplate(
            id=t.id,
            name=t.name,
            description=f"Template para {t.primary_context.value}",
            primary_context=t.primary_context,
            preview=f"Modelo otimizado para {t.name}",
        )
        for t in presets
    ]
    
    return PresetTemplatesResponse(presets=preset_responses)


@router.get("/user", response_model=TemplateListResponse)
async def list_user_templates():
    """
    Lista apenas os templates criados pelo usuário.
    """
    templates = template_service.get_user_templates()
    
    response_templates = [
        TemplateResponse(
            id=t.id,
            name=t.name,
            is_default=t.is_default,
            primary_context=t.primary_context,
            emergency_type=t.emergency_type,
            outpatient_specialty=t.outpatient_specialty,
            icu_type=t.icu_type,
            hospitalization_type=t.hospitalization_type,
            header_config=t.header_config,
            sections_config=t.sections_config,
            formatting_config=t.formatting_config,
            created_at=t.created_at,
            updated_at=t.updated_at,
        )
        for t in templates
    ]
    
    return TemplateListResponse(
        templates=response_templates,
        total=len(response_templates)
    )


@router.get("/default", response_model=TemplateResponse)
async def get_default_template():
    """
    Obtém o template marcado como padrão.
    """
    template = template_service.get_default_template()
    
    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum template padrão definido"
        )
    
    return TemplateResponse(
        id=template.id,
        name=template.name,
        is_default=template.is_default,
        primary_context=template.primary_context,
        emergency_type=template.emergency_type,
        outpatient_specialty=template.outpatient_specialty,
        icu_type=template.icu_type,
        hospitalization_type=template.hospitalization_type,
        header_config=template.header_config,
        sections_config=template.sections_config,
        formatting_config=template.formatting_config,
        created_at=template.created_at,
        updated_at=template.updated_at,
    )


@router.get("/{template_id}", response_model=TemplateResponse)
async def get_template(template_id: str):
    """
    Obtém um template específico pelo ID.
    """
    template = template_service.get_template(template_id)
    
    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Template não encontrado: {template_id}"
        )
    
    return TemplateResponse(
        id=template.id,
        name=template.name,
        is_default=template.is_default,
        primary_context=template.primary_context,
        emergency_type=template.emergency_type,
        outpatient_specialty=template.outpatient_specialty,
        icu_type=template.icu_type,
        hospitalization_type=template.hospitalization_type,
        header_config=template.header_config,
        sections_config=template.sections_config,
        formatting_config=template.formatting_config,
        created_at=template.created_at,
        updated_at=template.updated_at,
    )


@router.post("", response_model=TemplateResponse, status_code=status.HTTP_201_CREATED)
async def create_template(request: TemplateCreateRequest):
    """
    Cria um novo template de evolução.
    """
    template = template_service.create_template(request)
    
    return TemplateResponse(
        id=template.id,
        name=template.name,
        is_default=template.is_default,
        primary_context=template.primary_context,
        emergency_type=template.emergency_type,
        outpatient_specialty=template.outpatient_specialty,
        icu_type=template.icu_type,
        hospitalization_type=template.hospitalization_type,
        header_config=template.header_config,
        sections_config=template.sections_config,
        formatting_config=template.formatting_config,
        created_at=template.created_at,
        updated_at=template.updated_at,
    )


@router.put("/{template_id}", response_model=TemplateResponse)
async def update_template(template_id: str, request: TemplateUpdateRequest):
    """
    Atualiza um template existente.
    Não é possível atualizar templates pré-configurados.
    """
    if template_id.startswith("preset-"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não é possível modificar templates pré-configurados"
        )
    
    template = template_service.update_template(template_id, request)
    
    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Template não encontrado: {template_id}"
        )
    
    return TemplateResponse(
        id=template.id,
        name=template.name,
        is_default=template.is_default,
        primary_context=template.primary_context,
        emergency_type=template.emergency_type,
        outpatient_specialty=template.outpatient_specialty,
        icu_type=template.icu_type,
        hospitalization_type=template.hospitalization_type,
        header_config=template.header_config,
        sections_config=template.sections_config,
        formatting_config=template.formatting_config,
        created_at=template.created_at,
        updated_at=template.updated_at,
    )


@router.delete("/{template_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_template(template_id: str):
    """
    Remove um template.
    Não é possível remover templates pré-configurados.
    """
    if template_id.startswith("preset-"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não é possível remover templates pré-configurados"
        )
    
    success = template_service.delete_template(template_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Template não encontrado: {template_id}"
        )
