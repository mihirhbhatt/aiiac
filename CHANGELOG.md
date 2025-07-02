# Changelog

All notable changes to AIIAC will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-07-02

### Added
- Initial release of AIIAC (AI Infrastructure as Code Generator)
- Core Features:
  - Infrastructure as Code Generation
    - AWS, Azure, GCP support
    - Terraform, CloudFormation templates
    - Kubernetes manifests
  - Configuration Generation
    - Kubernetes configurations
    - Docker compose files
    - Application configs
  - CI/CD Pipeline Generation
    - GitHub Actions workflows
    - GitLab CI pipelines
    - Jenkins pipelines
  - Utility Code Generation
    - Network scanners
    - kubectl commands
    - MongoDB queries
- CLI Interface:
  - Interactive command-line tool
  - Rich text output
  - Progress indicators
- Web Interface:
  - Streamlit-based UI
  - Real-time code generation
  - Copy to clipboard functionality
  - File saving capabilities

### Dependencies
- Python 3.9+
- Required packages:
  - langchain>=0.1.0
  - langgraph>=0.0.10
  - pydantic>=2.0.0
  - click>=8.0.0
  - rich>=10.0.0
  - streamlit>=1.30.0
  - PyYAML>=6.0.0

### Documentation
- Added comprehensive README.md
- Added installation instructions
- Added usage examples
- Added API documentation

## [1.0.0-beta] - 2025-06-23

### Added
- Beta release for testing
- Basic infrastructure generation
- Simple CLI interface

### Fixed
- Import path issues
- Generator validation logic

## [1.0.0-alpha] - 2025-06-07

### Added
- Initial project structure
- Basic code generators
- Command line interface skeleton
