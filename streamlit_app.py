import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="FedID — National Identity Infrastructure",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Responsive full-screen styling for mobile and desktop
st.markdown("""
<style>
    /* Reset margins and paddings for seamless full-width */
    html, body, [data-testid="stAppViewContainer"] {
        margin: 0 !important;
        padding: 0 !important;
        overflow-x: hidden !important;
    }
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    header[data-testid="stHeader"] {
        display: none !important;
    }
    #MainMenu, footer {
        visibility: hidden !important;
    }
    iframe {
        border: none !important;
        width: 100% !important;
        max-width: 100% !important;
        min-height: 100vh !important;
        height: 100vh !important;
        display: block !important;
    }
</style>
""", unsafe_allow_html=True)

# Path to standalone bundle
standalone_path = os.path.join(os.path.dirname(__file__), "standalone.html")
if not os.path.exists(standalone_path):
    standalone_path = os.path.join(os.path.dirname(__file__), "frontend", "dist", "standalone.html")

if os.path.exists(standalone_path):
    with open(standalone_path, "r", encoding="utf-8") as f:
        app_html = f.read()
    # Render standalone FedID portal full screen
    components.html(app_html, height=1000, scrolling=True)
else:
    st.error("Deployment Error: standalone.html not found in repository root. Please ensure standalone.html is committed.")
