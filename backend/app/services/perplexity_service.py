"""
Serviço de integração com a API Perplexity.
Responsável por gerar evoluções médicas formatadas usando IA.
"""
import httpx
import json
from typing import Optional, Dict, Any, List
from datetime import datetime

from app.core.config import settings
from app.models.evolution import (
    EvolutionTemplate,
    PatientData,
    PrimaryContext,
    TitleFormat,
    SectionTitleOption,
    ExamOrganization,
    ReferenceValues,
    LabFormat,
    AbbreviationLevel,
    MedicationFormat,
)


class PerplexityService:
    """Serviço para geração de evoluções médicas via Perplexity API."""
    
    def __init__(self):
        """Inicializa o serviço com configurações da API."""
        self.api_key = settings.PERPLEXITY_API_KEY
        self.api_url = settings.PERPLEXITY_API_URL
        self.model = settings.PERPLEXITY_MODEL
    
    def _build_system_prompt(self, template: Optional[EvolutionTemplate] = None) -> str:
        """Constrói o prompt de sistema baseado no template."""
        base_prompt = """Você é um assistente especializado em documentação médica brasileira.
Sua função é formatar evoluções médicas a partir de texto livre, seguindo rigorosamente as configurações fornecidas.

REGRAS GERAIS:
1. Mantenha a precisão médica absoluta - não invente informações
2. Use terminologia médica adequada ao contexto brasileiro
3. Siga estritamente o formato e estrutura solicitados
4. Organize as informações de forma clara e profissional
5. Respeite as preferências de abreviações configuradas
6. Formate exames conforme especificado
7. Inclua apenas as seções configuradas

"""
        
        if template:
            base_prompt += self._build_template_instructions(template)
        
        return base_prompt
    
    def _build_template_instructions(self, template: EvolutionTemplate) -> str:
        """Constrói instruções específicas baseadas no template."""
        instructions = f"""
CONFIGURAÇÕES DO TEMPLATE: {template.name}

CONTEXTO: {self._get_context_description(template)}

CABEÇALHO - Incluir:
{self._build_header_instructions(template.header_config)}

SEÇÕES A INCLUIR:
{self._build_sections_instructions(template.sections_config)}

FORMATAÇÃO:
{self._build_formatting_instructions(template.formatting_config)}
"""
        return instructions
    
    def _get_context_description(self, template: EvolutionTemplate) -> str:
        """Retorna descrição do contexto do template."""
        context_map = {
            PrimaryContext.EMERGENCY: "Emergência/Pronto-Socorro",
            PrimaryContext.ICU: "UTI - Unidade de Terapia Intensiva",
            PrimaryContext.HOSPITALIZATION: "Internação/Enfermaria",
            PrimaryContext.OUTPATIENT: "Ambulatório/Consultório",
        }
        
        context = context_map.get(template.primary_context, "Não especificado")
        
        # Adiciona subcontexto se disponível
        if template.emergency_type:
            context += f" - {template.emergency_type.value}"
        elif template.outpatient_specialty:
            context += f" - {template.outpatient_specialty.value}"
        elif template.icu_type:
            context += f" - {template.icu_type.value}"
        elif template.hospitalization_type:
            context += f" - {template.hospitalization_type.value}"
        
        return context
    
    def _build_header_instructions(self, config) -> str:
        """Constrói instruções para o cabeçalho."""
        items = []
        if config.include_name:
            items.append("- Nome do paciente")
        if config.include_age:
            items.append("- Idade")
        if config.include_occupation:
            items.append("- Ocupação")
        if config.include_birthplace:
            items.append("- Naturalidade")
        if config.include_sexual_orientation:
            items.append("- Orientação sexual")
        if config.include_comorbidities:
            items.append("- Comorbidades/História relevante")
        if config.include_medications:
            items.append("- Medicações em uso contínuo (MUC)")
        if config.include_allergies:
            items.append("- Alergias")
        if config.include_previous_surgeries:
            items.append("- Cirurgias prévias")
        if config.include_family_history:
            items.append("- História familiar")
        if config.include_gestational_age:
            items.append("- Idade gestacional (IG)")
        if config.include_gpa:
            items.append("- Gestação/Para/Aborto (GPA)")
        if config.include_rapid_tests:
            items.append("- Testes rápidos")
        if config.include_bed:
            items.append("- Leito")
        if config.include_admission_date:
            items.append("- Data de internação")
        
        return "\n".join(items) if items else "- Dados básicos do paciente"
    
    def _build_sections_instructions(self, config) -> str:
        """Constrói instruções para as seções."""
        items = []
        if config.include_hda:
            items.append("- HDA (História da Doença Atual)")
        if config.include_physical_exam:
            items.append("- Exame Físico/Objetivo")
        if config.include_complementary_exams:
            items.append("- Exames Complementares")
        if config.include_assessment:
            items.append("- Impressão/Avaliação")
        if config.include_plan:
            items.append("- Conduta/Plano")
        if config.include_reevaluation:
            items.append("- Reavaliação")
        if config.include_daily_evolution:
            items.append("- Evolução do dia")
        if config.include_subjective:
            items.append("- Subjetivo (estilo SOAP)")
        
        return "\n".join(items) if items else "- Seções padrão"
    
    def _build_formatting_instructions(self, config) -> str:
        """Constrói instruções de formatação."""
        instructions = []
        
        # Formato de títulos
        hda_format = config.hda_format
        title_format_map = {
            TitleFormat.UPPERCASE: "MAIÚSCULAS",
            TitleFormat.CAPITALIZE: "Primeira Letra Maiúscula",
            TitleFormat.LOWERCASE: "minúsculas",
        }
        instructions.append(f"- Títulos das seções: {title_format_map.get(hda_format.title_format, 'MAIÚSCULAS')}")
        
        if hda_format.include_date:
            instructions.append(f"- Incluir data no formato {hda_format.date_format}")
        
        # Formato de exames
        exam_format = config.exam_format
        org_map = {
            ExamOrganization.BY_MODALITY: "Organizar por modalidade (Labs, Imagem, ECG)",
            ExamOrganization.CHRONOLOGICAL: "Organizar cronologicamente",
        }
        instructions.append(f"- Exames: {org_map.get(exam_format.organization, 'Por modalidade')}")
        
        ref_map = {
            ReferenceValues.ALWAYS: "Sempre incluir valores de referência",
            ReferenceValues.ONLY_ALTERED: "Incluir VR apenas se alterado",
            ReferenceValues.NEVER: "Não incluir valores de referência",
        }
        instructions.append(f"- {ref_map.get(exam_format.reference_values, 'VR se alterado')}")
        
        lab_map = {
            LabFormat.COMPACT: "Formato compacto: Hb 12,5 / Ht 37 | Leu 8.500",
            LabFormat.DETAILED: "Formato detalhado: Hemoglobina: 12,5 g/dL",
        }
        instructions.append(f"- Labs: {lab_map.get(exam_format.lab_format, 'Compacto')}")
        
        # Abreviações
        abbr = config.abbreviations
        abbr_map = {
            AbbreviationLevel.MAXIMUM: "Usar abreviações máximas (HAS, DM, DPOC, BEG, etc)",
            AbbreviationLevel.MODERATE: "Usar abreviações moderadas (só doenças comuns)",
            AbbreviationLevel.MINIMUM: "Escrever por extenso (mínimo de abreviações)",
        }
        instructions.append(f"- {abbr_map.get(abbr.medical_abbreviations, 'Abreviações máximas')}")
        
        med_map = {
            MedicationFormat.ABBREVIATED: "Medicações abreviadas (AAS, IECA, BRA)",
            MedicationFormat.FULL: "Medicações por extenso",
        }
        instructions.append(f"- {med_map.get(abbr.medication_format, 'Abreviadas')}")
        
        return "\n".join(instructions)
    
    def _build_user_prompt(
        self,
        raw_text: str,
        patient_data: Optional[PatientData] = None,
        evolution_type: Optional[str] = None
    ) -> str:
        """Constrói o prompt do usuário com o texto a ser formatado."""
        prompt = f"""Por favor, formate a seguinte evolução médica:

TEXTO LIVRE:
{raw_text}

"""
        
        if patient_data:
            prompt += "DADOS DO PACIENTE:\n"
            if patient_data.name:
                prompt += f"- Nome: {patient_data.name}\n"
            if patient_data.age:
                prompt += f"- Idade: {patient_data.age}\n"
            if patient_data.comorbidities:
                prompt += f"- Comorbidades: {patient_data.comorbidities}\n"
            if patient_data.medications:
                prompt += f"- Medicações: {patient_data.medications}\n"
            if patient_data.allergies:
                prompt += f"- Alergias: {patient_data.allergies}\n"
            if patient_data.bed:
                prompt += f"- Leito: {patient_data.bed}\n"
            prompt += "\n"
        
        if evolution_type:
            prompt += f"TIPO DE EVOLUÇÃO: {evolution_type}\n\n"
        
        prompt += """Retorne a evolução formatada seguindo EXATAMENTE as configurações especificadas.
Organize em seções claras e use a formatação correta para cada elemento.
Retorne APENAS o texto da evolução formatada, sem explicações adicionais."""
        
        return prompt
    
    async def generate_evolution(
        self,
        raw_text: str,
        template: Optional[EvolutionTemplate] = None,
        patient_data: Optional[PatientData] = None,
        evolution_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Gera uma evolução médica formatada usando a API Perplexity.
        
        Args:
            raw_text: Texto livre com informações do atendimento
            template: Template de configuração (opcional)
            patient_data: Dados do paciente (opcional)
            evolution_type: Tipo específico de evolução (opcional)
        
        Returns:
            Dicionário com a evolução formatada e metadados
        """
        start_time = datetime.now()
        
        system_prompt = self._build_system_prompt(template)
        user_prompt = self._build_user_prompt(raw_text, patient_data, evolution_type)
        
        # Se não houver API key configurada, usa formatação básica local
        if not self.api_key:
            return self._generate_fallback_evolution(raw_text, template, patient_data)
        
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    self.api_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": self.model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt},
                        ],
                        "temperature": 0.1,  # Baixa temperatura para consistência
                        "max_tokens": 4000,
                    },
                )
                
                response.raise_for_status()
                result = response.json()
                
                formatted_text = result["choices"][0]["message"]["content"]
                
                end_time = datetime.now()
                processing_time = int((end_time - start_time).total_seconds() * 1000)
                
                return {
                    "formatted_text": formatted_text,
                    "sections": self._extract_sections(formatted_text),
                    "processing_time_ms": processing_time,
                    "model_used": self.model,
                    "success": True,
                }
                
        except httpx.HTTPStatusError as e:
            return {
                "formatted_text": "",
                "sections": [],
                "processing_time_ms": 0,
                "error": f"Erro na API: {e.response.status_code}",
                "success": False,
            }
        except Exception as e:
            return {
                "formatted_text": "",
                "sections": [],
                "processing_time_ms": 0,
                "error": str(e),
                "success": False,
            }
    
    def _generate_fallback_evolution(
        self,
        raw_text: str,
        template: Optional[EvolutionTemplate] = None,
        patient_data: Optional[PatientData] = None
    ) -> Dict[str, Any]:
        """Gera uma evolução básica sem usar a API (fallback)."""
        sections = []
        formatted_parts = []
        order = 0
        
        # Cabeçalho
        if patient_data:
            header_parts = []
            if patient_data.name:
                header_parts.append(f"Paciente: {patient_data.name}")
            if patient_data.age:
                header_parts.append(f"Idade: {patient_data.age}")
            if patient_data.bed:
                header_parts.append(f"Leito: {patient_data.bed}")
            if patient_data.comorbidities:
                header_parts.append(f"Comorbidades: {patient_data.comorbidities}")
            if patient_data.medications:
                header_parts.append(f"MUC: {patient_data.medications}")
            if patient_data.allergies:
                header_parts.append(f"Alergias: {patient_data.allergies}")
            
            if header_parts:
                header_text = "\n".join(header_parts)
                formatted_parts.append(header_text)
                sections.append({
                    "title": "IDENTIFICAÇÃO",
                    "content": header_text,
                    "order": order
                })
                order += 1
        
        # Texto principal
        formatted_parts.append(f"\nHDA:\n{raw_text}")
        sections.append({
            "title": "HDA",
            "content": raw_text,
            "order": order
        })
        
        return {
            "formatted_text": "\n".join(formatted_parts),
            "sections": sections,
            "processing_time_ms": 0,
            "model_used": "fallback",
            "success": True,
            "warning": "API Perplexity não configurada. Usando formatação básica."
        }
    
    def _extract_sections(self, text: str) -> List[Dict[str, Any]]:
        """Extrai seções do texto formatado."""
        sections = []
        current_section = None
        current_content = []
        order = 0
        
        # Padrões comuns de títulos de seção
        section_patterns = [
            "IDENTIFICAÇÃO", "CABEÇALHO", "DADOS",
            "HDA", "HISTÓRIA DA DOENÇA ATUAL", "QUEIXA PRINCIPAL",
            "EXAME FÍSICO", "OBJETIVO", "EF",
            "EXAMES", "EXAMES COMPLEMENTARES", "LABS",
            "IMPRESSÃO", "AVALIAÇÃO", "HIPÓTESE DIAGNÓSTICA", "HD",
            "CONDUTA", "PLANO", "PRESCRIÇÃO",
            "SUBJETIVO", "S:", "SOAP",
            "REAVALIAÇÃO", "EVOLUÇÃO",
        ]
        
        lines = text.split("\n")
        
        for line in lines:
            line_upper = line.strip().upper()
            is_section_header = False
            
            for pattern in section_patterns:
                if line_upper.startswith(pattern) or line_upper == pattern:
                    # Salva seção anterior
                    if current_section:
                        sections.append({
                            "title": current_section,
                            "content": "\n".join(current_content).strip(),
                            "order": order
                        })
                        order += 1
                    
                    current_section = line.strip().rstrip(":")
                    current_content = []
                    is_section_header = True
                    break
            
            if not is_section_header and current_section:
                current_content.append(line)
        
        # Adiciona última seção
        if current_section:
            sections.append({
                "title": current_section,
                "content": "\n".join(current_content).strip(),
                "order": order
            })
        
        return sections


# Instância singleton do serviço
perplexity_service = PerplexityService()

# Teste de Git