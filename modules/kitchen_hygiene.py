"""
Food Verse AI - Module 3: Kitchen Hygiene & Food Safety Compliance (Epic 4)
Commercial and domestic kitchen visual inspection: hair containment, PPE glove adherence, sanitization state, cross-contamination, and itemized HACCP/FDA violation auditing.
"""

import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import os
import json


def render_compliance_gauge(score: int, grade: str):
    """Render a semi-circular Plotly gauge for Kitchen Compliance Score (0-100%)."""
    color = "#10B981" if score >= 85 else "#F59E0B" if score >= 70 else "#F43F5E"
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'suffix': "%", 'font': {'size': 26, 'color': '#F8FAFC'}},
        title={'text': f"<b>Compliance Index</b><br><span style='font-size:0.85em;color:#94A3B8'>{grade.split('(')[0]}</span>", 'font': {'size': 14, 'color': '#F8FAFC'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
            'bar': {'color': color},
            'bgcolor': "rgba(30, 41, 59, 0.5)",
            'borderwidth': 1,
            'bordercolor': "#334155",
            'steps': [
                {'range': [0, 60], 'color': 'rgba(244, 63, 94, 0.25)'},
                {'range': [60, 85], 'color': 'rgba(245, 158, 11, 0.25)'},
                {'range': [85, 100], 'color': 'rgba(16, 185, 129, 0.25)'}
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


def render_tab_kitchen_hygiene(ai_service):
    st.markdown("""
        <div class="glass-card" style="margin-bottom: 1.5rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h2 style="margin: 0; color: #34D399; font-size: 1.6rem;">🧼 Kitchen Hygiene & Food Safety Compliance</h2>
                    <p style="margin: 0.3rem 0 0 0; color: #94A3B8; font-size: 0.95rem;">
                        Real-time AI surveillance monitors commercial galleys, detecting hairnet compliance, glove protocols, sanitization state, and cross-contamination hazards.
                    </p>
                </div>
                <span class="badge badge-purple">Epic 4 Active</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_input, col_display = st.columns([1, 1.2], gap="large")

    image = None
    preset_key = None

    with col_input:
        st.markdown("### 🎥 Kitchen Visual Feed")
        input_mode = st.radio(
            "Select Kitchen Inspection Mode",
            ["Preset Demonstration Galleys", "Upload Kitchen Photo / Frame", "Live Camera Snapshot"],
            horizontal=True
        )

        if input_mode == "Preset Demonstration Galleys":
            preset_options = {
                "Executive Station A (Fully Compliant Commercial Galley)": "compliant_kitchen",
                "Line Station B (High-Risk Cross-Contamination Hazards)": "violation_kitchen"
            }
            selected_preset_label = st.selectbox("Select Station Scenario", list(preset_options.keys()))
            preset_key = preset_options[selected_preset_label]

            filename_map = {
                "compliant_kitchen": "compliant_kitchen.jpg",
                "violation_kitchen": "violation_kitchen.jpg"
            }
            img_path = os.path.join("assets", "sample_images", filename_map.get(preset_key, "compliant_kitchen.jpg"))
            if os.path.exists(img_path):
                image = Image.open(img_path)
            else:
                image = Image.new("RGB", (400, 300), color=(30, 45, 65))

            st.image(image, caption=f"Station Scenario: {selected_preset_label}", use_container_width=True)

        elif input_mode == "Upload Kitchen Photo / Frame":
            uploaded_file = st.file_uploader("Upload commercial kitchen photo or video snapshot", type=["jpg", "jpeg", "png", "webp"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Kitchen Snapshot", use_container_width=True)

        elif input_mode == "Live Camera Snapshot":
            camera_pic = st.camera_input("Capture live kitchen workspace")
            if camera_pic is not None:
                image = Image.open(camera_pic)
                st.image(image, caption="Live Workspace Snapshot", use_container_width=True)

        audit_button = st.button("🛡️ Run HACCP Hygiene Inspection", use_container_width=True, type="primary")

    with col_display:
        st.markdown("### 📊 Compliance Scorecard & Audit")

        if "hygiene_result" not in st.session_state or audit_button:
            if audit_button:
                if image is None and preset_key is None:
                    st.warning("Please upload a kitchen image or select a preset galley scenario.")
                    return
                with st.spinner("Inspecting PPE compliance, cross-contamination, and sanitation barriers..."):
                    result, is_fallback = ai_service.audit_kitchen_hygiene(image=image, preset_key=preset_key)
                    st.session_state["hygiene_result"] = result
                    st.session_state["hygiene_is_fallback"] = is_fallback
            else:
                result, is_fallback = ai_service.audit_kitchen_hygiene(image=image, preset_key="compliant_kitchen")
                st.session_state["hygiene_result"] = result
                st.session_state["hygiene_is_fallback"] = is_fallback

        result = st.session_state["hygiene_result"]
        is_fallback = st.session_state.get("hygiene_is_fallback", False)

        if is_fallback and ai_service.provider != "Demo Mode":
            st.info("ℹ️ Using FoodVerse High-Precision HACCP Demonstration Data.")

        score = result.get("overall_score", 90)
        grade = result.get("compliance_grade", "Grade A")
        grade_type = result.get("grade_type", "safe")

        # Color-coded status banner
        if score >= 85:
            banner_border = "#10B981"
            banner_bg = "rgba(16, 185, 129, 0.12)"
            badge_class = "badge-green"
            status_text = "HACCP & FDA CERTIFIED COMPLIANT"
        elif score >= 70:
            banner_border = "#F59E0B"
            banner_bg = "rgba(245, 158, 11, 0.12)"
            badge_class = "badge-amber"
            status_text = "CONDITIONAL COMPLIANCE - DEFICIENCIES FOUND"
        else:
            banner_border = "#F43F5E"
            banner_bg = "rgba(244, 63, 94, 0.12)"
            badge_class = "badge-red"
            status_text = "CRITICAL HAZARD - CLOSURE WARNING"

        st.markdown(f"""
            <div style="background: {banner_bg}; border: 2px solid {banner_border}; border-radius: 14px; padding: 1.25rem; margin-bottom: 1.25rem;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <span class="badge {badge_class}" style="font-size: 0.9rem; padding: 0.35rem 0.8rem;">{status_text}</span>
                        <h3 style="margin: 0.6rem 0 0.2rem 0; color: #F8FAFC;">{result.get('scenario_name', 'Kitchen Galley')}</h3>
                        <p style="margin: 0; color: #CBD5E1; font-size: 0.88rem;"><b>Standard:</b> US FDA Food Code 2022 & HACCP Codex Alimentarius</p>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge {badge_class}">{grade}</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        cg1, cg2 = st.columns([1, 1.4])
        with cg1:
            gauge_fig = render_compliance_gauge(score, grade)
            st.plotly_chart(gauge_fig, use_container_width=True, config={'displayModeBar': False})
        with cg2:
            st.markdown("#### 📋 Executive Inspector Summary")
            summary_text = result.get("haccp_summary", "Inspection completed.")
            st.markdown(f"""
                <div style="background: rgba(15, 23, 42, 0.6); border-radius: 10px; border: 1px solid rgba(255,255,255,0.06); padding: 1rem; font-size: 0.9rem; line-height: 1.5; color: #E2E8F0;">
                    {summary_text}
                </div>
            """, unsafe_allow_html=True)

    # 4 Core Hygiene Pillars
    st.markdown("---")
    st.markdown("### 🔍 Four Pillars of Food Safety Inspection")

    indicators = result.get("indicators", {})
    p1, p2, p3, p4 = st.columns(4)

    with p1:
        hair = indicators.get("hair_containment", {})
        status_txt = hair.get("status", "Compliant")
        is_ok = "Compliant" in status_txt
        st.markdown(f"""
            <div class="metric-box" style="text-align: left;">
                <div style="font-size: 1.2rem; margin-bottom: 0.2rem;">🧑‍🍳 Hair Containment</div>
                <span class="badge {'badge-green' if is_ok else 'badge-red'}">{status_txt}</span>
                <p style="font-size: 0.8rem; color: #94A3B8; margin-top: 0.5rem;">{hair.get('details', '')}</p>
            </div>
        """, unsafe_allow_html=True)

    with p2:
        glove = indicators.get("glove_usage", {})
        status_txt = glove.get("status", "Compliant")
        is_ok = "Compliant" in status_txt
        st.markdown(f"""
            <div class="metric-box" style="text-align: left;">
                <div style="font-size: 1.2rem; margin-bottom: 0.2rem;">🧤 Glove Usage & PPE</div>
                <span class="badge {'badge-green' if is_ok else 'badge-red'}">{status_txt}</span>
                <p style="font-size: 0.8rem; color: #94A3B8; margin-top: 0.5rem;">{glove.get('details', '')}</p>
            </div>
        """, unsafe_allow_html=True)

    with p3:
        san = indicators.get("workstation_sanitization", {})
        status_txt = san.get("status", "Compliant")
        is_ok = "Compliant" in status_txt
        st.markdown(f"""
            <div class="metric-box" style="text-align: left;">
                <div style="font-size: 1.2rem; margin-bottom: 0.2rem;">🧼 Surface Sanitization</div>
                <span class="badge {'badge-green' if is_ok else 'badge-red'}">{status_txt}</span>
                <p style="font-size: 0.8rem; color: #94A3B8; margin-top: 0.5rem;">{san.get('details', '')}</p>
            </div>
        """, unsafe_allow_html=True)

    with p4:
        cross = indicators.get("cross_contamination_hazard", {})
        status_txt = cross.get("status", "Zero Hazard")
        is_ok = "Zero" in status_txt
        st.markdown(f"""
            <div class="metric-box" style="text-align: left;">
                <div style="font-size: 1.2rem; margin-bottom: 0.2rem;">⚡ Cross-Contamination</div>
                <span class="badge {'badge-green' if is_ok else 'badge-red'}">{status_txt}</span>
                <p style="font-size: 0.8rem; color: #94A3B8; margin-top: 0.5rem;">{cross.get('details', '')}</p>
            </div>
        """, unsafe_allow_html=True)

    # Itemized Violation Logs
    st.markdown("---")
    st.markdown("### 📝 Itemized Violation & Corrective Action Log")

    violations = result.get("violations", [])
    if not violations or len(violations) == 0:
        st.markdown("""
            <div class="violation-card-safe">
                <b style="color: #34D399;">🌟 No Critical Food Safety Violations Detected!</b><br>
                Station meets all FDA 2022 hygiene standards. Continue regular 2-hour sanitization rotations.
            </div>
        """, unsafe_allow_html=True)
    else:
        for v in violations:
            sev = v.get("severity", "Major")
            card_class = "violation-card" if "Critical" in sev or "Major" in sev else "violation-card-safe"
            badge_class = "badge-red" if "Critical" in sev else "badge-amber" if "Major" in sev else "badge-cyan"
            st.markdown(f"""
                <div class="{card_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
                        <span style="font-weight: 700; color: #F8FAFC;">[{v.get('id', 'VIOL')}] {v.get('standard', 'FDA Code')}</span>
                        <span class="badge {badge_class}">{sev}</span>
                    </div>
                    <div style="font-size: 0.9rem; color: #E2E8F0; margin-bottom: 0.4rem;">
                        <b>Observation:</b> {v.get('finding')}
                    </div>
                    <div style="font-size: 0.85rem; color: #38BDF8;">
                        <b>⚡ Required Corrective Action:</b> {v.get('corrective_action')}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Export Certificate
    audit_json = json.dumps(result, indent=2)
    st.download_button(
        label="📥 Download Official HACCP Food Safety Audit Log (JSON)",
        data=audit_json,
        file_name=f"FoodVerse_HACCP_Audit_{result.get('scenario_name', 'Galley').replace(' ', '_')}.json",
        mime="application/json"
    )

