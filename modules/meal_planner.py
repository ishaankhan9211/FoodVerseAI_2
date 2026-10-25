"""
Food Verse AI - Module 5: Personalized Meal Planner (Epic 5)
Clinical BMR / TDEE computation (Mifflin-St Jeor), macronutrient target derivation, 7-day adaptive meal scheduling, and automated grocery shopping checklist.
"""

import streamlit as st
import json
import pandas as pd


def calculate_bmr_tdee(weight_kg: float, height_cm: float, age: int, gender: str, activity_level: str, goal: str):
    """
    Compute BMR via Mifflin-St Jeor Equation:
    Men: BMR = (10 × weight) + (6.25 × height) - (5 × age) + 5
    Women: BMR = (10 × weight) + (6.25 × height) - (5 × age) - 161
    """
    if gender.lower() == "male":
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    # Activity multiplier
    activity_multipliers = {
        "Sedentary (Desk job, little exercise)": 1.2,
        "Lightly Active (1-3 days/week)": 1.375,
        "Moderately Active (3-5 days/week)": 1.55,
        "Very Active (6-7 days intense)": 1.725,
        "Extra Active (Endurance / Physical job)": 1.9
    }
    multiplier = activity_multipliers.get(activity_level, 1.55)
    tdee = bmr * multiplier

    # Adjust target based on fitness goal
    goal_adjustments = {
        "Aggressive Fat Loss (-500 kcal)": -500,
        "Moderate Fat Loss (-300 kcal)": -300,
        "Maintenance (Weight Stability)": 0,
        "Clean Muscle Gain (+300 kcal)": 300,
        "Athletic High Performance (+500 kcal)": 500
    }
    adjustment = goal_adjustments.get(goal, 0)
    target_calories = max(1200, int(tdee + adjustment))

    # Protein target in grams:
    # 1.6 to 2.2g per kg for fat loss / muscle gain
    if "Fat Loss" in goal or "Muscle Gain" in goal:
        target_protein = int(weight_kg * 2.0)
    else:
        target_protein = int(weight_kg * 1.6)

    # Fats: ~25-30% of total calories (9 kcal/g)
    target_fat = int((target_calories * 0.28) / 9)
    # Remaining calories to Carbs (4 kcal/g)
    rem_cal = target_calories - (target_protein * 4) - (target_fat * 9)
    target_carbs = max(50, int(rem_cal / 4))

    return {
        "bmr": int(bmr),
        "tdee": int(tdee),
        "target_calories": target_calories,
        "target_protein": target_protein,
        "target_carbs": target_carbs,
        "target_fat": target_fat
    }


def render_tab_meal_planner(ai_service):
    st.markdown("""
        <div class="glass-card" style="margin-bottom: 1.5rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h2 style="margin: 0; color: #34D399; font-size: 1.6rem;">📋 Personalized Meal Planner & Biometrics</h2>
                    <p style="margin: 0.3rem 0 0 0; color: #94A3B8; font-size: 0.95rem;">
                        Scientific metabolic targets computed using the Mifflin-St Jeor equation paired with an adaptive 7-day meal plan and consolidated grocery checklist.
                    </p>
                </div>
                <span class="badge badge-green">Epic 5 Active</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_profile, col_plan = st.columns([1, 1.3], gap="large")

    with col_profile:
        st.markdown("### 👤 Anthropometrics & Goals")

        c1, c2 = st.columns(2)
        with c1:
            age = st.number_input("Age (years)", min_value=16, max_value=99, value=28)
            weight_kg = st.number_input("Weight (kg)", min_value=35.0, max_value=250.0, value=70.0, step=0.5)
        with c2:
            gender = st.selectbox("Biological Sex", ["Male", "Female"])
            height_cm = st.number_input("Height (cm)", min_value=120.0, max_value=230.0, value=175.0, step=1.0)

        activity_level = st.selectbox(
            "Physical Activity Level",
            [
                "Sedentary (Desk job, little exercise)",
                "Lightly Active (1-3 days/week)",
                "Moderately Active (3-5 days/week)",
                "Very Active (6-7 days intense)",
                "Extra Active (Endurance / Physical job)"
            ],
            index=2
        )

        c3, c4 = st.columns(2)
        with c3:
            fitness_goal = st.selectbox(
                "Primary Fitness Goal",
                [
                    "Moderate Fat Loss (-300 kcal)",
                    "Aggressive Fat Loss (-500 kcal)",
                    "Maintenance (Weight Stability)",
                    "Clean Muscle Gain (+300 kcal)",
                    "Athletic High Performance (+500 kcal)"
                ],
                index=0
            )
        with c4:
            dietary_style = st.selectbox(
                "Dietary Pattern",
                [
                    "Balanced / Omnivore",
                    "High Protein Mediterranean",
                    "Ketogenic (Low Carb)",
                    "Vegetarian",
                    "100% Plant-Based (Vegan)",
                    "Diabetic-Friendly (Low Glycemic)"
                ],
                index=1
            )

        allergies = st.text_input("Allergens / Ingredients to Exclude", placeholder="e.g. Shellfish, Peanuts, Dairy, Gluten")

        # Compute BMR & TDEE in real time
        metrics = calculate_bmr_tdee(weight_kg, height_cm, age, gender, activity_level, fitness_goal)

        st.markdown("#### ⚡ Clinical Caloric & Macro Targets")
        b1, b2, b3 = st.columns(3)
        b1.markdown(f"""<div class="metric-box"><div class="metric-lbl">BMR</div><div class="metric-val" style="font-size: 1.4rem; color: #94A3B8;">{metrics['bmr']}</div><div class="metric-lbl">kcal/day</div></div>""", unsafe_allow_html=True)
        b2.markdown(f"""<div class="metric-box"><div class="metric-lbl">TDEE</div><div class="metric-val" style="font-size: 1.4rem; color: #38BDF8;">{metrics['tdee']}</div><div class="metric-lbl">kcal/day</div></div>""", unsafe_allow_html=True)
        b3.markdown(f"""<div class="metric-box"><div class="metric-lbl">Target</div><div class="metric-val" style="font-size: 1.4rem; color: #34D399;">{metrics['target_calories']}</div><div class="metric-lbl">kcal/day</div></div>""", unsafe_allow_html=True)

        st.markdown(f"""
            <div style="margin: 0.8rem 0; padding: 0.8rem; background: rgba(30, 41, 59, 0.4); border-radius: 10px; border: 1px solid rgba(255,255,255,0.06);">
                <div style="display: flex; justify-content: space-around; text-align: center;">
                    <div><b style="color: #34D399;">{metrics['target_protein']}g</b><br><span style="font-size: 0.75rem; color: #94A3B8;">Protein (4 kcal/g)</span></div>
                    <div><b style="color: #38BDF8;">{metrics['target_carbs']}g</b><br><span style="font-size: 0.75rem; color: #94A3B8;">Carbs (4 kcal/g)</span></div>
                    <div><b style="color: #FBBF24;">{metrics['target_fat']}g</b><br><span style="font-size: 0.75rem; color: #94A3B8;">Fats (9 kcal/g)</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        plan_button = st.button("🗓️ Generate Adaptive 7-Day Plan", use_container_width=True, type="primary")

    with col_plan:
        st.markdown("### 🗓️ Adaptive 7-Day Meal Schedule")

        profile_payload = {
            "age": age,
            "gender": gender,
            "weight_kg": weight_kg,
            "height_cm": height_cm,
            "activity_level": activity_level,
            "dietary_constraint": dietary_style,
            "target_calories": metrics["target_calories"],
            "target_protein_g": metrics["target_protein"],
            "fitness_goal": fitness_goal,
            "allergies": allergies if allergies else "None"
        }

        if "meal_plan_result" not in st.session_state or plan_button:
            if plan_button:
                with st.spinner("Synthesizing 7-day periodized nutrition plan..."):
                    plan_data, is_fallback = ai_service.generate_meal_plan(profile_payload)
                    st.session_state["meal_plan_result"] = plan_data
                    st.session_state["meal_plan_is_fallback"] = is_fallback
            else:
                plan_data, is_fallback = ai_service.generate_meal_plan(profile_payload)
                st.session_state["meal_plan_result"] = plan_data
                st.session_state["meal_plan_is_fallback"] = is_fallback

        plan_data = st.session_state["meal_plan_result"]
        is_fallback = st.session_state.get("meal_plan_is_fallback", False)

        if is_fallback and ai_service.provider != "Demo Mode":
            st.info("ℹ️ Using FoodVerse High-Precision Clinical Demonstration Meal Schedule.")

        # Display Days as Tabs
        days_list = plan_data.get("days", [])
        if days_list:
            day_names = [d.get("day", f"Day {i+1}") for i, d in enumerate(days_list)]
            selected_day_tab = st.tabs(day_names)

            for idx, tab in enumerate(selected_day_tab):
                day_info = days_list[idx]
                with tab:
                    st.markdown(f"""
                        <div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1.1rem; margin-bottom: 1rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
                                <h4 style="margin: 0; color: #38BDF8;">{day_info.get('day', 'Day')} Schedule</h4>
                                <div>
                                    <span class="badge badge-cyan">{day_info.get('total_calories', metrics['target_calories'])} kcal</span>
                                    <span class="badge badge-green">{day_info.get('total_protein', metrics['target_protein'])}g Protein</span>
                                </div>
                            </div>
                            
                            <div style="margin-bottom: 0.6rem; padding: 0.6rem; border-left: 3px solid #34D399; background: rgba(15, 23, 42, 0.4); border-radius: 0 8px 8px 0;">
                                <b style="color: #34D399;">🌅 Breakfast:</b><br>
                                <span style="font-size: 0.9rem; color: #E2E8F0;">{day_info.get('breakfast', 'Nutritious Morning Meal')}</span>
                            </div>
                            
                            <div style="margin-bottom: 0.6rem; padding: 0.6rem; border-left: 3px solid #38BDF8; background: rgba(15, 23, 42, 0.4); border-radius: 0 8px 8px 0;">
                                <b style="color: #38BDF8;">☀️ Lunch:</b><br>
                                <span style="font-size: 0.9rem; color: #E2E8F0;">{day_info.get('lunch', 'Balanced Midday Meal')}</span>
                            </div>
                            
                            <div style="margin-bottom: 0.6rem; padding: 0.6rem; border-left: 3px solid #FBBF24; background: rgba(15, 23, 42, 0.4); border-radius: 0 8px 8px 0;">
                                <b style="color: #FBBF24;">🌙 Dinner:</b><br>
                                <span style="font-size: 0.9rem; color: #E2E8F0;">{day_info.get('dinner', 'High-Protein Evening Meal')}</span>
                            </div>
                            
                            <div style="padding: 0.6rem; border-left: 3px solid #C084FC; background: rgba(15, 23, 42, 0.4); border-radius: 0 8px 8px 0;">
                                <b style="color: #C084FC;">🍎 Wholesome Snack:</b><br>
                                <span style="font-size: 0.9rem; color: #E2E8F0;">{day_info.get('snack', 'Nutrient-Dense Snack')}</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

    # Bottom Full-Width Shopping List
    st.markdown("---")
    st.markdown("### 🛒 Consolidated 7-Day Grocery Shopping List")

    shopping_dict = plan_data.get("shopping_list", {})
    if shopping_dict:
        shop_cols = st.columns(len(shopping_dict))
        for s_idx, (category, items) in enumerate(shopping_dict.items()):
            with shop_cols[s_idx % len(shop_cols)]:
                st.markdown(f"""
                    <div class="glass-card" style="padding: 1rem; min-height: 240px;">
                        <h4 style="margin: 0 0 0.6rem 0; color: #34D399; font-size: 1rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 4px;">
                            {category}
                        </h4>
                        <ul style="padding-left: 1.2rem; margin: 0; font-size: 0.85rem; color: #CBD5E1; line-height: 1.6;">
                            {''.join([f'<li>{item}</li>' for item in items])}
                        </ul>
                    </div>
                """, unsafe_allow_html=True)

    # Download Buttons
    col_dl1, col_dl2 = st.columns(2)
    with col_dl1:
        plan_export_json = json.dumps(plan_data, indent=2)
        st.download_button(
            label="📥 Download Complete 7-Day Meal Plan (JSON)",
            data=plan_export_json,
            file_name="FoodVerse_7Day_Personalized_Meal_Plan.json",
            mime="application/json",
            use_container_width=True
        )
    with col_dl2:
        # Generate text shopping list
        txt_shopping = f"FoodVerse AI - Grocery Shopping List\nDietary Profile: {dietary_style} | Goal: {fitness_goal}\n" + "="*50 + "\n\n"
        for cat, itms in shopping_dict.items():
            txt_shopping += f"[{cat.upper()}]\n"
            for itm in itms:
                txt_shopping += f"  - [ ] {itm}\n"
            txt_shopping += "\n"
        st.download_button(
            label="📝 Download Printable Grocery Checklist (TXT)",
            data=txt_shopping,
            file_name="FoodVerse_Grocery_Shopping_Checklist.txt",
            mime="text/plain",
            use_container_width=True
        )

