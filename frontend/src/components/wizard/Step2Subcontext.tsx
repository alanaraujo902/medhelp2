'use client';

import { RadioGroup, RadioGroupItem } from '@/components/ui';
import { useWizardStore } from '@/store/wizardStore';

const subcontextOptions: Record<string, { title: string; options: { value: string; label: string }[] }> = {
  emergencia: {
    title: 'Tipo de emergência?',
    options: [
      { value: 'clinica_geral', label: 'Clínica Geral' },
      { value: 'obstetrica', label: 'Obstétrica (EO)' },
      { value: 'pediatrica', label: 'Pediátrica (EmerPed)' },
      { value: 'trauma', label: 'Trauma/Cirurgia' },
    ],
  },
  pacs: {
    title: 'Qual ambiente PACS?',
    options: [
      { value: 'pacs_urgencia', label: 'Urgência (Compacto S/O/E/I/C/P)' },
      { value: 'pacs_consultorio', label: 'Consultório (Intermediário + Conversão)' },
    ],
  },
  ambulatorio: {
    title: 'Qual especialidade?',
    options: [
      { value: 'clinica_geral', label: 'Clínica Geral' },
      { value: 'cirurgia_vascular', label: 'Cirurgia Vascular (Tabela de Pulsos)' },
      { value: 'endocrinologia', label: 'Endocrinologia (Recordatório/RS)' },
      { value: 'psiquiatria', label: 'Psiquiatria (HMIPV)' },
      { value: 'ginecologia', label: 'Ginecologia Geral' },
      { value: 'mastologia', label: 'Mastologia (Exame Lateralidade)' },
      { value: 'ptgi', label: 'PTGI (Colposcopia/Schiller)' },
      { value: 'infertilidade', label: 'Infertilidade (Reserva Ovariana)' },
      { value: 'oncologia_ginecologica', label: 'Oncologia Ginecológica' },
    ],
  },
  internacao: {
    title: 'Tipo de unidade?',
    options: [
      { value: 'clinica', label: 'Enfermaria Clínica' },
      { value: 'psiquiatrica', label: 'Internação Psiquiátrica (EEM Completo)' },
      { value: 'obstetrica', label: 'Maternidade (Alojamento Conjunto)' },
      { value: 'uti_neo', label: 'UTI Neonatal' },
    ],
  },
  uti: {
    title: 'Tipo de UTI?',
    options: [
      { value: 'geral', label: 'UTI Geral' },
      { value: 'coronariana', label: 'UTI Coronariana' },
      { value: 'neurologica', label: 'UTI Neurológica' },
      { value: 'pediatrica', label: 'UTI Pediátrica' },
      { value: 'neonatal', label: 'UTI Neonatal' },
    ],
  },
  mfc_ubs: {
    title: 'Tipo de atendimento UBS?',
    options: [
      { value: 'consulta_geral', label: 'Consulta Longitudinal' },
      { value: 'pre_natal_br', label: 'Pré-Natal Baixo Risco' },
      { value: 'puericultura', label: 'Puericultura' },
      { value: 'visita_domiciliar', label: 'Visita Domiciliar' },
    ],
  },
  consultorio: {
    title: 'Padrão DocctorMed?',
    options: [
      { value: 'consulta_geral', label: 'Consulta Particular' },
      { value: 'aso_masculino', label: 'ASO - Masculino' },
      { value: 'aso_feminino', label: 'ASO - Feminino' },
    ],
  },
};

export function Step2Subcontext() {
  const { primaryContext, subContext, setSubContext } = useWizardStore();

  if (!primaryContext) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500">Por favor, selecione um contexto primário primeiro.</p>
      </div>
    );
  }

  // Fallback para contextos não mapeados (UTI segue padrão Internação)
  const contextConfig = subcontextOptions[primaryContext] ?? subcontextOptions.internacao;

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-900">{contextConfig.title}</h2>
        <p className="text-gray-500 mt-2">Personalize o modelo para sua rotina específica</p>
      </div>

      <RadioGroup
        name="subcontext"
        value={subContext || ''}
        onChange={setSubContext}
        className="grid grid-cols-1 md:grid-cols-2 gap-3"
      >
        {contextConfig.options.map((option) => (
          <RadioGroupItem key={option.value} value={option.value} label={option.label} />
        ))}
      </RadioGroup>
    </div>
  );
}
