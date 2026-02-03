"""
Endpoints para geração de evoluções médicas.
"""
from fastapi import APIRouter, HTTPException, status
from datetime import datetime
import uuid

from app.schemas.evolution import (
    EvolutionGenerateRequest,
    EvolutionGenerateResponse,
    EvolutionSection,
)
from app.services.template_service import template_service
from app.services.perplexity_service import perplexity_service
from app.services.intelligence_service import detectar_tudo, validar_anti_invencao
from app.models.evolution import (
    EvolutionTemplate,
    HeaderConfig,
    SectionsConfig,
    FormattingConfig,
)

router = APIRouter(prefix="/evolution", tags=["Evolution"])


@router.post("/generate", response_model=EvolutionGenerateResponse)
async def generate_evolution(request: EvolutionGenerateRequest):
    """
    Gera uma evolução médica formatada a partir de texto livre.
    
    Usa inteligência automática para detectar contexto e especialidade quando não informados.
    Valida a saída contra regras anti-invenção.
    """
    template = None
    identificacao = None

    # 1. Inteligência Automática: detectar contexto e especialidade se não fornecidos
    identificacao = detectar_tudo(request.raw_text)
    contexto_final = request.primary_context or identificacao.primary_context
    especialidade_final = request.outpatient_specialty or identificacao.outpatient_specialty

    # Se template_id fornecido, busca o template
    if request.template_id:
        template = template_service.get_template(request.template_id)
        if not template:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Template não encontrado: {request.template_id}"
            )
    
    # Se configurações inline ou detectadas, cria template temporário
    else:
        template = EvolutionTemplate(
            id="temp",
            name="Configuração Temporária",
            primary_context=contexto_final,
            emergency_type=request.emergency_type,
            outpatient_specialty=especialidade_final,
            header_config=request.header_config or HeaderConfig(),
            sections_config=request.sections_config or SectionsConfig(),
            formatting_config=request.formatting_config or FormattingConfig(),
        )
    
    # Gera a evolução usando o serviço Perplexity
    result = await perplexity_service.generate_evolution(
        raw_text=request.raw_text,
        template=template,
        patient_data=request.patient_data,
        evolution_type=request.evolution_type,
    )
    
    # Se a API falhar, tenta usar o fallback local
    if not result.get("success", False):
        # Tenta gerar com fallback local
        result = perplexity_service._generate_fallback_evolution(
            raw_text=request.raw_text,
            template=template,
            patient_data=request.patient_data,
        )
        if not result.get("success", False):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=result.get("error", "Erro ao gerar evolução")
            )
    
    # Converte seções para o formato de resposta
    sections = [
        EvolutionSection(
            title=s["title"],
            content=s["content"],
            order=s["order"]
        )
        for s in result.get("sections", [])
    ]
    
    # 2. Validação Anti-Invenção
    validacao = validar_anti_invencao(request.raw_text, result.get("formatted_text", ""))

    # Monta metadados (incluindo identificação e validação)
    metadata = {
        "model_used": result.get("model_used", "unknown"),
        "validation_errors": validacao.erros,
        "validation_warnings": validacao.avisos,
        "validation_passed": validacao.passou,
    }
    if identificacao:
        metadata["detected_context"] = contexto_final.value
        metadata["detected_specialty"] = especialidade_final.value
        metadata["detection_confidence"] = round(identificacao.confianca, 2)
    if result.get("warning"):
        metadata["warning"] = result["warning"]
    
    return EvolutionGenerateResponse(
        id=str(uuid.uuid4()),
        formatted_text=result["formatted_text"],
        sections=sections,
        template_used=request.template_id,
        created_at=datetime.now(),
        processing_time_ms=result.get("processing_time_ms", 0),
        metadata=metadata,
    )


@router.post("/preview", response_model=EvolutionGenerateResponse)
async def preview_evolution(request: EvolutionGenerateRequest):
    """
    Gera uma prévia da evolução sem salvar.
    Útil para testar configurações antes de salvar um template.
    """
    # Usa a mesma lógica de generate, mas marca como preview
    response = await generate_evolution(request)
    response.metadata["is_preview"] = True
    return response
