from typing import Optional, List
from .base import BaseGenerator
from ..models.schemas import PipelineTemplate, GeneratorResponse, IaCTemplate, ConfigTemplate

class PipelineGenerator(BaseGenerator):
    """CI/CD Pipeline generator."""
    
    TEMPLATES = {
        "github": """
        Generate GitHub Actions workflow for:
        
        Requirements: {requirements}
        Infrastructure: {iac_description}
        Configuration: {config_description}
        
        Include:
        - CI/CD stages
        - Testing
        - Security scanning
        - Infrastructure deployment
        - Application deployment
        """,
        
        "gitlab": """
        Generate GitLab CI pipeline for:
        
        Requirements: {requirements}
        Infrastructure: {iac_description}
        Configuration: {config_description}
        
        Include:
        - CI/CD stages
        - Testing
        - Security scanning
        - Infrastructure deployment
        - Application deployment
        """,
        
        "jenkins": """
        Generate Jenkinsfile for:
        
        Requirements: {requirements}
        Infrastructure: {iac_description}
        Configuration: {config_description}
        
        Include:
        - Pipeline stages
        - Testing
        - Security scanning
        - Infrastructure deployment
        - Application deployment
        """
    }
    
    def generate(
        self,
        prompt: str,
        iac_template: Optional[IaCTemplate] = None,
        config_template: Optional[ConfigTemplate] = None,
        **kwargs
    ) -> GeneratorResponse:
        """Generate CI/CD pipeline."""
        platform = kwargs.get("platform", "github")
        
        template = self.TEMPLATES.get(platform)
        if not template:
            return GeneratorResponse(
                success=False,
                message=f"Pipeline platform {platform} not supported",
                templates=[]
            )
        
        try:
            formatted_prompt = self._prepare_prompt(
                template,
                requirements=prompt,
                iac_description=iac_template.description if iac_template else "Not provided",
                config_description=config_template.description if config_template else "Not provided"
            )
            
            response = self.llm(formatted_prompt)
            
            stages = self._extract_stages(response)
            
            template = PipelineTemplate(
                code=response,
                language=self._get_language(platform),
                description=f"Generated {platform} pipeline",
                type="pipeline",
                platform=platform,
                stages=stages
            )
            
            return GeneratorResponse(
                success=True,
                message="Successfully generated pipeline",
                templates=[template]
            )
            
        except Exception as e:
            return GeneratorResponse(
                success=False,
                message=f"Error generating pipeline: {str(e)}",
                templates=[]
            )
    
    def _get_language(self, platform: str) -> str:
        """Get language for pipeline platform."""
        language_map = {
            "github": "yaml",
            "gitlab": "yaml",
            "jenkins": "groovy"
        }
        return language_map.get(platform, "yaml")
    
    def _extract_stages(self, pipeline_code: str) -> List[str]:
        """Extract pipeline stages from code."""
        stages = []
        lines = pipeline_code.split("\n")
        
        for line in lines:
            if "stage:" in line.lower():
                stage = line.split("stage:")[1].strip().strip('"\'')
                stages.append(stage)
            elif "stage(" in line.lower():
                stage = line.split("stage(")[1].split(")")[0].strip('"\'')
                stages.append(stage)
                
        return stages