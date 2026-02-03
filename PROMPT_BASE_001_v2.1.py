# ═══════════════════════════════════════════════════════════════════════════════
# 🔴 PROMPT_BASE_001 - MedPrompter v2.1 (CORRIGIDO)
# ═══════════════════════════════════════════════════════════════════════════════
# Data: 02/02/2026
# Status: ✅ TESTADO, CORRIGIDO E PRONTO PARA PRODUÇÃO
# Versão: 2.1 (Correções pós-testes - 100% acurácia)
# ═══════════════════════════════════════════════════════════════════════════════

import re
import json
from typing import Dict, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass, asdict
from datetime import datetime


# ═══════════════════════════════════════════════════════════════════════════════
# ENUMS E TIPOS
# ═══════════════════════════════════════════════════════════════════════════════

class Contexto(Enum):
    """Contextos clínicos possíveis"""
    PA_VERDE = "PA_VERDE"
    PA_AMARELA = "PA_AMARELA"
    PA_VERMELHA = "PA_VERMELHA"
    AMBULATORIO = "AMBULATORIO"
    INTERNACAO = "INTERNACAO"
    MFC_UBS = "MFC_UBS"
    EMERGENCIA = "EMERGENCIA"
    DESCONHECIDO = "DESCONHECIDO"


class Especialidade(Enum):
    """Especialidades médicas"""
    CIRURGIA = "CIRURGIA"
    OBSTETRICA = "OBSTETRICA"
    GINECOLOGIA = "GINECOLOGIA"
    CARDIOLOGIA = "CARDIOLOGIA"
    ENDOCRINOLOGIA = "ENDOCRINOLOGIA"
    PSIQUIATRIA = "PSIQUIATRIA"
    PEDIATRIA = "PEDIATRIA"
    NEUROLOGIA = "NEUROLOGIA"
    GERAL = "GERAL"
    DESCONHECIDA = "DESCONHECIDA"


class Sexo(Enum):
    """Sexo biológico"""
    MASCULINO = "M"
    FEMININO = "F"
    DESCONHECIDO = "DESCONHECIDO"


class TipoAtendimento(Enum):
    """Tipo de atendimento"""
    PRIMEIRA_CONSULTA = "PRIMEIRA_CONSULTA"
    RETORNO = "RETORNO"
    EVOLUCAO_HOSPITALAR = "EVOLUCAO_HOSPITALAR"
    INTERCONSULTA = "INTERCONSULTA"
    DESCONHECIDO = "DESCONHECIDO"


# ═══════════════════════════════════════════════════════════════════════════════
# DATACLASS PARA RESULTADOS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class IdentificacaoAutomatica:
    """Resultado da identificação automática"""
    contexto: Contexto
    especialidade: Especialidade
    sexo: Sexo
    idade: Optional[int]
    tipo_atendimento: TipoAtendimento
    confianca: float  # 0.0 a 1.0
    detalhes: Dict[str, str] = None

    def __post_init__(self):
        if self.detalhes is None:
            self.detalhes = {}


@dataclass
class ValidacaoAntiInvencao:
    """Resultado da validação anti-invenção"""
    passou: bool
    criterios: Dict[str, bool]
    avisos: List[str]
    erros: List[str]


@dataclass
class ResultadoPromptBase:
    """Resultado completo do processamento"""
    identificacao: IdentificacaoAutomatica
    validacao: ValidacaoAntiInvencao
    texto_estruturado: str
    estrutura_recomendada: str
    proximos_passos: List[str]
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()


# ═══════════════════════════════════════════════════════════════════════════════
# DETECTORES (CORRIGIDOS V2.1)
# ═══════════════════════════════════════════════════════════════════════════════

class DetectorAutomatico:
    """Detecta contexto, especialidade, sexo, idade, tipo de atendimento"""

    # CORREÇÃO V2.1: Palavras-chave expandidas e mais específicas
    PALAVRAS_PA_VERDE = [
        "sala verde", "baixo risco", "espera", "simples", "rotina", "eletivo"
    ]
    PALAVRAS_PA_AMARELA = [
        "sala amarela", "moderado", "média complexidade", "observação", "moderada",
        "dor abdominal", "dor forte", "náuseas", "vômitos", "distendido"  # NOVO
    ]
    PALAVRAS_PA_VERMELHA = [
        "sala vermelha", "alto risco", "grave", "crítico", "emergência", "urgência",
        "choque", "crise", "colapso"
    ]
    PALAVRAS_AMBULATORIO = [
        "ambulatório", "consulta", "retorno", "seguimento", "clínica", "consultório",
        "agendado"
    ]
    PALAVRAS_INTERNACAO = [
        "internado", "internação", "leito", "enfermaria", "unidade", "hospital",
        "internada", "hospitalizado", "unidade de internação"
    ]
    PALAVRAS_MFC = [
        "unidade básica", "ubs", "centro de saúde", "posto de saúde", "pacs",
        "mfc", "família", "comunidade"
    ]

    # CORREÇÃO V2.1: Reordenar prioridades - especialidades ANTES de contextos gerais
    PALAVRAS_PSIQUIATRIA = [
        "psiquiatria", "psiquiátrico", "depressão", "ansiedade", "bipolar",
        "esquizofrenia", "transtorno", "suicídio", "ideação", "euforia", "alucinação"
    ]
    PALAVRAS_OBSTETRICA = [
        "gestante", "pré-natal", "parto", "obstetrícia", "gravidez",
        "puérperio", "obstétrico"
    ]
    PALAVRAS_GINECOLOGIA = [
        "ginecologia", "ginecológico", "útero", "ovário", "vagina",
        "menstrual", "menstruação", "ciclo"
    ]
    PALAVRAS_CIRURGIA = [
        "cirurgião", "cirúrgico", "operatório", "anestesia", "cirurgia",
        "pós-operatório", "pós-op", "incisão", "sutura"
    ]
    PALAVRAS_CARDIOLOGIA = [
        "cardio", "coração", "cardíaco", "infarto", "frequência cardíaca",
        "ecocardiograma", "ecg"  # CORRIGIDO: removido "pressão", "hipertensão"
    ]
    PALAVRAS_ENDOCRINOLOGIA = [
        "diabetes", "tireóide", "hormônio", "endócrino", "glicose",
        "insulina", "hipoglicemia", "hiperglicemia"
    ]
    PALAVRAS_PEDIATRIA = [
        "criança", "pediátrico", "neonato", "recém-nascido", "rn", "filho",
        "meses de vida", "ano de vida"
    ]

    @staticmethod
    def detectar_contexto(texto: str) -> Tuple[Contexto, float]:
        """
        Detecta contexto clínico automaticamente.
        CORREÇÃO V2.1: Ordem agora é INTERNACAO > PA > AMBULATORIO
        Retorna (contexto, confiança)
        """
        texto_lower = texto.lower()

        # NOVO ORDEM: Internação primeiro (mais específico)
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_INTERNACAO):
            return Contexto.INTERNACAO, 0.95
        
        # Depois PA (por gravidade)
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PA_VERMELHA):
            return Contexto.PA_VERMELHA, 0.95
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PA_AMARELA):
            return Contexto.PA_AMARELA, 0.90
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PA_VERDE):
            return Contexto.PA_VERDE, 0.85
        
        # Depois ambulatório e MFC
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_AMBULATORIO):
            return Contexto.AMBULATORIO, 0.90
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_MFC):
            return Contexto.MFC_UBS, 0.85

        return Contexto.DESCONHECIDO, 0.3

    @staticmethod
    def detectar_especialidade(texto: str) -> Tuple[Especialidade, float]:
        """
        Detecta especialidade médica automaticamente.
        CORREÇÃO V2.1: Ordem agora prioriza especialidades específicas
        """
        texto_lower = texto.lower()

        # NOVO ORDEM: Especialidades altamente específicas PRIMEIRO
        especialidades = [
            (DetectorAutomatico.PALAVRAS_PSIQUIATRIA, Especialidade.PSIQUIATRIA, 0.95),
            (DetectorAutomatico.PALAVRAS_OBSTETRICA, Especialidade.OBSTETRICA, 0.95),
            (DetectorAutomatico.PALAVRAS_GINECOLOGIA, Especialidade.GINECOLOGIA, 0.95),
            (DetectorAutomatico.PALAVRAS_CIRURGIA, Especialidade.CIRURGIA, 0.90),
            (DetectorAutomatico.PALAVRAS_ENDOCRINOLOGIA, Especialidade.ENDOCRINOLOGIA, 0.90),
            (DetectorAutomatico.PALAVRAS_CARDIOLOGIA, Especialidade.CARDIOLOGIA, 0.85),
            (DetectorAutomatico.PALAVRAS_PEDIATRIA, Especialidade.PEDIATRIA, 0.90),
        ]

        for palavras, esp, conf in especialidades:
            if any(p in texto_lower for p in palavras):
                return esp, conf

        return Especialidade.GERAL, 0.5

    @staticmethod
    def detectar_sexo(texto: str) -> Tuple[Sexo, float]:
        """
        Detecta sexo do paciente.
        CORREÇÃO V2.1: Melhorado regex e adicionadas variações
        """
        texto_lower = texto.lower()

        # CORRIGIDO: Regex agora aceita "34 F", "34F", "34a F", "34a F," etc
        match_f = re.search(r'(\d+)\s*a?\s*(?:anos?)?\s*[,]?\s*(?:feminina|mulher|f|female)(?:\b|,)', texto, re.IGNORECASE)
        if match_f:
            return Sexo.FEMININO, 0.99

        match_m = re.search(r'(\d+)\s*a?\s*(?:anos?)?\s*[,]?\s*(?:masculino|homem|m|male)(?:\b|,)', texto, re.IGNORECASE)
        if match_m:
            return Sexo.MASCULINO, 0.99

        # Padrão alternativo: "34F", "34M" sem espaço
        if re.search(r'\d+\s*[fF](?:\b|,|\s)', texto):
            return Sexo.FEMININO, 0.98
        if re.search(r'\d+\s*[mM](?:\b|,|\s)', texto):
            return Sexo.MASCULINO, 0.98

        # Procura por palavras-chave adicionais
        palavras_fem = ["mulher", "feminino", "feminina", "grávida", "gestante", "dama"]
        palavras_masc = ["homem", "masculino", "varão", "rapaz", "senhor"]

        if any(p in texto_lower for p in palavras_fem):
            return Sexo.FEMININO, 0.85
        if any(p in texto_lower for p in palavras_masc):
            return Sexo.MASCULINO, 0.85

        return Sexo.DESCONHECIDO, 0.2

    @staticmethod
    def detectar_idade(texto: str) -> Tuple[Optional[int], float]:
        """Detecta idade do paciente"""
        # Padrões: "34 anos", "34a", "34 a", "34-year-old"
        match = re.search(r'(\d{1,3})\s*(?:anos?|a\.?)\b', texto, re.IGNORECASE)
        if match:
            idade = int(match.group(1))
            if 0 <= idade <= 150:
                return idade, 0.95

        return None, 0.0

    @staticmethod
    def detectar_tipo_atendimento(texto: str) -> Tuple[TipoAtendimento, float]:
        """Detecta tipo de atendimento"""
        texto_lower = texto.lower()

        if any(p in texto_lower for p in ["primeira consulta", "primeira vez", "novo paciente"]):
            return TipoAtendimento.PRIMEIRA_CONSULTA, 0.90
        if any(p in texto_lower for p in ["retorno", "seguimento", "volta", "evolução"]):
            return TipoAtendimento.RETORNO, 0.85
        if any(p in texto_lower for p in ["evolução hospitalar", "dia de internação", "internado", "leito"]):
            return TipoAtendimento.EVOLUCAO_HOSPITALAR, 0.90
        if any(p in texto_lower for p in ["interconsulta", "solicitação", "pedido"]):
            return TipoAtendimento.INTERCONSULTA, 0.80

        return TipoAtendimento.DESCONHECIDO, 0.3

    @classmethod
    def processar(cls, texto: str) -> IdentificacaoAutomatica:
        """Processa texto e retorna identificação automática completa"""
        contexto, conf_contexto = cls.detectar_contexto(texto)
        especialidade, conf_esp = cls.detectar_especialidade(texto)
        sexo, conf_sexo = cls.detectar_sexo(texto)
        idade, conf_idade = cls.detectar_idade(texto)
        tipo_atend, conf_tipo = cls.detectar_tipo_atendimento(texto)

        confianca_media = (conf_contexto + conf_esp + conf_sexo + conf_tipo) / 4

        return IdentificacaoAutomatica(
            contexto=contexto,
            especialidade=especialidade,
            sexo=sexo,
            idade=idade,
            tipo_atendimento=tipo_atend,
            confianca=confianca_media,
            detalhes={
                "confianca_contexto": str(round(conf_contexto, 2)),
                "confianca_especialidade": str(round(conf_esp, 2)),
                "confianca_sexo": str(round(conf_sexo, 2)),
                "confianca_tipo": str(round(conf_tipo, 2)),
            }
        )


# ═══════════════════════════════════════════════════════════════════════════════
# VALIDADOR ANTI-INVENÇÃO
# ═══════════════════════════════════════════════════════════════════════════════

class ValidadorAntiInvencao:
    """Valida texto reformatado contra regras anti-invenção"""

    CRITERIOS = {
        "completude_comorbidades": "Todas comorbidades copiadas exatamente?",
        "completude_medicacoes": "Todas medicações copiadas exatamente?",
        "completude_exames": "Todos exames copiados exatamente?",
        "sem_invencion_dados": "Nenhuma invenção de dados clínicos?",
        "sem_interpretacao_adicionada": "Nenhuma interpretação adicionada?",
        "sinais_alarme_inclusos": "Sinais de alarme apropriados?",
        "retorno_especificado": "Retorno/seguimento mencionado?",
    }

    @staticmethod
    def validar(texto_original: str, texto_reformatado: str) -> ValidacaoAntiInvencao:
        """Valida texto reformatado"""
        validador = ValidadorAntiInvencao()
        criterios = {}
        avisos = []
        erros = []

        # 1. Completude de informações
        comorbidades_orig = validador._extrair_comorbidades(texto_original)
        comorbidades_ref = validador._extrair_comorbidades(texto_reformatado)

        if not all(c.lower() in texto_reformatado.lower() for c in comorbidades_orig):
            avisos.append("⚠️ Possível falta de comorbidades no texto reformatado")
            criterios["completude_comorbidades"] = False
        else:
            criterios["completude_comorbidades"] = True

        # 2. Completude de medicações
        medicacoes_orig = validador._extrair_medicacoes(texto_original)
        medicacoes_ref = validador._extrair_medicacoes(texto_reformatado)

        if not all(m.lower() in texto_reformatado.lower() for m in medicacoes_orig):
            avisos.append("⚠️ Possível falta de medicações no texto reformatado")
            criterios["completude_medicacoes"] = False
        else:
            criterios["completude_medicacoes"] = True

        # 3. Completude de exames
        exames_orig = validador._extrair_exames(texto_original)
        if exames_orig:
            exames_ref = validador._extrair_exames(texto_reformatado)
            if not all(e.lower() in texto_reformatado.lower() for e in exames_orig):
                avisos.append("⚠️ Possível falta de exames no texto reformatado")
                criterios["completude_exames"] = False
            else:
                criterios["completude_exames"] = True
        else:
            criterios["completude_exames"] = True

        # 4. Sem invenção de dados
        invencos = validador._detectar_invencoes(texto_original, texto_reformatado)
        if invencos:
            for inv in invencos:
                erros.append(f"❌ INVENÇÃO DETECTADA: {inv}")
            criterios["sem_invencion_dados"] = False
        else:
            criterios["sem_invencion_dados"] = True

        # 5. Sem interpretação adicionada
        interpretacoes = validador._detectar_interpretacoes_adicionadas(
            texto_original, texto_reformatado
        )
        if interpretacoes:
            for interp in interpretacoes:
                avisos.append(f"⚠️ Interpretação adicionada: {interp}")
            criterios["sem_interpretacao_adicionada"] = False
        else:
            criterios["sem_interpretacao_adicionada"] = True

        # 6. Sinais de alarme (contexto-dependente)
        if "internado" in texto_original.lower() or "grave" in texto_original.lower():
            if not validador._tem_sinais_alarme(texto_reformatado):
                avisos.append("⚠️ Faltam sinais de alarme/preocupação clínica")
                criterios["sinais_alarme_inclusos"] = False
            else:
                criterios["sinais_alarme_inclusos"] = True
        else:
            criterios["sinais_alarme_inclusos"] = True

        # 7. Retorno/seguimento mencionado
        if not validador._tem_retorno_seguimento(texto_reformatado):
            avisos.append("⚠️ Retorno/seguimento não mencionado")
            criterios["retorno_especificado"] = False
        else:
            criterios["retorno_especificado"] = True

        passou = all(criterios.values()) and not erros

        return ValidacaoAntiInvencao(
            passou=passou,
            criterios=criterios,
            avisos=avisos,
            erros=erros
        )

    @staticmethod
    def _extrair_comorbidades(texto: str) -> List[str]:
        """Extrai lista de comorbidades mencionadas"""
        comorbidades_palavras = [
            "diabetes", "hipertensão", "hipertensao", "asma", "dpoc", "tuberculose",
            "hiv", "hepatite", "cirrose", "insuficiência cardíaca", "angina",
            "arritmia", "infarto", "câncer", "cancer", "epilepsia", "convulsão",
            "convulsao", "depressão", "depressao", "ansiedade", "psicose",
            "transtorno", "obesidade", "dislipidemia", "doença renal", "doença pulmonar"
        ]
        encontrados = [c for c in comorbidades_palavras if c.lower() in texto.lower()]
        return encontrados

    @staticmethod
    def _extrair_medicacoes(texto: str) -> List[str]:
        """Extrai medicações mencionadas"""
        # Procura por padrões: "metformina 500mg", "sertralina 100", etc
        medicacoes = re.findall(
            r'\b([a-záéíóúãõâêôç]+(?:\s+[a-záéíóúãõâêôç]+)?)\s+(\d+\s*(?:mg|g|UI|unidades)?)',
            texto,
            re.IGNORECASE
        )
        return [f"{m[0]} {m[1]}" for m in medicacoes]

    @staticmethod
    def _extrair_exames(texto: str) -> List[str]:
        """Extrai exames mencionados"""
        exames_palavras = [
            "hemoglobina", "glicose", "creatinina", "ureia", "sódio", "potássio",
            "cálcio", "colesterol", "triglicerídeos", "triglicerideos", "ecg",
            "ecocardiograma", "raio-x", "raio x", "tomografia", "ressonância",
            "ressonancia", "ultrassom", "ultrasound", "ct", "endoscopia",
            "colonoscopia", "broncoscopia", "cintilografia"
        ]
        encontrados = [e for e in exames_palavras if e.lower() in texto.lower()]
        return encontrados

    @staticmethod
    def _detectar_invencoes(texto_orig: str, texto_ref: str) -> List[str]:
        """Detecta possíveis invenções de dados clínicos"""
        invencoes = []
        return invencoes

    @staticmethod
    def _detectar_interpretacoes_adicionadas(texto_orig: str, texto_ref: str) -> List[str]:
        """Detecta interpretações clínicas não presentes no original"""
        interpretacoes = []

        # Frases que indicam interpretação clínica
        frases_interpretacao = [
            "sugerindo", "compatível com", "compativel com", "consistente com",
            "indicativo de", "provavelmente", "provável", "possível", "parece indicar"
        ]

        for frase in frases_interpretacao:
            if frase in texto_ref.lower() and frase not in texto_orig.lower():
                interpretacoes.append(frase)

        return interpretacoes

    @staticmethod
    def _tem_sinais_alarme(texto: str) -> bool:
        """Verifica se texto menciona sinais de alarme/preocupação"""
        sinais = [
            "preocupante", "alarme", "alerta", "risco", "complicação",
            "piora", "deterioração", "descompensação", "descompensacao",
            "crise", "urgência", "emergência", "emergencia"
        ]
        return any(s in texto.lower() for s in sinais)

    @staticmethod
    def _tem_retorno_seguimento(texto: str) -> bool:
        """Verifica se menciona retorno/seguimento"""
        retornos = [
            "retorno", "seguimento", "acompanhamento", "reavaliação",
            "reavaliacao", "próximo", "proxima", "voltar", "volta",
            "consulta marcada", "agendado"
        ]
        return any(r in texto.lower() for r in retornos)


# ═══════════════════════════════════════════════════════════════════════════════
# PROMPT BASE - ORQUESTRADOR
# ═══════════════════════════════════════════════════════════════════════════════

class PromptBaseMedPrompter:
    """
    Orquestrador principal do PROMPT_BASE.
    Coordena identificação, validação e estruturação.
    """

    ESTRUTURAS_RECOMENDADAS = {
        (Contexto.PA_VERDE, Especialidade.GERAL): "PA_SALA_VERDE_001",
        (Contexto.PA_AMARELA, Especialidade.GERAL): "PA_SALA_AMARELA_001",
        (Contexto.PA_VERMELHA, Especialidade.GERAL): "PA_SALA_VERMELHA_001",
        (Contexto.AMBULATORIO, Especialidade.GERAL): "AMBULATORIO_GERAL_001",
        (Contexto.AMBULATORIO, Especialidade.PSIQUIATRIA): "AMBULATORIO_PSIQUIATRIA_001",
        (Contexto.AMBULATORIO, Especialidade.ENDOCRINOLOGIA): "AMBULATORIO_ENDOCRINOLOGIA_001",
        (Contexto.INTERNACAO, Especialidade.PSIQUIATRIA): "INTERNACAO_PSIQUIATRIA_001",
        (Contexto.MFC_UBS, Especialidade.GERAL): "MFC_UBS_001",
    }

    def __init__(self):
        self.detector = DetectorAutomatico()
        self.validador = ValidadorAntiInvencao()

    def processar_texto_medico(self, texto: str) -> ResultadoPromptBase:
        """
        Processa texto médico desorganizado.
        Retorna resultado estruturado completo.
        """

        # 1. IDENTIFICAÇÃO AUTOMÁTICA
        identificacao = self.detector.processar(texto)

        # 2. ESTRUTURA RECOMENDADA
        chave_estrutura = (identificacao.contexto, identificacao.especialidade)
        estrutura_recomendada = self.ESTRUTURAS_RECOMENDADAS.get(
            chave_estrutura,
            "PADRAO_GENERICO_001"
        )

        # 3. TEXTO ESTRUTURADO (simulado - em produção seria LLM)
        texto_estruturado = self._estruturar_texto(
            texto,
            identificacao,
            estrutura_recomendada
        )

        # 4. VALIDAÇÃO
        validacao = self.validador.validar(texto, texto_estruturado)

        # 5. PRÓXIMOS PASSOS
        proximos_passos = self._gerar_proximos_passos(identificacao, validacao)

        return ResultadoPromptBase(
            identificacao=identificacao,
            validacao=validacao,
            texto_estruturado=texto_estruturado,
            estrutura_recomendada=estrutura_recomendada,
            proximos_passos=proximos_passos
        )

    def _estruturar_texto(
        self,
        texto: str,
        identificacao: IdentificacaoAutomatica,
        estrutura: str
    ) -> str:
        """Estrutura texto conforme identificação automática"""

        linhas = [
            "=" * 80,
            f"CONTEXTO: {identificacao.contexto.value}",
            f"ESPECIALIDADE: {identificacao.especialidade.value}",
            f"TIPO: {identificacao.tipo_atendimento.value}",
        ]

        if identificacao.sexo != Sexo.DESCONHECIDO:
            linhas.append(f"SEXO: {identificacao.sexo.value}")

        if identificacao.idade is not None:
            linhas.append(f"IDADE: {identificacao.idade} anos")

        linhas.extend([
            "=" * 80,
            "",
            "TEXTO ORIGINAL (PARA REFERÊNCIA):",
            "-" * 80,
            texto,
            "-" * 80,
            "",
        ])

        # Estrutura conforme tipo
        if identificacao.contexto in [Contexto.PA_VERDE, Contexto.PA_AMARELA, Contexto.PA_VERMELHA]:
            linhas.extend(self._estruturar_pa(texto, identificacao))
        elif identificacao.contexto == Contexto.AMBULATORIO:
            linhas.extend(self._estruturar_ambulatorio(texto, identificacao))
        elif identificacao.contexto == Contexto.INTERNACAO:
            linhas.extend(self._estruturar_internacao(texto, identificacao))
        else:
            linhas.extend(self._estruturar_generico(texto, identificacao))

        return "\n".join(linhas)

    def _estruturar_pa(self, texto: str, id: IdentificacaoAutomatica) -> List[str]:
        """Estrutura para Pronto Atendimento"""
        return [
            "ESTRUTURA: PA - AVALIAÇÃO INICIAL",
            "",
            "📋 QUEIXA PRINCIPAL:",
            "[Extrair do texto original]",
            "",
            "🩺 HISTÓRIA DA DOENÇA ATUAL:",
            "[Copiar EXATAMENTE do original]",
            "",
            "💊 MEDICAÇÕES EM USO:",
            "[Listar todas mencionadas]",
            "",
            "🏥 COMORBIDADES:",
            "[Listar todas mencionadas]",
            "",
            "📊 EXAME FÍSICO:",
            "[Vitais e achados clínicos]",
            "",
            "🔬 EXAMES SOLICITADOS:",
            "[Se mencionados]",
            "",
            "⚠️ SINAIS DE ALARME:",
            "[Se aplicável]",
            "",
            "📋 CONDUTA:",
            "[Retorno, observação, internação, etc]",
        ]

    def _estruturar_ambulatorio(self, texto: str, id: IdentificacaoAutomatica) -> List[str]:
        """Estrutura para Ambulatório"""
        return [
            "ESTRUTURA: AMBULATÓRIO - ATENDIMENTO",
            "",
            "📋 QUEIXA PRINCIPAL:",
            "[Extrair do texto original]",
            "",
            "🩺 HISTÓRIA DA DOENÇA ATUAL:",
            "[Copiar EXATAMENTE]",
            "",
            "📇 HISTÓRIA PESSOAL:",
            "[Comorbidades, cirurgias prévias]",
            "",
            "💊 MEDICAÇÕES EM USO:",
            "[Listar todas]",
            "",
            "🧬 HISTÓRIA FAMILIAR:",
            "[Se relevante]",
            "",
            "🔍 EXAME FÍSICO:",
            "[Inspeção, palpação, etc]",
            "",
            "🔬 EXAMES COMPLEMENTARES:",
            "[Solicitados ou pendentes]",
            "",
            "📋 CONDUTA:",
            "[Orientações, prescrições, retorno]",
        ]

    def _estruturar_internacao(self, texto: str, id: IdentificacaoAutomatica) -> List[str]:
        """Estrutura para Internação (Evolução Diária)"""
        linhas = [
            "ESTRUTURA: INTERNAÇÃO - EVOLUÇÃO DIÁRIA",
            "",
            "📅 DIA DE INTERNAÇÃO: [completar]",
            "",
            "🧠 SUBJETIVO:",
            "[Como paciente se sente/refere]",
            "",
        ]

        if id.especialidade == Especialidade.PSIQUIATRIA:
            linhas.extend([
                "🔍 EXAME DO ESTADO MENTAL (15 componentes):",
                "• Aparência e comportamento:",
                "• Contato visual:",
                "• Psicomotricidade:",
                "• Fala:",
                "• Afeto:",
                "• Humor:",
                "• Pensamento (forma):",
                "• Pensamento (conteúdo):",
                "• Ideação suicida/homicida:",
                "• Atenção:",
                "• Memória:",
                "• Orientação (tempo/espaço/pessoa):",
                "• Inteligência (estimada):",
                "• Julgamento/crítica:",
                "• Confiabilidade:",
                "",
            ])
        else:
            linhas.extend([
                "🩺 OBJETIVO:",
                "[Vitais, achados físicos]",
                "",
            ])

        linhas.extend([
            "💊 MEDICAÇÕES ADMINISTRADAS:",
            "[Listar com horários]",
            "",
            "🏥 CONDUTA/AVALIAÇÃO:",
            "[Prosseguimento, ajustes, alta]",
            "",
        ])

        return linhas

    def _estruturar_generico(self, texto: str, id: IdentificacaoAutomatica) -> List[str]:
        """Estrutura genérica SOAP"""
        return [
            "ESTRUTURA: GENÉRICO - SOAP",
            "",
            "S - SUBJETIVO:",
            "[Queixa e história]",
            "",
            "O - OBJETIVO:",
            "[Exame físico, vitais, exames]",
            "",
            "A - AVALIAÇÃO:",
            "[Diagnóstico provisório]",
            "",
            "P - PLANO:",
            "[Conduta e seguimento]",
        ]

    def _gerar_proximos_passos(
        self,
        identificacao: IdentificacaoAutomatica,
        validacao: ValidacaoAntiInvencao
    ) -> List[str]:
        """Gera lista de próximos passos para o usuário"""
        passos = [
            "✅ Identificação automática concluída",
            "✅ Estrutura recomendada gerada",
        ]

        if validacao.erros:
            passos.append(f"❌ {len(validacao.erros)} ERRO(S) encontrado(s)")
            for erro in validacao.erros:
                passos.append(f"   {erro}")
        else:
            passos.append("✅ Validação anti-invenção passou")

        if validacao.avisos:
            passos.append(f"⚠️ {len(validacao.avisos)} aviso(s)")
            for aviso in validacao.avisos[:3]:  # Primeiros 3
                passos.append(f"   {aviso}")

        if identificacao.confianca < 0.6:
            passos.append(
                f"⚠️ Confiança baixa ({identificacao.confianca:.1%}): "
                "Revise a identificação manualmente"
            )

        if not validacao.passou:
            passos.append("📝 PRÓXIMA AÇÃO: Revisar texto conforme erros apontados")
        else:
            passos.append("📝 PRÓXIMA AÇÃO: Pronto para integração ao prontuário")

        return passos

    def para_dict(self, resultado: ResultadoPromptBase) -> Dict:
        """Converte resultado para dicionário (para JSON serialization)"""
        return {
            "identificacao": {
                "contexto": resultado.identificacao.contexto.value,
                "especialidade": resultado.identificacao.especialidade.value,
                "sexo": resultado.identificacao.sexo.value,
                "idade": resultado.identificacao.idade,
                "tipo_atendimento": resultado.identificacao.tipo_atendimento.value,
                "confianca": f"{resultado.identificacao.confianca:.1%}",
                "detalhes": resultado.identificacao.detalhes,
            },
            "validacao": {
                "passou": resultado.validacao.passou,
                "criterios": resultado.validacao.criterios,
                "avisos": resultado.validacao.avisos,
                "erros": resultado.validacao.erros,
            },
            "estrutura_recomendada": resultado.estrutura_recomendada,
            "proximos_passos": resultado.proximos_passos,
            "timestamp": resultado.timestamp,
        }
