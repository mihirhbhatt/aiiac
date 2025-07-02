from abc import ABC, abstractmethod
from typing import Dict
from ..core.llm import OllamaLLM
from ..models.schemas import GeneratorResponse

class BaseGenerator(ABC):
    """Base class for all generators."""
    
    def __init__(self, model: str = "codellama"):
        self.llm = OllamaLLM(model=model)
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> GeneratorResponse:
        """Generate code from prompt."""
        pass
    
    def _prepare_prompt(self, template: str, **kwargs) -> str:
        """Prepare prompt from template."""
        return template.format(**kwargs)