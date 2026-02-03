'use client';

import { Card, CardHeader, CardTitle, CardContent, Checkbox } from '@/components/ui';
import { useWizardStore } from '@/store/wizardStore';

export function Step3Sections() {
  const {
    primaryContext,
    subContext,
    headerConfig,
    setHeaderConfig,
    sectionsConfig,
    setSectionsConfig,
  } = useWizardStore();

  // Lógica de visibilidade baseada na Arquitetura Consolidada
  const isGO =
    subContext === 'obstetrica' ||
    subContext === 'obstetricia' ||
    subContext === 'pre_natal_br' ||
    subContext === 'ginecologia' ||
    subContext === 'mastologia' ||
    subContext === 'ptgi' ||
    subContext === 'infertilidade' ||
    subContext === 'oncologia_ginecologica';
  const isHospital = ['internacao', 'uti', 'emergencia'].includes(primaryContext || '');
  const isPACS = primaryContext === 'pacs' || primaryContext === 'pacs_urgencia' || primaryContext === 'pacs_consultorio';

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-900">Configuração de Seções</h2>
        <p className="text-gray-500 mt-2">Ative os campos específicos para sua especialidade</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card variant="bordered">
          <CardHeader>
            <CardTitle>Identificação e História</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <Checkbox
              label="Nome do paciente"
              checked={headerConfig.include_name}
              onChange={(e) => setHeaderConfig({ include_name: e.target.checked })}
            />
            <Checkbox
              label="Idade"
              checked={headerConfig.include_age}
              onChange={(e) => setHeaderConfig({ include_age: e.target.checked })}
            />
            <Checkbox
              label="Comorbidades (Hierárquicas > --)"
              checked={headerConfig.include_comorbidities}
              onChange={(e) => setHeaderConfig({ include_comorbidities: e.target.checked })}
            />
            <Checkbox
              label="Medicações em uso (MUC)"
              checked={headerConfig.include_medications}
              onChange={(e) => setHeaderConfig({ include_medications: e.target.checked })}
            />
            <Checkbox
              label="Alergias"
              checked={headerConfig.include_allergies}
              onChange={(e) => setHeaderConfig({ include_allergies: e.target.checked })}
            />

            {/* Campos Condicionais: Obstetrícia */}
            {isGO && (
              <div className="bg-purple-50 p-3 rounded-lg space-y-3 border border-purple-100 mt-4">
                <p className="text-xs font-bold text-purple-700 uppercase">Campos Gestações/Partos</p>
                <Checkbox
                  label="G P A C M E (Gestações, Partos...)"
                  checked={headerConfig.include_gpa}
                  onChange={(e) => setHeaderConfig({ include_gpa: e.target.checked })}
                />
                <Checkbox
                  label="Idade Gestacional (IG: XX+X)"
                  checked={headerConfig.include_gestational_age}
                  onChange={(e) => setHeaderConfig({ include_gestational_age: e.target.checked })}
                />
                <Checkbox
                  label="Sorologias/Vacinas (Inline |)"
                  checked={headerConfig.include_rapid_tests}
                  onChange={(e) => setHeaderConfig({ include_rapid_tests: e.target.checked })}
                />
              </div>
            )}

            {/* Campos Condicionais: Internação */}
            {isHospital && (
              <div className="bg-blue-50 p-3 rounded-lg space-y-3 border border-blue-100 mt-4">
                <p className="text-xs font-bold text-blue-700 uppercase">Localização Hospitalar</p>
                <Checkbox
                  label="Leito e Ala (Ex: Sala Recup)"
                  checked={headerConfig.include_bed}
                  onChange={(e) => setHeaderConfig({ include_bed: e.target.checked })}
                />
                <Checkbox
                  label="Data de Internação / D.I."
                  checked={headerConfig.include_admission_date}
                  onChange={(e) => setHeaderConfig({ include_admission_date: e.target.checked })}
                />
              </div>
            )}
          </CardContent>
        </Card>

        <Card variant="bordered">
          <CardHeader>
            <CardTitle>Estrutura do Exame e Conduta</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <Checkbox
              label="HDA (História da Doença Atual)"
              checked={sectionsConfig.include_hda}
              onChange={(e) => setSectionsConfig({ include_hda: e.target.checked })}
            />
            <Checkbox
              label="Exame Físico/Objetivo"
              checked={sectionsConfig.include_physical_exam}
              onChange={(e) => setSectionsConfig({ include_physical_exam: e.target.checked })}
            />
            <Checkbox
              label="Exame do Estado Mental (EEM)"
              checked={sectionsConfig.include_subjective}
              onChange={(e) => setSectionsConfig({ include_subjective: e.target.checked })}
            />
            <Checkbox
              label="Tabela de Pulsos (D/E)"
              checked={sectionsConfig.include_pulses_table ?? false}
              onChange={(e) => setSectionsConfig({ include_pulses_table: e.target.checked })}
            />
            <Checkbox
              label="Exames Complementares"
              checked={sectionsConfig.include_complementary_exams}
              onChange={(e) => setSectionsConfig({ include_complementary_exams: e.target.checked })}
            />
            <Checkbox
              label="Impressão/Avaliação"
              checked={sectionsConfig.include_assessment}
              onChange={(e) => setSectionsConfig({ include_assessment: e.target.checked })}
            />
            <Checkbox
              label="Conduta/Plano"
              checked={sectionsConfig.include_plan}
              onChange={(e) => setSectionsConfig({ include_plan: e.target.checked })}
            />

            {/* Conversão de Linguagem Leiga (PACS/Consultório) */}
            {(isPACS || primaryContext === 'ambulatorio') && (
              <div className="bg-green-50 p-3 rounded-lg border border-green-100 mt-4">
                <Checkbox
                  label="Bloco de Conversão Obrigatória"
                  description='"Converso com paciente em linguagem leiga..."'
                  checked={sectionsConfig.include_conversion_block ?? false}
                  onChange={(e) => setSectionsConfig({ include_conversion_block: e.target.checked })}
                />
              </div>
            )}

            <div className="border-t pt-3 mt-3">
              <Checkbox
                label="Sinais de Alarme Condicionais (→ SE)"
                checked={sectionsConfig.include_reevaluation}
                onChange={(e) => setSectionsConfig({ include_reevaluation: e.target.checked })}
              />
              <Checkbox
                label="Evolução diária (internação)"
                checked={sectionsConfig.include_daily_evolution}
                onChange={(e) => setSectionsConfig({ include_daily_evolution: e.target.checked })}
                className="mt-3"
              />
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
