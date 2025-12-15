'use client';

import { useRouter } from 'next/navigation';
import { ArrowLeft, ArrowRight } from 'lucide-react';
import { Button, Card, CardContent } from '@/components/ui';
import {
  StepIndicator,
  Step1Context,
  Step2Subcontext,
  Step3Sections,
  Step4Formatting,
  Step5Save,
} from '@/components/wizard';
import { useWizardStore } from '@/store/wizardStore';

const steps = [
  { id: 1, title: 'Contexto' },
  { id: 2, title: 'Especialidade' },
  { id: 3, title: 'Seções' },
  { id: 4, title: 'Formatação' },
  { id: 5, title: 'Salvar' },
];

export default function ConfigurePage() {
  const router = useRouter();
  const {
    currentStep,
    nextStep,
    prevStep,
    setStep,
    primaryContext,
    subContext,
    reset,
  } = useWizardStore();

  const canProceed = () => {
    switch (currentStep) {
      case 1:
        return !!primaryContext;
      case 2:
        return !!subContext;
      default:
        return true;
    }
  };

  const handleSave = () => {
    reset();
    router.push('/');
  };

  const handleTest = () => {
    router.push('/');
  };

  const renderStep = () => {
    switch (currentStep) {
      case 1:
        return <Step1Context />;
      case 2:
        return <Step2Subcontext />;
      case 3:
        return <Step3Sections />;
      case 4:
        return <Step4Formatting />;
      case 5:
        return <Step5Save onSave={handleSave} onTest={handleTest} />;
      default:
        return <Step1Context />;
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Configurar Modelo</h1>
        <p className="text-gray-500 mt-2">
          Crie um modelo personalizado para suas evoluções médicas
        </p>
      </div>

      <StepIndicator
        steps={steps}
        currentStep={currentStep}
        onStepClick={setStep}
      />

      <Card variant="bordered" className="mb-6">
        <CardContent className="py-8">
          {renderStep()}
        </CardContent>
      </Card>

      {/* Navegação */}
      <div className="flex items-center justify-between">
        <Button
          variant="outline"
          onClick={prevStep}
          disabled={currentStep === 1}
        >
          <ArrowLeft className="w-4 h-4 mr-2" />
          Anterior
        </Button>

        {currentStep < 5 && (
          <Button
            onClick={nextStep}
            disabled={!canProceed()}
          >
            Próximo
            <ArrowRight className="w-4 h-4 ml-2" />
          </Button>
        )}
      </div>
    </div>
  );
}
