'use client';

import { useState } from 'react';
import { Save, Eye, FileText } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent, Input, Checkbox, Button } from '@/components/ui';
import { useWizardStore } from '@/store/wizardStore';
import { createTemplate } from '@/lib/api';
import type { 
  EvolutionTemplate, 
  EmergencyType, 
  OutpatientSpecialty, 
  ICUType, 
  HospitalizationType 
} from '@/types';

interface Step5SaveProps {
  onSave?: () => void;
  onTest?: () => void;
}

export function Step5Save({ onSave, onTest }: Step5SaveProps) {
  const {
    templateName,
    setTemplateName,
    isDefault,
    setIsDefault,
    primaryContext,
    subContext,
    headerConfig,
    sectionsConfig,
    formattingConfig,
  } = useWizardStore();

  const [isSaving, setIsSaving] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);
  const [saveSuccess, setSaveSuccess] = useState(false);

  const handleSave = async () => {
    if (!templateName.trim()) {
      setSaveError('Por favor, insira um nome para o modelo');
      return;
    }

    if (!primaryContext) {
      setSaveError('Configuração incompleta. Por favor, revise os passos anteriores.');
      return;
    }

    setIsSaving(true);
    setSaveError(null);

    try {
      // PACS: primary_context vem do subContext (pacs_urgencia ou pacs_consultorio)
      const effectivePrimaryContext =
        primaryContext === 'pacs' && subContext
          ? subContext
          : primaryContext;

      const templateData: Partial<EvolutionTemplate> = {
        name: templateName,
        is_default: isDefault,
        primary_context: effectivePrimaryContext as EvolutionTemplate['primary_context'],
        header_config: headerConfig,
        sections_config: sectionsConfig,
        formatting_config: formattingConfig,
      };

      // Adiciona campos específicos baseado no contexto
      if (primaryContext === 'emergencia' && subContext) {
        templateData.emergency_type = subContext as EmergencyType;
      }
      if (primaryContext === 'ambulatorio' && subContext) {
        templateData.outpatient_specialty = subContext as OutpatientSpecialty;
      }
      if (primaryContext === 'uti' && subContext) {
        templateData.icu_type = subContext as ICUType;
      }
      if (primaryContext === 'internacao' && subContext) {
        templateData.hospitalization_type = subContext as HospitalizationType;
      }

      await createTemplate(templateData);
      setSaveSuccess(true);
      onSave?.();
    } catch (error) {
      console.error('Erro ao salvar template:', error);
      setSaveError('Erro ao salvar o modelo. Por favor, tente novamente.');
    } finally {
      setIsSaving(false);
    }
  };

  const getContextLabel = () => {
    const contexts: Record<string, string> = {
      emergencia: 'Emergência',
      uti: 'UTI',
      internacao: 'Internação',
      ambulatorio: 'Ambulatório',
      pacs: 'PACS',
      pacs_urgencia: 'PACS Urgência',
      pacs_consultorio: 'PACS Consultório',
      mfc_ubs: 'MFC/UBS',
      consultorio: 'Clínica Privada',
    };
    return contexts[primaryContext || ''] || 'Não definido';
  };

  const getSubcontextLabel = () => {
    if (!subContext) return 'Não especificado';
    return subContext.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
  };

  const countEnabledSections = () => {
    return Object.values(sectionsConfig).filter(Boolean).length;
  };

  const countEnabledHeaderFields = () => {
    return Object.values(headerConfig).filter(Boolean).length;
  };

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-900">Salvar Modelo</h2>
        <p className="text-gray-500 mt-2">
          Revise suas configurações e salve seu modelo personalizado
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Resumo das Configurações */}
        <Card variant="bordered">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <FileText className="w-5 h-5" />
              Resumo do Modelo
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-2 gap-4 text-sm">
              <div>
                <p className="text-gray-500">Contexto</p>
                <p className="font-medium">{getContextLabel()}</p>
              </div>
              <div>
                <p className="text-gray-500">Especialidade</p>
                <p className="font-medium">{getSubcontextLabel()}</p>
              </div>
              <div>
                <p className="text-gray-500">Campos no Cabeçalho</p>
                <p className="font-medium">{countEnabledHeaderFields()} campos</p>
              </div>
              <div>
                <p className="text-gray-500">Seções</p>
                <p className="font-medium">{countEnabledSections()} seções</p>
              </div>
              <div>
                <p className="text-gray-500">Formato de Título</p>
                <p className="font-medium">
                  {formattingConfig.hda_format.title_format === 'maiusculas' && 'MAIÚSCULAS'}
                  {formattingConfig.hda_format.title_format === 'primeira_maiuscula' && 'Primeira Maiúscula'}
                  {formattingConfig.hda_format.title_format === 'minusculas' && 'minúsculas'}
                </p>
              </div>
              <div>
                <p className="text-gray-500">Abreviações</p>
                <p className="font-medium">
                  {formattingConfig.abbreviations.medical_abbreviations === 'maximo' && 'Máximo'}
                  {formattingConfig.abbreviations.medical_abbreviations === 'moderado' && 'Moderado'}
                  {formattingConfig.abbreviations.medical_abbreviations === 'minimo' && 'Mínimo'}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Formulário de Salvamento */}
        <Card variant="bordered">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Save className="w-5 h-5" />
              Salvar como
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <Input
              label="Nome do modelo"
              placeholder="Ex: Meu Plantão Noturno PS"
              value={templateName}
              onChange={(e) => setTemplateName(e.target.value)}
              error={saveError && !templateName.trim() ? 'Nome é obrigatório' : undefined}
            />

            <Checkbox
              label="Definir como padrão"
              description="Este modelo será usado automaticamente"
              checked={isDefault}
              onChange={(e) => setIsDefault(e.target.checked)}
            />

            {saveError && (
              <div className="p-3 bg-red-50 border border-red-200 rounded-lg">
                <p className="text-sm text-red-600">{saveError}</p>
              </div>
            )}

            {saveSuccess && (
              <div className="p-3 bg-green-50 border border-green-200 rounded-lg">
                <p className="text-sm text-green-600">Modelo salvo com sucesso!</p>
              </div>
            )}

            <div className="flex gap-3 pt-4">
              <Button
                variant="outline"
                onClick={onTest}
                className="flex-1"
              >
                <Eye className="w-4 h-4 mr-2" />
                Testar antes
              </Button>
              <Button
                onClick={handleSave}
                isLoading={isSaving}
                className="flex-1"
              >
                <Save className="w-4 h-4 mr-2" />
                Salvar
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
