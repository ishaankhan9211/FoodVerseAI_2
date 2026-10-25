# 🥑 Food Verse AI — Multimodal Food Intelligence Agent
**Skill Wallet Capstone Project 3 • Food Science & AI Systems Engineering**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FDA 2022 Compliant](https://img.shields.io/badge/FDA_Food_Code-2022_Compliant-emerald.svg)](https://www.fda.gov/food/fda-food-code/food-code-2022)
[![HACCP Certified](https://img.shields.io/badge/HACCP-Codex_Alimentarius-purple.svg)](https://www.fao.org/fao-who-codexalimentarius/en/)
[![Zero Database](https://img.shields.io/badge/Architecture-Stateless_Cloud_Ready-cyan.svg)](#)

---

## 🌟 Executive Summary

**Food Verse AI** is an autonomous, multimodal food intelligence application designed for clinical nutritionists, culinary scientists, commercial kitchen inspectors, and health-conscious consumers. Built for seamless **1-click deployment on Streamlit Community Cloud**, it fuses state-of-the-art vision models (**Google Gemini 2.5 Flash**, **Groq LLaMA 3.2 Vision**) with scientifically rigorous nutrition and pathology algorithms—while featuring a **100% functional standalone demonstration mode** that requires zero external API keys or database dependencies.

---

## 🏛️ Core Intelligence Pillars & Modules

```
                                  ┌───────────────────────────┐
                                  │       Food Verse AI       │
                                  │ Multimodal AI Supervisor  │
                                  └─────────────┬─────────────┘
                                                │
         ┌──────────────────┬───────────────────┼───────────────────┬──────────────────┐
         ▼                  ▼                   ▼                   ▼                  ▼
   ┌───────────┐      ┌───────────┐       ┌───────────┐       ┌───────────┐      ┌───────────┐
   │  Tab 1:   │      │  Tab 2:   │       │  Tab 3:   │       │  Tab 4:   │      │  Tab 5:   │
   │ Nutrition │      │ Spoilage  │       │ Kitchen   │       │ Smart     │      │ Personal  │
   │   Audit   │      │Diagnostic │       │ Hygiene   │       │ Recipe    │      │ Meal Plan │
   │  (Epic 2) │      │ (Epic 3)  │       │ (Epic 4)  │       │ (Epic 4)  │      │ (Epic 5)  │
   └───────────┘      └───────────┘       └───────────┘       └───────────┘      └───────────┘
```

### 1. 🥗 Tab 1: Food Recognition & Nutrition Audit (Epic 2)
* **Vision Analysis:** Automatically identifies dish taxonomy, culinary tradition, constituent ingredients, and portion gram weights.
* **Biochemical Macro Breakdown:** Energy (kcal), Protein (g), Carbohydrates (g), Total & Saturated Fats (g), and Dietary Fiber (g).
* **Micronutrient Density:** Tracks Omega-3 fatty acids, Vitamin D, Vitamin B12, Potassium, and Magnesium vs USDA Recommended Daily Allowances (RDA).
* **Allergen Alert Matrix:** Evaluates 9 major FDA allergens (Fish, Sesame, Gluten, Dairy, Eggs, Peanuts, Tree Nuts, Shellfish, Soy) with severity tiers (*Critical, Moderate, Safe*).
* **Composite Health Score (1-100):** Evaluates nutrient density, fiber-to-carb ratios, and sodium levels.
* **Interactive Visualizations:** Plotly macronutrient donut charts, health score gauges, and downloadable JSON audit reports.

### 2. 🔬 Tab 2: Food Freshness & Spoilage Diagnostic (Epic 3)
* **Pathological Inspection:** Analyzes raw perishable foods (fruits, vegetables, meats, seafood, dairy) across 4 scientific axes:
  1. *Surface Texture & Osmotic Turgor:* Detects maceration, weeping fluids, and softening cell walls.
  2. *Discoloration & Oxidation:* Evaluates enzymatic browning (polyphenol oxidase) and lipid oxidation.
  3. *Wrinkling & Shrinkage:* Quantifies epidermal collapse and moisture loss.
  4. *Mold & Pathogen Detection:* Identifies fungal mycelium (*Botrytis cinerea, Penicillium, Aspergillus*) and bacterial biofilms.
* **Freshness Tri-State Classification:** `[Fresh | Moderately Fresh | Spoiled]`.
* **Actionable Directives:** Color-coded badges (`🟢 Safe to consume`, `🟡 Consume within 24h`, `🔴 Discard immediately`).
* **Preservation Protocols:** Storage temperature (°C/°F), ethylene isolation, humidity management, and culinary rescue advice.

### 3. 🧼 Tab 3: Kitchen Hygiene & Food Safety Compliance (Epic 4)
* **Commercial Surveillance:** Visual inspection of commercial and domestic prep stations against US FDA Food Code (2022) & HACCP standards.
* **Hygiene Compliance Indicators:**
  - *Hair Containment:* Detects chef hats, snoods, and beard restraints.
  - *PPE & Glove Usage:* Verifies single-use nitrile gloves during ready-to-eat food assembly.
  - *Surface Sanitization:* Audits stainless steel tables for grease, debris, and approved sanitizer buckets (200 ppm quat).
  - *Cross-Contamination Prevention:* Flags hazardous proximity between raw poultry/meat and ready-to-eat produce or unsegregated cutting boards.
* **Compliance Scoring & Grade:** Overall score (0-100%) and certification grades (Grade A, B, C, or Grade F Closure Warning).
* **Itemized Violation Logs:** Provides violation IDs, FDA/HACCP regulation references, and required immediate corrective actions.

### 4. 🍳 Tab 4: Smart Kitchen Recipe Assistant (Epic 4)
* **Zero-Waste Pantry Engine:** Input available pantry ingredients via interactive multi-select tags and custom text.
* **Nutritional Optimization:** Filters by dietary constraint (*High Protein, Vegan, Keto, Gluten-Free, Mediterranean*), max cooking time (10-90m), and skill level.
* **Culinary Chemistry Science Notes:** Explains chemical food transformations (e.g., Maillard reaction pyrazines, starch gelatinization, lycopene bioavailability).
* **Smart Substitutions:** Provides 1:1 culinary ingredient substitutions with ratio guidelines.

### 5. 📋 Tab 5: Personalized Meal Planner (Epic 5)
* **Anthropometric Profiling:** Captures age, biological sex, weight (kg), height (cm), activity level, and fitness objectives.
* **Clinically Validated Metabolic Computation:**
  - **Basal Metabolic Rate (BMR):** Computed via the **Mifflin-St Jeor Equation**:
    $$\text{BMR}_{\text{Men}} = 10 \times \text{weight} + 6.25 \times \text{height} - 5 \times \text{age} + 5$$
    $$\text{BMR}_{\text{Women}} = 10 \times \text{weight} + 6.25 \times \text{height} - 5 \times \text{age} - 161$$
  - **Total Daily Energy Expenditure (TDEE):** Computed via physical activity multipliers ($1.20$ to $1.90$).
  - **Macronutrient Partitioning:** Dynamically derived targets for Protein (g), Carbohydrates (g), and Healthy Fats (g).
* **Adaptive 7-Day Schedule:** Complete Monday-to-Sunday breakfast, lunch, dinner, and wholesome snacks with calorie and protein counters.
* **Categorized Grocery Shopping List:** Produce, Proteins, Dairy/Alternatives, Grains, and Seasonings ready for 1-click TXT/JSON download.

---

## 🚀 Quickstart Guide

### 1. Clone & Set Up Environment
```bash
# Clone repository
git clone https://github.com/your-username/FoodVerseAI_2.0.git
cd FoodVerseAI_2.0

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate       # On Linux/macOS
# or: .venv\Scripts\activate    # On Windows

# Install production dependencies
pip install -r requirements.txt
```

### 2. Launch Streamlit Application
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

### 3. Run Automated Unit Test Suite
```bash
python -m unittest tests/test_foodverse.py
```
*Executes full test suite validating BMR/TDEE calculations, fallback engines, chart renderers, and schema integrity.*

---

## 🔑 AI Provider Configuration

| Mode | Key Required? | Description |
| :--- | :---: | :--- |
| **Demo Mode** | ❌ No | **100% Standalone Out-Of-The-Box.** Uses high-fidelity, scientifically validated food science datasets with preloaded imagery for instant evaluation. |
| **Google Gemini** | Optional | Uses `gemini-2.5-flash` for live multimodal visual understanding. Add your key in the UI sidebar or in `.streamlit/secrets.toml`. |
| **Groq** | Optional | Uses `llama-3.2-11b-vision-preview` (multimodal) and `llama-3.3-70b-versatile` (culinary reasoning). |

### Optional Streamlit Secrets Configuration (`.streamlit/secrets.toml`):
```toml
GEMINI_API_KEY = "AIzaSy..."
GROQ_API_KEY = "gsk_..."
```

---

## 📁 Repository Directory Structure

```
FoodVerseAI_2.0/
├── app.py                      # Main application entry point & Streamlit UI layout
├── requirements.txt            # Streamlit Community Cloud dependencies
├── README.md                   # Technical documentation and architecture guide
├── .streamlit/
│   └── config.toml             # Streamlit visual theme and server configuration
├── modules/
│   ├── __init__.py
│   ├── ai_service.py           # Unified AI engine (Gemini, Groq, and Fallback engine)
│   ├── food_recognition.py     # Tab 1: Vision audit, macro charts, health score (Epic 2)
│   ├── freshness_diagnostic.py # Tab 2: Spoilage, surface pathology & storage tips (Epic 3)
│   ├── kitchen_hygiene.py      # Tab 3: HACCP / FDA kitchen compliance inspection (Epic 4)
│   ├── recipe_assistant.py     # Tab 4: Pantry-to-recipe AI generator & food science (Epic 4)
│   ├── meal_planner.py         # Tab 5: Mifflin-St Jeor BMR/TDEE & 7-day planner (Epic 5)
│   └── mock_data.py            # High-fidelity scientific demonstration presets
├── assets/
│   ├── css/
│   │   └── styles.css          # Modern glassmorphism theme & responsive typography
│   └── sample_images/          # Built-in visual samples for 1-click instant testing
└── tests/
    └── test_foodverse.py       # Comprehensive unit and integration test suite
```

---

## ☁️ 1-Click Streamlit Community Cloud Deployment

1. Push this repository to **GitHub**.
2. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
3. Click **"New App"** and select your repository:
   - **Repository:** `your-username/FoodVerseAI_2.0`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. *(Optional)* In **Advanced Settings**, paste your `GEMINI_API_KEY` or `GROQ_API_KEY` into the Secrets box.
5. Click **Deploy!** Your app is live with zero database configuration required.

---

## 📜 Standards & Compliance
- **FDA Food Code 2022:** § 2-402 (Hair restraints), § 3-301 (Bare hand contact), § 3-302 (Cross contamination), § 4-601 (Surface sanitation).
- **HACCP Principles:** Codex Alimentarius Hazard Analysis Critical Control Points.
- **USDA FoodData Central:** Reference macronutrient and micronutrient daily values.
- **Mifflin-St Jeor Equation:** Standard clinical formula for basal metabolic rate estimation.

---
*Developed for Skill Wallet Capstone Project 3 • Food Verse AI Multimodal Intelligence Agent.*

