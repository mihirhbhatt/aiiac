import pytest
from aiiac.generators.iac import IaCGenerator

def test_iac_generator():
    """Test IaC generator."""
    generator = IaCGenerator()
    result = generator.generate(
        "Create an S3 bucket",
        provider="aws",
        template_type="terraform"
    )
    
    assert result.success
    assert len(result.templates) == 1
    assert "resource" in result.templates[0].code.lower()