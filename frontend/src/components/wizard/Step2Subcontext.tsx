'use client';

import { RadioGroup, RadioGroupItem } from '@/components/ui';
import { useWizardStore } from '@/store/wizardStore';

const subcontextOptions = {
  emergencia: {
    title: 'Tipo de emergência?',
    options: [
      { value: 'clinica_geral', label: 'Clínica Geral' },
      { value: 'trauma', label: 'Trauma' },
      { value: 'cardiologica', label: 'Cardiológica' },
      { value: 'neurologica', label: 'Neurológica' },
      { value: 'pediatrica', label: 'Pediátrica' },
      { value: 'obstetrica', label: 'Obstétrica' },
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
  internacao: {
    title: 'Tipo de internação?',
    options: [
      { value: 'clinica', label: 'Clínica' },
      { value: 'cirurgica', label: 'Cirúrgica' },
      { value: 'obstetrica', label: 'Obstétrica' },
      { value: 'pediatrica', label: 'Pediátrica' },
    ],
  },
  ambulatorio: {
    title: 'Qual especialidade?',
    options: [
      { value: 'clinica_geral', label: 'Clínica Geral' },
      { value: 'cardiologia', label: 'Cardiologia' },
      { value: 'obstetricia', label: 'Obstetrícia' },
      { value: 'pediatria', label: 'Pediatria' },
      { value: 'ortopedia', label: 'Ortopedia' },
      { value: 'dermatologia', label: 'Dermatologia' },
      { value: 'psiquiatria', label: 'Psiquiatria' },
      { value: 'neurologia', label: 'Neurologia' },
      { value: 'gastroenterologia', label: 'Gastroenterologia' },
      { value: 'pneumologia', label: 'Pneumologia' },
      { value: 'endocrinologia', label: 'Endocrinologia' },
      { value: 'nefrologia', label: 'Nefrologia' },
      { value: 'reumatologia', label: 'Reumatologia' },
      { value: 'urologia', label: 'Urologia' },
      { value: 'ginecologia', label: 'Ginecologia' },
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

  const contextConfig = subcontextOptions[primaryContext];

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-900">{contextConfig.title}</h2>
        <p className="text-gray-500 mt-2">
          Selecione a especialidade ou tipo específico
        </p>
      </div>

      <RadioGroup
        name="subcontext"
        value={subContext || ''}
        onChange={setSubContext}
        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3"
      >
        {contextConfig.options.map((option) => (
          <RadioGroupItem
            key={option.value}
            value={option.value}
            label={option.label}
          />
        ))}
      </RadioGroup>
    </div>
  );
}
