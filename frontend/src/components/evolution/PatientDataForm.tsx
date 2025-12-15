'use client';

import { Card, CardHeader, CardTitle, CardContent, Input } from '@/components/ui';
import { useWizardStore } from '@/store/wizardStore';

export function PatientDataForm() {
  const { patientData, setPatientData, headerConfig, primaryContext, subContext } = useWizardStore();

  const isObstetric = subContext === 'obstetrica' || subContext === 'obstetricia';
  const isHospitalization = primaryContext === 'internacao' || primaryContext === 'uti';

  return (
    <Card variant="bordered">
      <CardHeader>
        <CardTitle>Dados do Paciente (Opcional)</CardTitle>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-gray-500 mb-4">
          Preencha os dados do paciente para incluir no cabeçalho da evolução
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {headerConfig.include_name && (
            <Input
              label="Nome"
              placeholder="Nome do paciente"
              value={patientData.name || ''}
              onChange={(e) => setPatientData({ name: e.target.value })}
            />
          )}

          {headerConfig.include_age && (
            <Input
              label="Idade"
              placeholder="Ex: 45 anos"
              value={patientData.age || ''}
              onChange={(e) => setPatientData({ age: e.target.value })}
            />
          )}

          {headerConfig.include_occupation && (
            <Input
              label="Ocupação"
              placeholder="Ex: Professora"
              value={patientData.occupation || ''}
              onChange={(e) => setPatientData({ occupation: e.target.value })}
            />
          )}

          {headerConfig.include_birthplace && (
            <Input
              label="Naturalidade"
              placeholder="Ex: Porto Alegre/RS"
              value={patientData.birthplace || ''}
              onChange={(e) => setPatientData({ birthplace: e.target.value })}
            />
          )}

          {headerConfig.include_comorbidities && (
            <Input
              label="Comorbidades"
              placeholder="Ex: HAS, DM2"
              value={patientData.comorbidities || ''}
              onChange={(e) => setPatientData({ comorbidities: e.target.value })}
            />
          )}

          {headerConfig.include_medications && (
            <Input
              label="Medicações em Uso"
              placeholder="Ex: Losartana 50mg, Metformina 850mg"
              value={patientData.medications || ''}
              onChange={(e) => setPatientData({ medications: e.target.value })}
            />
          )}

          {headerConfig.include_allergies && (
            <Input
              label="Alergias"
              placeholder="Ex: Dipirona, Penicilina"
              value={patientData.allergies || ''}
              onChange={(e) => setPatientData({ allergies: e.target.value })}
            />
          )}

          {headerConfig.include_previous_surgeries && (
            <Input
              label="Cirurgias Prévias"
              placeholder="Ex: Colecistectomia (2019)"
              value={patientData.previous_surgeries || ''}
              onChange={(e) => setPatientData({ previous_surgeries: e.target.value })}
            />
          )}

          {headerConfig.include_family_history && (
            <Input
              label="História Familiar"
              placeholder="Ex: Pai com IAM aos 55 anos"
              value={patientData.family_history || ''}
              onChange={(e) => setPatientData({ family_history: e.target.value })}
            />
          )}

          {/* Campos de Obstetrícia */}
          {isObstetric && headerConfig.include_gestational_age && (
            <Input
              label="Idade Gestacional"
              placeholder="Ex: 32 semanas"
              value={patientData.gestational_age || ''}
              onChange={(e) => setPatientData({ gestational_age: e.target.value })}
            />
          )}

          {isObstetric && headerConfig.include_gpa && (
            <Input
              label="GPA"
              placeholder="Ex: G2P1A0"
              value={patientData.gpa || ''}
              onChange={(e) => setPatientData({ gpa: e.target.value })}
            />
          )}

          {isObstetric && headerConfig.include_rapid_tests && (
            <Input
              label="Testes Rápidos"
              placeholder="Ex: HIV NR, VDRL NR, HBsAg NR"
              value={patientData.rapid_tests || ''}
              onChange={(e) => setPatientData({ rapid_tests: e.target.value })}
            />
          )}

          {/* Campos de Internação */}
          {isHospitalization && headerConfig.include_bed && (
            <Input
              label="Leito"
              placeholder="Ex: L04, Ex15"
              value={patientData.bed || ''}
              onChange={(e) => setPatientData({ bed: e.target.value })}
            />
          )}

          {isHospitalization && headerConfig.include_admission_date && (
            <Input
              label="Data de Internação"
              type="date"
              value={patientData.admission_date || ''}
              onChange={(e) => setPatientData({ admission_date: e.target.value })}
            />
          )}
        </div>
      </CardContent>
    </Card>
  );
}
