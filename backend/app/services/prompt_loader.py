"""
Orquestrador de Módulos de Prompt.
Responsável pela leitura de arquivos .md da estrutura prompt_modules/.
"""
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class PromptModuleLoader:
    """Carrega módulos de prompt do sistema de arquivos."""

    def __init__(self) -> None:
        self.base_path = Path(__file__).parent.parent / "prompt_modules"

    def get_module(self, category: str, module_name: str) -> str:
        """
        Lê um arquivo .md da estrutura de módulos.

        Args:
            category: Caminho da categoria (ex: "base", "contexto", "secoes/conduta")
            module_name: Nome do arquivo sem extensão (ex: "PROMPT_BASE_001")

        Returns:
            Conteúdo do arquivo em UTF-8, ou string vazia se não existir.
        """
        if not module_name:
            return ""

        file_path = self.base_path / category / f"{module_name.upper()}.md"

        try:
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    return f.read()
            else:
                logger.warning("Módulo não encontrado: %s", file_path)
                return ""
        except Exception as e:
            logger.error("Erro ao ler módulo %s: %s", module_name, e)
            return ""


prompt_loader = PromptModuleLoader()
