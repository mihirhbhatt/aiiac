from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class CodeTemplate(BaseModel):
    """Base template for generated code."""
    code: str = Field(..., description="Generated code")
    language: str = Field(..., description="Programming language")
    description: str = Field(..., description="Description of the code")
    type: str = Field(..., description="Template type")

class IaCTemplate(CodeTemplate):
    """Infrastructure as Code template."""
    provider: str = Field(..., description="Cloud provider")
    resource_type: str = Field(..., description="Type of infrastructure")

class ConfigTemplate(CodeTemplate):
    """Configuration template."""
    format: str = Field(..., description="Configuration format")
    environment: str = Field(..., description="Target environment")

class PipelineTemplate(CodeTemplate):
    """CI/CD Pipeline template."""
    platform: str = Field(..., description="CI/CD platform")
    stages: List[str] = Field(default_factory=list)

class GeneratorResponse(BaseModel):
    """Response from code generators."""
    success: bool
    message: str
    templates: List[CodeTemplate] = []
    metadata: Dict = Field(default_factory=dict)