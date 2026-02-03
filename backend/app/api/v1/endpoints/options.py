"""
Endpoints para obter opções de configuração do sistema.
Fornece listas de valores disponíveis para os formulários do frontend.
"""
from fastapi import APIRouter

from app.schemas.evolution import (
    ContextOption,
    ConfigurationOptionsResponse,
)
from app.models.evolution import (
    PrimaryContext,
    EmergencyType,
    OutpatientSpecialty,
    ICUType,
    HospitalizationType,
    TitleFormat,
    ExamOrganization,
    ReferenceValues,
    AbbreviationLevel,
    MedicationFormat,
)

router = APIRouter(prefix="/options", tags=["Options"])


def _enum_to_options(enum_class, labels: dict) -> list:
    """Converte um Enum para lista de opções."""
    return [
        ContextOption(
            value=item.value,
            label=labels.get(item.value, item.value),
        )
        for item in enum_class
    ]


@router.get("", response_model=ConfigurationOptionsResponse)
async def get_all_options():
    """
    Retorna todas as opções de configuração disponíveis.
    Usado para popular os formulários de configuração no frontend.
    """
    
    # Labels em português para cada opção
    primary_context_labels = {
        "emergencia": "Emergência/Pronto-Socorro",
        "uti": "UTI",
        "internacao": "Internação/Enfermaria",
        "ambulatorio": "Ambulatório/Consultório",
        "pa_verde": "PA Sala Verde",
        "pa_amarela": "PA Sala Amarela",
        "pa_vermelha": "PA Sala Vermelha",
        "pacs_urgencia": "PACS Urgência",
        "pacs_consultorio": "PACS Consultórios",
        "mfc_ubs": "MFC/UBS",
        "consultorio": "Consultório Privado",
    }
    
    emergency_type_labels = {
        "clinica_geral": "Clínica Geral",
        "trauma": "Trauma",
        "cardiologica": "Cardiológica",
        "neurologica": "Neurológica",
        "pediatrica": "Pediátrica",
        "obstetrica": "Obstétrica",
    }
    
    outpatient_specialty_labels = {
        "clinica_geral": "Clínica Geral",
        "cardiologia": "Cardiologia",
        "obstetricia": "Obstetrícia",
        "pediatria": "Pediatria",
        "ortopedia": "Ortopedia",
        "dermatologia": "Dermatologia",
        "psiquiatria": "Psiquiatria",
        "neurologia": "Neurologia",
        "gastroenterologia": "Gastroenterologia",
        "pneumologia": "Pneumologia",
        "endocrinologia": "Endocrinologia",
        "nefrologia": "Nefrologia",
        "reumatologia": "Reumatologia",
        "urologia": "Urologia",
        "ginecologia": "Ginecologia",
        "cirurgia_geral": "Cirurgia Geral",
        "cirurgia_vascular": "Cirurgia Vascular",
        "mastologia": "Mastologia",
        "ptgi": "PTGI",
        "oncologia_ginecologica": "Oncologia Ginecológica",
        "infertilidade": "Infertilidade",
        "endocrino_ginecologia": "Endócrino-Ginecologia",
        "neuropediatria": "Neuropediatria",
        "medicina_interna": "Medicina Interna",
    }
    
    icu_type_labels = {
        "geral": "UTI Geral",
        "coronariana": "UTI Coronariana",
        "neurologica": "UTI Neurológica",
        "pediatrica": "UTI Pediátrica",
        "neonatal": "UTI Neonatal",
    }
    
    hospitalization_type_labels = {
        "clinica": "Clínica",
        "cirurgica": "Cirúrgica",
        "obstetrica": "Obstétrica",
        "pediatrica": "Pediátrica",
    }
    
    title_format_labels = {
        "maiusculas": "MAIÚSCULAS",
        "primeira_maiuscula": "Primeira Letra Maiúscula",
        "minusculas": "minúsculas",
    }
    
    exam_organization_labels = {
        "por_modalidade": "Por Modalidade (Labs, Imagem, ECG)",
        "cronologica": "Cronológica (todos juntos)",
    }
    
    reference_value_labels = {
        "sempre": "Sempre incluir (ex: VR <0,042)",
        "so_alterado": "Só se alterado",
        "nunca": "Nunca incluir",
    }
    
    abbreviation_level_labels = {
        "maximo": "Máximo (HAS, DM, DPOC, BEG, etc)",
        "moderado": "Moderado (só doenças comuns)",
        "minimo": "Mínimo (escrever por extenso)",
    }
    
    medication_format_labels = {
        "abreviado": "Abreviadas (AAS, IECA, BRA)",
        "extenso": "Por extenso (Ácido acetilsalicílico)",
    }
    
    return ConfigurationOptionsResponse(
        primary_contexts=_enum_to_options(PrimaryContext, primary_context_labels),
        emergency_types=_enum_to_options(EmergencyType, emergency_type_labels),
        outpatient_specialties=_enum_to_options(OutpatientSpecialty, outpatient_specialty_labels),
        icu_types=_enum_to_options(ICUType, icu_type_labels),
        hospitalization_types=_enum_to_options(HospitalizationType, hospitalization_type_labels),
        title_formats=_enum_to_options(TitleFormat, title_format_labels),
        exam_organizations=_enum_to_options(ExamOrganization, exam_organization_labels),
        reference_value_options=_enum_to_options(ReferenceValues, reference_value_labels),
        abbreviation_levels=_enum_to_options(AbbreviationLevel, abbreviation_level_labels),
        medication_formats=_enum_to_options(MedicationFormat, medication_format_labels),
    )


@router.get("/contexts/{context}/subtypes")
async def get_context_subtypes(context: str):
    """
    Retorna os subtipos disponíveis para um contexto primário específico.
    """
    subtypes = {
        "emergencia": _enum_to_options(EmergencyType, {
            "clinica_geral": "Clínica Geral",
            "trauma": "Trauma",
            "cardiologica": "Cardiológica",
            "neurologica": "Neurológica",
            "pediatrica": "Pediátrica",
            "obstetrica": "Obstétrica",
        }),
        "uti": _enum_to_options(ICUType, {
            "geral": "UTI Geral",
            "coronariana": "UTI Coronariana",
            "neurologica": "UTI Neurológica",
            "pediatrica": "UTI Pediátrica",
            "neonatal": "UTI Neonatal",
        }),
        "internacao": _enum_to_options(HospitalizationType, {
            "clinica": "Clínica",
            "cirurgica": "Cirúrgica",
            "obstetrica": "Obstétrica",
            "pediatrica": "Pediátrica",
        }),
        "ambulatorio": _enum_to_options(OutpatientSpecialty, outpatient_specialty_labels),
    }
    
    return {
        "context": context,
        "subtypes": subtypes.get(context, [])
    }


@router.get("/evolution-types/{context}")
async def get_evolution_types(context: str):
    """
    Retorna os tipos de evolução disponíveis para um contexto.
    """
    evolution_types = {
        "emergencia": [
            {"value": "alta_mesmo_atendimento", "label": "Alta no mesmo atendimento"},
            {"value": "exames_prescricao_reavaliacao", "label": "Exames/Prescrição + Reavaliação"},
            {"value": "reavaliacao_alta", "label": "Reavaliação com Alta"},
            {"value": "reavaliacao_internacao", "label": "Reavaliação com Internação"},
        ],
        "internacao": [
            {"value": "nota_internacao", "label": "Nota de Internação"},
            {"value": "evolucao_dia", "label": "Evolução do Dia/Rotina"},
            {"value": "nota_alta", "label": "Nota de Alta"},
            {"value": "nota_transferencia", "label": "Nota de Transferência"},
        ],
        "uti": [
            {"value": "admissao", "label": "Admissão na UTI"},
            {"value": "evolucao_diaria", "label": "Evolução Diária"},
            {"value": "alta_uti", "label": "Alta da UTI"},
        ],
        "ambulatorio": [
            {"value": "primeira_consulta", "label": "Primeira Consulta"},
            {"value": "retorno", "label": "Consulta de Retorno"},
            {"value": "urgencia", "label": "Atendimento de Urgência"},
        ],
    }
    
    return {
        "context": context,
        "evolution_types": evolution_types.get(context, [])
    }
