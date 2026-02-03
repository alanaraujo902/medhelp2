"""
Serviço de Inteligência: Detecção automática e Validação Anti-Invenção.
Baseado na lógica do PROMPT_BASE_001_v2.1 - MedPrompter.
"""
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

from app.models.evolution import PrimaryContext, OutpatientSpecialty


# ============================================
# DATACLASSES DE RESULTADO
# ============================================

@dataclass
class IdentificacaoAutomatica:
    """Resultado da identificação automática."""
    primary_context: PrimaryContext
    outpatient_specialty: OutpatientSpecialty
    sexo: str  # "M" | "F" | "DESCONHECIDO"
    idade: Optional[int]
    tipo_atendimento: str  # PRIMEIRA_CONSULTA | RETORNO | EVOLUCAO_HOSPITALAR | etc
    confianca: float
    detalhes: Dict[str, str]


@dataclass
class ValidacaoAntiInvencao:
    """Resultado da validação anti-invenção."""
    passou: bool
    criterios: Dict[str, bool]
    avisos: List[str]
    erros: List[str]


# ============================================
# DETECTOR AUTOMÁTICO
# ============================================

class DetectorAutomatico:
    """Detecta contexto, especialidade, sexo, idade e tipo de atendimento."""

    PALAVRAS_PA_VERDE = [
        "sala verde", "baixo risco", "espera", "simples", "rotina", "eletivo"
    ]
    PALAVRAS_PA_AMARELA = [
        "sala amarela", "moderado", "média complexidade", "observação", "moderada",
        "dor abdominal", "dor forte", "náuseas", "vômitos", "distendido"
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
    PALAVRAS_PACS_URGENCIA = [
        "s / o / e / i / c", "soap expandido", "urgent", "briefing", "rápido"
    ]
    PALAVRAS_PACS_CONSULTORIO = [
        "conversão padronizada", "15-30 min", "prescrições ultra-detalhadas"
    ]

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
    PALAVRAS_VASCULAR = [
        "vascular", "daop", "itb", "pulsos", "safenectomia", "ecodoppler"
    ]
    PALAVRAS_MASTOLOGIA = [
        "mastologia", "mamas", "qsl", "qsm", "qil", "qim", "birads"
    ]
    PALAVRAS_ENDOCRINOLOGIA = [
        "diabetes", "tireóide", "tireoide", "hormônio", "endócrino", "glicose",
        "insulina", "hipoglicemia", "hiperglicemia", "tsh", "t4l"
    ]
    PALAVRAS_CARDIOLOGIA = [
        "cardio", "coração", "cardíaco", "infarto", "frequência cardíaca",
        "ecocardiograma", "ecg"
    ]
    PALAVRAS_PEDIATRIA = [
        "criança", "pediátrico", "neonato", "recém-nascido", "filho",
        "meses de vida", "ano de vida", "lactente", "infantil"
    ]

    CONTEXTO_TO_PRIMARY = {
        "PA_VERDE": PrimaryContext.PA_GREEN,
        "PA_AMARELA": PrimaryContext.PA_YELLOW,
        "PA_VERMELHA": PrimaryContext.PA_RED,
        "AMBULATORIO": PrimaryContext.OUTPATIENT,
        "INTERNACAO": PrimaryContext.HOSPITALIZATION,
        "MFC_UBS": PrimaryContext.MFC_UBS,
        "EMERGENCIA": PrimaryContext.EMERGENCY,
    }

    ESPECIALIDADE_TO_OUTPATIENT = {
        "PSIQUIATRIA": OutpatientSpecialty.PSYCHIATRY,
        "OBSTETRICA": OutpatientSpecialty.OBSTETRICS,
        "GINECOLOGIA": OutpatientSpecialty.GYNECOLOGY,
        "CIRURGIA": OutpatientSpecialty.GENERAL_SURGERY,
        "ENDOCRINOLOGIA": OutpatientSpecialty.ENDOCRINOLOGY,
        "CARDIOLOGIA": OutpatientSpecialty.CARDIOLOGY,
        "PEDIATRIA": OutpatientSpecialty.PEDIATRICS,
        "GERAL": OutpatientSpecialty.GENERAL_CLINIC,
    }

    @staticmethod
    def detectar_contexto(texto: str) -> Tuple[PrimaryContext, float]:
        """Detecta contexto clínico automaticamente."""
        texto_lower = texto.lower()

        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_INTERNACAO):
            return PrimaryContext.HOSPITALIZATION, 0.95

        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PA_VERMELHA):
            return PrimaryContext.PA_RED, 0.95
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PA_AMARELA):
            return PrimaryContext.PA_YELLOW, 0.90
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PA_VERDE):
            return PrimaryContext.PA_GREEN, 0.85

        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PACS_URGENCIA):
            return PrimaryContext.PACS_URGENCIA, 0.90
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PACS_CONSULTORIO):
            return PrimaryContext.PACS_CONSULTORIO, 0.85

        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_AMBULATORIO):
            return PrimaryContext.OUTPATIENT, 0.90
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_MFC):
            return PrimaryContext.MFC_UBS, 0.85

        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_PA_VERMELHA):
            return PrimaryContext.EMERGENCY, 0.80

        return PrimaryContext.OUTPATIENT, 0.5  # Default para ambulatorial

    @staticmethod
    def detectar_especialidade(texto: str) -> Tuple[OutpatientSpecialty, float]:
        """Detecta especialidade médica automaticamente."""
        texto_lower = texto.lower()

        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_VASCULAR):
            return OutpatientSpecialty.VASCULAR_SURGERY, 0.95
        if any(p in texto_lower for p in DetectorAutomatico.PALAVRAS_MASTOLOGIA):
            return OutpatientSpecialty.MASTOLOGY, 0.95

        especialidades = [
            (DetectorAutomatico.PALAVRAS_PSIQUIATRIA, OutpatientSpecialty.PSYCHIATRY, 0.95),
            (DetectorAutomatico.PALAVRAS_OBSTETRICA, OutpatientSpecialty.OBSTETRICS, 0.95),
            (DetectorAutomatico.PALAVRAS_GINECOLOGIA, OutpatientSpecialty.GYNECOLOGY, 0.95),
            (DetectorAutomatico.PALAVRAS_CIRURGIA, OutpatientSpecialty.GENERAL_SURGERY, 0.90),
            (DetectorAutomatico.PALAVRAS_ENDOCRINOLOGIA, OutpatientSpecialty.ENDOCRINOLOGY, 0.90),
            (DetectorAutomatico.PALAVRAS_CARDIOLOGIA, OutpatientSpecialty.CARDIOLOGY, 0.85),
            (DetectorAutomatico.PALAVRAS_PEDIATRIA, OutpatientSpecialty.PEDIATRICS, 0.90),
        ]

        for palavras, esp, conf in especialidades:
            if any(p in texto_lower for p in palavras):
                return esp, conf

        return OutpatientSpecialty.GENERAL_CLINIC, 0.5

    @staticmethod
    def detectar_sexo(texto: str) -> Tuple[str, float]:
        """Detecta sexo do paciente."""
        texto_lower = texto.lower()

        match_f = re.search(
            r'(\d+)\s*a?\s*(?:anos?)?\s*[,]?\s*(?:feminina|mulher|f|female)(?:\b|,)',
            texto, re.IGNORECASE
        )
        if match_f:
            return "F", 0.99

        match_m = re.search(
            r'(\d+)\s*a?\s*(?:anos?)?\s*[,]?\s*(?:masculino|homem|m|male)(?:\b|,)',
            texto, re.IGNORECASE
        )
        if match_m:
            return "M", 0.99

        if re.search(r'\d+\s*[fF](?:\b|,|\s)', texto):
            return "F", 0.98
        if re.search(r'\d+\s*[mM](?:\b|,|\s)', texto):
            return "M", 0.98

        if any(p in texto_lower for p in ["mulher", "feminino", "feminina", "grávida", "gestante", "dama"]):
            return "F", 0.85
        if any(p in texto_lower for p in ["homem", "masculino", "varão", "rapaz", "senhor"]):
            return "M", 0.85

        return "DESCONHECIDO", 0.2

    @staticmethod
    def detectar_idade(texto: str) -> Tuple[Optional[int], float]:
        """Detecta idade do paciente."""
        match = re.search(r'(\d{1,3})\s*(?:anos?|a\.?)\b', texto, re.IGNORECASE)
        if match:
            idade = int(match.group(1))
            if 0 <= idade <= 150:
                return idade, 0.95
        return None, 0.0

    @staticmethod
    def detectar_tipo_atendimento(texto: str) -> Tuple[str, float]:
        """Detecta tipo de atendimento."""
        texto_lower = texto.lower()

        if any(p in texto_lower for p in ["primeira consulta", "primeira vez", "novo paciente"]):
            return "PRIMEIRA_CONSULTA", 0.90
        if any(p in texto_lower for p in ["retorno", "seguimento", "volta"]):
            return "RETORNO", 0.85
        if any(p in texto_lower for p in ["evolução", "evolucao", "dia de internação", "internado", "leito"]):
            return "EVOLUCAO_HOSPITALAR", 0.90
        if any(p in texto_lower for p in ["interconsulta", "solicitação", "pedido"]):
            return "INTERCONSULTA", 0.80

        return "DESCONHECIDO", 0.3

    @classmethod
    def detectar_tudo(cls, texto: str) -> IdentificacaoAutomatica:
        """Processa texto e retorna identificação automática completa."""
        contexto, conf_contexto = cls.detectar_contexto(texto)
        especialidade, conf_esp = cls.detectar_especialidade(texto)
        sexo, conf_sexo = cls.detectar_sexo(texto)
        idade, conf_idade = cls.detectar_idade(texto)
        tipo_atend, conf_tipo = cls.detectar_tipo_atendimento(texto)

        confianca_media = (conf_contexto + conf_esp + conf_sexo + conf_tipo) / 4

        return IdentificacaoAutomatica(
            primary_context=contexto,
            outpatient_specialty=especialidade,
            sexo=sexo,
            idade=idade,
            tipo_atendimento=tipo_atend,
            confianca=confianca_media,
            detalhes={
                "confianca_contexto": str(round(conf_contexto, 2)),
                "confianca_especialidade": str(round(conf_esp, 2)),
                "confianca_sexo": str(round(conf_sexo, 2)),
                "confianca_tipo": str(round(conf_tipo, 2)),
            },
        )


# ============================================
# VALIDADOR ANTI-INVENÇÃO
# ============================================

class ValidadorAntiInvencao:
    """Valida texto reformatado contra regras anti-invenção."""

    @staticmethod
    def validar(texto_original: str, texto_reformatado: str) -> ValidacaoAntiInvencao:
        """Valida texto reformatado."""
        criterios: Dict[str, bool] = {}
        avisos: List[str] = []
        erros: List[str] = []

        # 1. Completude de comorbidades
        comorbidades_orig = ValidadorAntiInvencao._extrair_comorbidades(texto_original)
        criterios["completude_comorbidades"] = (
            all(c.lower() in texto_reformatado.lower() for c in comorbidades_orig)
            if comorbidades_orig else True
        )
        if not criterios["completude_comorbidades"]:
            avisos.append("Possível falta de comorbidades no texto reformatado")

        # 2. Completude de medicações
        medicacoes_orig = ValidadorAntiInvencao._extrair_medicacoes(texto_original)
        criterios["completude_medicacoes"] = (
            all(m.lower() in texto_reformatado.lower() for m in medicacoes_orig)
            if medicacoes_orig else True
        )
        if not criterios["completude_medicacoes"]:
            avisos.append("Possível falta de medicações no texto reformatado")

        # 3. Completude de exames
        exames_orig = ValidadorAntiInvencao._extrair_exames(texto_original)
        criterios["completude_exames"] = (
            all(e.lower() in texto_reformatado.lower() for e in exames_orig)
            if exames_orig else True
        )
        if not criterios["completude_exames"] and exames_orig:
            avisos.append("Possível falta de exames no texto reformatado")

        # 4. Sem invenção de dados
        invencoes = ValidadorAntiInvencao._detectar_invencoes(texto_original, texto_reformatado)
        criterios["sem_invencao_dados"] = len(invencoes) == 0
        for inv in invencoes:
            erros.append(f"INVENÇÃO DETECTADA: {inv}")

        # 5. Sem interpretação adicionada
        interpretacoes = ValidadorAntiInvencao._detectar_interpretacoes_adicionadas(
            texto_original, texto_reformatado
        )
        criterios["sem_interpretacao_adicionada"] = len(interpretacoes) == 0
        for interp in interpretacoes:
            avisos.append(f"Interpretação adicionada: {interp}")

        # 6. Sinais de alarme
        if "internado" in texto_original.lower() or "grave" in texto_original.lower():
            criterios["sinais_alarme_inclusos"] = ValidadorAntiInvencao._tem_sinais_alarme(texto_reformatado)
            if not criterios["sinais_alarme_inclusos"]:
                avisos.append("Faltam sinais de alarme/preocupação clínica")
        else:
            criterios["sinais_alarme_inclusos"] = True

        # 7. Retorno/seguimento
        criterios["retorno_especificado"] = ValidadorAntiInvencao._tem_retorno_seguimento(texto_reformatado)
        if not criterios["retorno_especificado"]:
            avisos.append("Retorno/seguimento não mencionado")

        passou = all(criterios.values()) and len(erros) == 0

        return ValidacaoAntiInvencao(
            passou=passou,
            criterios=criterios,
            avisos=avisos,
            erros=erros,
        )

    @staticmethod
    def _extrair_comorbidades(texto: str) -> List[str]:
        comorbidades_palavras = [
            "diabetes", "hipertensão", "hipertensao", "asma", "dpoc", "tuberculose",
            "hiv", "hepatite", "cirrose", "insuficiência cardíaca", "angina",
            "arritmia", "infarto", "câncer", "cancer", "epilepsia", "convulsão",
            "convulsao", "depressão", "depressao", "ansiedade", "psicose",
            "transtorno", "obesidade", "dislipidemia", "doença renal", "doença pulmonar",
        ]
        return [c for c in comorbidades_palavras if c.lower() in texto.lower()]

    @staticmethod
    def _extrair_medicacoes(texto: str) -> List[str]:
        medicacoes = re.findall(
            r'\b([a-záéíóúãõâêôç]+(?:\s+[a-záéíóúãõâêôç]+)?)\s+(\d+\s*(?:mg|g|UI|unidades)?)',
            texto,
            re.IGNORECASE
        )
        return [f"{m[0]} {m[1]}" for m in medicacoes] if medicacoes else []

    @staticmethod
    def _extrair_exames(texto: str) -> List[str]:
        exames_palavras = [
            "hemoglobina", "glicose", "creatinina", "ureia", "sódio", "potássio",
            "cálcio", "colesterol", "triglicerídeos", "triglicerideos", "ecg",
            "ecocardiograma", "raio-x", "raio x", "tomografia", "ressonância",
            "ressonancia", "ultrassom", "ultrasound", "ct", "endoscopia",
        ]
        return [e for e in exames_palavras if e.lower() in texto.lower()]

    @staticmethod
    def _detectar_invencoes(texto_orig: str, texto_ref: str) -> List[str]:
        """Detecta possíveis invenções (heurística básica)."""
        invencoes: List[str] = []
        return invencoes

    @staticmethod
    def _detectar_interpretacoes_adicionadas(texto_orig: str, texto_ref: str) -> List[str]:
        frases_interpretacao = [
            "sugerindo", "compatível com", "compativel com", "consistente com",
            "indicativo de", "provavelmente", "provável", "possível", "parece indicar"
        ]
        interpretacoes = []
        for frase in frases_interpretacao:
            if frase in texto_ref.lower() and frase not in texto_orig.lower():
                interpretacoes.append(frase)
        return interpretacoes

    @staticmethod
    def _tem_sinais_alarme(texto: str) -> bool:
        sinais = [
            "preocupante", "alarme", "alerta", "risco", "complicação",
            "piora", "deterioração", "descompensação", "descompensacao",
            "crise", "urgência", "emergência", "emergencia"
        ]
        return any(s in texto.lower() for s in sinais)

    @staticmethod
    def _tem_retorno_seguimento(texto: str) -> bool:
        retornos = [
            "retorno", "seguimento", "acompanhamento", "reavaliação",
            "reavaliacao", "próximo", "proxima", "voltar", "volta",
            "consulta marcada", "agendado"
        ]
        return any(r in texto.lower() for r in retornos)


# Instância singleton
detector = DetectorAutomatico()
validador = ValidadorAntiInvencao()


def detectar_tudo(texto: str) -> IdentificacaoAutomatica:
    """Função de conveniência para detectar contexto e especialidade."""
    return detector.detectar_tudo(texto)


def validar_anti_invencao(texto_original: str, texto_reformatado: str) -> ValidacaoAntiInvencao:
    """Função de conveniência para validar texto reformatado."""
    return validador.validar(texto_original, texto_reformatado)
