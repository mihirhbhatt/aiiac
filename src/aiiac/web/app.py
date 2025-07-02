import streamlit as st
from pathlib import Path
import sys
from typing import Optional

# Add the project root to Python path
from aiiac.generators.iac import IaCGenerator
from aiiac.generators.config import ConfigGenerator
from aiiac.generators.pipeline import PipelineGenerator
from aiiac.generators.utility import UtilityGenerator

def init_session_state():
    """Initialize session state variables."""
    if 'generated_code' not in st.session_state:
        st.session_state.generated_code = None
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = 'Infrastructure'

def render_header():
    """Render the application header."""
    st.title("AIIAC - AI Infrastructure as Code Generator")
    st.markdown("""
    Generate Infrastructure as Code, configurations, and CI/CD pipelines using AI.
    """)

def render_infrastructure_tab():
    """Render infrastructure generation tab."""
    st.header("Generate Infrastructure Code")
    
    col1, col2 = st.columns(2)
    
    with col1:
        cloud_provider = st.selectbox(
            "Cloud Provider",
            ["aws", "azure", "gcp"]
        )
    
    with col2:
        template_type = st.selectbox(
            "Template Type",
            ["terraform", "cloudformation", "kubernetes"]
        )
    
    description = st.text_area(
        "Infrastructure Description",
        placeholder="Example: Create an ECS cluster with Fargate and ALB"
    )
    
    if st.button("Generate Infrastructure"):
        with st.spinner("Generating infrastructure code..."):
            generator = IaCGenerator()
            result = generator.generate(
                description,
                provider=cloud_provider,
                template_type=template_type
            )
            
            if result.success:
                st.session_state.generated_code = result.templates[0].code
                st.success("Infrastructure code generated successfully!")
            else:
                st.error(f"Error: {result.message}")

def render_configuration_tab():
    """Render configuration generation tab."""
    st.header("Generate Configuration")
    
    config_type = st.selectbox(
        "Configuration Type",
        ["kubernetes", "docker", "terraform_vars"]
    )
    
    environment = st.selectbox(
        "Environment",
        ["development", "staging", "production"]
    )
    
    description = st.text_area(
        "Configuration Description",
        placeholder="Example: Configure a web application with Redis cache"
    )
    
    if st.button("Generate Configuration"):
        with st.spinner("Generating configuration..."):
            generator = ConfigGenerator()
            result = generator.generate(
                description,
                config_type=config_type,
                environment=environment
            )
            
            if result.success:
                st.session_state.generated_code = result.templates[0].code
                st.success("Configuration generated successfully!")
            else:
                st.error(f"Error: {result.message}")

def render_pipeline_tab():
    """Render pipeline generation tab."""
    st.header("Generate CI/CD Pipeline")
    
    platform = st.selectbox(
        "CI/CD Platform",
        ["github", "gitlab", "jenkins"]
    )
    
    description = st.text_area(
        "Pipeline Description",
        placeholder="Example: Create a pipeline for Python application deployment"
    )
    
    if st.button("Generate Pipeline"):
        with st.spinner("Generating pipeline..."):
            generator = PipelineGenerator()
            result = generator.generate(
                description,
                platform=platform
            )
            
            if result.success:
                st.session_state.generated_code = result.templates[0].code
                st.success("Pipeline generated successfully!")
            else:
                st.error(f"Error: {result.message}")

def render_utility_tab():
    """Render utility generation tab."""
    st.header("Generate Utility Code")
    
    utility_type = st.selectbox(
        "Utility Type",
        ["network_scanner", "kubectl", "mongo_query"]
    )
    
    description = st.text_area(
        "Utility Description",
        placeholder="Example: Create a network port scanner"
    )
    
    if st.button("Generate Utility"):
        with st.spinner("Generating utility code..."):
            generator = UtilityGenerator()
            result = generator.generate(
                description,
                utility_type=utility_type
            )
            
            if result.success:
                st.session_state.generated_code = result.templates[0].code
                st.success("Utility code generated successfully!")
            else:
                st.error(f"Error: {result.message}")

def render_output():
    """Render the generated code output."""
    if st.session_state.generated_code:
        st.header("Generated Code")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.code(st.session_state.generated_code)
        
        with col2:
            if st.button("Copy to Clipboard"):
                st.write("Copied to clipboard!")
                st.toast("Code copied to clipboard!")
            
            if st.button("Save to File"):
                save_path = Path("generated_code.txt")
                save_path.write_text(st.session_state.generated_code)
                st.success(f"Saved to: {save_path}")

def main():
    """Main application function."""
    init_session_state()
    render_header()
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "Infrastructure",
        "Configuration",
        "Pipeline",
        "Utility"
    ])
    
    with tab1:
        render_infrastructure_tab()
    
    with tab2:
        render_configuration_tab()
    
    with tab3:
        render_pipeline_tab()
    
    with tab4:
        render_utility_tab()
    
    # Render output section
    render_output()

if __name__ == "__main__":
    main()