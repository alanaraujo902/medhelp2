"""
Schemas de Request/Response para a API de Evolução Médica.
Define os contratos de entrada e saída dos endpoints.
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

from app.models.evolution import (
    PrimaryContext,
    EmergencyType,
    OutpatientSpecialty,
    ICUType,
    HospitalizationType,
    HeaderConfig,
    SectionsConfig,
    FormattingConfig,
    PatientData,
)


# ============================================
# Schemas de Template
# ============================================

class TemplateCreateRequest(BaseModel):
    """Request para criar um novo template."""
    name: str = Field(..., min_length=1, max_length=100)
    is_default: bool = False
    primary_context: PrimaryContext
    emergency_type: Optional[EmergencyType] = None
    outpatient_specialty: Optional[OutpatientSpecialty] = None
    icu_type: Optional[ICUType] = None
    hospitalization_type: Optional[HospitalizationType] = None
    header_config: HeaderConfig = Field(default_factory=HeaderConfig)
    sections_config: SectionsConfig = Field(default_factory=SectionsConfig)
    formatting_config: FormattingConfig = Field(default_factory=FormattingConfig)


class TemplateUpdateRequest(BaseModel):
    """Request para atualizar um template existente."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    is_default: Optional[bool] = None
    primary_context: Optional[PrimaryContext] = None
    emergency_type: Optional[EmergencyType] = None
    outpatient_specialty: Optional[OutpatientSpecialty] = None
    icu_type: Optional[ICUType] = None
    hospitalization_type: Optional[HospitalizationType] = None
    header_config: Optional[HeaderConfig] = None
    sections_config: Optional[SectionsConfig] = None
    formatting_config: Optional[FormattingConfig] = None


class TemplateResponse(BaseModel):
    """Response com dados do template."""
    id: str
    name: str
    is_default: bool
    primary_context: PrimaryContext
    emergency_type: Optional[EmergencyType] = None
    outpatient_specialty: Optional[OutpatientSpecialty] = None
    icu_type: Optional[ICUType] = None
    hospitalization_type: Optional[HospitalizationType] = None
    header_config: HeaderConfig
    sections_config: SectionsConfig
    formatting_config: FormattingConfig
    created_at: datetime
    updated_at: datetime


class TemplateListResponse(BaseModel):
    """Response com lista de templates."""
    templates: List[TemplateResponse]
    total: int


# ============================================
# Schemas de Geração de Evolução
# ============================================

class EvolutionGenerateRequest(BaseModel):
    """Request para gerar uma evolução formatada."""
    raw_text: str = Field(..., min_length=10, description="Texto corrido com informações do atendimento")
    template_id: Optional[str] = None
    patient_data: Optional[PatientData] = None
    evolution_type: Optional[str] = None
    
    # Configurações inline (se não usar template)
    primary_context: Optional[PrimaryContext] = None
    emergency_type: Optional[EmergencyType] = None
    outpatient_specialty: Optional[OutpatientSpecialty] = None
    header_config: Optional[HeaderConfig] = None
    sections_config: Optional[SectionsConfig] = None
    formatting_config: Optional[FormattingConfig] = None


class EvolutionSection(BaseModel):
    """Seção individual da evolução."""
    title: str
    content: str
    order: int


class EvolutionGenerateResponse(BaseModel):
    """Response com a evolução gerada."""
    id: str
    formatted_text: str
    sections: List[EvolutionSection]
    template_used: Optional[str] = None
    created_at: datetime
    processing_time_ms: int
    metadata: Dict[str, Any] = Field(default_factory=dict)


# ============================================
# Schemas de Opções de Configuração
# ============================================

class ContextOption(BaseModel):
    """Opção de contexto para seleção."""
    value: str
    label: str
    description: Optional[str] = None


class SubcontextOptions(BaseModel):
    """Opções de subcontexto baseadas no contexto primário."""
    context: PrimaryContext
    options: List[ContextOption]


class ConfigurationOptionsResponse(BaseModel):
    """Response com todas as opções de configuração disponíveis."""
    primary_contexts: List[ContextOption]
    emergency_types: List[ContextOption]
    outpatient_specialties: List[ContextOption]
    icu_types: List[ContextOption]
    hospitalization_types: List[ContextOption]
    title_formats: List[ContextOption]
    exam_organizations: List[ContextOption]
    reference_value_options: List[ContextOption]
    abbreviation_levels: List[ContextOption]
    medication_formats: List[ContextOption]


# ============================================
# Schemas de Templates Pré-configurados
# ============================================

class PresetTemplate(BaseModel):
    """Template pré-configurado do sistema."""
    id: str
    name: str
    description: str
    primary_context: PrimaryContext
    preview: str  # Exemplo de como ficaria a evolução


class PresetTemplatesResponse(BaseModel):
    """Response com templates pré-configurados."""
    presets: List[PresetTemplate]


# ============================================
# Schemas de Erro e Status
# ============================================

class ErrorResponse(BaseModel):
    """Response de erro padrão."""
    error: str
    detail: Optional[str] = None
    code: Optional[str] = None


class HealthCheckResponse(BaseModel):
    """Response do health check."""
    status: str
    version: str
    timestamp: datetime
    services: Dict[str, str]
