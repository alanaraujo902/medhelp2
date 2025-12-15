'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Plus, Trash2, Star, FileText } from 'lucide-react';
import { Button, Card, CardHeader, CardTitle, CardContent } from '@/components/ui';
import { getTemplates, deleteTemplate } from '@/lib/api';
import type { EvolutionTemplate } from '@/types';
import { cn } from '@/lib/utils';

export default function TemplatesPage() {
  const router = useRouter();
  const [templates, setTemplates] = useState<EvolutionTemplate[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [deletingId, setDeletingId] = useState<string | null>(null);

  useEffect(() => {
    fetchTemplates();
  }, []);

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

  const handleDelete = async (id: string) => {
    if (!confirm('Tem certeza que deseja excluir este modelo?')) return;

    setDeletingId(id);
    try {
      await deleteTemplate(id);
      setTemplates(templates.filter(t => t.id !== id));
    } catch (err) {
      console.error('Erro ao excluir template:', err);
      alert('Erro ao excluir modelo.');
    } finally {
      setDeletingId(null);
    }
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
      emergencia: 'bg-red-100 text-red-700 border-red-200',
      uti: 'bg-purple-100 text-purple-700 border-purple-200',
      internacao: 'bg-blue-100 text-blue-700 border-blue-200',
      ambulatorio: 'bg-green-100 text-green-700 border-green-200',
    };
    return colors[context] || 'bg-gray-100 text-gray-700 border-gray-200';
  };

  const presets = templates.filter(t => t.id.startsWith('preset-'));
  const userTemplates = templates.filter(t => !t.id.startsWith('preset-'));

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-red-600">{error}</p>
        <Button onClick={() => window.location.reload()} className="mt-4">
          Tentar Novamente
        </Button>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Modelos</h1>
          <p className="text-gray-500 mt-2">
            Gerencie seus modelos de evolução médica
          </p>
        </div>
        <Button onClick={() => router.push('/configure')}>
          <Plus className="w-4 h-4 mr-2" />
          Novo Modelo
        </Button>
      </div>

      {/* Modelos do Usuário */}
      <Card variant="bordered">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <FileText className="w-5 h-5" />
            Meus Modelos
          </CardTitle>
        </CardHeader>
        <CardContent>
          {userTemplates.length === 0 ? (
            <div className="text-center py-8 text-gray-500">
              <p>Você ainda não criou nenhum modelo personalizado.</p>
              <Button
                variant="outline"
                onClick={() => router.push('/configure')}
                className="mt-4"
              >
                <Plus className="w-4 h-4 mr-2" />
                Criar Primeiro Modelo
              </Button>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {userTemplates.map((template) => (
                <div
                  key={template.id}
                  className="p-4 rounded-lg border border-gray-200 hover:border-gray-300 transition-colors"
                >
                  <div className="flex items-start justify-between mb-3">
                    <div>
                      <h3 className="font-medium text-gray-900 flex items-center gap-2">
                        {template.name}
                        {template.is_default && (
                          <Star className="w-4 h-4 text-yellow-500 fill-yellow-500" />
                        )}
                      </h3>
                      <span className={cn(
                        'inline-block mt-1 px-2 py-0.5 rounded text-xs font-medium border',
                        getContextColor(template.primary_context)
                      )}>
                        {getContextLabel(template.primary_context)}
                      </span>
                    </div>
                    <Button
                      variant="ghost"
                      size="icon"
                      onClick={() => handleDelete(template.id)}
                      disabled={deletingId === template.id}
                      className="text-gray-400 hover:text-red-600"
                    >
                      <Trash2 className="w-4 h-4" />
                    </Button>
                  </div>
                  <p className="text-xs text-gray-500">
                    Criado em {new Date(template.created_at).toLocaleDateString('pt-BR')}
                  </p>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>

      {/* Modelos Pré-configurados */}
      <Card variant="bordered">
        <CardHeader>
          <CardTitle>Modelos Prontos</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {presets.map((template) => (
              <div
                key={template.id}
                className="p-4 rounded-lg border border-gray-200 bg-gray-50"
              >
                <h3 className="font-medium text-gray-900">{template.name}</h3>
                <span className={cn(
                  'inline-block mt-1 px-2 py-0.5 rounded text-xs font-medium border',
                  getContextColor(template.primary_context)
                )}>
                  {getContextLabel(template.primary_context)}
                </span>
                <p className="text-xs text-gray-500 mt-2">
                  Modelo do sistema (não editável)
                </p>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
