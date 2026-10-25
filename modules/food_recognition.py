"""
Food Verse AI - Module 1: Food Recognition & Nutrition Audit (Epic 2)
Multimodal dish recognition, ingredient & portion auditing, macro breakdowns, allergen alerts, and composite health scoring.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
from PIL import Image
import os


def render_macro_donut(protein_g: float, carbs_g: float, fats_g: float, fiber_g: float):
    """Render interactive Plotly donut chart for macronutrient distribution."""
    # Convert to calories for macro ratios: Protein: 4 kcal/g, Carbs: 4 kcal/g, Fat: 9 kcal/g, Fiber: 2 kcal/g
    p_cal = protein_g * 4
    c_cal = carbs_g * 4
    f_cal = fats_g * 9
    fib_cal = fiber_g * 2

    labels = ['Protein', 'Carbohydrates', 'Healthy Fats', 'Dietary Fiber']
    values = [p_cal, c_cal, f_cal, fib_cal]
    grams = [f"{protein_g:.1f}g", f"{carbs_g:.1f}g", f"{fats_g:.1f}g", f"{fiber_g:.1f}g"]
    colors = ['#10B981', '#38BDF8', '#F59E0B', '#A78BFA']

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.58,
        textinfo='label+percent',
        customdata=grams,
        hovertemplate='<b>%{label}</b><br>Calories: %{value:.0f} kcal<br>Weight: %{customdata}<br>Caloric Ratio: %{percent}<extra></extra>',
        marker=dict(colors=colors, line=dict(color='#0F172A', width=2))
    )])

    fig.update_layout(
        showlegend=False,
        margin=dict(t=10, b=10, l=10, r=10),
        height=260,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        annotations=[dict(text='<b>MACROS</b>', x=0.5, y=0.5, font_size=14, font_color='#F8FAFC', showarrow=False)]
    )
    return fig


def render_health_score_gauge(score: int, grade: str):
    """Render a semi-circular Plotly gauge for the Composite Health Score (1-100)."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'suffix': "/100", 'font': {'size': 26, 'color': '#F8FAFC'}},
        title={'text': f"<b>Health Score</b><br><span style='font-size:0.8em;color:#94A3B8'>{grade}</span>", 'font': {'size': 14, 'color': '#F8FAFC'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
            'bar': {'color': "#10B981" if score >= 80 else "#F59E0B" if score >= 60 else "#F43F5E"},
            'bgcolor': "rgba(30, 41, 59, 0.5)",
            'borderwidth': 1,
            'bordercolor': "#334155",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(244, 63, 94, 0.2)'},
                {'range': [50, 75], 'color': 'rgba(245, 158, 11, 0.2)'},
                {'range': [75, 100], 'color': 'rgba(16, 185, 129, 0.2)'}
            ],
            'threshold': {
                'line': {'color': "#38BDF8", 'width': 3},
                'thickness': 0.75,
                'value': score
            }
        }
    ))

    fig.update_layout(
        height=220,
        margin=dict(t=30, b=10, l=20, r=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "#F8FAFC", 'family': "Plus Jakarta Sans"}
    )
    return fig


def render_tab_food_recognition(ai_service):
    st.markdown("""
        <div class="glass-card" style="margin-bottom: 1.5rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h2 style="margin: 0; color: #34D399; font-size: 1.6rem;">🥗 Food Recognition & Nutrition Audit</h2>
                    <p style="margin: 0.3rem 0 0 0; color: #94A3B8; font-size: 0.95rem;">
                        Multimodal computer vision audits dish taxonomy, micro-ingredients, macronutrients, allergens, and clinical health scoring.
                    </p>
                </div>
                <span class="badge badge-green">Epic 2 Active</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_input, col_display = st.columns([1, 1.2], gap="large")

    image = None
    preset_key = None

    with col_input:
        st.markdown("### 📸 Visual Ingestion")
        input_mode = st.radio(
            "Select Input Source",
            ["Preset Demonstration Samples", "Upload Dish Image", "Live Camera Capture"],
            horizontal=True
        )

        if input_mode == "Preset Demonstration Samples":
            preset_options = {
                "Mediterranean Salmon Bowl": "salmon_bowl",
                "Royal Hyderabadi Chicken Biryani": "chicken_biryani",
                "Sourdough Avocado Toast & Eggs": "avocado_toast",
                "Crispy Teriyaki Tofu Stir-Fry": "tofu_stirfry"
            }
            selected_preset_label = st.selectbox("Choose a Curated Meal Sample", list(preset_options.keys()))
            preset_key = preset_options[selected_preset_label]

            # Load preset image
            img_filename = "salmon_bowl.jpg" if preset_key == "salmon_bowl" else "chicken_biryani.jpg"
            img_path = os.path.join("assets", "sample_images", img_filename)
            if os.path.exists(img_path):
                image = Image.open(img_path)
            else:
                image = Image.new("RGB", (400, 300), color=(30, 45, 65))

            st.image(image, caption=f"Preset Image: {selected_preset_label}", use_container_width=True)

        elif input_mode == "Upload Dish Image":
            uploaded_file = st.file_uploader("Upload a photo of your meal (JPG, PNG, WEBP)", type=["jpg", "jpeg", "png", "webp"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Meal Photo", use_container_width=True)

        elif input_mode == "Live Camera Capture":
            camera_pic = st.camera_input("Take a photo of your plate")
            if camera_pic is not None:
                image = Image.open(camera_pic)
                st.image(image, caption="Camera Snapshot", use_container_width=True)

        analyze_button = st.button("🚀 Analyze Nutrition & Macros", use_container_width=True, type="primary")

    with col_display:
        st.markdown("### 📊 Nutritional Audit Results")

        # Session state persistence for results
        if "nutrition_result" not in st.session_state or analyze_button:
            if analyze_button:
                if image is None and preset_key is None:
                    st.warning("Please upload an image or choose a preset meal sample to audit.")
                    return
                with st.spinner("Auditing meal with Multimodal Vision & NutriScientist Engine..."):
                    result, is_fallback = ai_service.analyze_nutrition(image=image, preset_key=preset_key)
                    st.session_state["nutrition_result"] = result
                    st.session_state["nutrition_is_fallback"] = is_fallback
            else:
                # Default initial demo
                result, is_fallback = ai_service.analyze_nutrition(image=image, preset_key="salmon_bowl")
                st.session_state["nutrition_result"] = result
                st.session_state["nutrition_is_fallback"] = is_fallback

        result = st.session_state["nutrition_result"]
        is_fallback = st.session_state.get("nutrition_is_fallback", False)

        if is_fallback and ai_service.provider != "Demo Mode":
            st.info("ℹ️ Using FoodVerse High-Precision Demonstration Data (Demo / Fallback mode active).")

        # Dish Title & Badges
        st.markdown(f"""
            <div class="glass-card" style="padding: 1.25rem;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h3 style="margin: 0; color: #F8FAFC; font-size: 1.4rem;">{result.get('dish_name', 'Analyzed Dish')}</h3>
                        <p style="margin: 0.2rem 0; color: #94A3B8; font-size: 0.9rem;">
                            <b>Cuisine:</b> {result.get('cuisine', 'Global')} &nbsp;•&nbsp; 
                            <b>Portion:</b> {result.get('serving_size', '1 Serving')}
                        </p>
                    </div>
                    <span class="badge badge-cyan">{int(result.get('confidence', 0.95) * 100)}% Confidence</span>
                </div>
                <div style="margin-top: 0.75rem; display: flex; flex-wrap: wrap; gap: 0.5rem;">
                    {''.join([f'<span class="badge badge-purple">{tag}</span>' for tag in result.get('dietary_tags', [])])}
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Macro Tiles
        nutr = result.get("nutrition", {})
        cal = nutr.get("calories", 0)
        prot = nutr.get("protein", 0)
        carbs = nutr.get("carbohydrates", 0)
        fats = nutr.get("fats", 0)
        fiber = nutr.get("fiber", 0)

        m1, m2, m3, m4, m5 = st.columns(5)
        m1.markdown(f"""<div class="metric-box"><div class="metric-lbl">Energy</div><div class="metric-val" style="color: #38BDF8;">{cal}</div><div class="metric-lbl">kcal</div></div>""", unsafe_allow_html=True)
        m2.markdown(f"""<div class="metric-box"><div class="metric-lbl">Protein</div><div class="metric-val" style="color: #34D399;">{prot}g</div><div class="metric-lbl">{int((prot*4/max(cal,1))*100)}% cal</div></div>""", unsafe_allow_html=True)
        m3.markdown(f"""<div class="metric-box"><div class="metric-lbl">Carbs</div><div class="metric-val" style="color: #38BDF8;">{carbs}g</div><div class="metric-lbl">{int((carbs*4/max(cal,1))*100)}% cal</div></div>""", unsafe_allow_html=True)
        m4.markdown(f"""<div class="metric-box"><div class="metric-lbl">Fats</div><div class="metric-val" style="color: #FBBF24;">{fats}g</div><div class="metric-lbl">{int((fats*9/max(cal,1))*100)}% cal</div></div>""", unsafe_allow_html=True)
        m5.markdown(f"""<div class="metric-box"><div class="metric-lbl">Fiber</div><div class="metric-val" style="color: #C084FC;">{fiber}g</div><div class="metric-lbl">RDA {int((fiber/28)*100)}%</div></div>""", unsafe_allow_html=True)

        # Charts Section: Macro Donut & Health Score Gauge
        c_chart1, c_chart2 = st.columns([1.1, 0.9])
        with c_chart1:
            donut_fig = render_macro_donut(prot, carbs, fats, fiber)
            st.plotly_chart(donut_fig, use_container_width=True, config={'displayModeBar': False})
        with c_chart2:
            h_score = result.get("health_score", 85)
            h_grade = result.get("health_score_grade", "A")
            gauge_fig = render_health_score_gauge(h_score, h_grade)
            st.plotly_chart(gauge_fig, use_container_width=True, config={'displayModeBar': False})

    # Bottom Full-Width Deep Breakdown: Ingredients, Allergens, Science Note
    st.markdown("---")
    st.markdown("### 🔬 In-Depth Biochemical & Ingredient Audit")

    col_ing, col_allergen = st.columns([1.2, 1], gap="medium")

    with col_ing:
        st.markdown("#### 🥗 Itemized Ingredient Breakdown")
        ingredients = result.get("ingredients", [])
        if ingredients:
            ing_df = pd.DataFrame(ingredients)
            # Rename columns nicely
            renamed_df = ing_df.rename(columns={
                "name": "Component",
                "amount": "Est. Portion",
                "calories": "Calories (kcal)",
                "protein": "Protein (g)"
            })
            st.dataframe(renamed_df, use_container_width=True, hide_index=True)
        else:
            st.write("No itemized ingredients found.")

        # Micronutrient highlights
        micros = result.get("micronutrients", [])
        if micros:
            st.markdown("#### ⚡ Micronutrient & Mineral Density")
            micro_cols = st.columns(len(micros))
            for i, m in enumerate(micros):
                with micro_cols[i % len(micro_cols)]:
                    st.markdown(f"""
                        <div style="background: rgba(15, 23, 42, 0.6); padding: 0.6rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.06); text-align: center;">
                            <div style="font-size: 0.72rem; color: #94A3B8;">{m.get('nutrient')}</div>
                            <div style="font-size: 1.1rem; font-weight: 700; color: #38BDF8;">{m.get('amount')}</div>
                            <div style="font-size: 0.7rem; color: #34D399;">{m.get('dv_percent', 0)}% Daily Value</div>
                        </div>
                    """, unsafe_allow_html=True)

    with col_allergen:
        st.markdown("#### ⚠️ Allergen & Food Sensitivity Alerts")
        allergens = result.get("allergens", [])
        for a in allergens:
            sev = a.get("severity", "Trace")
            badge_class = "badge-red" if sev == "Critical" else "badge-amber" if sev == "Moderate" else "badge-green"
            st.markdown(f"""
                <div style="margin-bottom: 0.6rem; padding: 0.8rem; border-radius: 10px; background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255,255,255,0.05);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
                        <span style="font-weight: 700; color: #F8FAFC;">{a.get('name')}</span>
                        <span class="badge {badge_class}">{sev}</span>
                    </div>
                    <div style="font-size: 0.82rem; color: #CBD5E1;">{a.get('description')}</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("#### 🧠 Food Science Audit & Clinical Summary")
        summary_text = result.get("science_audit_summary", "Audit complete.")
        st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.08); border-left: 3px solid #10B981; padding: 0.9rem; border-radius: 0 10px 10px 0; font-size: 0.9rem; line-height: 1.5; color: #E2E8F0;">
                {summary_text}
            </div>
        """, unsafe_allow_html=True)

        # Export Report Button
        report_json = json.dumps(result, indent=2)
        st.download_button(
            label="📥 Download Official Nutritional Audit Report (JSON)",
            data=report_json,
            file_name=f"FoodVerse_Nutrition_Audit_{result.get('dish_name', 'Dish').replace(' ', '_')}.json",
            mime="application/json",
            use_container_width=True
        )

