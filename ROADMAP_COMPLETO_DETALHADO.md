# 🚀 ROADMAP COMPLETO - MedPrompter
## Visão Geral com Detalhamento das Fases | 26/01/2026

---

## 📐 **VISÃO GERAL DO PROJETO**

```
FASE 1: Banco de Módulos          FASE 2: Configuração              FASE 3: Reescrita                  FASE 4: Distribuição
(VOCÊ: Prompts)                   Inteligente (Alan: Backend)       Automática (Alan: IA)              (Alan: DevOps)
│                                 │                                 │                                   │
├─ Módulos atomizados             ├─ Persistência de config          ├─ Identificação automática        ├─ API REST
├─ Templates reutilizáveis        ├─ UI das preferências             ├─ Seleção de módulos              ├─ Apps mobile
├─ Banco de dados estruturado     ├─ Validação de inputs             ├─ Composição inteligente          ├─ Integrações
└─ Documentação de specs           └─ Testes de config               └─ Verificação de qualidade        └─ Deploy
```

---

## 🎯 **FASE 1: BANCO DE MÓDULOS (VOCÊ - PROMPTS)**

### **Objetivo:** 
Criar biblioteca atomizada de ~140 módulos de prompts que são blocos de construção para qualquer evolução/consulta médica.

### **Entrega:** 
Arquivo estruturado com todos os módulos em markdown + documentação de composição

---

## **1.1 ESTRUTURA DOS MÓDULOS**

### **Tipo 1: PROMPT_BASE (1 módulo)**

**O que é:** Instruções fundamentais que NUNCA mudam. Todo prompt composto começa com isso.

**Seu conteúdo:**
```
## 🔴 REGRAS CRÍTICAS - ANTI-INVENÇÃO

1. NUNCA adicione informações não fornecidas
2. NUNCA crie dados clínicos fictícios
3. NUNCA interprete exames criando história
4. NUNCA omita informações do original
5. NUNCA invente diagnósticos

## 🤖 IDENTIFICAÇÃO AUTOMÁTICA (para Alan implementar)

[IA deve identificar AUTOMATICAMENTE:]
- Idade do paciente (para ajustar linguagem)
- Sexo (para concordância e procedimentos específicos)
- Contexto (PA vs Ambulatório vs Internação)
- Especialidade (Gineco, Cardio, Neuro, etc)
- Subtipo (1ª consulta vs retorno)

[IA NÃO deve perguntar nada - apenas identificar]

## ✅ COMPLETUDE E COERÊNCIA

1. Sempre copiar TODAS as informações fornecidas
2. Manter ordem lógica SOAP/SOEIC
3. Incluir negativas relevantes
4. Completar seções conforme padrão
5. Manter coerência clínica

## 🔒 SEGURANÇA

1. Incluir sinais de alarme apropriados
2. Mencionar retorno/seguimento
3. Verificar doses de medicações (não recomendações)
4. Confirmar contraindicações óbvias
5. NUNCA recomendações não-médicas
```

**Custo de tempo:** 2-3 horas (escrever bem, testar lógica)

---

### **Tipo 2: MÓDULOS CONTEXTO (10 módulos)**

**O que é:** Define o "where" - em qual ambiente está acontecendo o atendimento?

**Seus 10 tipos:**
1. CONTEXTO_MFC.md
2. CONTEXTO_PA_SALA_VERDE.md
3. CONTEXTO_PA_SALA_AMARELA.md
4. CONTEXTO_PA_SALA_VERMELHA.md
5. CONTEXTO_PA_INTERNACAO.md
6. CONTEXTO_EMERGENCIA_HOSPITALAR.md
7. CONTEXTO_CONSULTORIO.md
8. CONTEXTO_AMBULATORIO.md
9. CONTEXTO_AVALIACAO.md
10. CONTEXTO_INTERNACAO.md

**Estrutura de CADA módulo (exemplo CONTEXTO_PA_SALA_VERDE):**

```markdown
# CONTEXTO: PA/UPA - Sala Verde

## Definição
Você está formatando um atendimento de PRONTO ATENDIMENTO em baixo risco.

## Características
- Tempo disponível: 5-10 minutos
- Abreviações: MÁXIMAS (BEG, LOC, MUC, AAA)
- Paciente: Estável, sem perigo de vida iminente
- Objetivo: Diagnóstico rápido + conduta sintomática

## Estrutura OBRIGATÓRIA
- Cabeçalho: Mínimo
- História: Comorbidades apenas se relevante
- Subjetivo: 2-3 linhas, bem objetivo
- Objetivo: BEG LOC MUC AAA + sistemas relevantes (abreviado)
- Exames: Inline ou ausentes
- Impressão: 1 linha
- Conduta: Medicação sintomática + retorno se piorar

## O que NUNCA fazer
- Texto narrativo longo
- Explicações detalhadas
- Exame físico completo
- Abreviações insuficientes
- Perguntas ao paciente

## Diferenças das OUTRAS salas do PA
- Sala Amarela: Tempo 10-15min, mais detalhado, exames básicos
- Sala Vermelha: Reavaliações contínuas, urgência, possível internação
```

**Custo de tempo por módulo:** 1-1,5 horas (definir características + diferenças)

**Total Tipo 2:** 10-15 horas

---

### **Tipo 3: MÓDULOS CABEÇALHO (7 módulos)**

**O que é:** Define "como começar" cada tipo de prontuário

**Seus 7 tipos:**
1. CABECALHO_MFC.md
2. CABECALHO_PA.md
3. CABECALHO_EMERGENCIA.md
4. CABECALHO_CONSULTORIO.md
5. CABECALHO_AMBULATORIO.md
6. CABECALHO_INTERNACAO.md
7. CABECALHO_INTERNACAO_OBSTETRICA.md

**Estrutura de CADA módulo (exemplo CABECALHO_PA):**

```markdown
# CABEÇALHO: PA/UPA

## Formato Obrigatório

PA - [Especialidade] - [Data DD/MM/AA]
[NOME], [IDADE]

# História Relevante (se houver)
# Medicamentos em uso (se houver)
# Alergias

## Notas
- Data SEMPRE em formato DD/MM/AA
- Idade: somente número
- História: APENAS se comorbidades relevantes ao caso
- Medicamentos: APENAS se em uso contínuo e relevante
- Alergias: SEMPRE mencionar (nega se não houver)

## Exemplo Real
PA - Clínica Geral - 26/01/26
Maria da Silva, 34

# HAS
# MED: Losartana 50mg 1x/dia
# Alergias: Nega

```

**Custo de tempo por módulo:** 0,5-1 hora (formato + exemplos)

**Total Tipo 3:** 3,5-7 horas

---

### **Tipo 4: MÓDULOS HISTÓRIA (8 módulos)**

**O que é:** Como estruturar o histórico do paciente em diferentes contextos

**Seus 8 tipos:**
1. HISTORIA_COMORBIDADES_SISTEMAS.md
2. HISTORIA_MEDICACOES.md
3. HISTORIA_ALERGIAS.md
4. HISTORIA_SOCIAL.md
5. HISTORIA_FAMILIAR.md
6. HISTORIA_GINECO_OBSTETRICA.md
7. HISTORIA_VASCULAR.md
8. HISTORIA_PSIQUIATRICA.md

**Estrutura de CADA módulo (exemplo HISTORIA_COMORBIDADES_SISTEMAS):**

```markdown
# HISTÓRIA: Comorbidades por Sistemas

## Quando Usar
Em ambulatório, consultório, internação - quando precisa lista completa

## Formato

### Cardiovascular
- HAS (desde 2015, em uso de losartana)
- DAC (PO CRM 2022)

### Pulmonar
- DPOC (tabagista 40 anos-maço)

### Endócrino
- DM2 (desde 2010, em uso de metformina)

### Outros
- Obesidade (IMC 32 kg/m²)

## Regras
1. Organizar por SISTEMA (não por relevância)
2. Incluir DATAS quando disponível
3. Adicionar contexto/tratamento se relevante
4. NÃO omitir comorbidades do original
5. Negativas só se pertinente ao caso

## Variantes

### Simples (PA, Emergência)
- HAS
- DM2
- Tabagismo

### Detalhada (Ambulatório, Internação)
- HAS (desde 2015, em mau controle, PAS 150-160)
- DM2 (desde 2010, complicações: nefropatia, retinopatia)

### Com Datas (Cirurgia Vascular, Histórico Cirúrgico)
- DAC multiarterial (2015)
- PO CRM com CEC (02/12/22)
  - Safenectomia D
  - ACFA (cardiovertido 05/2022)
```

**Custo de tempo por módulo:** 1-1,5 horas (regras + variantes + exemplos)

**Total Tipo 4:** 8-12 horas

---

### **Tipo 5: MÓDULOS HDA (4 módulos)**

**O que é:** Como estruturar a História da Doença Atual em diferentes contextos

**Seus 4 tipos:**
1. HDA_NARRATIVO_DETALHADO.md
2. HDA_COMPACTO.md
3. HDA_OBSTETRICO.md
4. HDA_PSIQUIATRICO.md

**Estrutura de CADA módulo (exemplo HDA_COMPACTO):**

```markdown
# HDA: Compacto (PA/Emergência)

## Quando Usar
- PA (todas as salas)
- Emergência Hospitalar (admissão)
- Contextos com tempo limitado

## Estrutura (2-5 linhas)

HDA [data/hora]
[Narrativa direta dos sintomas]
[Negativas relevantes]

## Regras
1. Iniciar DIRETAMENTE com o sintoma (não "Paciente procura...")
2. Incluir HORA de início se relevante
3. Máximo 5 linhas
4. Última linha: "Nega [negativas relevantes]."
5. Coerência cronológica

## Exemplo 1 - Dor Abdominal
```
HDA 10:01
Paciente procura atendimento referindo dor em FIE há 3 dias, 
em fisgadas intermitentes, com piora progressiva, associada a 
náuseas e ausência de evacuação há 2 dias. Nega febre, vômitos, 
relação com alimentação específica.
```

## Exemplo 2 - Dispneia
```
HDA 14:30
Há 2 dias com dispneia progressiva de repouso, associada a 
tosse seca, febre não aferida. Nega dor torácica, palpitações. 
Antecedente de DPOC. Procura hoje por piora.
```

## Variantes

### Ultra-Compacto (Centro Obstétrico, PACS)
```
HDA 10:00
Contração 5/10min há 4h, boa amplitude, sem perdas líquidas.
```

### Narrativo (Consultório, Ambulatório)
```
HDA 24/01/26
Paciente vem encaminhada da UBS para avaliação de ciclos 
menstruais irregulares há 8 meses, com intervalos variando de 
21 a 60 dias. Refere também ganho de peso progressivo de 8kg 
em 6 meses, apesar de alimentação adequada...
```
```

**Custo de tempo por módulo:** 1-1,5 horas

**Total Tipo 5:** 4-6 horas

---

### **Tipo 6: MÓDULOS SUBJETIVO (10 módulos)**

**O que é:** Como o paciente relata seus sintomas em cada contexto

**Seus 10 tipos:**
1. SUBJETIVO_MFC_NARRATIVO.md
2. SUBJETIVO_PA_VERDE_COMPACTO.md
3. SUBJETIVO_PA_AMARELA_SEMI.md
4. SUBJETIVO_EMERGENCIA_ENCONTRO.md
5. SUBJETIVO_CONSULTORIO_DETALHADO.md
6. SUBJETIVO_AMBULATORIO.md
7. SUBJETIVO_INTERNACAO_ENCONTRO.md
8. SUBJETIVO_CO_ULTRA_COMPACTO.md
9. SUBJETIVO_EO_OBSTETRICO.md
10. SUBJETIVO_PSIQUIATRIA_EEM.md

**Estrutura de CADA módulo (exemplo SUBJETIVO_PA_VERDE_COMPACTO):**

```markdown
# SUBJETIVO: PA - Sala Verde (Compacto)

## Quando Usar
- PA Sala Verde
- Primeiros atendimentos de baixa complexidade
- Tempo: 5-10 minutos

## Estrutura (2-3 linhas)

Subjetivo:
[Frase de chegada]. [Queixa principal]. [Duração]. [Associações]. 
[Negativas em 1 linha].

## Padrão de Abertura
Escolher UM:
- "Paciente chega à emergência..."
- "Paciente procura atendimento..."
- "Pcte em consulta..."
- "Encontro pcte em leito..."

## Regras
1. DIRETO ao ponto (sem narrativa)
2. Queixa principal em PRIMEIRA frase
3. Duração clara (há X dias/horas)
4. Máximo 2-3 sintomas associados
5. Negativas: "Nega [...]"
6. NUNCA "O paciente relata que o paciente..."

## Exemplo 1
```
Subjetivo:
Paciente procura atendimento referindo dor abdominal em FIE há 2 
dias. Nega febre, vômitos, alteração do hábito intestinal.
```

## Exemplo 2
```
Subjetivo:
Procura PA por desconforto no peito iniciado há 2 horas durante 
atividade física. Desconforto aliviou com repouso. Nega dispneia. 
Nega palpitações.
```

## Variantes por Contexto

### MFC (Narrativo - 4-8 linhas)
```
Subjetivo:
Paciente vem acompanhada pela mãe, queixando-se de cefaleia 
progressiva há 3 dias. Refere também sensação de tontura ao 
levantar, especialmente de manhã. Apresenta história de enxaqueca 
desde adolescência. Nega alterações visuais, fotofobia. Refere 
estresse recente por mudança de trabalho.
```

### Ambulatório (Detalhado - contextuado)
```
Subjetivo:
Paciente vem para avaliação de queixa de amenorreia há 4 meses. 
Refere também ganho de peso de 8kg no período, apesar de 
alimentação mantida. Acompanhante (marido) relata também 
irregularidade nos ciclos menstruais nos últimos 2 anos. Nega 
sintomas de depressão. Refere libido preservada.
```

### Internação - Encontro (Padrão fixo)
```
Subjetivo:
Encontro paciente em leito da enfermaria, lúcido, orientado e 
comunicativo. Refere melhora progressiva da dor abdominal. Nega 
novas queixas. Tolerando bem alimentação via oral.
```

### Centro Obstétrico (Ultra-compacto)
```
Subjetivo:
Paciente em trabalho de parto com contração cada 3-5 minutos, 
de boa amplitude. Nega perdas líquidas típicas ou sangramento. 
Encontra-se tranquila.
```
```

**Custo de tempo por módulo:** 1,5-2 horas (estrutura + variantes + exemplos reais)

**Total Tipo 6:** 15-20 horas

---

### **Tipo 7: MÓDULOS OBJETIVO (13 módulos)**

**O que é:** Exame físico em diferentes níveis de detalhamento

**Seus 13 tipos:**
1. OBJETIVO_MFC_COMPLETO.md
2. OBJETIVO_PA_ABREVIADO_EXTREMO.md
3. OBJETIVO_PA_SEMI_DETALHADO.md
4. OBJETIVO_EMERGENCIA_ESTAVEL_INSTAVEL.md
5. OBJETIVO_CONSULTORIO_DETALHADO.md
6. OBJETIVO_AMBULATORIO.md
7. OBJETIVO_INTERNACAO_COMPLETO.md
8. OBJETIVO_CO_OBSTETRICO.md
9. OBJETIVO_EO_OBSTETRICO.md
10. OBJETIVO_CARDIO_ESPECIFICO.md
11. OBJETIVO_VASCULAR_ESPECIFICO.md
12. OBJETIVO_PSIQUIATRIA_EEM_COMPLETO.md
13. OBJETIVO_GINECO_MAMAS_DETALHADAS.md

**Estrutura de CADA módulo (exemplo OBJETIVO_PA_ABREVIADO_EXTREMO):**

```markdown
# OBJETIVO: PA - Sala Verde (Abreviado Extremo)

## Quando Usar
- PA Sala Verde
- Baixo risco
- Tempo crítico (5-10 min)
- Abreviações MÁXIMAS

## Estrutura Obrigatória

Objetivo:
- SV: PA [X/X] | FC [X] | TAx [X] | SO2 [X]%
- BEG LOC MUC AAA
- [Sistema]: [achados abreviados]
- [Sistema]: [achados abreviados]

## Regras Críticas
1. SEMPRE iniciar com SV (Sinais Vitais)
2. SEMPRE linha 2: "BEG LOC MUC AAA"
3. Apenas sistemas RELEVANTES ao caso
4. Máximo abreviações (nunca "bom estado geral")
5. Negativas IMPLÍCITAS (se não mencionar, é normal)

## Abreviações PERMITIDAS (EXTREMAS)
- BEG = Bom Estado Geral
- LOC = Lúcido, Orientado no tempo e espaço
- MUC = Mucosas Úmidas e Coradas
- AAA = Acianótico, Anictérico, Afebril
- MVUD = Murmúrios Vesiculares Universalmente Distribuídos
- SRA = Sem Ruídos Anormais
- RHA+ = Ruídos Hidro-Aéreos Presentes
- TEC 3s = Tempo Enchimento Capilar 3 segundos

## Exemplo 1 - Dor Abdominal
```
Objetivo:
- SV: PA 130/85 | FC 82 | TAx 36,8 | SO2 98%
- BEG LOC MUC AAA
- Abd: globoso depressível, sensível palpação FIE, Murphy e 
  Blumberg negativos, RHA+
```

## Exemplo 2 - Dispneia
```
Objetivo:
- SV: PA 128/82 | FC 98 | TAx 37,2 | SO2 94%
- BEG LOC MUC AAA, leve taquipneia
- SR: MVUD bilateralmente, SRA
- SCV: RR 2T BNF
```

## NUNCA
- Escrever "bom estado geral" (usar BEG)
- Omitir sinais vitais
- Exame físico completo (apenas relevante)
- Repetir "paciente" em cada linha
- Abreviações não-padrão (próprias criações)

## Variantes Conforme Contexto

### Completo (Internação, MFC, Consultório)
[Exame físico sistema por sistema, por extenso ou semi-abreviado]

### Semi-detalhado (PA Amarela, Ambulatório)
[Abreviações moderadas, sistemas por extenso mas concisos]

### Com Especificidades

#### Cardiovascular
- RR: Ritmo Regular
- 2T: 2 Tempos (normal)
- BNF: Bulhas Normofonéticas
- Sopros: presença/grau
- TEC: Tempo Enchimento Capilar

#### Respiratório
- MVUD: Murmúrios Vesiculares
- Roncos, sibilos, crepitações
- Expansibilidade
- Respiração: tipo, frequência

#### Abdome
- Tensão, depressibilidade
- RHA: frequência
- Percussão
- Palpação: sensibilidade, massas, hepatomegalia
- Sinais específicos: Murphy, Blumberg, Giordano

#### Obstétrico
- AU: Altura Uterina (cm)
- MF: Movimentação Fetal
- BCF: Batimentos Cardio-Fetais
- DU: Dinâmica Uterina
- TU: Tônus Uterino
- TV: Toque Vaginal (G/M/F, P/C, dilatação)
```

**Custo de tempo por módulo:** 2-3 horas (estrutura + abreviações + variantes + especificidades)

**Total Tipo 7:** 26-39 horas

---

### **Tipo 8: MÓDULOS EXAMES (9 módulos)**

**O que é:** Como apresentar Labs, Imagens e Exames Especiais

**Seus 9 tipos:**
1. EXAMES_LABS_INLINE.md
2. EXAMES_LABS_TABULAR.md
3. EXAMES_IMAGEM_LAUDO.md
4. EXAMES_IMAGING_ESPECIFICO_CARDIO.md
5. EXAMES_VASCULAR_PULSOS_ITB.md
6. EXAMES_OBSTETRICO_ECO.md
7. EXAMES_OBSTETRICO_CTG.md
8. EXAMES_PSIQUIATRIA_LABS.md
9. EXAMES_ESPECIFICO_GINECO.md

**Estrutura de CADA módulo (exemplo EXAMES_LABS_INLINE):**

```markdown
# EXAMES: Labs - Formato Inline

## Quando Usar
- PA (todas as salas)
- Emergência (apresentação rápida)
- Internação (quando poucos valores)

## Formato Padrão

Exames Laboratoriais:
DD/MM/AA: [Nome exame]: [valores inline com | separador]

## Estrutura Inline

### Com | Separador
```
26/01/26: Hemograma: Hb 13,2 | Ht 39% | Leuco 5.234 | Plaq 245
26/01/26: Bioquímica: Ur 28 | Cr 0,9 | Na 140 | K 4,2 | Glc 95
```

### Com / Separador
```
26/01/26: Hemograma: Hb 13,2 / Ht 39% / Leuco 5.234 / Plaq 245
```

### Com Valores de Referência
```
26/01/26: TSH 1,54 (0,27-5,10) | T4L 1,12 (0,93-1,71)
```

## Regras
1. SEMPRE data do exame (DD/MM/AA)
2. SEMPRE nome do exame (ou tipo: Hemograma, Bioquímica)
3. Separadores CONSISTENTES (escolher | ou /)
4. Valores de referência: OPCIONAL (conforme config usuário)
5. Unidades: OPCIONAL (conforme config usuário)
6. NÃO inventar valores não fornecidos
7. Ordem LÓGICA (hemograma antes de bioquímica)

## Exemplo Completo com Múltiplas Datas

Exames Laboratoriais:
- 24/01/26: Hemograma: Hb 12,0 | Ht 36 | Leuco 8.500 | Plaq 280
- 25/01/26: Hemograma: Hb 11,2 | Ht 34 | Leuco 7.800 | Plaq 250
  (Nota: Queda de Hb 12,0 > 11,2 = 0,8 g/dL)

## Variantes

### PA (Mínimo)
```
26/01/26: Hemograma: Hb 13,2 | Leuco 5.234
```

### Internação (Detalhado com tracking)
```
24/01/26: Hemograma: Hb 13,0 | Ht 39 | Leuco 6.500 | Plaq 250
25/01/26: Hemograma: Hb 12,5 | Ht 38 | Leuco 6.200 | Plaq 245
26/01/26: Hemograma: Hb 12,0 | Ht 37 | Leuco 5.900 | Plaq 240
(Evolução: queda progressiva de Hb)

26/01/26: Bioquímica: Ca 9,8 (9-10,5) | P 3,2 (2,5-4,5) | 
          Mg 2,1 (1,8-2,3) | Alb 3,5 (3,5-5,0)
```

### Especifico Endócrino (Com VR sempre)
```
26/01/26: TSH 1,54 (0,27-5,10) | T4L 1,12 (0,93-1,71)
26/01/26: Glc jejum 95 (70-100) | Insulina 8 (2-12) | HOMA-IR 1,9
```
```

**Custo de tempo por módulo:** 1,5-2 horas

**Total Tipo 8:** 13,5-18 horas

---

### **Tipo 9: MÓDULOS IMPRESSÃO (6 módulos)**

**O que é:** Como sintetizar o diagnóstico/impressão

**Seus 6 tipos:**
1. IMPRESSAO_DIAGNOSTICO_SINTETICO.md
2. IMPRESSAO_DIAGNOSTICO_DIFERENCIAL.md
3. IMPRESSAO_RISCO_ESTRATIFICACAO.md
4. IMPRESSAO_PROBLEMA_LISTA.md
5. IMPRESSAO_OBSTETRICA_BAIXO_ALTO_RISCO.md
6. IMPRESSAO_PSIQUIATRIA_DIAGNOSTICOS.md

**Estrutura de CADA módulo (exemplo IMPRESSAO_DIAGNOSTICO_SINTETICO):**

```markdown
# IMPRESSÃO: Diagnóstico Sintético

## Quando Usar
- PA (todas as salas)
- Emergência (admissão rápida)
- Consultório (retorno)

## Estrutura (1 linha ou máximo 3)

Impressão:
[Diagnóstico principal (pode ser sindrômico ou definitivo)]
[Observação de gravidade/estabilidade] (OPCIONAL)

## Regras
1. MÁXIMO 1 linha por diagnóstico
2. Começar com diagnóstico principal
3. Observação de gravidade SE relevante
4. NÃO incluir tratamento aqui
5. Ordem: Principal → Secundário → Tertúrio

## Exemplo 1
```
Impressão:
Gastroenterite aguda | Desidratação leve | Estável
```

## Exemplo 2
```
Impressão:
Infecção do Trato Urinário com possível pielonefrite | 
Instável (febre 39, taquicardia 120)
```

## Exemplo 3
```
Impressão:
Cólica renal | Cálculo 5mm meia pelve direita | 
Sem insuficiência renal
```

## Variantes

### Sintetíssimo (PA Verde)
```
Impressão:
Faringite aguda
```

### Com Observações (PA Amarela)
```
Impressão:
Pneumonia adquirida na comunidade
Infiltrado basal bilateral - risco de sepse
```

### Diferencial (Ambulatório)
```
Impressão:
- Hipotireoidismo primário
  vs
- Disfunção ovariana/Síndrome do Ovário Policístico
```

### Lista de Problemas (Internação)
```
Impressão:
1. Diabete Melito 2 - descompensado
2. Insuficiência Renal Crônica estágio 3B
3. HAS em mau controle
```
```

**Custo de tempo por módulo:** 1-1,5 horas

**Total Tipo 9:** 6-9 horas

---

### **Tipo 10: MÓDULOS CONDUTA (15 módulos)**

**O que é:** Como estruturar a ação/tratamento recomendado

**Seus 15 tipos:**
1. CONDUTA_CONVERSAO_AUSENTE.md
2. CONDUTA_CONVERSAO_CURTA.md
3. CONDUTA_CONVERSAO_LONGA_PADRAO.md
4. CONDUTA_PRESCRICAO_NOMES.md
5. CONDUTA_PRESCRICAO_DETALHADA.md
6. CONDUTA_PRESCRICAO_ULTRA_DETALHADA.md
7. CONDUTA_SINAIS_ALARME_GERAL.md
8. CONDUTA_SINAIS_ALARME_ESPECIFICO.md
9. CONDUTA_EXAMES_SOLICITACAO.md
10. CONDUTA_SEGUIMENTO_RETORNO.md
11. CONDUTA_ALTA_HOSPITALAR.md
12. CONDUTA_INTERNACAO_DECISAO.md
13. CONDUTA_OBSTETRICA_ORIENTACOES_PARTO.md
14. CONDUTA_OBSTETRICA_ORIENTACOES_PRENATAL.md
15. CONDUTA_PSIQUIATRIA_PLANO.md

**Estrutura de CADA módulo (exemplo CONDUTA_PRESCRICAO_DETALHADA):**

```markdown
# CONDUTA: Prescrição Detalhada

## Quando Usar
- Consultório
- Internação
- Ambulatório
- Qualquer contexto onde medicação é recomendada

## Estrutura de CADA Medicação

[NOME GENÉRICO] [dose] [forma] --------- [quantidade]
- Posologia: [horários específicos]
- Duração: [X dias/semanas]
- Instrução adicional: [se necessário]
- Alerta: [se medicação de risco]

## Regras Críticas
1. Nome genérico em MAIÚSCULAS
2. Dose + forma SEMPRE explícitos
3. Linha visual de separação (---)
4. Quantidade prescrita AO FINAL
5. Posologia com HORÁRIOS específicos ("às 8h e 20h", não "2x/dia")
6. Duração EXPLÍCITA ("por 7 dias", não "enquanto necessário")
7. Alertas OBRIGATÓRIOS para: AINEs, Tramadol, Antibióticos, Benzodiazepínicos
8. NÃO criar recomendações próprias (copiar do original)

## Exemplo 1 - Simples

```
IBUPROFENO 600mg comprimido ----------------------------- 15cp
- Tomar 1 comprimido de manhã e 1 à noite, por 5 dias.
- Não ultrapassar 5 dias seguidos de tratamento.
- Alerta: Este medicamento pode agravar problemas no 
  estômago, rins e coração se tomado por muitos dias.
```

## Exemplo 2 - Com Múltiplos Medicamentos

```
AMOXICILINA 500mg cápsula --------------------------------- 30cp
- Tomar 1 cápsula a cada 8 horas, por 7 dias (total: 3x/dia).
- Preferencialmente com água, pode ser com ou sem alimentos.
- Alerta: Pode causar alergias (erupção, inchaço). Se ocorrer, 
  parar imediatamente e procurar emergência.

DIPIRONA 500mg comprimido --------------------------------- 30cp
- Tomar 1 comprimido a cada 6 horas se febre/dor, máximo 4x/dia.
- Não usar se alergia a dipirona ou enxaqueca frequente.

OMEPRAZOL 20mg cápsula ------------------------------------ 30cp
- Tomar 1 cápsula pela manhã, em jejum, 30min antes do café.
- Usar enquanto tomar antibiótico e por mais 7 dias após.
```

## Exemplo 3 - Ultra-Detalhada (Consultório)

```
LOSARTANA 50mg comprimido --------------------------------- 30cp
- Tomar 1 comprimido TODOS os dias, preferencialmente à noite.
- Pode tomar com ou sem alimentos.
- NUNCA parar sem aviso médico, mesmo que se sinta bem.
- Pode causar tontura nos primeiros dias - sentar se isso ocorrer.
- Não tomar se grávida ou planejando gravidez.

ATORVASTATINA 20mg comprimido ----------------------------- 30cp
- Tomar 1 comprimido à noite (melhor absorção).
- Usar continuamente.
- Pode causar dor muscular - avisar imediatamente se ocorrer.
- Não tomar se alergia a estatinas.

ÁCIDO ACETILSALICÍLICO 100mg comprimido ------------------- 30cp
- Tomar 1 comprimido todos os dias pela manhã.
- Usar continuamente.
- Proteger o estômago - sempre tomar com alimento ou omeprazol.
```

## Variantes

### Nomes (Mínimo - PA Verde)
```
Prescrevo:
- Ibuprofeno 600mg, 3x/dia, 5 dias
- Dipirona 500mg se febre/dor
```

### Nomes (Médio - PA Amarela)
```
Prescrevo:
IBUPROFENO 600mg comprimido - 15cp
- 1 comprimido de 8 em 8 horas, por 5 dias
```

### Ultra-Detalhada (Consultório, Internação)
[Conforme estrutura acima - MUITO detalhado]
```

**Custo de tempo por módulo:** 2-2,5 horas

**Total Tipo 10:** 30-37,5 horas

---

### **Tipo 11: MÓDULOS ABREVIAÇÕES (7 módulos)**

**O que é:** Dicionário de abreviações por nível

**Seus 7 tipos:**
1. ABREVIACOES_EXTREMAS.md
2. ABREVIACOES_MODERADAS.md
3. ABREVIACOES_HIBRIDAS.md
4. ABREVIACOES_MINIMAS.md
5. ABREVIACOES_OBSTETRICA.md
6. ABREVIACOES_VASCULAR.md
7. ABREVIACOES_PSIQUIATRIA.md

**Estrutura de CADA módulo (exemplo ABREVIACOES_EXTREMAS):**

```markdown
# ABREVIAÇÕES: Nível EXTREMO

## Quando Usar
- PA Sala Verde
- Contextos com tempo crítico
- Quando usuário escolhe abreviações "Extremas"

## Estrutura: [ABREVIAÇÃO] = [significado] (exemplo)

### Estado Geral
- BEG = Bom Estado Geral
- LOC = Lúcido, Orientado no tempo/espaço/pessoa
- MUC = Mucosas Úmidas e Coradas
- AAA = Acianótico, Anictérico, Afebril
- MVUD = Murmúrios Vesiculares Universalmente Distribuídos
- SRA = Sem Ruídos Anormais
- RR = Ritmo Regular
- 2T = 2 Tempos (bulhas)
- BNF = Bulhas Normofonéticas
- RHA+ = Ruídos Hidro-Aéreos Presentes

### Sinais Vitais
- PA = Pressão Arterial
- FC = Frequência Cardíaca
- TAx = Temperatura Axilar
- SO2 = Saturação de Oxigênio
- FR = Frequência Respiratória
- HGT = Hemoglicoteste

### Sistemas
- SR = Sistema Respiratório
- SCV = Sistema CardioVascular
- Abd = Abdome
- Ext = Extremidades
- MuscEsq = Musculoesquelético
- OMRL = Orelhas, Nariz, Garganta (Otorrinolaringologia)

### Diagnósticos
- HAS = Hipertensão Arterial Sistêmica
- DM = Diabetes Mellitus
- DAC = Doença Arterial Coronariana
- ICC = Insuficiência Cardíaca Congestiva
- DPOC = Doença Pulmonar Obstrutiva Crônica
- ITU = Infecção do Trato Urinário
- DIP = Doença Inflamatória Pélvica

### Medicações
- AC = Antes do Café
- AA = Antes do Almoço
- AJ = Antes da Janta
- VO = Via Oral
- IM = Intramuscular
- IV = Intravenosa
- UI = Unidades Internacionais

### Procedimentos
- PA = Pressão Arterial / Pronto Atendimento (contexto)
- ECG = Eletrocardiograma
- RX = Radiografia
- US = Ultrassom
- TC = Tomografia Computadorizada
- RM = Ressonância Magnética
- PCte = Paciente

## Regra de Uso
✅ SEMPRE: BEG LOC MUC AAA (sempre junto, nesta ordem)
❌ NUNCA: Estado geral normal (sempre usar BEG)
```

**Custo de tempo por módulo:** 1-1,5 horas

**Total Tipo 11:** 7-10,5 horas

---

### **Tipo 12: MÓDULOS FORMATAÇÃO (6 módulos)**

**O que é:** Padrões de formatação (datas, listas, separadores)

**Seus 6 tipos:**
1. FORMATACAO_LABS_INLINE.md
2. FORMATACAO_LABS_TABULAR.md
3. FORMATACAO_MEDICACOES.md
4. FORMATACAO_DATAS.md
5. FORMATACAO_LISTAS.md
6. FORMATACAO_SEPARADORES.md

**Estrutura de CADA módulo (exemplo FORMATACAO_DATAS):**

```markdown
# FORMATAÇÃO: Datas

## Contexto e Variações

### PA/Emergência (Compacto)
DD/MM/AA (sem barra entre dia/mês, sem zero à esquerda se dia único)
Exemplo: 26/01/26, 5/12/25

### Consultório/Ambulatório (Formal)
DD/MM/AAAA (com 4 dígitos de ano)
Exemplo: 26/01/2026

### Procedimentos Cirúrgicos (Com marcador)
[DD/MM/AA] entre colchetes, seguido de procedimento
Exemplo: [02/12/22] PO CRM com CEC

### Exames Laboratoriais (Com data e hora se relevante)
DD/MM/AA HH:MM (se hora é importante)
Exemplo: 26/01/26 10:30

### Internação (Com dia da semana)
DD/MM/AA (XXX-feira)
Exemplo: 26/01/26 (seg-feira)

### Histórico Temporal (Com "há")
Há [tempo] (sem data específica se não fornecida)
Exemplo: "Há 3 dias iniciou com...", "Há 2 semanas foi..."

## Regra Geral
Escolher UM formato conforme contexto e manter CONSISTÊNCIA em todo o documento
```

**Custo de tempo por módulo:** 0,5-1 hora

**Total Tipo 12:** 3-6 horas

---

### **Tipo 13: TEMPLATES ESPECIAIS (12 módulos)**

**O que é:** Estruturas completas e pré-montadas para contextos muito específicos

**Seus 12 tipos:**
1. TEMPLATE_ALTA_HOSPITALAR_OBSTETRICA.md
2. TEMPLATE_CENTRO_OBSTETRICO.md
3. TEMPLATE_EMERGENCIA_OBSTETRICA.md
4. TEMPLATE_PNAR.md
5. TEMPLATE_EEM_PSIQUIATRIA_COMPLETO.md
6. TEMPLATE_EEM_PSIQUIATRIA_ABREVIADO.md
7. TEMPLATE_VASCULAR_PULSOS_ITB.md
8. TEMPLATE_CARDIO_AUSCULTA.md
9. TEMPLATE_GINECO_MAMAS_DIREITA_ESQUERDA.md
10. TEMPLATE_AMBULATORIO_LISTA_PROBLEMAS.md
11. TEMPLATE_INTERNACAO_PSIQUIATRIA_CHECKLIST.md
12. TEMPLATE_ASO_OCUPACIONAL.md

**Estrutura de CADA módulo (exemplo TEMPLATE_ALTA_HOSPITALAR_OBSTETRICA):**

```markdown
# TEMPLATE: Alta Hospitalar Obstétrica

## Quando Usar
- Mulher que pariu (normal ou cesárea)
- Pós-parto imediato/mediato
- Sempre narrativa (não SOAP)

## Estrutura Obrigatória

[Identificação completa - GxPxCxAx, IG, TS]

Narrativa contínua contando:
1. Motivo da internação
2. Como foi a gravidez (IG, anomalias detectadas)
3. Tipo de parto e condições
4. RN: APGAR, peso, sexo, placenta
5. Evolução puerperal
6. Medicações prescritas

Orientações de Alta (sempre presente):
- Abstinência sexual 30 dias
- Higiene de períneo/ferida
- Retirar pontos em 7-10 dias na UBS
- Revisão ginecológica em até 30 dias
- Amamentação recomendações
- Anticoncepção conforme prescrito
- Sinais de alerta (febre, dor, sangramento fétido)
- Controles condicionais (TTG 75g → SE DMG; PA → SE HAS)

Assinatura com ATM (120 dias)

## Exemplo

[Completo com todos os elementos]

## Variantes
- Normal vs Cesárea (diferenças em orientações de higiene/movimento)
- Com/sem complicações PO (episiotomia, laceração)
- RN internado vs RN em domicílio (orientações diferentes)
```

**Custo de tempo por módulo:** 2-3 horas (estrutura completa + exemplos + variantes)

**Total Tipo 13:** 24-36 horas

---

### **Tipo 14: CHECKLISTS (14 módulos)**

**O que é:** Validação de qualidade - checklist para verificar se prompt ficou correto

**Seus 14 tipos:**
1. CHECKLIST_ANTI_INVENCAO.md
2. CHECKLIST_COMPLETUDE_SOAP.md
3. CHECKLIST_ABREVIACOES_CONSISTENCIA.md
4. CHECKLIST_FORMATACAO_CONSISTENCIA.md
5. CHECKLIST_MEDICACOES_SEGURANCA.md
6. CHECKLIST_ORIENTACOES_PACIENTE.md
7. CHECKLIST_SINAIS_ALARME.md
8. CHECKLIST_OBSTETRICA.md
9. CHECKLIST_PSIQUIATRIA.md
10. CHECKLIST_VASCULAR.md
11. CHECKLIST_CARDIO.md
12. CHECKLIST_INTERNACAO.md
13. CHECKLIST_ALTA_HOSPITALAR.md
14. CHECKLIST_FINAL_UNIVERSAL.md

**Estrutura de CADA módulo (exemplo CHECKLIST_ANTI_INVENCAO):**

```markdown
# CHECKLIST: Anti-Invenção

## Uso
Aplicar DEPOIS de reescrever - validar se foi adicionado algo não fornecido

## Verificar

### ✅ Informações do Original
- [ ] Todos os sintomas mencionados estão presentes
- [ ] Todos os exames mencionados estão presentes
- [ ] Todos os medicamentos mencionados estão presentes
- [ ] Todas as comorbidades mencionadas estão presentes
- [ ] Negativas do original foram mantidas

### ❌ Invenções Detectadas
- [ ] Não há hipóteses diagnósticas não mencionadas no original
- [ ] Não há recomendações de exames não solicitados originalmente
- [ ] Não há medicações não prescritas originalmente
- [ ] Não há diagnósticos criados
- [ ] Não há valores de exame interpolados/estimados

### 📝 Formatação
- [ ] Abreviações são CONSISTENTES com config do usuário
- [ ] Datas estão no formato correto
- [ ] Estrutura SOAP/SOEIC/etc está correta para o contexto
- [ ] Não há repetição desnecessária de informações

### ⚠️ Segurança Clínica
- [ ] Sinais de alarme apropriados estão presentes
- [ ] Retorno/seguimento foi mencionado
- [ ] Doses de medicações estão corretas (se mensionadas)
- [ ] Não há recomendações perigosas

## Resultado
- ✅ PASSOU: Zero invenções detectadas
- ⚠️ REVISAR: [Listar itens que precisam ajuste]
- ❌ RECUSAR: [Listar invenções críticas]
```

**Custo de tempo por módulo:** 1-1,5 horas

**Total Tipo 14:** 14-21 horas

---

## **1.2 RESUMO DE TEMPO - FASE 1**

| Tipo | Nome | Qty | Tempo/un | Total |
|:---|:---|---:|---:|---:|
| 1 | PROMPT_BASE | 1 | 2,5h | 2,5h |
| 2 | CONTEXTO | 10 | 1,25h | 12,5h |
| 3 | CABEÇALHO | 7 | 0,75h | 5,25h |
| 4 | HISTÓRIA | 8 | 1,25h | 10h |
| 5 | HDA | 4 | 1,25h | 5h |
| 6 | SUBJETIVO | 10 | 1,75h | 17,5h |
| 7 | OBJETIVO | 13 | 2,5h | 32,5h |
| 8 | EXAMES | 9 | 1,75h | 15,75h |
| 9 | IMPRESSÃO | 6 | 1,25h | 7,5h |
| 10 | CONDUTA | 15 | 2,25h | 33,75h |
| 11 | ABREVIAÇÕES | 7 | 1,25h | 8,75h |
| 12 | FORMATAÇÃO | 6 | 0,75h | 4,5h |
| 13 | TEMPLATES ESPECIAIS | 12 | 2,5h | 30h |
| 14 | CHECKLISTS | 14 | 1,25h | 17,5h |
| | | **140** | | **202,5h** |

---

### **Estimativa Final Fase 1 (SÓ VOCÊ - PROMPTS)**
- **140 módulos**
- **~202,5 horas de trabalho**
- **~5 semanas a 40h/semana** (ou 10 semanas a 20h/semana)
- **Ou 2,5 semanas em sprint com 80h/semana** (não recomendado - qualidade)

---

## **🎯 FASE 2: CONFIGURAÇÃO INTELIGENTE**

### **Responsável:** Alan (Backend)

### **O que você faz:**
1. Define as **variáveis de configuração** que o usuário pode escolher
2. Escreve exemplos de **como cada configuração afeta o output**
3. Valida se as configurações cobrem **todos os casos de uso**

### **O que Alan faz:**
1. Cria banco de dados de configurações por usuário
2. UI para o usuário escolher preferências (1x na vida, editável)
3. API para carregar preferências quando reescrever
4. Testes de persistência

### **Configurações a Definir:**

```
1. ABREVIAÇÕES
   [ ] Extremas (BEG, LOC, MUC, AAA)
   [ ] Moderadas (Orosc, SR, SCV, mas "estado geral" por extenso)
   [ ] Híbridas (BEG LOTE AAA, mas sistemas detalhados)
   [ ] Mínimas (quase por extenso)

2. ESTRUTURA DE PRONTUÁRIO
   [ ] SOAP (Subjetivo-Objetivo-Avaliação-Conduta)
   [ ] SOEIC (Subjetivo-Objetivo-Exames-Impressão-Conduta)
   [ ] HDA-SOAP (Historia estruturada)

3. FORMATAÇÃO
   [ ] Hipertexto simples
   [ ] Com bullets/dashes
   [ ] Espaçamento amplo
   [ ] Compacto
   [ ] Com separadores visuais (---, ===)

4. ESTILO DE LABS
   [ ] Inline com | separador
   [ ] Inline com / separador
   [ ] Com valores de referência
   [ ] Sem unidades
   [ ] Com unidades
   [ ] Tabular

5. ESTILO DE MEDICAÇÕES
   [ ] Nomes genéricos apenas
   [ ] Genéricos + comerciais
   [ ] Ultra-detalhadas (dose, forma, hora, duração, alertas)
   [ ] Simples (nome e dose)

6. ASSINATURA
   [Personalização livre: Título, Nome, Especialidade, Pós-grad, etc]

7. OUTRAS
   [ ] Incluir CID-10 automaticamente?
   [ ] Incluir valores de referência (labs)?
   [ ] Expandir abreviações específicas manualmente?
```

### **Tempo Fase 2 (SUA PARTE):**
- Definir 7 blocos de configuração: **2-3 horas**
- Testar com exemplos: **1-2 horas**
- Documentar para Alan: **1 hora**

**Total você (Fase 2): ~5 horas**

---

## **🤖 FASE 3: REESCRITA AUTOMÁTICA**

### **Responsável:** Alan (IA + Backend)

### **O que você faz:**
1. Define **critérios de identificação automática** para cada contexto
2. Escreve **ordem de composição de módulos** para cada combinação
3. Testa com **casos de teste reais**

### **O que Alan faz:**
1. Implementa IA para identificar:
   - Sexo (automaticamente da narrativa)
   - Idade (automaticamente da narrativa)
   - Contexto (PA vs Ambulatório vs Internação - você deixa explícito ou IA detecta)
   - Especialidade (IA detecta por palavras-chave)
   - Subtipo (1ª consulta vs retorno - por keywords)
2. Carrega configurações do usuário
3. Seleciona módulos apropriados
4. Compõe prompt final
5. Executa reescrita via LLM
6. Valida output com checklists

### **Exemplo de Composição (você define):**

**Contexto: PA Sala Verde**
```
Estrutura de módulos:

1. PROMPT_BASE_001 (regras críticas)
2. CONTEXTO_PA_SALA_VERDE
3. CABECALHO_PA
4. HISTORIA_COMORBIDADES_SISTEMAS (se houver)
5. HDA_COMPACTO
6. SUBJETIVO_PA_VERDE_COMPACTO
7. OBJETIVO_PA_ABREVIADO_EXTREMO
8. EXAMES_LABS_INLINE (se houver exames)
9. IMPRESSAO_DIAGNOSTICO_SINTETICO
10. CONDUTA_CONVERSAO_CURTA
11. CONDUTA_PRESCRICAO_NOMES (se medicação)
12. CONDUTA_SINAIS_ALARME_GERAL
13. ABREVIACOES_EXTREMAS (conforme config usuário)
14. FORMATACAO_DATAS (conforme config usuário)
15. CHECKLIST_FINAL_UNIVERSAL

Ordem de execução: 1 > 2 > 3 > [4 se aplicável] > 5 > 6 > 7 > [8 se aplicável] > 
                  9 > 10 > [11 se aplicável] > 12 > 13 > 14 > 15
```

### **Tempo Fase 3 (SUA PARTE):**
- Definir composições para 7 padrões × 4 contextos cada = 28 composições: **15-20 horas**
- Criar 30-40 casos de teste reais: **10-15 horas**
- Testar e validar: **5-10 horas**

**Total você (Fase 3): ~30-45 horas (1-2 semanas)**

---

## **📦 FASE 4: DISTRIBUIÇÃO E INTEGRAÇÕES**

### **Responsável:** Alan (DevOps + Frontend)

### **O que você faz:**
1. Escreve documentação de **UX do app** (como usuário interage)
2. Aprova **UI mockups** (interface das configurações, área de reescrita)
3. Valida **qualidade de outputs** com casos reais

### **O que Alan faz:**
1. API REST para reescrita
2. Apps mobile (iOS/Android) ou web
3. Integrações (prontuários eletrônicos, cloud storage, etc)
4. Deploy, CI/CD, monitoramento

### **Tempo Fase 4 (SUA PARTE):**
- Documentação UX: **2-3 horas**
- Aprovação UI/UX: **1-2 horas** (ongoing)
- Validação de qualidade: **contínua** (2h/semana)

**Total você (Fase 4): ~5h inicial + contínuo**

---

## **📊 RESUMO TOTAL DE TEMPO**

| Fase | Descrição | Seu Tempo | Alan |
|:---|:---|---:|:---|
| **1** | Banco de Módulos (140 módulos) | **202,5h** (5-10 semanas) | Espera |
| **2** | Configuração Inteligente | **5h** (alguns dias) | **40-80h** (2-3 semanas) |
| **3** | Reescrita Automática | **30-45h** (1-2 semanas) | **80-120h** (3-4 semanas) |
| **4** | Distribuição/Integrações | **5h + contínuo** | **200-400h** (2-4 meses) |
| | **TOTAL** | **~242-257h** | **~320-600h** |

---

## **💡 INSIGHTS E DICAS PRÁTICAS**

### **Fase 1: Escrita dos Módulos**

#### **1. Paralelização com Alan**
- Enquanto você escreve módulos 1-5 (Base, Contexto, Cabeçalho, História, HDA)
- Alan já pode começar a estruturar banco de dados e API básica
- **Ganho de tempo: 2-3 semanas**

#### **2. Priorizar por Impacto**
Não faça tudo de uma vez. Comece por:

**Semana 1-2: CORE (Tier 1)**
- PROMPT_BASE_001 ✅
- CONTEXTO: PA_VERDE, PA_AMARELA, CONSULTORIO, AMBULATORIO (4 módulos)
- CABEÇALHO: PA, CONSULTORIO (2 módulos)
- SUBJETIVO: PA_VERDE, CONSULTORIO (2 módulos)
- OBJETIVO: PA_ABREVIADO_EXTREMO, CONSULTORIO_DETALHADO (2 módulos)
- IMPRESSAO: DIAGNOSTICO_SINTETICO (1 módulo)
- CONDUTA: CONVERSAO_CURTA, PRESCRICAO_DETALHADA, SINAIS_ALARME_GERAL (3 módulos)
- ABREVIACOES: EXTREMAS, MINIMAS (2 módulos)
- CHECKLIST: FINAL_UNIVERSAL (1 módulo)

**Total Tier 1: ~20 módulos, ~50 horas = 1-2 semanas**

Depois você já tem MVP funcional. Alan pode começar a integrar.

**Semana 3-4: TIER 2**
- Adicionar especialidades principais (Cardio, Gineco, Psiquiatria)
- Adicionar contextos secundários (Internação, Avaliação)

**Semana 5+: TIER 3**
- Especialidades complementares
- Refinamento dos módulos existentes

#### **3. Template System**
Não reescrever do zero cada módulo. Template:

```markdown
# [TIPO]: [NOME]

## Quando Usar
[Brevíssimo - 2 linhas]

## Estrutura
[Como deve ficar formatado]

## Regras
[Do's and Don'ts - máximo 5 regras críticas]

## Exemplo(s)
[1-2 exemplos reais do seu arquivo de análise]

## Variantes
[Se houver subtipo]
```

**Isso padroniza e acelera muito.**

#### **4. Reusar Conhecimento do Mapeamento**
Você JÁ fez mapeamento completo nos arquivos anexos. 
**Copie e adapte de lá**, não reescreva.

Seus arquivos têm:
- Exemplos reais de Cirurgia Vascular (pulsos, ITB)
- Exemplos reais de Endócrino (insulina, IMC)
- Exemplos reais de Obstetrícia (GxPxCxAx, IG, TV)
- Exemplos reais de Psiquiatria (EEM 15 componentes)
- Exemplos reais de PA (abreviações extremas)

**Use isso como base!**

#### **5. Versionamento**
Use versionamento para módulos:
```
MODULO_SUBJETIVO_PA_VERDE_v1.0.md
MODULO_SUBJETIVO_PA_VERDE_v1.1.md (bugfix)
MODULO_SUBJETIVO_PA_VERDE_v2.0.md (expansão)
```

Assim Alan pode usar sempre a versão estável enquanto você refina.

#### **6. Testes Contínuos**
Conforme escreve módulos, teste com 1-2 casos reais:
- PA Verde: teste com 3-5 casos reais de PA baixo risco
- Ambulatório: teste com 1-2 casos reais de consultório

Isso pega erros cedo.

#### **7. Documentação de Composição**
Crie arquivo separado com ordem de composição para cada contexto:

```markdown
# COMPOSIÇÃO DE PROMPTS

## PA - Sala Verde
1. PROMPT_BASE_001
2. CONTEXTO_PA_SALA_VERDE
3. CABECALHO_PA
[... lista completa]

## Consultório
1. PROMPT_BASE_001
2. CONTEXTO_CONSULTORIO
[... lista completa]

[... para cada contexto]
```

**Alan precisa disso.**

---

### **Fase 2: Configuração**

#### **1. Não Crie Configurações Desnecessárias**
Não precisa de 100 opções. Apenas:
- Abreviações (4 níveis)
- Estrutura prontuário (3 tipos)
- Formatação (espaçamento + separadores)
- Labs (inline vs tabular, com/sem VR)
- Medicações (simples vs detalhada)
- Assinatura (customizável)

**Máximo 10 configurações. Simplicidade = adoção.**

#### **2. Default Sensato**
Configurações DEFAULT devem ser "best practice":
- Abreviações: Moderadas (acessível + profissional)
- Estrutura: SOAP (padrão universal)
- Formatação: Espaçamento amplo (legibilidade)
- Labs: Inline com / separador (compacto)
- Medicações: Detalhada (segurança)
- Assinatura: Padrão simples

Assim usuário novo tem experiência OK imediatamente.

---

### **Fase 3: Reescrita**

#### **1. Identificação Automática**
Não peça ao usuário:
- "É adulto ou pediátrico?" → IA detecta
- "É masculino ou feminino?" → IA detecta
- "É 1ª consulta ou retorno?" → IA detecta por keywords

**Apenas 2 perguntas OBRIGATÓRIAS:**
1. Qual é o PADRÃO? (MFC / PA / Emergência / Consultório / Ambulatório / etc)
2. Qual é o CONTEXTO? (Verde/Amarela/etc)

**Tudo mais: IA infere.**

#### **2. Checklist Automático**
Após reescrever, execute SEMPRE:
```
CHECKLIST_ANTI_INVENCAO ✅
CHECKLIST_COMPLETUDE_SOAP ✅
CHECKLIST_MEDICACOES_SEGURANCA ✅
CHECKLIST_FINAL_UNIVERSAL ✅
```

Se algum falhar → avisar usuário → propor revisão

#### **3. Feedback Loop**
Cada reescrita deve gerar feedback:
- ✅ Passou em todos os checklists? → Excelente! Pronto para copiar
- ⚠️ Alertas? → Mostrar avisos ao usuário (e.g., "Possível invenção detectada em linha 23")
- ❌ Falha crítica? → Não devolver, pedir revisão

---

### **Geral: Estratégia de Sucesso**

#### **1. Comece Pequeno, Expand Rápido**
- Semana 1: Apenas PA Verde (1 padrão, 1 contexto)
- Semana 2: PA Verde/Amarela + Consultório
- Semana 3: Adicionar Ambulatório + Internação
- Semana 4+: Especialidades

**MVP em 2 semanas, depois expande.**

#### **2. Documento Vivo**
Seus arquivos de módulos não são "código".
- Estão sempre evoluindo
- Usuários vão pedir tweaks
- Especialidades novas aparecem

**Mantenha com versionamento flexível.**

#### **3. Comunidade Médica é Seu Beta**
Assim que tiver MVP, colete feedback de 5-10 médicos reais.
- "O que deveria ser diferente?"
- "Que contextos faltam?"
- "Que especialidades deveria adicionar?"

**Melhora design rápido.**

#### **4. Automação > Configuração**
Sempre que possível, deixe a IA decidir (identificação automática).
- Menos cliques para usuário
- Menos erros de configuração
- Experiência mais fluida

#### **5. Segurança Médica FIRST**
Qualquer ambiguidade → erro para o lado conservador.
- Quando em dúvida se foi invenção → avisar usuário
- Checklists de medicação → rigorosos
- Sinais de alarme → sempre presente

**Responsabilidade médica pesada.**

---

## **📅 CRONOGRAMA SUGERIDO**

```
SEMANA 1-2: Fase 1 TIER 1 (você escrevendo)
├─ PROMPT_BASE
├─ 4 CONTEXTOS principais
├─ 4 CABECALHO
├─ 4 SUBJETIVO
├─ 4 OBJETIVO
├─ 1 IMPRESSAO
├─ 3 CONDUTA
├─ 2 ABREVIACOES
└─ 1 CHECKLIST
Alan: Setup BD + API básica

SEMANA 3: Fase 2 (você definindo configurações)
Alan: Implementar persistência config + UI

SEMANA 4-6: Fase 1 TIER 2 (você expandindo)
├─ Especialidades principais
├─ Contextos secundários
├─ Templates especiais Obstetrica + Psiquiatria
Alan: Integrar módulos + testar composição

SEMANA 7-8: Fase 3 (você testando + criando casos teste)
Alan: Implementar IA de identificação + composição

SEMANA 9+: Fase 4 (você validando + Alan deployando)
├─ Beta com 5-10 médicos
├─ Feedback + ajustes
└─ Iteração contínua

TOTAL: ~3 meses para MVP "production-ready"
```

---

## **🚀 PRÓXIMOS PASSOS**

1. **Você:**
   - Revisar este documento
   - Confirmar se estimativas de tempo fazem sentido
   - Escolher ordem de prioridade (qual módulo escreve primeira)
   - Começar com Tier 1

2. **Alan:**
   - Setup técnico de BD e API
   - Revisar estrutura de módulos
   - Preparar ambiente para integração

3. **Juntos:**
   - Definir formato exato de arquivo de módulo (JSON? YAML? Markdown puro?)
   - Definir convenções de nomeação
   - Setup de versionamento/git

---

**Projeto é grande, mas totalmente factível em 3 meses com trabalho consistente! 🎯**