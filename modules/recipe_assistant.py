"""
Food Verse AI - Module 4: Smart Kitchen Recipe Assistant (Epic 4)
Generative culinary AI: pantry inventory matching, cooking step generation, culinary chemistry science notes, and intelligent ingredient substitutions.
"""

import streamlit as st
import json


def render_tab_recipe_assistant(ai_service):
    st.markdown("""
        <div class="glass-card" style="margin-bottom: 1.5rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h2 style="margin: 0; color: #34D399; font-size: 1.6rem;">🍳 Smart Kitchen Recipe Assistant</h2>
                    <p style="margin: 0.3rem 0 0 0; color: #94A3B8; font-size: 0.95rem;">
                        Transform on-hand pantry ingredients into gourmet, nutritionally balanced recipes with culinary science notes and smart ingredient substitutions.
                    </p>
                </div>
                <span class="badge badge-cyan">Epic 4 Active</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_pantry, col_results = st.columns([1, 1.3], gap="large")

    with col_pantry:
        st.markdown("### 🥫 Available Pantry Inventory")

        # Quick common ingredients multiselect
        common_ingredients = [
            "Chicken Breast", "Atlantic Salmon", "Eggs", "Firm Tofu",
            "Quinoa", "Brown Rice", "Pasta / Linguine", "Cannellini Beans",
            "Garlic", "Onions", "Cherry Tomatoes", "Baby Spinach", "Broccoli", "Avocado", "Lemon",
            "Olive Oil", "Sesame Oil", "Soy Sauce / Tamari", "Greek Yogurt", "Cheddar Cheese"
        ]

        selected_ingredients = st.multiselect(
            "Select items already in your pantry/fridge:",
            options=common_ingredients,
            default=["Chicken Breast", "Quinoa", "Garlic", "Baby Spinach", "Lemon", "Olive Oil"]
        )

        custom_items_input = st.text_input(
            "Add other custom ingredients (comma separated):",
            placeholder="e.g. ginger, mushrooms, bell peppers, coconut milk"
        )

        all_ingredients = list(selected_ingredients)
        if custom_items_input:
            extra_items = [i.strip() for i in custom_items_input.split(",") if i.strip()]
            all_ingredients.extend(extra_items)

        st.markdown("### ⚙️ Culinary Preferences")
        c_pref1, c_pref2 = st.columns(2)
        with c_pref1:
            diet_style = st.selectbox(
                "Dietary Constraint",
                ["Any / Balanced", "High Protein", "Vegetarian", "Vegan / Plant-Based", "Low Carb / Keto", "Gluten-Free"]
            )
            difficulty = st.select_slider(
                "Skill Level",
                options=["Beginner", "Intermediate", "MasterChef"],
                value="Beginner"
            )

        with c_pref2:
            max_cook_time = st.slider("Max Total Cooking Time (mins)", min_value=10, max_value=90, value=30, step=5)
            servings = st.number_input("Portions / Servings", min_value=1, max_value=8, value=3)

        generate_btn = st.button("✨ Generate Nutritious Recipes", use_container_width=True, type="primary")

    with col_results:
        st.markdown("### 🍽️ AI Generated Culinary Creations")

        if "recipe_results" not in st.session_state or generate_btn:
            if generate_btn:
                if not all_ingredients:
                    st.warning("Please select or enter at least one pantry ingredient.")
                    return
                with st.spinner("Synthesizing culinary flavor pairings & nutritional optimization..."):
                    recipes, is_fallback = ai_service.generate_recipes(
                        ingredients=all_ingredients,
                        dietary_style=diet_style,
                        max_time=max_cook_time,
                        skill_level=difficulty
                    )
                    st.session_state["recipe_results"] = recipes
                    st.session_state["recipe_is_fallback"] = is_fallback
            else:
                # Default demo
                recipes, is_fallback = ai_service.generate_recipes(ingredients=all_ingredients)
                st.session_state["recipe_results"] = recipes
                st.session_state["recipe_is_fallback"] = is_fallback

        recipes = st.session_state["recipe_results"]
        is_fallback = st.session_state.get("recipe_is_fallback", False)

        if is_fallback and ai_service.provider != "Demo Mode":
            st.info("ℹ️ Using FoodVerse High-Precision Culinary Demonstration Recipes.")

        if not recipes:
            st.warning("No recipes generated. Please adjust pantry ingredients and try again.")
            return

        # Render each recipe as an expandable card
        for idx, recipe in enumerate(recipes):
            with st.expander(f"🍲 {recipe.get('title', 'Chef Creation')} ({recipe.get('total_time', '30m')})", expanded=(idx == 0)):
                # Quick Meta Header
                st.markdown(f"""
                    <div style="display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 0.8rem;">
                        <span class="badge badge-green">⏱️ {recipe.get('total_time', '30 mins')}</span>
                        <span class="badge badge-cyan">🔥 {recipe.get('calories_per_serving', 400)} kcal / serving</span>
                        <span class="badge badge-purple">💪 {recipe.get('protein_g', 30)}g Protein</span>
                        <span class="badge badge-amber">👨‍🍳 {recipe.get('difficulty', 'Easy')}</span>
                        <span class="badge badge-green">🍽️ {recipe.get('servings', 2)} Servings</span>
                    </div>
                """, unsafe_allow_html=True)

                # Ingredients used
                matched = recipe.get("matched_ingredients", [])
                missing = recipe.get("missing_optional", [])
                st.markdown(f"""
                    <div style="font-size: 0.9rem; margin-bottom: 0.8rem;">
                        <b>Utilized from your pantry:</b> <span style="color: #34D399;">{', '.join(matched) if matched else 'All standard pantry staples'}</span><br>
                        {f'<b>Optional enhancements:</b> <span style="color: #94A3B8;">{", ".join(missing)}</span>' if missing else ''}
                    </div>
                """, unsafe_allow_html=True)

                # Science Note Box
                science_note = recipe.get("science_note")
                if science_note:
                    st.markdown(f"""
                        <div style="background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38BDF8; padding: 0.75rem 1rem; border-radius: 0 10px 10px 0; margin-bottom: 1rem; font-size: 0.88rem; line-height: 1.45; color: #E2E8F0;">
                            <b>🧪 Culinary Science & Reaction Insight:</b><br>{science_note}
                        </div>
                    """, unsafe_allow_html=True)

                # Step-by-Step Instructions
                st.markdown("#### 👩‍🍳 Cooking Instructions")
                steps = recipe.get("steps", [])
                for s_num, step in enumerate(steps):
                    st.markdown(f"""
                        <div class="step-card">
                            <div class="step-num">{s_num + 1}</div>
                            <div style="color: #F8FAFC; font-size: 0.92rem; align-self: center; line-height: 1.4;">
                                {step}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

                # Ingredient Substitutions
                subs = recipe.get("substitutions", [])
                if subs:
                    st.markdown("#### 🔄 Smart Ingredient Substitutions")
                    for sub in subs:
                        st.markdown(f"""
                            <div style="background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 0.6rem 0.9rem; margin-bottom: 0.5rem; font-size: 0.85rem;">
                                <b>If out of {sub.get('original')}:</b> Replace with <span style="color: #38BDF8; font-weight: 600;">{sub.get('substitute')}</span> (Ratio: {sub.get('ratio', '1:1')}).<br>
                                <span style="color: #94A3B8;">💡 {sub.get('note', '')}</span>
                            </div>
                        """, unsafe_allow_html=True)

                # Download Recipe Card
                recipe_json = json.dumps(recipe, indent=2)
                st.download_button(
                    label=f"📥 Download Recipe '{recipe.get('title', 'Recipe')}' (JSON)",
                    data=recipe_json,
                    file_name=f"FoodVerse_Recipe_{recipe.get('title', 'Recipe').replace(' ', '_')}.json",
                    mime="application/json",
                    key=f"dl_rec_{idx}"
                )

