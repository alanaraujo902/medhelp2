"""
Modelos de domínio para o Sistema de Evolução Médica.
Define as estruturas de dados principais do sistema.
"""
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


# ============================================
# NÍVEL 1: Contexto Primário
# ============================================

class PrimaryContext(str, Enum):
    """Contexto primário de trabalho do médico."""
    EMERGENCY = "emergencia"
    ICU = "uti"
    HOSPITALIZATION = "internacao"
    OUTPATIENT = "ambulatorio"
    # Contextos PA (Pronto Atendimento)
    PA_GREEN = "pa_verde"
    PA_YELLOW = "pa_amarela"
    PA_RED = "pa_vermelha"
    # PACS
    PACS_URGENCIA = "pacs_urgencia"
    PACS_CONSULTORIO = "pacs_consultorio"
    # Atenção Primária
    MFC_UBS = "mfc_ubs"
    # Clínica Privada
    PRIVATE_CLINIC = "consultorio"


# ============================================
# NÍVEL 2: Especialidade/Subcontexto
# ============================================

class EmergencyType(str, Enum):
    """Tipos de emergência disponíveis."""
    GENERAL_CLINIC = "clinica_geral"
    TRAUMA = "trauma"
    CARDIOLOGY = "cardiologica"
    NEUROLOGY = "neurologica"
    PEDIATRIC = "pediatrica"
    OBSTETRIC = "obstetrica"


class OutpatientSpecialty(str, Enum):
    """Especialidades ambulatoriais."""
    GENERAL_CLINIC = "clinica_geral"
    CARDIOLOGY = "cardiologia"
    OBSTETRICS = "obstetricia"
    PEDIATRICS = "pediatria"
    ORTHOPEDICS = "ortopedia"
    DERMATOLOGY = "dermatologia"
    PSYCHIATRY = "psiquiatria"
    NEUROLOGY = "neurologia"
    GASTROENTEROLOGY = "gastroenterologia"
    PULMONOLOGY = "pneumologia"
    ENDOCRINOLOGY = "endocrinologia"
    NEPHROLOGY = "nefrologia"
    RHEUMATOLOGY = "reumatologia"
    UROLOGY = "urologia"
    GYNECOLOGY = "ginecologia"
    # Cirurgia
    GENERAL_SURGERY = "cirurgia_geral"
    VASCULAR_SURGERY = "cirurgia_vascular"
    # Ginecologia - subespecialidades
    MASTOLOGY = "mastologia"
    PTGI = "ptgi"  # Patologias do Trato Genital Inferior
    ONCOGYNECOLOGY = "oncologia_ginecologica"
    INFERTILITY = "infertilidade"
    ENDOCRINO_GYNECOLOGY = "endocrino_ginecologia"  # Climatério
    NEUROPEDIATRICS = "neuropediatria"
    INTERNAL_MEDICINE = "medicina_interna"


class ICUType(str, Enum):
    """Tipos de UTI."""
    GENERAL = "geral"
    CORONARY = "coronariana"
    NEUROLOGICAL = "neurologica"
    PEDIATRIC = "pediatrica"
    NEONATAL = "neonatal"


class HospitalizationType(str, Enum):
    """Tipos de internação."""
    CLINICAL = "clinica"
    SURGICAL = "cirurgica"
    OBSTETRIC = "obstetrica"
    PEDIATRIC = "pediatrica"


# ============================================
# NÍVEL 3: Configuração de Seções
# ============================================

class HeaderConfig(BaseModel):
    """Configuração do cabeçalho da evolução."""
    include_name: bool = True
    include_age: bool = True
    include_occupation: bool = False
    include_birthplace: bool = False
    include_sexual_orientation: bool = False
    include_comorbidities: bool = True
    include_medications: bool = True
    include_allergies: bool = True
    include_previous_surgeries: bool = False
    include_family_history: bool = False
    
    # Campos específicos para Obstetrícia
    include_gestational_age: bool = False
    include_gpa: bool = False  # Gestação/Para/Aborto
    include_rapid_tests: bool = False
    
    # Campos específicos para Internação
    include_bed: bool = False
    include_admission_date: bool = False


class SectionsConfig(BaseModel):
    """Configuração das seções da evolução."""
    include_hda: bool = True  # História da Doença Atual
    include_physical_exam: bool = True
    include_complementary_exams: bool = True
    include_assessment: bool = True  # Impressão/Avaliação
    include_plan: bool = True  # Conduta/Plano

    # Seções opcionais por contexto
    include_reevaluation: bool = False  # Para internação
    include_daily_evolution: bool = False  # Evolução diária
    include_subjective: bool = False  # Estilo SOAP / EEM
    include_conversion_block: bool = False  # "Converso em linguagem leiga..." (PACS Consultório)
    include_pulses_table: bool = False  # Tabela de Pulsos D/E (Cirurgia Vascular)


# ============================================
# NÍVEL 4: Detalhamento de Formatação
# ============================================

class TitleFormat(str, Enum):
    """Formato do título das seções."""
    UPPERCASE = "maiusculas"
    CAPITALIZE = "primeira_maiuscula"
    LOWERCASE = "minusculas"


class SectionTitleOption(str, Enum):
    """Opções de título para seção HDA."""
    HDA = "HDA"
    FULL_NAME = "História da Doença Atual"
    WITH_COMPLAINT = "Queixa Principal e HDA"
    CUSTOM = "custom"


class ExamOrganization(str, Enum):
    """Organização dos exames."""
    BY_MODALITY = "por_modalidade"  # Labs, Imagem, ECG
    CHRONOLOGICAL = "cronologica"


class ReferenceValues(str, Enum):
    """Quando incluir valores de referência."""
    ALWAYS = "sempre"
    ONLY_ALTERED = "so_alterado"
    NEVER = "nunca"


class MeasurementUnits(str, Enum):
    """Quando incluir unidades de medida."""
    ALWAYS_OMIT = "sempre_omitir"
    ALWAYS_INCLUDE = "sempre_incluir"


class LabFormat(str, Enum):
    """Formato de exibição dos exames laboratoriais."""
    COMPACT = "compacto"  # Hb 12,5 / Ht 37 | Leu 8.500
    DETAILED = "detalhado"  # Hemoglobina: 12,5 g/dL


class AbbreviationLevel(str, Enum):
    """Nível de uso de abreviações."""
    MAXIMUM = "maximo"  # HAS, DM, DPOC, BEG, etc
    MODERATE = "moderado"  # Só doenças comuns
    MINIMUM = "minimo"  # Escrever por extenso


class MedicationFormat(str, Enum):
    """Formato de medicações."""
    ABBREVIATED = "abreviado"  # AAS, IECA, BRA
    FULL = "extenso"  # Ácido acetilsalicílico


class SectionFormatConfig(BaseModel):
    """Configuração de formatação de uma seção."""
    title_option: SectionTitleOption = SectionTitleOption.HDA
    custom_title: Optional[str] = None
    title_format: TitleFormat = TitleFormat.UPPERCASE
    include_date: bool = True
    date_format: str = "DD/MM"


class ExamFormatConfig(BaseModel):
    """Configuração de formatação de exames."""
    organization: ExamOrganization = ExamOrganization.BY_MODALITY
    reference_values: ReferenceValues = ReferenceValues.ONLY_ALTERED
    measurement_units: MeasurementUnits = MeasurementUnits.ALWAYS_OMIT
    lab_format: LabFormat = LabFormat.COMPACT


class AbbreviationConfig(BaseModel):
    """Configuração de abreviações."""
    medical_abbreviations: AbbreviationLevel = AbbreviationLevel.MAXIMUM
    medication_format: MedicationFormat = MedicationFormat.ABBREVIATED


class FormattingConfig(BaseModel):
    """Configuração completa de formatação."""
    hda_format: SectionFormatConfig = Field(default_factory=SectionFormatConfig)
    exam_format: ExamFormatConfig = Field(default_factory=ExamFormatConfig)
    abbreviations: AbbreviationConfig = Field(default_factory=AbbreviationConfig)


# ============================================
# Modelo Completo de Template
# ============================================

class EvolutionTemplate(BaseModel):
    """Template completo de evolução médica."""
    id: Optional[str] = None
    name: str
    is_default: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    # Nível 1
    primary_context: PrimaryContext
    
    # Nível 2 - Subcontexto (apenas um será preenchido)
    emergency_type: Optional[EmergencyType] = None
    outpatient_specialty: Optional[OutpatientSpecialty] = None
    icu_type: Optional[ICUType] = None
    hospitalization_type: Optional[HospitalizationType] = None
    
    # Nível 3
    header_config: HeaderConfig = Field(default_factory=HeaderConfig)
    sections_config: SectionsConfig = Field(default_factory=SectionsConfig)
    
    # Nível 4
    formatting_config: FormattingConfig = Field(default_factory=FormattingConfig)


# ============================================
# Tipos de Evolução por Contexto
# ============================================

class EmergencyEvolutionType(str, Enum):
    """Tipos de evolução em contexto de emergência."""
    DISCHARGE_SAME_VISIT = "alta_mesmo_atendimento"
    EXAMS_PRESCRIPTION_REEVALUATION = "exames_prescricao_reavaliacao"
    REEVALUATION_DISCHARGE = "reavaliacao_alta"
    REEVALUATION_HOSPITALIZATION = "reavaliacao_internacao"


class HospitalizationEvolutionType(str, Enum):
    """Tipos de evolução em contexto de internação."""
    ADMISSION_NOTE = "nota_internacao"
    DAILY_EVOLUTION = "evolucao_dia"
    DISCHARGE_NOTE = "nota_alta"
    TRANSFER_NOTE = "nota_transferencia"


# ============================================
# Dados do Paciente e Evolução
# ============================================

class PatientData(BaseModel):
    """Dados do paciente para a evolução."""
    name: Optional[str] = None
    age: Optional[str] = None
    occupation: Optional[str] = None
    birthplace: Optional[str] = None
    sexual_orientation: Optional[str] = None
    comorbidities: Optional[str] = None
    medications: Optional[str] = None
    allergies: Optional[str] = None
    previous_surgeries: Optional[str] = None
    family_history: Optional[str] = None
    
    # Obstetrícia
    gestational_age: Optional[str] = None
    gpa: Optional[str] = None
    rapid_tests: Optional[str] = None
    
    # Internação
    bed: Optional[str] = None
    admission_date: Optional[str] = None


class EvolutionInput(BaseModel):
    """Entrada de texto livre para geração da evolução."""
    raw_text: str = Field(..., description="Texto corrido com informações do atendimento")
    template_id: Optional[str] = None
    patient_data: Optional[PatientData] = None
    evolution_type: Optional[str] = None  # Tipo específico de evolução


class GeneratedEvolution(BaseModel):
    """Evolução gerada pelo sistema."""
    id: Optional[str] = None
    template_id: Optional[str] = None
    formatted_text: str
    sections: Dict[str, str] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)
    metadata: Dict[str, Any] = Field(default_factory=dict)
