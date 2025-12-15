'use client';

import { Card, CardHeader, CardTitle, CardContent, RadioGroup, RadioGroupItem, Checkbox, Input } from '@/components/ui';
import { useWizardStore } from '@/store/wizardStore';
import type { 
  TitleFormat, 
  SectionTitleOption, 
  ExamOrganization, 
  ReferenceValues,
  LabFormat,
  AbbreviationLevel,
  MedicationFormat 
} from '@/types';

export function Step4Formatting() {
  const { formattingConfig, setFormattingConfig } = useWizardStore();

  const updateHdaFormat = (updates: Partial<typeof formattingConfig.hda_format>) => {
    setFormattingConfig({
      hda_format: { ...formattingConfig.hda_format, ...updates },
    });
  };

  const updateExamFormat = (updates: Partial<typeof formattingConfig.exam_format>) => {
    setFormattingConfig({
      exam_format: { ...formattingConfig.exam_format, ...updates },
    });
  };

  const updateAbbreviations = (updates: Partial<typeof formattingConfig.abbreviations>) => {
    setFormattingConfig({
      abbreviations: { ...formattingConfig.abbreviations, ...updates },
    });
  };

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-900">Detalhamento de Formatação</h2>
        <p className="text-gray-500 mt-2">
          Configure como as seções e exames serão formatados
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Formatação de Seções */}
        <Card variant="bordered">
          <CardHeader>
            <CardTitle>Seção &quot;HDA&quot;</CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div>
              <p className="text-sm font-medium text-gray-700 mb-3">Título da seção:</p>
              <RadioGroup
                name="title_option"
                value={formattingConfig.hda_format.title_option}
                onChange={(value) => updateHdaFormat({ title_option: value as SectionTitleOption })}
                className="space-y-2"
              >
                <RadioGroupItem value="HDA" label="HDA" />
                <RadioGroupItem value="História da Doença Atual" label="História da Doença Atual" />
                <RadioGroupItem value="Queixa Principal e HDA" label="Queixa Principal e HDA" />
                <RadioGroupItem value="custom" label="Personalizado" />
              </RadioGroup>
              
              {formattingConfig.hda_format.title_option === 'custom' && (
                <Input
                  placeholder="Digite o título personalizado"
                  value={formattingConfig.hda_format.custom_title || ''}
                  onChange={(e) => updateHdaFormat({ custom_title: e.target.value })}
                  className="mt-3"
                />
              )}
            </div>

            <div>
              <p className="text-sm font-medium text-gray-700 mb-3">Formato de título:</p>
              <RadioGroup
                name="title_format"
                value={formattingConfig.hda_format.title_format}
                onChange={(value) => updateHdaFormat({ title_format: value as TitleFormat })}
                className="space-y-2"
              >
                <RadioGroupItem value="maiusculas" label="MAIÚSCULAS" />
                <RadioGroupItem value="primeira_maiuscula" label="Primeira letra maiúscula" />
                <RadioGroupItem value="minusculas" label="minúsculas" />
              </RadioGroup>
            </div>

            <div>
              <Checkbox
                label="Incluir data?"
                description={`Formato: ${formattingConfig.hda_format.date_format}`}
                checked={formattingConfig.hda_format.include_date}
                onChange={(e) => updateHdaFormat({ include_date: e.target.checked })}
              />
            </div>
          </CardContent>
        </Card>

        {/* Formatação de Exames */}
        <Card variant="bordered">
          <CardHeader>
            <CardTitle>Seção &quot;Exames&quot;</CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div>
              <p className="text-sm font-medium text-gray-700 mb-3">Organização dos exames:</p>
              <RadioGroup
                name="exam_organization"
                value={formattingConfig.exam_format.organization}
                onChange={(value) => updateExamFormat({ organization: value as ExamOrganization })}
                className="space-y-2"
              >
                <RadioGroupItem 
                  value="por_modalidade" 
                  label="Por modalidade" 
                  description="Labs, Imagem, ECG"
                />
                <RadioGroupItem 
                  value="cronologica" 
                  label="Cronológica pura" 
                  description="Todos juntos por data"
                />
              </RadioGroup>
            </div>

            <div>
              <p className="text-sm font-medium text-gray-700 mb-3">Valores de referência:</p>
              <RadioGroup
                name="reference_values"
                value={formattingConfig.exam_format.reference_values}
                onChange={(value) => updateExamFormat({ reference_values: value as ReferenceValues })}
                className="space-y-2"
              >
                <RadioGroupItem 
                  value="sempre" 
                  label="Sempre incluir" 
                  description="Ex: VR <0,042"
                />
                <RadioGroupItem value="so_alterado" label="Só se alterado" />
                <RadioGroupItem value="nunca" label="Nunca incluir" />
              </RadioGroup>
            </div>

            <div>
              <p className="text-sm font-medium text-gray-700 mb-3">Formatação de Labs:</p>
              <RadioGroup
                name="lab_format"
                value={formattingConfig.exam_format.lab_format}
                onChange={(value) => updateExamFormat({ lab_format: value as LabFormat })}
                className="space-y-2"
              >
                <RadioGroupItem 
                  value="compacto" 
                  label="Compacto" 
                  description="Hb 12,5 / Ht 37 | Leu 8.500"
                />
                <RadioGroupItem 
                  value="detalhado" 
                  label="Detalhado" 
                  description="Hemoglobina: 12,5 g/dL"
                />
              </RadioGroup>
            </div>
          </CardContent>
        </Card>

        {/* Abreviações */}
        <Card variant="bordered" className="lg:col-span-2">
          <CardHeader>
            <CardTitle>Uso de Abreviações</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <p className="text-sm font-medium text-gray-700 mb-3">Abreviações médicas:</p>
                <RadioGroup
                  name="abbreviation_level"
                  value={formattingConfig.abbreviations.medical_abbreviations}
                  onChange={(value) => updateAbbreviations({ medical_abbreviations: value as AbbreviationLevel })}
                  className="space-y-2"
                >
                  <RadioGroupItem 
                    value="maximo" 
                    label="Máximo" 
                    description="HAS, DM, DPOC, BEG, etc"
                  />
                  <RadioGroupItem 
                    value="moderado" 
                    label="Moderado" 
                    description="Só doenças comuns"
                  />
                  <RadioGroupItem 
                    value="minimo" 
                    label="Mínimo" 
                    description="Escrever por extenso"
                  />
                </RadioGroup>
              </div>

              <div>
                <p className="text-sm font-medium text-gray-700 mb-3">Medicações:</p>
                <RadioGroup
                  name="medication_format"
                  value={formattingConfig.abbreviations.medication_format}
                  onChange={(value) => updateAbbreviations({ medication_format: value as MedicationFormat })}
                  className="space-y-2"
                >
                  <RadioGroupItem 
                    value="abreviado" 
                    label="Abreviadas" 
                    description="AAS, IECA, BRA"
                  />
                  <RadioGroupItem 
                    value="extenso" 
                    label="Por extenso" 
                    description="Ácido acetilsalicílico"
                  />
                </RadioGroup>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
