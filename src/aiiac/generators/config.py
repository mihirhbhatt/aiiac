from typing import Optional
from .base import BaseGenerator
from ..models.schemas import ConfigTemplate, GeneratorResponse, IaCTemplate

class ConfigGenerator(BaseGenerator):
    """Configuration generator."""
    
    TEMPLATES = {
        "kubernetes": """
        Generate Kubernetes configuration for:
        
        Requirements: {requirements}
        Infrastructure: {iac_description}
        Environment: {environment}
        
        Include:
        - ConfigMaps
        - Secrets (templates)
        - Resource limits
        - Environment variables
        """,
        
        "docker": """
        Generate Docker configuration for:
        
        Requirements: {requirements}
        Environment: {environment}
        
        Include:
        - Dockerfile
        - Docker Compose
        - Environment settings
        - Volume mappings
        """,
        
        "terraform_vars": """
        Generate Terraform variables for:
        
        Requirements: {requirements}
        Environment: {environment}
        
        Include:
        - Variable definitions
        - Default values
        - Environment-specific values
        """
    }
    
    def generate(
        self,
        prompt: str,
        iac_template: Optional[IaCTemplate] = None,
        **kwargs
    ) -> GeneratorResponse:
        """Generate configuration files."""
        config_type = kwargs.get("config_type", "kubernetes")
        environment = kwargs.get("environment", "development")
        
        template = self.TEMPLATES.get(config_type)
        if not template:
            return GeneratorResponse(
                success=False,
                message=f"Configuration type {config_type} not supported",
                templates=[]
            )
        
        try:
            formatted_prompt = self._prepare_prompt(
                template,
                requirements=prompt,
                iac_description=iac_template.description if iac_template else "Not provided",
                environment=environment
            )
            
            response = self.llm(formatted_prompt)
            
            template = ConfigTemplate(
                code=response,
                language=self._get_language(config_type),
                description=f"Generated {config_type} configuration for {environment}",
                type="config",
                format=self._get_format(config_type),
                environment=environment
            )
            
            return GeneratorResponse(
                success=True,
                message="Successfully generated configuration",
                templates=[template]
            )
            
        except Exception as e:
            return GeneratorResponse(
                success=False,
                message=f"Error generating configuration: {str(e)}",
                templates=[]
            )
    
    def _get_language(self, config_type: str) -> str:
        """Get language for config type."""
        language_map = {
            "kubernetes": "yaml",
            "docker": "dockerfile",
            "terraform_vars": "hcl"
        }
        return language_map.get(config_type, "yaml")
    
    def _get_format(self, config_type: str) -> str:
        """Get format for config type."""
        format_map = {
            "kubernetes": "yaml",
            "docker": "compose",
            "terraform_vars": "tfvars"
        }
        return format_map.get(config_type, "yaml")