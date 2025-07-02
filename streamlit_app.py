import streamlit as st
from pathlib import Path
from generators.iac import IaCGenerator
from generators.config import ConfigGenerator
from generators.pipeline import PipelineGenerator
from generators.utility import UtilityGenerator

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


# Add the src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))

import streamlit as st
from aiiac.web.app import main

if __name__ == "__main__":
    main()