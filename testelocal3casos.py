from PROMPT_BASE_001_v2 import PromptBaseMedPrompter

prompt_base = PromptBaseMedPrompter()

# Teste os 3 casos:
casos = {
    "CASO_1": """Paciente João Silva, 45 anos, masculino. Chega com dor abdominal forte.
Começou ontem à noite. Sente náuseas e vômitos.
Tem diabetes e pressão alta desde 10 anos.
Toma metformina 1000mg e losartana 50mg.
Vitais: PA 160/100, FC 110, T 37.2.
Abdômen: distendido, sensível, sem peritonite.""",
    
    "CASO_2": """Marta, 34 anos, feminina. Retorno em ambulatório de endocrinologia.
Diabética tipo 2 desde 8 anos. Refere dificuldade em controle glicêmico.
Medicações atuais: metformina 850mg 3x, glipizida 5mg 2x, insulina lantus 20UI noturna.
Nega disúria, polidipsia, claudicação. Comorbidades: HAS, hiperlipidemia.
Antecedentes: cesariana, apendicectomia.
PA: 130/80, FC: 75, IMC: 32 (obesa).
Glicemia capilar: 280 mg/dL.
Solicitar: hemoglobina glicosilada, colesterol, triglicerídeos, TSH.
Orientações: dieta, atividade física, retorno em 30 dias.""",
    
    "CASO_3": """Paciente Lucas, 28 anos, masculino. Internado há 3 dias por depressão grave.
Hoje apresenta-se mais comunicativo. Dormiu bem à noite.
Nega ideação suicida atualmente. Cooperativo e orientado.
Medicações: sertralina 100mg, trazodona 50mg à noite, haloperidol 5mg.
Sem alucinações visuais ou auditivas referidas.
Apetite melhorado. Higiene pessoal adequada.
Próximo: manter medicações, avaliação do psicólogo amanhã."""
}

for nome, texto in casos.items():
    print(f"\n{'='*80}")
    print(f"🧪 {nome}")
    print('='*80)
    resultado = prompt_base.processar_texto_medico(texto)
    print(f"✅ Contexto: {resultado.identificacao.contexto.value}")
    print(f"✅ Especialidade: {resultado.identificacao.especialidade.value}")
    print(f"✅ Sexo: {resultado.identificacao.sexo.value}")
    print(f"✅ Idade: {resultado.identificacao.idade}")
    print(f"✅ Tipo: {resultado.identificacao.tipo_atendimento.value}")
    print(f"✅ Confiança: {resultado.identificacao.confianca:.1%}")
