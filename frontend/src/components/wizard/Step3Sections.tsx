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

  const isObstetric = subContext === 'obstetrica' || subContext === 'obstetricia';
  const isHospitalization = primaryContext === 'internacao' || primaryContext === 'uti';

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-900">Configuração de Seções</h2>
        <p className="text-gray-500 mt-2">
          Selecione o que incluir no cabeçalho e quais seções sua evolução terá
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Cabeçalho */}
        <Card variant="bordered">
          <CardHeader>
            <CardTitle>Cabeçalho</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <p className="text-sm text-gray-500 mb-4">O que incluir no cabeçalho?</p>
            
            <div className="space-y-3">
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
                label="Ocupação"
                checked={headerConfig.include_occupation}
                onChange={(e) => setHeaderConfig({ include_occupation: e.target.checked })}
              />
              <Checkbox
                label="Naturalidade"
                checked={headerConfig.include_birthplace}
                onChange={(e) => setHeaderConfig({ include_birthplace: e.target.checked })}
              />
              
              <div className="border-t pt-3 mt-3">
                <Checkbox
                  label="Comorbidades (História relevante)"
                  checked={headerConfig.include_comorbidities}
                  onChange={(e) => setHeaderConfig({ include_comorbidities: e.target.checked })}
                />
                <Checkbox
                  label="Medicações em uso contínuo (MUC)"
                  checked={headerConfig.include_medications}
                  onChange={(e) => setHeaderConfig({ include_medications: e.target.checked })}
                  className="mt-3"
                />
                <Checkbox
                  label="Alergias"
                  checked={headerConfig.include_allergies}
                  onChange={(e) => setHeaderConfig({ include_allergies: e.target.checked })}
                  className="mt-3"
                />
                <Checkbox
                  label="Cirurgias prévias"
                  checked={headerConfig.include_previous_surgeries}
                  onChange={(e) => setHeaderConfig({ include_previous_surgeries: e.target.checked })}
                  className="mt-3"
                />
                <Checkbox
                  label="História familiar"
                  checked={headerConfig.include_family_history}
                  onChange={(e) => setHeaderConfig({ include_family_history: e.target.checked })}
                  className="mt-3"
                />
              </div>

              {/* Campos de Obstetrícia */}
              {isObstetric && (
                <div className="border-t pt-3 mt-3">
                  <p className="text-sm font-medium text-purple-700 mb-3">Obstetrícia</p>
                  <Checkbox
                    label="Idade gestacional (IG)"
                    checked={headerConfig.include_gestational_age}
                    onChange={(e) => setHeaderConfig({ include_gestational_age: e.target.checked })}
                  />
                  <Checkbox
                    label="Gestação/Para/Aborto (GPA)"
                    checked={headerConfig.include_gpa}
                    onChange={(e) => setHeaderConfig({ include_gpa: e.target.checked })}
                    className="mt-3"
                  />
                  <Checkbox
                    label="Testes rápidos"
                    checked={headerConfig.include_rapid_tests}
                    onChange={(e) => setHeaderConfig({ include_rapid_tests: e.target.checked })}
                    className="mt-3"
                  />
                </div>
              )}

              {/* Campos de Internação */}
              {isHospitalization && (
                <div className="border-t pt-3 mt-3">
                  <p className="text-sm font-medium text-blue-700 mb-3">Internação</p>
                  <Checkbox
                    label="Leito (Ex: L04, L15)"
                    checked={headerConfig.include_bed}
                    onChange={(e) => setHeaderConfig({ include_bed: e.target.checked })}
                  />
                  <Checkbox
                    label="Data de internação"
                    checked={headerConfig.include_admission_date}
                    onChange={(e) => setHeaderConfig({ include_admission_date: e.target.checked })}
                    className="mt-3"
                  />
                </div>
              )}
            </div>
          </CardContent>
        </Card>

        {/* Estrutura das Seções */}
        <Card variant="bordered">
          <CardHeader>
            <CardTitle>Estrutura das Seções</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <p className="text-sm text-gray-500 mb-4">Quais seções sua evolução terá?</p>
            
            <div className="space-y-3">
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

              <div className="border-t pt-3 mt-3">
                <p className="text-sm font-medium text-gray-700 mb-3">Opcionais por contexto</p>
                <Checkbox
                  label="Reavaliação (para internação)"
                  checked={sectionsConfig.include_reevaluation}
                  onChange={(e) => setSectionsConfig({ include_reevaluation: e.target.checked })}
                />
                <Checkbox
                  label="Evolução (diária de internação)"
                  checked={sectionsConfig.include_daily_evolution}
                  onChange={(e) => setSectionsConfig({ include_daily_evolution: e.target.checked })}
                  className="mt-3"
                />
                <Checkbox
                  label="Subjetivo (estilo SOAP)"
                  checked={sectionsConfig.include_subjective}
                  onChange={(e) => setSectionsConfig({ include_subjective: e.target.checked })}
                  className="mt-3"
                />
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
