# AIIAC (AI Infrastructure as Code Generator)

AIIAC is a powerful CLI and web tool that generates Infrastructure as Code, configurations, and CI/CD pipelines using AI.

## Features

- 🏗️ Infrastructure as Code Generation (Terraform, CloudFormation, Kubernetes)
- ⚙️ Configuration Generation (Docker, K8s, Application Config)
- 🔄 CI/CD Pipeline Generation (GitHub Actions, GitLab CI, Jenkins)
- 🛠️ Utility Code Generation (Network Scanner, kubectl commands, MongoDB queries)
- 🎯 Multiple Cloud Provider Support (AWS, Azure, GCP)
- 💾 Output Saving and Validation
- 🌐 Web Interface (Streamlit)

## Installation

## Install Ollama 
ollama run codellama
### CLI Installation

```bash
# Clone the repository
git clone https://github.com/mihirhbhatt/aiiac
cd aiiac

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .


# Requirements
Python 3.9+
Ollama with CodeLlama model
Required Python packages (installed automatically):
click
rich
langchain
langgraph
pydantic
requests
PyYAML
streamlit (for web interface)

# Usage
## CLI Usage 
```bash
 1. Generate Infrastructure Code:
    aiiac create "Create an ECS cluster with Fargate" --cloud aws --type terraform

2. Generate Configuration:
aiiac config "web application" --type kubernetes --env prod

3. Generate Pipeline:
aiiac pipeline "deployment workflow" --platform github

4. Generate Utility:
aiiac util network_scanner "scan all open ports"

5. List Available Generators:
aiiac list

# Web Interface Usage
streamlit run src/aiiac/web/app.py
  

# Docker Build and run :

docker build -t aiiac .
docker run -p 8501:8501 aiiac

