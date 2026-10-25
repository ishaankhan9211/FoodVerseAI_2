"""
Food Verse AI - Module 2: Food Freshness & Spoilage Diagnostic (Epic 3)
Multimodal perishable food diagnosis: surface texture inspection, enzymatic browning, wrinkling, fungal mold detection, and shelf-life prediction.
"""

import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import os
import json


def render_freshness_gauge(score: int, stage: str):
    """Render a semi-circular gauge for freshness score (0 - 100)."""
    color = "#10B981" if stage == "Fresh" else "#F59E0B" if stage == "Moderately Fresh" else "#F43F5E"
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'suffix': "%", 'font': {'size': 26, 'color': '#F8FAFC'}},
        title={'text': f"<b>Freshness Index</b><br><span style='font-size:0.85em;color:#94A3B8'>{stage}</span>", 'font': {'size': 14, 'color': '#F8FAFC'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
            'bar': {'color': color},
            'bgcolor': "rgba(30, 41, 59, 0.5)",
            'borderwidth': 1,
            'bordercolor': "#334155",
            'steps': [
                {'range': [0, 40], 'color': 'rgba(244, 63, 94, 0.25)'},
                {'range': [40, 75], 'color': 'rgba(245, 158, 11, 0.25)'},
                {'range': [75, 100], 'color': 'rgba(16, 185, 129, 0.25)'}
            ]
        }
    ))

    fig.update_layout(
        height=210,
        margin=dict(t=30, b=10, l=20, r=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "#F8FAFC", 'family': "Plus Jakarta Sans"}
    )
    return fig


def render_tab_freshness(ai_service):
    st.markdown("""
        <div class="glass-card" style="margin-bottom: 1.5rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h2 style="margin: 0; color: #34D399; font-size: 1.6rem;">🔬 Food Freshness & Spoilage Diagnostic</h2>
                    <p style="margin: 0.3rem 0 0 0; color: #94A3B8; font-size: 0.95rem;">
                        Computer vision diagnostics inspect cellular turgor, surface necrosis, wrinkling, and fungal mycelium on perishable produce, seafood, meats, and dairy.
                    </p>
                </div>
                <span class="badge badge-amber">Epic 3 Active</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_input, col_display = st.columns([1, 1.2], gap="large")

    image = None
    preset_key = None

    with col_input:
        st.markdown("### 📸 Perishable Ingestion")
        input_mode = st.radio(
            "Select Diagnostic Input",
            ["Preset Perishable Samples", "Upload Perishable Photo", "Live Camera Inspection"],
            horizontal=True
        )

        if input_mode == "Preset Perishable Samples":
            preset_options = {
                "Fresh Organic Strawberries (Optimal)": "fresh_strawberry",
                "Moldy Decomposed Strawberries (Pathogenic)": "spoiled_strawberry",
                "Atlantic Salmon Fillet (Marginal)": "moderate_salmon",
                "Ripe Hass Avocado (Fresh)": "fresh_avocado"
            }
            selected_preset_label = st.selectbox("Choose a Biological Sample Case", list(preset_options.keys()))
            preset_key = preset_options[selected_preset_label]

            # Match sample graphic
            filename_map = {
                "fresh_strawberry": "fresh_strawberry.jpg",
                "spoiled_strawberry": "spoiled_strawberry.jpg",
                "moderate_salmon": "salmon_bowl.jpg",
                "fresh_avocado": "fresh_strawberry.jpg"
            }
            img_path = os.path.join("assets", "sample_images", filename_map.get(preset_key, "fresh_strawberry.jpg"))
            if os.path.exists(img_path):
                image = Image.open(img_path)
            else:
                image = Image.new("RGB", (400, 300), color=(30, 45, 65))

            st.image(image, caption=f"Selected Case: {selected_preset_label}", use_container_width=True)

        elif input_mode == "Upload Perishable Photo":
            uploaded_file = st.file_uploader("Upload raw item photo (Fruits, Vegetables, Meats, Dairy)", type=["jpg", "jpeg", "png", "webp"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Perishable Photo", use_container_width=True)

        elif input_mode == "Live Camera Inspection":
            camera_pic = st.camera_input("Take a photo of your perishable item")
            if camera_pic is not None:
                image = Image.open(camera_pic)
                st.image(image, caption="Live Inspection Photo", use_container_width=True)

        diagnose_button = st.button("🧪 Run Spoilage Diagnostic", use_container_width=True, type="primary")

    with col_display:
        st.markdown("### 📋 Pathology & Freshness Diagnostic Report")

        if "freshness_result" not in st.session_state or diagnose_button:
            if diagnose_button:
                if image is None and preset_key is None:
                    st.warning("Please upload an image or select a sample case to diagnose.")
                    return
                with st.spinner("Analyzing surface micro-structures, oxidation, and spore colonies..."):
                    result, is_fallback = ai_service.diagnose_freshness(image=image, preset_key=preset_key)
                    st.session_state["freshness_result"] = result
                    st.session_state["freshness_is_fallback"] = is_fallback
            else:
                # Default initial demo
                result, is_fallback = ai_service.diagnose_freshness(image=image, preset_key="fresh_strawberry")
                st.session_state["freshness_result"] = result
                st.session_state["freshness_is_fallback"] = is_fallback

        result = st.session_state["freshness_result"]
        is_fallback = st.session_state.get("freshness_is_fallback", False)

        if is_fallback and ai_service.provider != "Demo Mode":
            st.info("ℹ️ Using FoodVerse High-Precision Diagnostic Fallback Data.")

        # Freshness Stage & Action Classification
        stage = result.get("freshness_stage", "Fresh")
        action_badge = result.get("action_badge", "Safe to consume")
        action_type = result.get("action_type", "safe")
        score = result.get("freshness_score", 90)

        # Style based on action_type
        if action_type == "danger" or stage == "Spoiled":
            badge_color = "badge-red"
            banner_bg = "rgba(244, 63, 94, 0.12)"
            banner_border = "#F43F5E"
            action_icon = "🛑 DISCARD IMMEDIATELY"
        elif action_type == "warning" or stage == "Moderately Fresh":
            badge_color = "badge-amber"
            banner_bg = "rgba(245, 158, 11, 0.12)"
            banner_border = "#F59E0B"
            action_icon = "⚠️ CONSUME WITHIN 24 HOURS"
        else:
            badge_color = "badge-green"
            banner_bg = "rgba(16, 185, 129, 0.12)"
            banner_border = "#10B981"
            action_icon = "✅ SAFE TO CONSUME"

        st.markdown(f"""
            <div style="background: {banner_bg}; border: 2px solid {banner_border}; border-radius: 14px; padding: 1.2rem; margin-bottom: 1.25rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span class="badge {badge_color}" style="font-size: 0.95rem; padding: 0.4rem 0.9rem;">{action_icon}</span>
                        <h3 style="margin: 0.6rem 0 0.2rem 0; color: #F8FAFC;">{result.get('item_name', 'Item')}</h3>
                        <p style="margin: 0; color: #CBD5E1; font-size: 0.88rem;"><b>Classification:</b> {result.get('category', 'Produce')} &nbsp;•&nbsp; <b>Remaining Shelf Life:</b> {result.get('shelf_life_remaining', 'N/A')}</p>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge {badge_color}">{stage}</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Gauge & Advice Side-by-side
        cg1, cg2 = st.columns([1, 1.4])
        with cg1:
            gauge_fig = render_freshness_gauge(score, stage)
            st.plotly_chart(gauge_fig, use_container_width=True, config={'displayModeBar': False})
        with cg2:
            st.markdown("#### 🛡️ Food Safety Directive")
            advice_text = result.get("food_safety_advice", "Follow standard food safety guidelines.")
            st.markdown(f"""
                <div style="background: rgba(15, 23, 42, 0.6); border-radius: 10px; border: 1px solid rgba(255,255,255,0.06); padding: 1rem; font-size: 0.92rem; line-height: 1.5; color: #E2E8F0;">
                    {advice_text}
                </div>
            """, unsafe_allow_html=True)

    # Bottom Inspection Breakdown
    st.markdown("---")
    st.markdown("### 🔬 Multimodal Surface & Pathology Inspection Criteria")

    insp = result.get("inspection", {})
    i1, i2 = st.columns(2)
    with i1:
        st.markdown(f"""
            <div class="glass-card" style="margin-bottom: 1rem; padding: 1rem;">
                <h4 style="margin: 0 0 0.4rem 0; color: #38BDF8; font-size: 1rem;">🔍 1. Surface Texture & Osmotic Turgor</h4>
                <p style="margin: 0; color: #CBD5E1; font-size: 0.88rem; line-height: 1.45;">
                    {insp.get('surface_texture', 'Surface is intact with normal firmness.')}
                </p>
            </div>
            <div class="glass-card" style="margin-bottom: 1rem; padding: 1rem;">
                <h4 style="margin: 0 0 0.4rem 0; color: #FBBF24; font-size: 1rem;">🍂 2. Discoloration & Enzymatic Oxidation</h4>
                <p style="margin: 0; color: #CBD5E1; font-size: 0.88rem; line-height: 1.45;">
                    {insp.get('discoloration', 'Zero pigment degradation observed.')}
                </p>
            </div>
        """, unsafe_allow_html=True)

    with i2:
        st.markdown(f"""
            <div class="glass-card" style="margin-bottom: 1rem; padding: 1rem;">
                <h4 style="margin: 0 0 0.4rem 0; color: #C084FC; font-size: 1rem;">⚡ 3. Wrinkling & Epidermal Shrinkage</h4>
                <p style="margin: 0; color: #CBD5E1; font-size: 0.88rem; line-height: 1.45;">
                    {insp.get('wrinkling', 'Taut epidermis without creasing.')}
                </p>
            </div>
            <div class="glass-card" style="margin-bottom: 1rem; padding: 1rem;">
                <h4 style="margin: 0 0 0.4rem 0; color: #FB7185; font-size: 1rem;">🧫 4. Mold, Mycelium & Microbial Colonization</h4>
                <p style="margin: 0; color: #CBD5E1; font-size: 0.88rem; line-height: 1.45;">
                    {insp.get('mold_status', 'No spores detected.')}
                </p>
            </div>
        """, unsafe_allow_html=True)

    # Preservation Protocol
    st.markdown("#### 🧊 Post-Harvest Preservation & Scientific Storage Protocols")
    tips = result.get("preservation_tips", [])
    for idx, tip in enumerate(tips):
        st.markdown(f"""
            <div class="step-card">
                <div class="step-num">{idx + 1}</div>
                <div style="color: #E2E8F0; font-size: 0.92rem; align-self: center;">{tip}</div>
            </div>
        """, unsafe_allow_html=True)

    # Export Diagnostic Summary
    diag_export = json.dumps(result, indent=2)
    st.download_button(
        label="📥 Export Spoilage Diagnostic Certificate (JSON)",
        data=diag_export,
        file_name=f"FoodVerse_Diagnostic_{result.get('item_name', 'Item').replace(' ', '_')}.json",
        mime="application/json"
    )

