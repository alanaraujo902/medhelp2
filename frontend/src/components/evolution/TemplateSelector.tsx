'use client';

import { useState, useEffect } from 'react';
import { FileText, Plus, Check } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent, Button } from '@/components/ui';
import { useWizardStore } from '@/store/wizardStore';
import { getTemplates } from '@/lib/api';
import type { EvolutionTemplate } from '@/types';
import { cn } from '@/lib/utils';

interface TemplateSelectorProps {
  onCreateNew?: () => void;
}

export function TemplateSelector({ onCreateNew }: TemplateSelectorProps) {
  const { selectedTemplateId, setSelectedTemplateId, loadTemplate } = useWizardStore();
  const [templates, setTemplates] = useState<EvolutionTemplate[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchTemplates = async () => {
      try {
        const response = await getTemplates();
        setTemplates(response.templates);
      } catch (err) {
        console.error('Erro ao carregar templates:', err);
        setError('Erro ao carregar modelos. Verifique se o backend está rodando.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchTemplates();
  }, []);

  const handleSelectTemplate = (template: EvolutionTemplate) => {
    setSelectedTemplateId(template.id);
    loadTemplate(template);
  };

  const getContextLabel = (context: string) => {
    const labels: Record<string, string> = {
      emergencia: 'Emergência',
      uti: 'UTI',
      internacao: 'Internação',
      ambulatorio: 'Ambulatório',
    };
    return labels[context] || context;
  };

  const getContextColor = (context: string) => {
    const colors: Record<string, string> = {
      emergencia: 'bg-red-100 text-red-700',
      uti: 'bg-purple-100 text-purple-700',
      internacao: 'bg-blue-100 text-blue-700',
      ambulatorio: 'bg-green-100 text-green-700',
    };
    return colors[context] || 'bg-gray-100 text-gray-700';
  };

  if (isLoading) {
    return (
      <Card variant="bordered">
        <CardContent className="py-12">
          <div className="flex items-center justify-center">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600" />
          </div>
        </CardContent>
      </Card>
    );
  }

  if (error) {
    return (
      <Card variant="bordered">
        <CardContent className="py-12">
          <div className="text-center text-red-600">
            <p>{error}</p>
          </div>
        </CardContent>
      </Card>
    );
  }

  const presets = templates.filter(t => t.id.startsWith('preset-'));
  const userTemplates = templates.filter(t => !t.id.startsWith('preset-'));

  return (
    <Card variant="bordered">
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle className="flex items-center gap-2">
          <FileText className="w-5 h-5" />
          Selecionar Modelo
        </CardTitle>
        <Button variant="outline" size="sm" onClick={onCreateNew}>
          <Plus className="w-4 h-4 mr-2" />
          Criar Novo
        </Button>
      </CardHeader>
      <CardContent>
        {/* Templates Pré-configurados */}
        <div className="mb-6">
          <h4 className="text-sm font-medium text-gray-700 mb-3">Modelos Prontos</h4>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {presets.map((template) => (
              <button
                key={template.id}
                onClick={() => handleSelectTemplate(template)}
                className={cn(
                  'flex items-start gap-3 p-4 rounded-lg border-2 transition-all text-left',
                  selectedTemplateId === template.id
                    ? 'border-blue-500 bg-blue-50'
                    : 'border-gray-200 hover:border-gray-300'
                )}
              >
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <span className="font-medium text-gray-900">{template.name}</span>
                    {selectedTemplateId === template.id && (
                      <Check className="w-4 h-4 text-blue-600" />
                    )}
                  </div>
                  <span className={cn(
                    'inline-block mt-1 px-2 py-0.5 rounded text-xs font-medium',
                    getContextColor(template.primary_context)
                  )}>
                    {getContextLabel(template.primary_context)}
                  </span>
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* Templates do Usuário */}
        {userTemplates.length > 0 && (
          <div>
            <h4 className="text-sm font-medium text-gray-700 mb-3">Meus Modelos</h4>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {userTemplates.map((template) => (
                <button
                  key={template.id}
                  onClick={() => handleSelectTemplate(template)}
                  className={cn(
                    'flex items-start gap-3 p-4 rounded-lg border-2 transition-all text-left',
                    selectedTemplateId === template.id
                      ? 'border-blue-500 bg-blue-50'
                      : 'border-gray-200 hover:border-gray-300'
                  )}
                >
                  <div className="flex-1">
                    <div className="flex items-center gap-2">
                      <span className="font-medium text-gray-900">{template.name}</span>
                      {template.is_default && (
                        <span className="px-2 py-0.5 bg-yellow-100 text-yellow-700 rounded text-xs">
                          Padrão
                        </span>
                      )}
                      {selectedTemplateId === template.id && (
                        <Check className="w-4 h-4 text-blue-600" />
                      )}
                    </div>
                    <span className={cn(
                      'inline-block mt-1 px-2 py-0.5 rounded text-xs font-medium',
                      getContextColor(template.primary_context)
                    )}>
                      {getContextLabel(template.primary_context)}
                    </span>
                  </div>
                </button>
              ))}
            </div>
          </div>
        )}

        {userTemplates.length === 0 && (
          <div className="text-center py-6 text-gray-500">
            <p>Você ainda não criou nenhum modelo personalizado.</p>
            <Button variant="outline" size="sm" onClick={onCreateNew} className="mt-3">
              <Plus className="w-4 h-4 mr-2" />
              Criar Primeiro Modelo
            </Button>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
