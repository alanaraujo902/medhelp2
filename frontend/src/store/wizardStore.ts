import { create } from 'zustand';
import type {
  PrimaryContext,
  HeaderConfig,
  SectionsConfig,
  FormattingConfig,
  PatientData,
  EvolutionTemplate,
  GeneratedEvolution,
} from '@/types';
import {
  defaultHeaderConfig,
  defaultSectionsConfig,
  defaultFormattingConfig,
} from '@/types';

interface WizardStore {
  // Estado do Wizard
  currentStep: number;
  totalSteps: number;
  
  // Nível 1: Contexto Primário
  primaryContext: PrimaryContext | null;
  
  // Nível 2: Subcontexto
  subContext: string | null;
  
  // Nível 3: Configurações de Seções
  headerConfig: HeaderConfig;
  sectionsConfig: SectionsConfig;
  
  // Nível 4: Formatação
  formattingConfig: FormattingConfig;
  
  // Dados do Template
  templateName: string;
  isDefault: boolean;
  selectedTemplateId: string | null;
  
  // Dados do Paciente
  patientData: PatientData;
  
  // Texto da Evolução
  rawText: string;
  evolutionType: string | null;
  
  // Evolução Gerada
  generatedEvolution: GeneratedEvolution | null;
  isGenerating: boolean;
  
  // Ações
  setStep: (step: number) => void;
  nextStep: () => void;
  prevStep: () => void;
  
  setPrimaryContext: (context: PrimaryContext) => void;
  setSubContext: (subContext: string) => void;
  
  setHeaderConfig: (config: Partial<HeaderConfig>) => void;
  setSectionsConfig: (config: Partial<SectionsConfig>) => void;
  setFormattingConfig: (config: Partial<FormattingConfig>) => void;
  
  setTemplateName: (name: string) => void;
  setIsDefault: (isDefault: boolean) => void;
  setSelectedTemplateId: (id: string | null) => void;
  
  setPatientData: (data: Partial<PatientData>) => void;
  setRawText: (text: string) => void;
  setEvolutionType: (type: string) => void;
  
  setGeneratedEvolution: (evolution: GeneratedEvolution | null) => void;
  setIsGenerating: (isGenerating: boolean) => void;
  
  loadTemplate: (template: EvolutionTemplate) => void;
  reset: () => void;
}

const initialState = {
  currentStep: 1,
  totalSteps: 5,
  primaryContext: null,
  subContext: null,
  headerConfig: defaultHeaderConfig,
  sectionsConfig: defaultSectionsConfig,
  formattingConfig: defaultFormattingConfig,
  templateName: '',
  isDefault: false,
  selectedTemplateId: null,
  patientData: {},
  rawText: '',
  evolutionType: null,
  generatedEvolution: null,
  isGenerating: false,
};

export const useWizardStore = create<WizardStore>((set, get) => ({
  ...initialState,
  
  setStep: (step) => set({ currentStep: step }),
  
  nextStep: () => {
    const { currentStep, totalSteps } = get();
    if (currentStep < totalSteps) {
      set({ currentStep: currentStep + 1 });
    }
  },
  
  prevStep: () => {
    const { currentStep } = get();
    if (currentStep > 1) {
      set({ currentStep: currentStep - 1 });
    }
  },
  
  setPrimaryContext: (context) => {
    // Ajusta configurações baseado no contexto
    const updates: Partial<WizardStore> = {
      primaryContext: context,
      subContext: null,
    };
    
    // Configurações específicas por contexto
    if (context === 'internacao' || context === 'uti') {
      updates.headerConfig = {
        ...get().headerConfig,
        include_bed: true,
        include_admission_date: true,
      };
      updates.sectionsConfig = {
        ...get().sectionsConfig,
        include_reevaluation: true,
      };
    }
    
    if (context === 'ambulatorio') {
      updates.headerConfig = {
        ...get().headerConfig,
        include_occupation: true,
        include_family_history: true,
      };
    }
    
    set(updates);
  },
  
  setSubContext: (subContext) => {
    const updates: Partial<WizardStore> = { subContext };
    const goSubcontexts = [
      'obstetrica', 'obstetricia', 'pre_natal_br',
      'ginecologia', 'mastologia', 'ptgi', 'infertilidade', 'oncologia_ginecologica',
    ];

    // Configurações para Obstetrícia/Ginecologia
    if (goSubcontexts.includes(subContext)) {
      updates.headerConfig = {
        ...get().headerConfig,
        include_gestational_age: true,
        include_gpa: true,
        include_rapid_tests: true,
      };
    }

    // Conversão obrigatória para PACS Consultório
    if (subContext === 'pacs_consultorio') {
      updates.sectionsConfig = {
        ...get().sectionsConfig,
        include_conversion_block: true,
      };
    }

    // Tabela de pulsos para Cirurgia Vascular
    if (subContext === 'cirurgia_vascular') {
      updates.sectionsConfig = {
        ...get().sectionsConfig,
        include_pulses_table: true,
      };
    }

    set(updates);
  },
  
  setHeaderConfig: (config) => set((state) => ({
    headerConfig: { ...state.headerConfig, ...config },
  })),
  
  setSectionsConfig: (config) => set((state) => ({
    sectionsConfig: { ...state.sectionsConfig, ...config },
  })),
  
  setFormattingConfig: (config) => set((state) => ({
    formattingConfig: { ...state.formattingConfig, ...config },
  })),
  
  setTemplateName: (name) => set({ templateName: name }),
  setIsDefault: (isDefault) => set({ isDefault }),
  setSelectedTemplateId: (id) => set({ selectedTemplateId: id }),
  
  setPatientData: (data) => set((state) => ({
    patientData: { ...state.patientData, ...data },
  })),
  
  setRawText: (text) => set({ rawText: text }),
  setEvolutionType: (type) => set({ evolutionType: type }),
  
  setGeneratedEvolution: (evolution) => set({ generatedEvolution: evolution }),
  setIsGenerating: (isGenerating) => set({ isGenerating }),
  
  loadTemplate: (template) => {
    const pc = template.primary_context;
    // PACS: pacs_urgencia/pacs_consultorio → primaryContext "pacs", subContext específico
    const isPacs = pc === 'pacs_urgencia' || pc === 'pacs_consultorio';
    const primaryContext = isPacs ? 'pacs' : pc;
    const subContext = isPacs
      ? pc
      : (template.emergency_type || template.outpatient_specialty || template.icu_type || template.hospitalization_type || null);
    set({
      primaryContext,
      subContext,
      headerConfig: template.header_config,
      sectionsConfig: template.sections_config,
      formattingConfig: template.formatting_config,
      templateName: template.name,
      isDefault: template.is_default,
      selectedTemplateId: template.id,
    });
  },
  
  reset: () => set(initialState),
}));
