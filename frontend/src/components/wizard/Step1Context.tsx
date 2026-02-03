'use client';

import { Building2, Heart, Bed, Stethoscope, Activity, Home, Briefcase } from 'lucide-react';
import { cn } from '@/lib/utils';
import { useWizardStore } from '@/store/wizardStore';
import type { PrimaryContext } from '@/types';

const contexts = [
  {
    value: 'emergencia' as PrimaryContext,
    label: 'Emergência/Pronto-Socorro',
    description: 'Atendimentos de urgência e emergência',
    icon: Building2,
    color: 'red',
  },
  {
    value: 'uti' as PrimaryContext,
    label: 'UTI',
    description: 'Unidade de Terapia Intensiva',
    icon: Heart,
    color: 'purple',
  },
  {
    value: 'internacao' as PrimaryContext,
    label: 'Internação/Enfermaria',
    description: 'Pacientes internados em enfermaria',
    icon: Bed,
    color: 'blue',
  },
  {
    value: 'ambulatorio' as PrimaryContext,
    label: 'Ambulatório/Consultório',
    description: 'Consultas ambulatoriais e de consultório',
    icon: Stethoscope,
    color: 'green',
  },
  {
    value: 'pacs' as PrimaryContext,
    label: 'PACS',
    description: 'Pronto Atendimento / Urgência compacta',
    icon: Activity,
    color: 'orange',
  },
  {
    value: 'mfc_ubs' as PrimaryContext,
    label: 'MFC/UBS',
    description: 'Medicina de Família e Comunidade',
    icon: Home,
    color: 'teal',
  },
  {
    value: 'consultorio' as PrimaryContext,
    label: 'Clínica Privada',
    description: 'Consultório particular (DocctorMed)',
    icon: Briefcase,
    color: 'slate',
  },
];

const colorClasses = {
  red: {
    selected: 'border-red-500 bg-red-50',
    icon: 'text-red-600 bg-red-100',
    hover: 'hover:border-red-300',
  },
  purple: {
    selected: 'border-purple-500 bg-purple-50',
    icon: 'text-purple-600 bg-purple-100',
    hover: 'hover:border-purple-300',
  },
  blue: {
    selected: 'border-blue-500 bg-blue-50',
    icon: 'text-blue-600 bg-blue-100',
    hover: 'hover:border-blue-300',
  },
  green: {
    selected: 'border-green-500 bg-green-50',
    icon: 'text-green-600 bg-green-100',
    hover: 'hover:border-green-300',
  },
  orange: {
    selected: 'border-orange-500 bg-orange-50',
    icon: 'text-orange-600 bg-orange-100',
    hover: 'hover:border-orange-300',
  },
  teal: {
    selected: 'border-teal-500 bg-teal-50',
    icon: 'text-teal-600 bg-teal-100',
    hover: 'hover:border-teal-300',
  },
  slate: {
    selected: 'border-slate-500 bg-slate-50',
    icon: 'text-slate-600 bg-slate-100',
    hover: 'hover:border-slate-300',
  },
};

export function Step1Context() {
  const { primaryContext, setPrimaryContext } = useWizardStore();

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-900">Onde você trabalha?</h2>
        <p className="text-gray-500 mt-2">
          Selecione o contexto principal do seu ambiente de trabalho
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {contexts.map((context) => {
          const Icon = context.icon;
          const isSelected = primaryContext === context.value;
          const colors = colorClasses[context.color as keyof typeof colorClasses];

          return (
            <button
              key={context.value}
              type="button"
              onClick={() => setPrimaryContext(context.value)}
              className={cn(
                'flex items-start gap-4 p-6 rounded-xl border-2 transition-all text-left',
                isSelected
                  ? colors.selected
                  : `border-gray-200 bg-white ${colors.hover}`
              )}
            >
              <div
                className={cn(
                  'flex-shrink-0 w-12 h-12 rounded-lg flex items-center justify-center',
                  colors.icon
                )}
              >
                <Icon className="w-6 h-6" />
              </div>
              <div>
                <h3 className="font-semibold text-gray-900">{context.label}</h3>
                <p className="text-sm text-gray-500 mt-1">{context.description}</p>
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
}
