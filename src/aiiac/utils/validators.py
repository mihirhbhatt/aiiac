from typing import Dict, Any
import re

def validate_output(code: str, language: str) -> bool:
    """Validate generated code."""
    if language == "yaml":
        return validate_yaml(code)
    elif language == "terraform":
        return validate_terraform(code)
    elif language == "python":
        return validate_python(code)
    return True

def validate_yaml(code: str) -> bool:
    """Validate YAML code."""
    try:
        import yaml
        yaml.safe_load(code)
        return True
    except:
        return False

def validate_terraform(code: str) -> bool:
    """Validate Terraform code."""
    required_blocks = ["resource", "provider"]
    return all(block in code.lower() for block in required_blocks)

def validate_python(code: str) -> bool:
    """Validate Python code."""
    try:
        compile(code, '<string>', 'exec')
        return True
    except Exception:
        return False