/**
 * Tipos TypeScript para o Sistema de Evolução Médica
 */

// ============================================
// Enums e Tipos Base
// ============================================

export type PrimaryContext = 'emergencia' | 'uti' | 'internacao' | 'ambulatorio';

export type EmergencyType = 
  | 'clinica_geral' 
  | 'trauma' 
  | 'cardiologica' 
  | 'neurologica' 
  | 'pediatrica' 
  | 'obstetrica';

export type OutpatientSpecialty = 
  | 'clinica_geral' 
  | 'cardiologia' 
  | 'obstetricia' 
  | 'pediatria'
  | 'ortopedia'
  | 'dermatologia'
  | 'psiquiatria'
  | 'neurologia'
  | 'gastroenterologia'
  | 'pneumologia'
  | 'endocrinologia'
  | 'nefrologia'
  | 'reumatologia'
  | 'urologia'
  | 'ginecologia';

export type ICUType = 
  | 'geral' 
  | 'coronariana' 
  | 'neurologica' 
  | 'pediatrica' 
  | 'neonatal';

export type HospitalizationType = 
  | 'clinica' 
  | 'cirurgica' 
  | 'obstetrica' 
  | 'pediatrica';

export type TitleFormat = 'maiusculas' | 'primeira_maiuscula' | 'minusculas';

export type SectionTitleOption = 'HDA' | 'História da Doença Atual' | 'Queixa Principal e HDA' | 'custom';

export type ExamOrganization = 'por_modalidade' | 'cronologica';

export type ReferenceValues = 'sempre' | 'so_alterado' | 'nunca';

export type MeasurementUnits = 'sempre_omitir' | 'sempre_incluir';

export type LabFormat = 'compacto' | 'detalhado';

export type AbbreviationLevel = 'maximo' | 'moderado' | 'minimo';

export type MedicationFormat = 'abreviado' | 'extenso';

// ============================================
// Configurações
// ============================================

export interface HeaderConfig {
  include_name: boolean;
  include_age: boolean;
  include_occupation: boolean;
  include_birthplace: boolean;
  include_sexual_orientation: boolean;
  include_comorbidities: boolean;
  include_medications: boolean;
  include_allergies: boolean;
  include_previous_surgeries: boolean;
  include_family_history: boolean;
  include_gestational_age: boolean;
  include_gpa: boolean;
  include_rapid_tests: boolean;
  include_bed: boolean;
  include_admission_date: boolean;
}

export interface SectionsConfig {
  include_hda: boolean;
  include_physical_exam: boolean;
  include_complementary_exams: boolean;
  include_assessment: boolean;
  include_plan: boolean;
  include_reevaluation: boolean;
  include_daily_evolution: boolean;
  include_subjective: boolean;
}

export interface SectionFormatConfig {
  title_option: SectionTitleOption;
  custom_title?: string;
  title_format: TitleFormat;
  include_date: boolean;
  date_format: string;
}

export interface ExamFormatConfig {
  organization: ExamOrganization;
  reference_values: ReferenceValues;
  measurement_units: MeasurementUnits;
  lab_format: LabFormat;
}

export interface AbbreviationConfig {
  medical_abbreviations: AbbreviationLevel;
  medication_format: MedicationFormat;
}

export interface FormattingConfig {
  hda_format: SectionFormatConfig;
  exam_format: ExamFormatConfig;
  abbreviations: AbbreviationConfig;
}

// ============================================
// Template
// ============================================

export interface EvolutionTemplate {
  id: string;
  name: string;
  is_default: boolean;
  primary_context: PrimaryContext;
  emergency_type?: EmergencyType;
  outpatient_specialty?: OutpatientSpecialty;
  icu_type?: ICUType;
  hospitalization_type?: HospitalizationType;
  header_config: HeaderConfig;
  sections_config: SectionsConfig;
  formatting_config: FormattingConfig;
  created_at: string;
  updated_at: string;
}

export interface PresetTemplate {
  id: string;
  name: string;
  description: string;
  primary_context: PrimaryContext;
  preview: string;
}

// ============================================
// Dados do Paciente
// ============================================

export interface PatientData {
  name?: string;
  age?: string;
  occupation?: string;
  birthplace?: string;
  sexual_orientation?: string;
  comorbidities?: string;
  medications?: string;
  allergies?: string;
  previous_surgeries?: string;
  family_history?: string;
  gestational_age?: string;
  gpa?: string;
  rapid_tests?: string;
  bed?: string;
  admission_date?: string;
}

// ============================================
// Evolução
// ============================================

export interface EvolutionSection {
  title: string;
  content: string;
  order: number;
}

export interface GeneratedEvolution {
  id: string;
  formatted_text: string;
  sections: EvolutionSection[];
  template_used?: string;
  created_at: string;
  processing_time_ms: number;
  metadata: Record<string, unknown>;
}

// ============================================
// Opções de Configuração
// ============================================

export interface ContextOption {
  value: string;
  label: string;
  description?: string;
}

export interface ConfigurationOptions {
  primary_contexts: ContextOption[];
  emergency_types: ContextOption[];
  outpatient_specialties: ContextOption[];
  icu_types: ContextOption[];
  hospitalization_types: ContextOption[];
  title_formats: ContextOption[];
  exam_organizations: ContextOption[];
  reference_value_options: ContextOption[];
  abbreviation_levels: ContextOption[];
  medication_formats: ContextOption[];
}

// ============================================
// API Responses
// ============================================

export interface TemplateListResponse {
  templates: EvolutionTemplate[];
  total: number;
}

export interface PresetTemplatesResponse {
  presets: PresetTemplate[];
}

export interface EvolutionGenerateRequest {
  raw_text: string;
  template_id?: string;
  patient_data?: PatientData;
  evolution_type?: string;
  primary_context?: PrimaryContext;
  emergency_type?: EmergencyType;
  outpatient_specialty?: OutpatientSpecialty;
  header_config?: HeaderConfig;
  sections_config?: SectionsConfig;
  formatting_config?: FormattingConfig;
}

export interface HealthCheckResponse {
  status: string;
  version: string;
  timestamp: string;
  services: Record<string, string>;
}

// ============================================
// Wizard State
// ============================================

export interface WizardState {
  currentStep: number;
  primaryContext?: PrimaryContext;
  subContext?: string;
  headerConfig: HeaderConfig;
  sectionsConfig: SectionsConfig;
  formattingConfig: FormattingConfig;
  templateName: string;
  isDefault: boolean;
}

export const defaultHeaderConfig: HeaderConfig = {
  include_name: true,
  include_age: true,
  include_occupation: false,
  include_birthplace: false,
  include_sexual_orientation: false,
  include_comorbidities: true,
  include_medications: true,
  include_allergies: true,
  include_previous_surgeries: false,
  include_family_history: false,
  include_gestational_age: false,
  include_gpa: false,
  include_rapid_tests: false,
  include_bed: false,
  include_admission_date: false,
};

export const defaultSectionsConfig: SectionsConfig = {
  include_hda: true,
  include_physical_exam: true,
  include_complementary_exams: true,
  include_assessment: true,
  include_plan: true,
  include_reevaluation: false,
  include_daily_evolution: false,
  include_subjective: false,
};

export const defaultFormattingConfig: FormattingConfig = {
  hda_format: {
    title_option: 'HDA',
    title_format: 'maiusculas',
    include_date: true,
    date_format: 'DD/MM',
  },
  exam_format: {
    organization: 'por_modalidade',
    reference_values: 'so_alterado',
    measurement_units: 'sempre_omitir',
    lab_format: 'compacto',
  },
  abbreviations: {
    medical_abbreviations: 'maximo',
    medication_format: 'abreviado',
  },
};
