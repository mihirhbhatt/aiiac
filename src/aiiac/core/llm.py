from typing import Dict, List, Optional
import requests
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun

class OllamaLLM(LLM):
    """Ollama LLM integration."""
    
    base_url: str = "http://localhost:11434"
    model: str = "codellama"
    temperature: float = 0.1
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @property
    def _llm_type(self) -> str:
        return "ollama"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Dict
    ) -> str:
        """Call the Ollama API."""
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "temperature": self.temperature,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()["response"]