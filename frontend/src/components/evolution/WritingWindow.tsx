'use client';

import { useState } from 'react';
import { Sparkles, Copy, Check, RotateCcw } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent, TextArea, Button } from '@/components/ui';
import { useWizardStore } from '@/store/wizardStore';
import { generateEvolution } from '@/lib/api';

export function WritingWindow() {
  const {
    rawText,
    setRawText,
    patientData,
    selectedTemplateId,
    primaryContext,
    headerConfig,
    sectionsConfig,
    formattingConfig,
    generatedEvolution,
    setGeneratedEvolution,
    isGenerating,
    setIsGenerating,
    evolutionType,
  } = useWizardStore();

  const [copied, setCopied] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleGenerate = async () => {
    if (!rawText.trim()) {
      setError('Por favor, insira o texto da evolução');
      return;
    }

    setIsGenerating(true);
    setError(null);

    try {
      const request = {
        raw_text: rawText,
        template_id: selectedTemplateId || undefined,
        patient_data: Object.keys(patientData).length > 0 ? patientData : undefined,
        evolution_type: evolutionType || undefined,
        primary_context: !selectedTemplateId ? primaryContext || undefined : undefined,
        header_config: !selectedTemplateId ? headerConfig : undefined,
        sections_config: !selectedTemplateId ? sectionsConfig : undefined,
        formatting_config: !selectedTemplateId ? formattingConfig : undefined,
      };

      const result = await generateEvolution(request);
      setGeneratedEvolution(result);
    } catch (err) {
      console.error('Erro ao gerar evolução:', err);
      setError('Erro ao gerar evolução. Verifique se o backend está rodando.');
    } finally {
      setIsGenerating(false);
    }
  };

  const handleCopy = async () => {
    if (generatedEvolution?.formatted_text) {
      await navigator.clipboard.writeText(generatedEvolution.formatted_text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const handleReset = () => {
    setRawText('');
    setGeneratedEvolution(null);
    setError(null);
  };

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-900">Janela de Escrita</h2>
        <p className="text-gray-500 mt-2">
          Digite o texto corrido da evolução e a IA irá formatá-lo
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Área de Entrada */}
        <Card variant="bordered" className="h-fit">
          <CardHeader>
            <CardTitle>Texto Livre</CardTitle>
          </CardHeader>
          <CardContent>
            <TextArea
              placeholder="Digite aqui as informações do atendimento em texto corrido...

Exemplo:
Paciente Maria Silva, 45 anos, hipertensa e diabética, em uso de losartana e metformina. Refere cefaleia intensa há 2 dias, associada a náuseas. Nega febre. PA 180x100, FC 88, Tax 36.5. Lúcida, orientada, pupilas isocóricas. Rigidez de nuca ausente. Hemograma normal, glicemia 156. TC crânio sem alterações. HD: Crise hipertensiva. Conduta: Captopril 25mg VO, observação por 2h, orientações."
              value={rawText}
              onChange={(e) => setRawText(e.target.value)}
              rows={16}
              error={error || undefined}
            />

            <div className="flex gap-3 mt-4">
              <Button
                variant="outline"
                onClick={handleReset}
                disabled={isGenerating}
              >
                <RotateCcw className="w-4 h-4 mr-2" />
                Limpar
              </Button>
              <Button
                onClick={handleGenerate}
                isLoading={isGenerating}
                className="flex-1"
              >
                <Sparkles className="w-4 h-4 mr-2" />
                Gerar Evolução
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Área de Saída */}
        <Card variant="bordered" className="h-fit">
          <CardHeader className="flex flex-row items-center justify-between">
            <CardTitle>Evolução Formatada</CardTitle>
            {generatedEvolution && (
              <Button
                variant="ghost"
                size="sm"
                onClick={handleCopy}
              >
                {copied ? (
                  <>
                    <Check className="w-4 h-4 mr-2 text-green-600" />
                    Copiado!
                  </>
                ) : (
                  <>
                    <Copy className="w-4 h-4 mr-2" />
                    Copiar
                  </>
                )}
              </Button>
            )}
          </CardHeader>
          <CardContent>
            {generatedEvolution ? (
              <div className="space-y-4">
                <div className="bg-gray-50 rounded-lg p-4 font-mono text-sm whitespace-pre-wrap max-h-[500px] overflow-y-auto">
                  {generatedEvolution.formatted_text}
                </div>
                
                {typeof generatedEvolution.metadata?.warning === 'string' && generatedEvolution.metadata.warning && (
                  <div className="p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
                    <p className="text-sm text-yellow-700">
                      {generatedEvolution.metadata.warning}
                    </p>
                  </div>
                )}

                <div className="flex items-center justify-between text-xs text-gray-500">
                  <span>
                    Tempo de processamento: {generatedEvolution.processing_time_ms}ms
                  </span>
                  <span>
                    {generatedEvolution.sections.length} seções
                  </span>
                </div>
              </div>
            ) : (
              <div className="flex flex-col items-center justify-center h-64 text-gray-400">
                <Sparkles className="w-12 h-12 mb-4" />
                <p className="text-center">
                  A evolução formatada aparecerá aqui após você clicar em &quot;Gerar Evolução&quot;
                </p>
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
