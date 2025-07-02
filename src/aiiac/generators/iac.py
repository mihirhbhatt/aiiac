from typing import Dict
from .base import BaseGenerator
from ..models.schemas import IaCTemplate, GeneratorResponse

class IaCGenerator(BaseGenerator):
    """Infrastructure as Code generator."""
    
    TEMPLATES = {
        "terraform": """
        Generate Terraform code for the following infrastructure:
        
        Requirements:
        {requirements}
        
        Provider: {provider}
        Resource Type: {resource_type}
        
        Include:
        - Resource configurations
        - Variables
        - Outputs
        - Provider configuration
        """,
    }
    
    def generate(self, prompt: str, **kwargs) -> GeneratorResponse:
        """Generate infrastructure code."""
        template_type = kwargs.get("template_type", "terraform")
        provider = kwargs.get("provider", "aws")
        
        template = self.TEMPLATES.get(template_type)
        if not template:
            return GeneratorResponse(
                success=False,
                message=f"Template type {template_type} not supported",
                templates=[]
            )
        
        try:
            formatted_prompt = self._prepare_prompt(
                template,
                requirements=prompt,
                provider=provider,
                resource_type=kwargs.get("resource_type", "general")
            )
            
            response = self.llm(formatted_prompt)
            
            template = IaCTemplate(
                code=response,
                language=template_type,
                description=f"Generated {template_type} code for {provider}",
                type="iac",
                provider=provider,
                resource_type=kwargs.get("resource_type", "general")
            )
            
            return GeneratorResponse(
                success=True,
                message="Successfully generated IaC",
                templates=[template]
            )
            
        except Exception as e:
            return GeneratorResponse(
                success=False,
                message=f"Error generating IaC: {str(e)}",
                templates=[]
            )