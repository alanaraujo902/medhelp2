"""
Serviço de gerenciamento de templates de evolução médica.
Implementa operações CRUD e gerenciamento de templates pré-configurados.
"""
from typing import List, Optional, Dict
from datetime import datetime
import uuid

from app.models.evolution import (
    EvolutionTemplate,
    PrimaryContext,
    EmergencyType,
    OutpatientSpecialty,
    ICUType,
    HospitalizationType,
    HeaderConfig,
    SectionsConfig,
    FormattingConfig,
    SectionFormatConfig,
    ExamFormatConfig,
    AbbreviationConfig,
    TitleFormat,
    SectionTitleOption,
    ExamOrganization,
    ReferenceValues,
    MeasurementUnits,
    LabFormat,
    AbbreviationLevel,
    MedicationFormat,
)
from app.schemas.evolution import (
    TemplateCreateRequest,
    TemplateUpdateRequest,
    TemplateResponse,
    PresetTemplate,
)


class TemplateService:
    """Serviço para gerenciamento de templates de evolução."""
    
    def __init__(self):
        """Inicializa o serviço com armazenamento em memória."""
        self._templates: Dict[str, EvolutionTemplate] = {}
        self._initialize_preset_templates()
    
    def _initialize_preset_templates(self):
        """Inicializa templates pré-configurados do sistema."""
        presets = [
            # Emergência Clínica - Padrão SOAP
            EvolutionTemplate(
                id="preset-emergency-soap",
                name="Emergência Clínica - Padrão SOAP",
                is_default=False,
                primary_context=PrimaryContext.EMERGENCY,
                emergency_type=EmergencyType.GENERAL_CLINIC,
                header_config=HeaderConfig(
                    include_name=True,
                    include_age=True,
                    include_comorbidities=True,
                    include_medications=True,
                    include_allergies=True,
                ),
                sections_config=SectionsConfig(
                    include_hda=True,
                    include_physical_exam=True,
                    include_complementary_exams=True,
                    include_assessment=True,
                    include_plan=True,
                    include_subjective=True,
                ),
                formatting_config=FormattingConfig(
                    hda_format=SectionFormatConfig(
                        title_option=SectionTitleOption.WITH_COMPLAINT,
                        title_format=TitleFormat.UPPERCASE,
                        include_date=True,
                    ),
                    exam_format=ExamFormatConfig(
                        organization=ExamOrganization.BY_MODALITY,
                        reference_values=ReferenceValues.ONLY_ALTERED,
                        lab_format=LabFormat.COMPACT,
                    ),
                    abbreviations=AbbreviationConfig(
                        medical_abbreviations=AbbreviationLevel.MAXIMUM,
                        medication_format=MedicationFormat.ABBREVIATED,
                    ),
                ),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            
            # UTI - Evolução Diária Completa
            EvolutionTemplate(
                id="preset-icu-daily",
                name="UTI - Evolução Diária Completa",
                is_default=False,
                primary_context=PrimaryContext.ICU,
                icu_type=ICUType.GENERAL,
                header_config=HeaderConfig(
                    include_name=True,
                    include_age=True,
                    include_comorbidities=True,
                    include_medications=True,
                    include_allergies=True,
                    include_previous_surgeries=True,
                    include_bed=True,
                    include_admission_date=True,
                ),
                sections_config=SectionsConfig(
                    include_hda=True,
                    include_physical_exam=True,
                    include_complementary_exams=True,
                    include_assessment=True,
                    include_plan=True,
                    include_daily_evolution=True,
                ),
                formatting_config=FormattingConfig(
                    hda_format=SectionFormatConfig(
                        title_option=SectionTitleOption.FULL_NAME,
                        title_format=TitleFormat.UPPERCASE,
                        include_date=True,
                    ),
                    exam_format=ExamFormatConfig(
                        organization=ExamOrganization.CHRONOLOGICAL,
                        reference_values=ReferenceValues.ALWAYS,
                        lab_format=LabFormat.DETAILED,
                    ),
                    abbreviations=AbbreviationConfig(
                        medical_abbreviations=AbbreviationLevel.MODERATE,
                        medication_format=MedicationFormat.FULL,
                    ),
                ),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            
            # Internação - Modelo CFM Padrão
            EvolutionTemplate(
                id="preset-hospitalization-cfm",
                name="Internação - Modelo CFM Padrão",
                is_default=False,
                primary_context=PrimaryContext.HOSPITALIZATION,
                hospitalization_type=HospitalizationType.CLINICAL,
                header_config=HeaderConfig(
                    include_name=True,
                    include_age=True,
                    include_comorbidities=True,
                    include_medications=True,
                    include_allergies=True,
                    include_previous_surgeries=True,
                    include_bed=True,
                    include_admission_date=True,
                ),
                sections_config=SectionsConfig(
                    include_hda=True,
                    include_physical_exam=True,
                    include_complementary_exams=True,
                    include_assessment=True,
                    include_plan=True,
                    include_reevaluation=True,
                ),
                formatting_config=FormattingConfig(
                    hda_format=SectionFormatConfig(
                        title_option=SectionTitleOption.FULL_NAME,
                        title_format=TitleFormat.CAPITALIZE,
                        include_date=True,
                    ),
                    exam_format=ExamFormatConfig(
                        organization=ExamOrganization.BY_MODALITY,
                        reference_values=ReferenceValues.ONLY_ALTERED,
                        lab_format=LabFormat.DETAILED,
                    ),
                    abbreviations=AbbreviationConfig(
                        medical_abbreviations=AbbreviationLevel.MODERATE,
                        medication_format=MedicationFormat.FULL,
                    ),
                ),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            
            # Ambulatório - Consulta Particular
            EvolutionTemplate(
                id="preset-outpatient-private",
                name="Ambulatório - Consulta Particular",
                is_default=False,
                primary_context=PrimaryContext.OUTPATIENT,
                outpatient_specialty=OutpatientSpecialty.GENERAL_CLINIC,
                header_config=HeaderConfig(
                    include_name=True,
                    include_age=True,
                    include_occupation=True,
                    include_comorbidities=True,
                    include_medications=True,
                    include_allergies=True,
                    include_family_history=True,
                ),
                sections_config=SectionsConfig(
                    include_hda=True,
                    include_physical_exam=True,
                    include_complementary_exams=True,
                    include_assessment=True,
                    include_plan=True,
                ),
                formatting_config=FormattingConfig(
                    hda_format=SectionFormatConfig(
                        title_option=SectionTitleOption.FULL_NAME,
                        title_format=TitleFormat.CAPITALIZE,
                        include_date=True,
                    ),
                    exam_format=ExamFormatConfig(
                        organization=ExamOrganization.BY_MODALITY,
                        reference_values=ReferenceValues.ALWAYS,
                        lab_format=LabFormat.DETAILED,
                    ),
                    abbreviations=AbbreviationConfig(
                        medical_abbreviations=AbbreviationLevel.MINIMUM,
                        medication_format=MedicationFormat.FULL,
                    ),
                ),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            
            # Ambulatório - SUS/Público
            EvolutionTemplate(
                id="preset-outpatient-sus",
                name="Ambulatório - SUS/Público",
                is_default=False,
                primary_context=PrimaryContext.OUTPATIENT,
                outpatient_specialty=OutpatientSpecialty.GENERAL_CLINIC,
                header_config=HeaderConfig(
                    include_name=True,
                    include_age=True,
                    include_comorbidities=True,
                    include_medications=True,
                    include_allergies=True,
                ),
                sections_config=SectionsConfig(
                    include_hda=True,
                    include_physical_exam=True,
                    include_complementary_exams=True,
                    include_assessment=True,
                    include_plan=True,
                ),
                formatting_config=FormattingConfig(
                    hda_format=SectionFormatConfig(
                        title_option=SectionTitleOption.HDA,
                        title_format=TitleFormat.UPPERCASE,
                        include_date=True,
                    ),
                    exam_format=ExamFormatConfig(
                        organization=ExamOrganization.BY_MODALITY,
                        reference_values=ReferenceValues.ONLY_ALTERED,
                        lab_format=LabFormat.COMPACT,
                    ),
                    abbreviations=AbbreviationConfig(
                        medical_abbreviations=AbbreviationLevel.MAXIMUM,
                        medication_format=MedicationFormat.ABBREVIATED,
                    ),
                ),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
        ]
        
        for preset in presets:
            self._templates[preset.id] = preset
    
    def create_template(self, request: TemplateCreateRequest) -> EvolutionTemplate:
        """Cria um novo template."""
        template_id = str(uuid.uuid4())
        now = datetime.now()
        
        template = EvolutionTemplate(
            id=template_id,
            name=request.name,
            is_default=request.is_default,
            primary_context=request.primary_context,
            emergency_type=request.emergency_type,
            outpatient_specialty=request.outpatient_specialty,
            icu_type=request.icu_type,
            hospitalization_type=request.hospitalization_type,
            header_config=request.header_config,
            sections_config=request.sections_config,
            formatting_config=request.formatting_config,
            created_at=now,
            updated_at=now,
        )
        
        # Se marcado como padrão, remove o padrão dos outros
        if request.is_default:
            self._clear_default_flag()
        
        self._templates[template_id] = template
        return template
    
    def get_template(self, template_id: str) -> Optional[EvolutionTemplate]:
        """Obtém um template pelo ID."""
        return self._templates.get(template_id)
    
    def get_all_templates(self) -> List[EvolutionTemplate]:
        """Obtém todos os templates."""
        return list(self._templates.values())
    
    def get_user_templates(self) -> List[EvolutionTemplate]:
        """Obtém apenas templates criados pelo usuário (não presets)."""
        return [t for t in self._templates.values() if not t.id.startswith("preset-")]
    
    def get_preset_templates(self) -> List[EvolutionTemplate]:
        """Obtém apenas templates pré-configurados."""
        return [t for t in self._templates.values() if t.id.startswith("preset-")]
    
    def update_template(self, template_id: str, request: TemplateUpdateRequest) -> Optional[EvolutionTemplate]:
        """Atualiza um template existente."""
        template = self._templates.get(template_id)
        if not template:
            return None
        
        # Atualiza apenas campos fornecidos
        update_data = request.model_dump(exclude_unset=True)
        
        for field, value in update_data.items():
            if value is not None:
                setattr(template, field, value)
        
        template.updated_at = datetime.now()
        
        # Se marcado como padrão, remove o padrão dos outros
        if request.is_default:
            self._clear_default_flag(except_id=template_id)
        
        self._templates[template_id] = template
        return template
    
    def delete_template(self, template_id: str) -> bool:
        """Remove um template."""
        if template_id in self._templates:
            # Não permite deletar presets
            if template_id.startswith("preset-"):
                return False
            del self._templates[template_id]
            return True
        return False
    
    def get_default_template(self) -> Optional[EvolutionTemplate]:
        """Obtém o template marcado como padrão."""
        for template in self._templates.values():
            if template.is_default:
                return template
        return None
    
    def _clear_default_flag(self, except_id: Optional[str] = None):
        """Remove a flag de padrão de todos os templates, exceto o especificado."""
        for template_id, template in self._templates.items():
            if template_id != except_id and template.is_default:
                template.is_default = False
                template.updated_at = datetime.now()


# Instância singleton do serviço
template_service = TemplateService()
