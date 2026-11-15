import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="FedID — National Identity Infrastructure",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main {
        background-color: #0b1120;
    }
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://api.iconify.design/lucide:shield-check.svg?color=%2306b6d4&width=48", width=48)
    st.title("FedID")
    st.caption("National Zero-Knowledge Identity Layer")
    st.divider()
    
    st.markdown("### 🔐 Investor Access Protocol")
    st.info("""
    **Restricted Demo Environment**  
    API OTP tokens are rate-limited to prevent unauthorized usage.
    
    🔑 **Master Passkey:** `investor`  
    📧 **Contact Founder:**  
    [pushkarpatade97@gmail.com](mailto:pushkarpatade97@gmail.com)
    """)
    
    st.divider()
    st.markdown("### 🏛️ Technology Stack")
    st.markdown("""
    - **ZK Cryptography:** Native SHA-256 / ZKP-SNARK
    - **Transit Encryption:** AES-256-GCM Keystroke Cipher
    - **Email Service:** Real OTP via EmailJS
    - **Identity Standard:** W3C DID Specification
    - **Regulatory Compliance:** DPDP Act 2023 (India)
    - **Frontend:** React 19 + Vite + Tailwind v4
    - **Backend:** Node.js + Express 5 + MongoDB
    """)

# Main Content Header
st.markdown("""
<div style="text-align: center; padding: 20px 0 25px 0;">
    <span class="badge" style="background: rgba(6, 182, 212, 0.15); color: #06b6d4; border: 1px solid rgba(6, 182, 212, 0.3);">
        CIPHATHON '26 • CODE WARRIORS • MIT-WPU
    </span>
    <h1 style="font-size: 3.2rem; font-weight: 900; margin: 15px 0 10px 0; letter-spacing: -0.03em;">
        One Identity. <span style="background: linear-gradient(90deg, #06b6d4, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Every Institution.</span>
    </h1>
    <p style="font-size: 1.1rem; color: #94a3b8; max-width: 800px; margin: 0 auto; line-height: 1.6;">
        FedID structurally eliminates identity silos across federal domains. Citizens register once — generating mathematically unforgeable Zero-Knowledge tokens that prove eligibility (Age, Banking KYC, Medical ABDM, Tax) without ever exposing raw Personally Identifiable Information.
    </p>
</div>
""", unsafe_allow_html=True)

# Metrics Grid
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown("""
    <div class="metric-card">
        <h2 style="color: #38bdf8; margin: 0;">8+</h2>
        <p style="color: #64748b; font-size: 11px; text-transform: uppercase; margin: 5px 0 0 0;">Domains Covered</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2 style="color: #22c55e; margin: 0;">0 Bytes</h2>
        <p style="color: #64748b; font-size: 11px; text-transform: uppercase; margin: 5px 0 0 0;">PII Data Exposed</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2 style="color: #a855f7; margin: 0;">AES-256</h2>
        <p style="color: #64748b; font-size: 11px; text-transform: uppercase; margin: 5px 0 0 0;">Live Stream Cipher</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h2 style="color: #f59e0b; margin: 0;">1-Click</h2>
        <p style="color: #64748b; font-size: 11px; text-transform: uppercase; margin: 5px 0 0 0;">Single-Use Burn</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="metric-card">
        <h2 style="color: #ef4444; margin: 0;">₹4.2T</h2>
        <p style="color: #64748b; font-size: 11px; text-transform: uppercase; margin: 5px 0 0 0;">Fraud Prevented</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Live Portal Embed
tab1, tab2 = st.tabs(["🚀 Launch Live FedID Interactive Portal", "📖 Executive Architecture Deck"])

with tab1:
    st.markdown("""
    <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px; margin-bottom: 20px;">
        <h3 style="margin-top:0;">🌐 Interactive Application Window</h3>
        <p style="color: #94a3b8; font-size: 13px;">
            Experience the step-by-step FedID portal below: <b>Page 1: VIP Passkey</b> ➔ <b>Page 2: 3-Layer Login (Real Email OTP)</b> ➔ <b>Page 3: Main ZKP Platform</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔑 Quick Demo Credentials (For Evaluators)"):
        st.markdown("""
        - **Step 1 VIP Passkey:** `investor`
        - **Step 2 Login:** Click `⚡ Auto-fill Samarth` (or username `samarth`, password `password123`)
        - **Step 2 OTP:** Sent to your real email via EmailJS + simulated SMS
        - **Step 2 Security Question:** `sarang`
        """)

    # Check for standalone single-file bundle (root or frontend/dist)
    standalone_path = os.path.join(os.path.dirname(__file__), "standalone.html")
    if not os.path.exists(standalone_path):
        standalone_path = os.path.join(os.path.dirname(__file__), "frontend", "dist", "standalone.html")
    
    col_mode, _ = st.columns([2, 3])
    with col_mode:
        mode = st.radio("Display Mode:", ["Cloud Native Bundle (Recommended for Streamlit Cloud)", "Custom URL (Localhost / Remote)"], horizontal=True)

    if mode == "Cloud Native Bundle (Recommended for Streamlit Cloud)" and os.path.exists(standalone_path):
        with open(standalone_path, "r", encoding="utf-8") as f:
            app_html = f.read()
        components.html(app_html, height=920, scrolling=True)
    else:
        portal_url = st.text_input("FedID Portal URL", value="http://localhost:5173", help="Point this to your local server or deployed Vercel frontend URL")
        components.iframe(portal_url, height=920, scrolling=True)

with tab2:
    st.markdown("""
    ### 🛡️ Why FedID?
    Current identity solutions rely on centralized databases that store raw Aadhaar, PAN, and demographic numbers across hundreds of private entities. This creates:
    - **Massive Honey-pots:** A single breach compromises millions of citizen records.
    - **Over-sharing:** Proving legal age to enter a venue forces a citizen to disclose full Date of Birth, Address, and Guardian names.
    - **Duplicate / Phantom Beneficiaries:** Subsidies and Direct Benefit Transfers (DBT) bleed trillions of rupees annually due to synthetic identities.

    ### ⚡ The FedID Solution
    1. **Zero-Knowledge Architecture:** Cryptographic proofs confirm claims (e.g. `age >= 18`, `valid_pan == true`, `blood_group == B+`) without transmitting underlying values.
    2. **Hardware Enclave Tokenization:** Master secret entropy binds citizen parameters to unforgeable SHA-256 tokens.
    3. **Single-Use Burning:** Verifying institutions permanently consume tokens on first scan, preventing replay attacks and double-spending.
    4. **DPDP Act 2023 Native:** Built-in concurrent session checks and zero-retention data policies guarantee absolute compliance with national data privacy mandates.
    """)
