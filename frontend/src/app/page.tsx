'use client';

import { useState } from 'react';
import { TemplateSelector, PatientDataForm, WritingWindow } from '@/components/evolution';
import { useWizardStore } from '@/store/wizardStore';

export default function HomePage() {
  const { selectedTemplateId } = useWizardStore();
  const [showPatientForm, setShowPatientForm] = useState(false);

  return (
    <div className="space-y-6">
      {/* Seletor de Template */}
      <TemplateSelector onCreateNew={() => window.location.href = '/configure'} />

      {/* Formulário de Dados do Paciente (colapsável) */}
      {selectedTemplateId && (
        <div>
          <button
            onClick={() => setShowPatientForm(!showPatientForm)}
            className="text-sm text-blue-600 hover:text-blue-700 mb-4"
          >
            {showPatientForm ? '▼ Ocultar dados do paciente' : '▶ Adicionar dados do paciente (opcional)'}
          </button>
          {showPatientForm && <PatientDataForm />}
        </div>
      )}

      {/* Janela de Escrita */}
      <WritingWindow />
    </div>
  );
}
