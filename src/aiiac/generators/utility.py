from typing import List
from .base import BaseGenerator
from ..models.schemas import CodeTemplate, GeneratorResponse

class UtilityGenerator(BaseGenerator):
    """Utility code generator."""
    
    TEMPLATES = {
        "network_scanner": """
        Generate a Python network scanner that:
        
        Requirements: {requirements}
        
        Include:
        - Port scanning
        - Error handling
        - Security best practices
        - Documentation
        """,
        
        "kubectl": """
        Generate kubectl commands for:
        
        Requirements: {requirements}
        
        Include:
        - Command explanation
        - Required permissions
        - Example usage
        """,
        
        "mongo_query": """
        Generate MongoDB query for:
        
        Requirements: {requirements}
        
        Include:
        - Query explanation
        - Index recommendations
        - Performance considerations
        """
    }
    
    def generate(self, prompt: str, **kwargs) -> GeneratorResponse:
        """Generate utility code."""
        utility_type = kwargs.get("utility_type", "network_scanner")
        
        template = self.TEMPLATES.get(utility_type)
        if not template:
            return GeneratorResponse(
                success=False,
                message=f"Utility type {utility_type} not supported",
                templates=[]
            )
        
        try:
            formatted_prompt = self._prepare_prompt(
                template,
                requirements=prompt
            )
            
            response = self.llm(formatted_prompt)
            
            template = CodeTemplate(
                code=response,
                language=self._get_language(utility_type),
                description=f"Generated {utility_type} utility",
                type="utility"
            )
            
            return GeneratorResponse(
                success=True,
                message="Successfully generated utility",
                templates=[template]
            )
            
        except Exception as e:
            return GeneratorResponse(
                success=False,
                message=f"Error generating utility: {str(e)}",
                templates=[]
            )
    
    def _get_language(self, utility_type: str) -> str:
        """Get language for utility type."""
        language_map = {
            "network_scanner": "python",
            "kubectl": "bash",
            "mongo_query": "mongodb"
        }
        return language_map.get(utility_type, "text")