"""
Food Verse AI - Multimodal Food Intelligence Agent
Skill Wallet Capstone Project 3
Production-ready Streamlit application engineered for high-performance multimodal food intelligence.
"""

import streamlit as st
import os

# Page Configuration - Must be the first Streamlit command
st.set_page_config(
    page_title="Food Verse AI - Multimodal Food Intelligence Agent",
    page_icon="🥑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load External CSS Styles
def load_custom_css():
    css_path = os.path.join(os.path.dirname(__file__), "assets", "css", "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        # Fallback minimal styling
        st.markdown("""
            <style>
                .glass-card { background: rgba(30, 41, 59, 0.7); border-radius: 12px; padding: 1rem; margin-bottom: 1rem; }
            </style>
        """, unsafe_allow_html=True)

load_custom_css()

# Import Modules
from modules.ai_service import AIService
from modules.food_recognition import render_tab_food_recognition
from modules.freshness_diagnostic import render_tab_freshness
from modules.kitchen_hygiene import render_tab_kitchen_hygiene
from modules.recipe_assistant import render_tab_recipe_assistant
from modules.meal_planner import render_tab_meal_planner


# -------------------------------------------------------------
# Sidebar: Configuration, Model Selection & Persona
# -------------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 0.5rem 0 1.2rem 0;">
            <div style="font-size: 2.8rem; line-height: 1; margin-bottom: 0.4rem;">🥑</div>
            <h2 style="margin: 0; font-size: 1.45rem; font-weight: 800; background: linear-gradient(135deg, #34D399, #38BDF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Food Verse AI
            </h2>
            <div style="font-size: 0.78rem; font-weight: 600; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 0.2rem;">
                Multimodal Intelligence Agent
            </div>
            <div style="margin-top: 0.5rem;">
                <span class="badge badge-green" style="font-size: 0.72rem;">Capstone Project 3</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ Intelligence Engine")

    # Check for secrets or environment variables
    env_gemini = os.environ.get("GEMINI_API_KEY", "")
    env_groq = os.environ.get("GROQ_API_KEY", "")

    provider_choice = st.selectbox(
        "Select AI Provider",
        [
            "Demo Mode (Standalone Demonstration)",
            "Google Gemini (gemini-2.5-flash)",
            "Groq (llama-3.2-vision & llama-3.3)"
        ],
        index=0,
        help="Demo Mode functions 100% offline with curated scientific presets. Gemini or Groq enable live multimodal inference."
    )

    api_key_input = ""
    if "Gemini" in provider_choice:
        provider = "Google Gemini"
        api_key_input = st.text_input(
            "Gemini API Key",
            value=env_gemini,
            type="password",
            placeholder="AIzaSy...",
            help="Get your free Gemini API key from Google AI Studio (ai.google.dev)"
        )
        if not api_key_input:
            st.caption("💡 *No key provided? App automatically runs in high-fidelity Demo Mode.*")
    elif "Groq" in provider_choice:
        provider = "Groq"
        api_key_input = st.text_input(
            "Groq API Key",
            value=env_groq,
            type="password",
            placeholder="gsk_...",
            help="Get your free Groq API key from console.groq.com"
        )
        if not api_key_input:
            st.caption("💡 *No key provided? App automatically runs in high-fidelity Demo Mode.*")
    else:
        provider = "Demo Mode"
        st.success("🟢 Standalone Demo Mode Active (Zero API Key Required).")

    # Instantiate unified AI service
    ai_service = AIService(provider=provider, api_key=api_key_input)

    st.markdown("---")
    st.markdown("### 🧑‍🔬 AI Persona & Scientific Credentials")
    st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.6); padding: 0.85rem; border-radius: 10px; border: 1px solid rgba(255,255,255,0.06); font-size: 0.82rem; color: #CBD5E1; line-height: 1.5;">
            <b>Active Persona:</b> NutriScientist & Chief Food Safety Compliance Officer.<br><br>
            <b>Compliance Frameworks:</b><br>
            • US FDA Food Code (2022 Revision)<br>
            • USDA FoodData Central Biomarkers<br>
            • HACCP Critical Control Points (CCPs)<br>
            • Mifflin-St Jeor Clinical BMR Standards
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📊 System Status")
    st.markdown(f"""
        <div style="font-size: 0.8rem; color: #94A3B8; line-height: 1.6;">
            <div><b>Status:</b> <span style="color: #34D399;">Ready & Operational</span></div>
            <div><b>Mode:</b> {provider}</div>
            <div><b>Storage:</b> In-Memory State (Stateless Cloud)</div>
            <div><b>Deployment:</b> Streamlit Cloud Optimized</div>
        </div>
    """, unsafe_allow_html=True)


# -------------------------------------------------------------
# Main Application Content
# -------------------------------------------------------------

# Hero Banner
st.markdown("""
    <div class="hero-header">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
            <div>
                <div class="hero-title">Food Verse AI — Multimodal Food Intelligence Agent</div>
                <div class="hero-subtitle">
                    Autonomous food science, precision nutrition auditing, perishable spoilage diagnostics, 
                    commercial HACCP hygiene compliance, generative recipe synthesis, and biometric meal planning.
                </div>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <span class="badge badge-green">🌿 Multimodal Vision</span>
                <span class="badge badge-cyan">🔬 Food Pathometry</span>
                <span class="badge badge-purple">🛡️ HACCP 2022</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Navigation Tabs across the 5 Core Intelligence Pillars
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🥗 Nutrition Audit (Epic 2)",
    "🔬 Spoilage Diagnostic (Epic 3)",
    "🧼 Kitchen Hygiene (Epic 4)",
    "🍳 Recipe Assistant (Epic 4)",
    "📋 Personalized Planner (Epic 5)"
])

with tab1:
    render_tab_food_recognition(ai_service)

with tab2:
    render_tab_freshness(ai_service)

with tab3:
    render_tab_kitchen_hygiene(ai_service)

with tab4:
    render_tab_recipe_assistant(ai_service)

with tab5:
    render_tab_meal_planner(ai_service)


# -------------------------------------------------------------
# Footer
# -------------------------------------------------------------
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748B; font-size: 0.85rem; padding: 1rem 0 2rem 0;">
        <b>Food Verse AI — Multimodal Food Intelligence Agent</b> • Skill Wallet Capstone Project 3<br>
        Engineered with Streamlit, Plotly, Google Gemini 2.5 Flash, Groq Vision, and FDA/HACCP Food Science Protocols.
        <br>Zero External Database Footprint • Seamless 1-Click Deployment on Streamlit Community Cloud.
    </div>
""", unsafe_allow_html=True)

