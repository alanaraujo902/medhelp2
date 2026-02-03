# 🏗️ ARQUITETURA COMPLETA CONSOLIDADA - MedPrompter
## Versão Final Integrada | 26/01/2026

---

## 📐 **FUNDAÇÃO: FASES DO PROJETO**

### **Fase 1: Banco de Módulos de Prompts** (ATUAL)
Objetivo: Criar estrutura robusta de templates reutilizáveis

### **Fase 2: Configuração Inteligente**
Usuário configura suas preferências 1x na vida da app (e pode editar anytime)

### **Fase 3: Reescrita Inteligente**
Usuário cola texto → IA identifica contexto, especialidade, sexo, idade → reescreve automaticamente

### **Fase 4: Distribuição e Integrações**
API, apps, web, LLMs, etc

---

## 🏥 **ESTRUTURA HIERÁRQUICA**

```
MEDPROMPTER
│
├── 🔧 CONFIGURAÇÕES GLOBAIS (Escolha 1x, editável sempre)
│   ├── Abreviações (quais manter/expandir)
│   ├── Estrutura de prontuário preferida
│   ├── Formatação (tabulações, separadores, espaçamento)
│   ├── Estilo de labs (com/sem unidades, formato inline/tabular)
│   ├── Estilo de medicações (nomes comerciais/genéricos, detalhamento)
│   ├── Assinatura padrão
│   └── Outras preferências pessoais
│
├── 🏥 PADRÕES ESTRUTURAIS (7 padrões principais)
│   ├── MFC (UBS/ESF)
│   ├── PA/UPA (Pronto Atendimento)
│   ├── Emergência Hospitalar
│   ├── Consultório
│   ├── Ambulatório - [Especialidade]
│   ├── Avaliação - [Especialidade]
│   └── Internação - [Especialidade]
│
└── 🎯 CONTEXTOS (variações por padrão)
    ├── MFC → Consulta / Pré-natal / Puericultura / Domiciliar
    ├── PA/UPA → Verde / Amarela / Vermelha / Internação
    ├── Emergência → Admissão / Evolução / Alta / Transferência
    ├── Consultório → 1ª consulta / Retorno / ASO
    ├── Ambulatório → 1ª consulta / Retorno (esp. específica)
    ├── Avaliação → [contexto único de interconsulta hospitalar]
    └── Internação → Admissão / Evolução diária / Sumário alta (esp. específica)
```

---

## **📊 MAPEAMENTO COMPLETO: ESPECIALIDADES E CONTEXTOS**

### **1. MFC (UBS/ESF)**
**Característica:** Atenção primária, generalist, completo e educativo

**Contextos:**
- Consulta geral
- Pré-natal baixo risco
- Puericultura
- Visita domiciliar

**Estrutura SOAP:**
- **Subjetivo:** Narrativo, contextual, acompanhantes mencionados
- **Objetivo:** Detalhado por sistemas
- **Avaliação/Impressão:** Diagnóstico + contexto social
- **Conduta:** Prescritivo, orientações longas e educativas

**Especialidades:** Clínica Geral, Pediatria, Obstetrícia (baixo risco)

---

### **2. PA/UPA (Pronto Atendimento)**

#### **2a) Sala Verde (Baixo Risco)**
- Estrutura SOAP ultra-abreviada
- Abreviações máximas: BEG, LOC, MUC, AA
- Tempo: 5-10 minutos
- Subjetivo: 2-3 linhas
- Objetivo: BEG LOC MUC AAA + sistemas relevan

tes
- Conduta: Curta, medicação sintomática

#### **2b) Sala Amarela (Risco Moderado)**
- Estrutura SOAP completa
- Abreviações moderadas
- Tempo: 10-15 minutos
- Subjetivo: 3-5 linhas com HDA
- Objetivo: Semi-detalhado por sistemas
- Conduta: Mais detalhada com exames e orientações

#### **2c) Sala Vermelha (Alto Risco/Urgência)**
- Estrutura SOAP rápida + observação frequente
- Reavaliações contínuas
- Abreviações máximas
- Foco em impressão + conduta urgente
- Monitorização constante

#### **2d) Contexto Internação (PA)**
- Paciente internado no PA/UPA
- Evolução diária curta
- Conduta de acompanhamento
- Monitorização de sinais vitais

---

### **3. Emergência Hospitalar**

**Característica:** Internação hospitalar com estrutura SOAP + observação pós-admissão

**Contextos:**
- Admissão de emergência
- Evolução diária hospitalar
- Nota de alta/transferência

**Estrutura:**
- **Subjetivo:** "Encontro paciente em leito..." (padrão fixo)
- **Objetivo:** Detalhado, sinais vitais estáveis ou não
- **Avaliação:** Diagnóstico + risco
- **Conduta:** "Mantidas" (evolução) ou "Ajustes" (mudanças)

**Especialidades:** Clínica Médica, Cirurgia Geral, Pediatria, Obstetrícia, Psiquiatria, UTI

---

### **4. Consultório (Privado/Convênio)**

**Característica:** Tempo mais longo, relação contínua com paciente, prescritivo e detalhado

**Contextos:**
- 1ª consulta: Completa com história detalhada
- Retorno: Subjetivo breve, foco em evolução
- ASO (Atestado de Saúde Ocupacional): Focado em capacidade laborativa

**Estrutura:**
- **Cabeçalho:** Identificação completa (nome, telefone, procedência)
- **História:** Comorbidades, medicações, alergias
- **HDA:** Sempre presente (narrativo)
- **Objetivo:** Semi-detalhado a detalhado por sistemas
- **Impressão:** Diagnóstico + contexto
- **Conduta:** "Converso com paciente..." (educativo), prescrições ultra-detalhadas

**Especialidades:** Todas (cada uma com variações)

---

### **5. Ambulatório - [Especialidade]**

**Característica:** Consultas agendadas, investigação aprofundada, especializada

**Contextos:**
- 1ª consulta: História completa + lista de problemas
- Retorno: Focado em evolução de problemas prévios

**Estrutura:**
- **Identificação:** Completa + motivo do encaminhamento
- **História Médica Pregressa:** Detalhada por sistemas
- **HDA:** Narrativa especializada
- **Objetivo:** Exame físico geral + específico da especialidade
- **Exames:** Organizados por modalidade (labs, imagem, específicos)
- **Impressão:** Diagnóstico/hipóteses diagnósticas
- **Conduta:** Plano terapêutico + seguimento

**Especialidades Mapeadas:**
- **Cirurgia Geral:** Foco em abdome, hérnias, APOA
- **Cirurgia Vascular:** Tabela de pulsos, ITB, lesões vasculares
- **Cardiologia:** Ausculta cardíaca detalhada, ECG, ecocardiograma
- **Endocrinologia:** 
  - Tireoide: TI-RADS, PAAF, eco com doppler
  - DM: Recordatório alimentar, HGT, insulinoterapia
  - Geral: Revisão de Sistemas completa, IMC sempre calculado
- **Ginecologia-Obstetrícia:**
  - Pré-natal (PNAR - Alto Risco): Lista de problemas gineco-obstétricos, orientações pré-natal massivas
  - Gineco Geral: Ciclos, contracepção, IST
  - Infertilidade: Histórico do parceiro, exames de reserva ovariana
  - Mastologia: HDA narrativa, exame de mamas por lateralidade (Direita/Esquerda)
  - Endócrino-Gineco: Índice Menopausal de Kupperman, TRH
  - OncoGinecologia: Ultra-compacto, BEG LOC MUC, rotina pré-operatória
  - PTGI: Colposcopia, Teste de Schiller, siglas de lesões (LIEAG, LIEBG)

---

### **6. Avaliação - [Especialidade]**

**Característica:** Interconsulta hospitalar - paciente já internado, especialidade chamada para avaliar

**Contextos:**
- Sempre avaliação de interconsulta

**Estrutura:**
- **Identificação:** Breve (já internado)
- **Motivo da internação:** Resumido
- **Motivo da avaliação:** Específico (por que a especialidade foi chamada)
- **Anamnese dirigida:** Perguntas específicas da especialidade
- **Exame físico:** Geral breve + específico detalhado
- **Impressão:** Da especialidade sobre o caso
- **Conduta:** Recomendações da especialidade

**Exemplos:**
- Avaliação - Cardiologia (paciente internado em clínica, cardio chamado)
- Avaliação - Endocrinologia (paciente internado em cirurgia, endócr chamado para DM)

---

### **7. Internação - [Especialidade]**

**Característica:** Paciente internado em leito. Admissão, evoluções diárias, sumário de alta

**Contextos:**
- **Admissão:** História completa, identificação do leito
- **Evolução Diária:** Curta (2-4 parágrafos), dinâmica
- **Sumário de Alta:** Narrativa da internação + recomendações

**Estrutura Varia por Especialidade:**

#### **7a) Internação Psiquiátrica**
- **Estrutura única:** EEM (Exame do Estado Mental) padronizado
- **Checklist pré-evolução:** Pensamentos, sono, riscos, fissura
- **Identificação completa:** Etnia, religião, escolaridade, contatos
- **15 componentes do EEM:** Hiiene, consciência, atenção, orientação, pensamento, sensopercepção, afeto, humor, inteligência, memória, fala, psicomotricidade, insight, conduta, juízo crítico
- **Prescrição medicamentosa:** Numerada (1), (2), etc
- **Assinatura:** R1 + Supervisor

#### **7b) Internação Endocrinologia**
- **Identificação:** Telefone, ocupação, sala de recuperação específica
- **Patologia - Exames:** Seção separada (AP, diagnóstico histopatológico)
- **"Encontro paciente em leito da sala de recuperação"** (padrão fixo)
- **Sinais clínicos específicos:** Trousseau, Chvostek, etc
- **Tracking de valores PO:** Ca, PTH em evolução temporal
- **Conduta conforme discussão:** Decisão em equipe

#### **7c) Internação Obstetrícia (Maternidade)**
- **Alta Hospitalar Pós-Parto:** Narrativa única (sem SOAP)
- **GxPxCxAx:** No início
- **RN:** APGAR, peso, sexo, placenta em gramas
- **Orientações de Alta:** Bloco detalhado (abstinência sexual, amamentação, revisão gineco, etc)
- **ATM:** 120 dias de licença-maternidade
- **Receitas:** Detalhadas por tipo de parto (normal/cesárea/episiotomia)

#### **7d) Internação Clínica Geral**
- **Estrutura SOAP padrão**
- **"Encontro paciente em leito..."** (padrão)
- **Avaliação diária curta** (2-3 parágrafos)
- **Evolução de sintomas**
- **Ajustes de tratamento**

#### **7e) Centro Obstétrico (CO)**
- **ULTRA COMPACTO:** 5-10 linhas total
- **Título:** `--- Avaliação de [Procedimento] ---`
- **Procedimentos específicos:** DU (dinâmica uterina), MAP (monitorização anteparto), Ocitocina, MgSO4
- **"Avaliação finalizada às XX:"** (hora exata)
- **"Informo equipe médica"** (obrigatório)
- **Sem impressão** - conduta direta

#### **7f) Emergência Obstétrica (EO)**
- **Identificação:** "Nome do bebê" entre aspas (se escolhido)
- **IG:** Sempre formato XX+X com data da eco que datou
- **Vacinas e Sorologias:** Inline com | separadores
- **Exame Obstétrico:** AU, MF, BCF, DU, TU, períneo, EE, TV
- **TV:** Formato (G/M/F, P/C, dilatação em cm)

---

## **🎯 ESPECIALIDADES POR PADRÃO**

### **Presente em TODOS os padrões:**
- Clínica Geral/Medicina Interna
- Pediatria
- Obstetrícia (variações)

### **Presente em Ambulatório + Internação + Avaliação:**
- Cardiologia
- Pneumologia
- Gastroenterologia
- Neurologia
- Reumatologia
- Nefrologia
- Oncologia
- Infectologia

### **Presente em Ambulatório + Internação:**
- Endocrinologia
- Cirurgia Geral
- Cirurgia Vascular
- Urologia
- Otorrinolaringologia
- Oftalmologia

### **Presente em Ginecologia-Obstetrícia (MÚLTIPLAS SUBESPECIALIDADES):**
- Obstetrícia (Geral + Alto Risco)
- Ginecologia Geral
- Endócrino-Ginecologia (Infertilidade, Climatério)
- Mastologia
- OncoGinecologia
- PTGI (Patologias do Trato Genital Inferior)

### **Presente em Psiquiatria:**
- Psiquiatria Geral (adulto + infanto-juvenil)
- Com Internação + Centro Dia possível
- EEM obrigatório

---

## **🔧 CONFIGURAÇÕES GLOBAIS**

Usuário escolhe **UMA VEZ** (e pode alterar no menu Configurações):

### **1. Abreviações**
```
[ ] Extremas (BEG, LOC, MUC, AAA, MVUD, etc)
[ ] Moderadas (Orosc, SR, SCV, Abd, mas estado geral por extenso)
[ ] Híbridas (meio termo - BEG LOTE AAA mas sistemas detalhados)
[ ] Mínimas (quase por extenso, exceto de lista)
```

### **2. Estrutura de Prontuário**
```
[ ] SOAP (Subjetivo-Objetivo-Avaliação-Conduta)
[ ] SOEIC (Subjetivo-Objetivo-Exames-Impressão-Conduta)
[ ] HDA-SOAP (História Doença Atual estruturada)
```

### **3. Formatação**
```
[ ] Hipertexto simples (markdown nativo)
[ ] Com bullets/dashes para listas
[ ] Com espaçamento amplo entre seções
[ ] Compacto (espaçamento mínimo)
[ ] Com separadores visuais (---, ===, etc)
```

### **4. Estilo de Labs**
```
[ ] Inline com | separador: Hb 13,2 | Ht 39 | Leu 5.234
[ ] Inline com / separador: Hb 13,2 / Ht 39 / Leu 5.234
[ ] Com valores de referência: Hb 13,2 (12-17)
[ ] Sem unidades: Hb 13,2
[ ] Com unidades: Hb 13,2 g/dL
[ ] Tabular/visual (quando muitos valores)
```

### **5. Estilo de Medicações**
```
[ ] Nomes genéricos apenas: Ibuprofeno 600mg
[ ] Nomes genéricos + comerciais: Ibuprofeno 600mg (Ibuprofeno, Antiflamantório-X)
[ ] Ultra-detalhadas com instruções: dose, forma, horários, duração, alertas
[ ] Simples: nome e dose
```

### **6. Assinatura**
```
Modelo:
[Título] [Nome]
[Pós-graduação/Residência]
[Outros]
```

---

## **📋 BANCO DE MÓDULOS ESTRUTURADO**

### **Organização de Módulos:**

```
/prompt_modules/

├── base/
│   └── PROMPT_BASE_001.md
│       (Instruções anti-invenção, regras críticas, checklist)
│
├── contexto/
│   ├── CONTEXTO_MFC.md
│   ├── CONTEXTO_PA_SALA_VERDE.md
│   ├── CONTEXTO_PA_SALA_AMARELA.md
│   ├── CONTEXTO_PA_SALA_VERMELHA.md
│   ├── CONTEXTO_PA_INTERNACAO.md
│   ├── CONTEXTO_EMERGENCIA_HOSPITALAR.md
│   ├── CONTEXTO_CONSULTORIO.md
│   ├── CONTEXTO_AMBULATORIO.md
│   ├── CONTEXTO_AVALIACAO.md
│   └── CONTEXTO_INTERNACAO.md
│
├── cabecalho/
│   ├── CABECALHO_MFC.md
│   ├── CABECALHO_PA.md
│   ├── CABECALHO_EMERGENCIA.md
│   ├── CABECALHO_CONSULTORIO.md
│   ├── CABECALHO_AMBULATORIO.md
│   ├── CABECALHO_INTERNACAO.md
│   └── CABECALHO_INTERNACAO_OBSTETRICA.md
│
├── historia/
│   ├── HISTORIA_COMORBIDADES_SISTEMAS.md
│   ├── HISTORIA_MEDICACOES.md
│   ├── HISTORIA_ALERGIAS.md
│   ├── HISTORIA_SOCIAL.md
│   ├── HISTORIA_FAMILIAR.md
│   ├── HISTORIA_GINECO_OBSTETRICA.md
│   ├── HISTORIA_VASCULAR.md
│   └── HISTORIA_PSIQUIATRICA.md
│
├── hda/
│   ├── HDA_NARRATIVO_DETALHADO.md
│   ├── HDA_COMPACTO.md
│   ├── HDA_OBSTETRICO.md
│   └── HDA_PSIQUIATRICO.md
│
├── subjetivo/
│   ├── SUBJETIVO_MFC_NARRATIVO.md
│   ├── SUBJETIVO_PA_VERDE_COMPACTO.md
│   ├── SUBJETIVO_PA_AMARELA_SEMI.md
│   ├── SUBJETIVO_EMERGENCIA_ENCONTRO.md
│   ├── SUBJETIVO_CONSULTORIO_DETALHADO.md
│   ├── SUBJETIVO_AMBULATORIO.md
│   ├── SUBJETIVO_INTERNACAO_ENCONTRO.md
│   ├── SUBJETIVO_CO_ULTRA_COMPACTO.md
│   ├── SUBJETIVO_EO_OBSTETRICO.md
│   └── SUBJETIVO_PSIQUIATRIA_EEM.md
│
├── objetivo/
│   ├── OBJETIVO_MFC_COMPLETO.md
│   ├── OBJETIVO_PA_ABREVIADO_EXTREMO.md
│   ├── OBJETIVO_PA_SEMI_DETALHADO.md
│   ├── OBJETIVO_EMERGENCIA_ESTAVEL_INSTAVEL.md
│   ├── OBJETIVO_CONSULTORIO_DETALHADO.md
│   ├── OBJETIVO_AMBULATORIO.md
│   ├── OBJETIVO_INTERNACAO_COMPLETO.md
│   ├── OBJETIVO_CO_OBSTETRICO.md
│   ├── OBJETIVO_EO_OBSTETRICO.md
│   ├── OBJETIVO_CARDIO_ESPECIFICO.md
│   ├── OBJETIVO_VASCULAR_ESPECIFICO.md
│   ├── OBJETIVO_PSIQUIATRIA_EEM_COMPLETO.md
│   ├── OBJETIVO_PSIQUIATRIA_EEM_ABREVIADO.md
│   └── OBJETIVO_GINECO_MAMAS_DETALHADAS.md
│
├── exames/
│   ├── EXAMES_LABS_INLINE.md
│   ├── EXAMES_LABS_TABULAR.md
│   ├── EXAMES_IMAGEM_LAUDO.md
│   ├── EXAMES_IMAGING_ESPECIFICO_CARDIO.md
│   ├── EXAMES_VASCULAR_PULSOS_ITB.md
│   ├── EXAMES_OBSTETRICO_ECO.md
│   ├── EXAMES_OBSTETRICO_CTG.md
│   ├── EXAMES_PSIQUIATRIA_LABS.md
│   └── EXAMES_ESPECIFICO_GINECO.md
│
├── impressao/
│   ├── IMPRESSAO_DIAGNOSTICO_SINTETICO.md
│   ├── IMPRESSAO_DIAGNOSTICO_DIFERENCIAL.md
│   ├── IMPRESSAO_RISCO_ESTRATIFICACAO.md
│   ├── IMPRESSAO_PROBLEMA_LISTA.md
│   ├── IMPRESSAO_OBSTETRICA_BAIXO_ALTO_RISCO.md
│   └── IMPRESSAO_PSIQUIATRIA_DIAGNOSTICOS.md
│
├── conduta/
│   ├── CONDUTA_CONVERSAO_AUSENTE.md
│   ├── CONDUTA_CONVERSAO_CURTA.md
│   ├── CONDUTA_CONVERSAO_LONGA_PADRAO.md
│   ├── CONDUTA_PRESCRICAO_NOMES.md
│   ├── CONDUTA_PRESCRICAO_DETALHADA.md
│   ├── CONDUTA_PRESCRICAO_ULTRA_DETALHADA.md
│   ├── CONDUTA_SINAIS_ALARME_GERAL.md
│   ├── CONDUTA_SINAIS_ALARME_ESPECIFICO.md
│   ├── CONDUTA_EXAMES_SOLICITACAO.md
│   ├── CONDUTA_SEGUIMENTO_RETORNO.md
│   ├── CONDUTA_ALTA_HOSPITALAR.md
│   ├── CONDUTA_INTERNACAO_DECISAO.md
│   ├── CONDUTA_OBSTETRICA_ORIENTACOES_PARTO.md
│   ├── CONDUTA_OBSTETRICA_ORIENTACOES_PRENATAL.md
│   └── CONDUTA_PSIQUIATRIA_PLANO.md
│
├── abreviacoes/
│   ├── ABREVIACOES_EXTREMAS.md
│   ├── ABREVIACOES_MODERADAS.md
│   ├── ABREVIACOES_HIBRIDAS.md
│   ├── ABREVIACOES_MINIMAS.md
│   ├── ABREVIACOES_OBSTETRICA.md
│   ├── ABREVIACOES_VASCULAR.md
│   └── ABREVIACOES_PSIQUIATRIA.md
│
├── formatacao/
│   ├── FORMATACAO_LABS_INLINE.md
│   ├── FORMATACAO_LABS_TABULAR.md
│   ├── FORMATACAO_MEDICACOES.md
│   ├── FORMATACAO_DATAS.md
│   ├── FORMATACAO_LISTAS.md
│   └── FORMATACAO_SEPARADORES.md
│
├── templates_especiais/
│   ├── TEMPLATE_ALTA_HOSPITALAR_OBSTETRICA.md
│   ├── TEMPLATE_CENTRO_OBSTETRICO.md
│   ├── TEMPLATE_EMERGENCIA_OBSTETRICA.md
│   ├── TEMPLATE_PNAR.md
│   ├── TEMPLATE_EEM_PSIQUIATRIA_COMPLETO.md
│   ├── TEMPLATE_EEM_PSIQUIATRIA_ABREVIADO.md
│   ├── TEMPLATE_VASCULAR_PULSOS_ITB.md
│   ├── TEMPLATE_CARDIO_AUSCULTA.md
│   ├── TEMPLATE_GINECO_MAMAS_DIREITA_ESQUERDA.md
│   ├── TEMPLATE_AMBULATORIO_LISTA_PROBLEMAS.md
│   ├── TEMPLATE_INTERNACAO_PSIQUIATRIA_CHECKLIST.md
│   └── TEMPLATE_ASO_OCUPACIONAL.md
│
└── checklists/
    ├── CHECKLIST_ANTI_INVENCAO.md
    ├── CHECKLIST_COMPLETUDE_SOAP.md
    ├── CHECKLIST_ABREVIACOES_CONSISTENCIA.md
    ├── CHECKLIST_FORMATACAO_CONSISTENCIA.md
    ├── CHECKLIST_MEDICACOES_SEGURANCA.md
    ├── CHECKLIST_ORIENTACOES_PACIENTE.md
    ├── CHECKLIST_SINAIS_ALARME.md
    ├── CHECKLIST_OBSTETRICA.md
    ├── CHECKLIST_PSIQUIATRIA.md
    ├── CHECKLIST_VASCULAR.md
    ├── CHECKLIST_CARDIO.md
    ├── CHECKLIST_INTERNACAO.md
    ├── CHECKLIST_ALTA_HOSPITALAR.md
    └── CHECKLIST_FINAL_UNIVERSAL.md
```

---

## **⚡ REGRAS CRÍTICAS UNIVERSAIS**

### **1. Anti-Invenção (ABSOLUTO)**
```
❌ NUNCA adicionar informações não fornecidas
❌ NUNCA criar dados clínicos fictícios
❌ NUNCA interpretar exames criando história
❌ NUNCA omitir informações do original
❌ NUNCA inferir diagnósticos não mencionados
```

### **2. Completude de Informações (OBRIGATÓRIO)**
```
✅ SEMPRE copiar TODAS as informações fornecidas
✅ SEMPRE manter a ordem lógica do SOAP
✅ SEMPRE incluir negativas relevantes
✅ SEMPRE completar seções conforme padrão
✅ SEMPRE manter coerência clínica
```

### **3. Formatação Consistente (OBRIGATÓRIO)**
```
✅ SEMPRE usar abreviações escolhidas pelo usuário
✅ SEMPRE manter estilo de labs escolhido
✅ SEMPRE manter estilo de medicações escolhido
✅ SEMPRE usar padrão de datas do usuário
✅ SEMPRE manter hierarquia de títulos consistente
```

### **4. Segurança do Paciente (CRÍTICO)**
```
✅ SEMPRE incluir sinais de alarme apropriados
✅ SEMPRE mencionar retorno/seguimento
✅ SEMPRE verificar doses de medicações
✅ SEMPRE confirmar contraindicações óbvias
✅ NUNCA recomendar ações não-médicas
```

### **5. Inteligência Contextual (AUTOMÁTICO)**
```
✅ IA identifica sexo, idade, contexto sem perguntar
✅ IA ajusta linguagem (adulto vs pediátrico)
✅ IA ajusta abreviações vs extenso conforme contexto
✅ IA escolhe SOAP variação correta
✅ IA seleciona módulos apropriados sem intervenção
```

---

## **📊 FLUXO DE USO DO APP**

### **1. Primeiro Acesso**
```
1. Usuário faz login
2. Pergunta: "Qual seu padrão principal?" (MFC/PA/Emergência/Consultório/etc)
3. Pergunta: "Qual sua especialidade principal?"
4. Abre CONFIGURAÇÕES GLOBAIS (abreviações, formatação, labs, meds, etc)
5. Salva preferências → pronto para usar
```

### **2. Uso Diário**
```
1. Usuário abre app
2. Escolhe PADRÃO (MFC/PA/Emergência/etc) e CONTEXTO (Green/Yellow/etc)
3. Cola texto desorganizado
4. Clica "Reescrever"
5. IA:
   - Identifica sexo, idade, especialidade
   - Carrega configurações do usuário
   - Seleciona contexto + padrão
   - Aplica módulos apropriados
   - Reescreve no formato correto
6. Usuário revisa, edita se necessário, copia para prontuário
```

### **3. Configuração (Menu)**
```
Usuário pode alterar anytime:
- Abreviações
- Formatação
- Estilo labs
- Estilo medicações
- Assinatura
- Outras preferências
```

---

## **🔑 ELEMENTOS ÚNICOS POR CONTEXTO**

### **MFC**
- "Paciente em consulta desacompanhado/acompanhado"
- Revisão de Sistemas completa
- Educativo: "Oriento...", "Explico..."
- Prescrições detalhadas com alertas
- Sinais de alarme padronizados
- "- ciente e concordante"
- Encaminhamentos para especialidade

### **PA Verde**
- "BEG LOC MUC AAA" padrão
- Abreviações máximas
- Subjetivo 2-3 linhas
- Conduta: meds sintomáticas
- Sem exames (ou inline)

### **PA Amarela**
- Abreviações moderadas
- Subjetivo 3-5 linhas com HDA
- Objetivo semi-detalhado
- Exames básicos
- Conduta: meds + possível exame

### **PA Vermelha**
- Reavaliações contínuas
- Monitorização constante
- Urgência na conduta
- Possível internação

### **Emergência Hospitalar**
- "Encontro paciente em leito..."
- SVE (sinais vitais estáveis)
- Evolução diária curta
- "Mantidas" (conduta)
- Acompanhamento contínuo

### **Consultório**
- Identificação completa + telefone
- "Paciente vem a consulta...acompanhado por..."
- "Converso com paciente em linguagem leiga..." (obrigatório)
- Prescrições ULTRA-detalhadas
- Atestados + receitas
- "- ciente e concordante"

### **Ambulatório**
- "Motivo do Encaminhamento"
- Lista de problemas (especialmente Gineco)
- Revisão de Sistemas (especialmente Endocrinologia)
- Exames específicos da especialidade
- Plano terapêutico detalhado
- Retorno agendado

### **Avaliação (Interconsulta)**
- "Motivo da avaliação"
- Anamnese dirigida à especialidade
- Exame físico focado
- Impressão específica
- Recomendações ao time

### **Internação**
- "Encontro paciente em leito da [sala/ala]..."
- Identificação do leito
- Evolução diária curta
- Ajustes terapêuticos
- Sumário de alta narrativo
- Orientações de alta detalhadas (especialmente Obstetrícia)

### **Obstetrícia/Ginecologia - Elementos Únicos**
- GxPxCxAx (identificação)
- "Nome do bebê" entre aspas (quando escolhido)
- IG em XX+X (semanas+dias)
- TV: (G/M/F, P/C, dilatação)
- Orientações PRÉ-NATAL: bloco gigante e padronizado
- Orientações Condicionais: `→ SE DMG`, `→ SE HAS`
- ATM: 120 dias licença-maternidade
- "Nega disúria ou febre. Nega perdas líquidas..."
- "Relata boa movimentação fetal"
- Exame de Mamas: "Pendulares, simétricas..."
- "abdome gravídico" (não globoso)

### **Psiquiatria - Elementos Únicos**
- EEM (Exame do Estado Mental): 15 componentes obrigatórios
- Checklist pré-evolução
- Identificação completa (etnia, religião, escolaridade)
- Medicações numeradas: (1), (2), etc
- "Questionado/Questionada, refere..."
- Risco de suicídio/heteroagressão sempre mencionado
- Plano terapêutico específico

### **Vascular - Elementos Únicos**
- Tabela de pulsos: Comparativa temporal (D/E, scores)
- ITB (Índice Tornozelo-Braquial): cálculos
- "TEC" (Tempo Enchimento Capilar)
- Histórico cirúrgico vascular com datas [DD/MM/AA]
- "RETORNO EM X MESES" (sempre CAPS)
- Tracking de lesões/feridas (FO)

---

## **🎯 PROCESSO DE DESENVOLVIMENTO**

### **Fase 1: Banco de Módulos (AGORA)**
1. ✅ Arquitetura definida
2. ⏳ Criar tabela mestra detalhada (todos os módulos + dependências)
3. ⏳ Escrever PROMPT_BASE_001 (regras críticas anti-invenção)
4. ⏳ Escrever módulos contexto (10 módulos)
5. ⏳ Escrever módulos cabeçalho (7 módulos)
6. ⏳ Escrever módulos história (8 módulos)
7. ⏳ Escrever módulos subjetivo (10 módulos)
8. ⏳ Escrever módulos objetivo (13 módulos)
9. ⏳ Escrever módulos exames (9 módulos)
10. ⏳ Escrever módulos impressão (6 módulos)
11. ⏳ Escrever módulos conduta (15 módulos)
12. ⏳ Escrever módulos abreviações (7 módulos)
13. ⏳ Escrever módulos formatação (6 módulos)
14. ⏳ Escrever templates especiais (12 módulos)
15. ⏳ Escrever checklists (14 módulos)
16. ⏳ Validar com casos de teste reais

### **Total de Módulos Base:** ~140 módulos atomizados

### **Composição de Prompts:**
Cada prompt é composição de:
- 1x PROMPT_BASE
- 1x CONTEXTO
- 1x CABEÇALHO
- Múltiplos HISTÓRIA (conforme necessário)
- 1x HDA (se aplicável)
- 1x SUBJETIVO
- 1x OBJETIVO (ou múltiplos para especialidades)
- Múltiplos EXAMES (conforme necessário)
- 1x IMPRESSÃO
- Múltiplos CONDUTA (conforme necessário)
- 1x ABREVIACOES (conforme config usuário)
- 1x FORMATACAO (conforme config usuário)
- 1x CHECKLIST (universal)

---

## **✅ PRINCÍPIOS FINALISTAS**

1. **Usuário escolhe 1x suas preferências** → app faz o resto automaticamente
2. **IA identifica contexto automaticamente** → sem perguntas extras
3. **Módulos são atomizados e reutilizáveis** → máxima flexibilidade
4. **Regras anti-invenção são ABSOLUTAS** → zero tolerância
5. **Cada prompt é composição inteligente** → não templates copy-paste
6. **Especialidades variadas** → mas mesma lógica
7. **Segurança do paciente primeiro** → sempre
8. **Velocidade no uso** → mínimo de cliques
9. **Qualidade garantida** → checklists múltiplos
10. **Configuração flexível** → usuário no controle

---

## **🚀 STATUS FINAL**

### **✅ CONSOLIDADO:**
- Arquitetura completa (7 padrões × múltiplos contextos)
- 27+ contextos mapeados
- 40+ especialidades incluídas
- Subespecialidades Gineco detalhadas (6 tipos)
- Regras críticas universais definidas
- Fluxo de UX claro
- Banco de módulos estruturado (~140 módulos)
- Configurações globais especificadas

### **⏳ PRÓXIMO:**
Iniciar escrita dos módulos conforme prioridade:

**Tier 1 (Crítico):**
- PROMPT_BASE_001
- CONTEXTO_PA_SALA_VERDE
- CONTEXTO_CONSULTORIO
- CONTEXTO_AMBULATORIO

**Tier 2 (Importante):**
- Módulos SUBJETIVO, OBJETIVO, CONDUTA (principais variações)
- TEMPLATE_OBSTETRICA
- TEMPLATE_EEM_PSIQUIATRIA

**Tier 3 (Complementar):**
- Módulos especializados por especialidade
- Checklists
- Formatação

---

**Arquitetura consolidada e pronta para produção! 🎯**