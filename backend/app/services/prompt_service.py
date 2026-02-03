"""
Serviço de montagem de prompts (assemble_full_prompt).
Utiliza o prompt_loader para carregar módulos.
"""
from typing import List, Tuple

from app.services.prompt_loader import prompt_loader


def assemble_full_prompt(
    context_key: str,
    specialty_key: str = "",
    sections: List[Tuple[str, str]] | None = None,
    abbreviation_key: str = "",
) -> str:
    """
    Monta o prompt completo combinando os módulos necessários.

    Args:
        context_key: Chave do contexto (ex: "PA_VERDE", "AMBULATORIO", "PACS_URGENCIA")
        specialty_key: Chave da especialidade (ex: "VASCULAR_PULSOS", "PSIQUIATRIA_EEM")
        sections: Lista de (categoria, módulo) para seções adicionais.
        abbreviation_key: Chave do nível de abreviações (ex: "EXTREMAS", "MODERADAS")

    Returns:
        Prompt completo concatenado.
    """
    parts: List[str] = []

    base = prompt_loader.get_module("base", "PROMPT_BASE_001")
    if base:
        parts.append(base)

    ctx = prompt_loader.get_module("contexto", context_key.upper().replace("-", "_"))
    if ctx:
        parts.append(ctx)

    if specialty_key:
        esp = prompt_loader.get_module("especialidades", specialty_key.upper().replace("-", "_"))
        if esp:
            parts.append(esp)

    if sections:
        for category, module_name in sections:
            content = prompt_loader.get_module(category, module_name.upper().replace("-", "_"))
            if content:
                parts.append(content)

    if abbreviation_key:
        abbr = prompt_loader.get_module("abreviacoes", abbreviation_key.upper().replace("-", "_"))
        if abbr:
            parts.append(abbr)

    return "\n\n".join(p for p in parts if p.strip())
