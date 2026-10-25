"""
Food Verse AI - Unified Multimodal AI Service
Supports Google Gemini, Groq Vision, and Standalone Demonstration Mode with automatic graceful fallback.
"""

import json
import base64
import io
import re
from typing import Dict, Any, Optional, Tuple
from PIL import Image

try:
    from google import genai
    from google.genai import types as genai_types
    GOOGLE_GENAI_AVAILABLE = True
except ImportError:
    GOOGLE_GENAI_AVAILABLE = False

try:
    import google.generativeai as legacy_genai
    LEGACY_GENAI_AVAILABLE = True
except ImportError:
    LEGACY_GENAI_AVAILABLE = False

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

from modules.mock_data import (
    NUTRITION_PRESETS,
    FRESHNESS_PRESETS,
    HYGIENE_PRESETS,
    RECIPE_DATABASE,
    MEAL_PLANS
)


class AIService:
    def __init__(self, provider: str = "Demo Mode", api_key: str = ""):
        self.provider = provider
        self.api_key = api_key.strip()
        self.is_demo_mode = (self.provider == "Demo Mode") or (not self.api_key)

    def _clean_json_response(self, text: str) -> Dict[str, Any]:
        """Strip markdown code fences and parse JSON robustly."""
        if not text:
            raise ValueError("Empty response received from AI model.")
        
        # Remove markdown code blocks if present
        text_clean = re.sub(r"^```(?:json)?", "", text.strip(), flags=re.MULTILINE)
        text_clean = re.sub(r"```$", "", text_clean.strip(), flags=re.MULTILINE).strip()
        
        # Try finding json object or array
        match = re.search(r"(\{.*\}|\[.*\])", text_clean, re.DOTALL)
        if match:
            text_clean = match.group(1)
            
        return json.loads(text_clean)

    def _image_to_base64_data_url(self, image: Image.Image) -> str:
        """Convert a PIL Image to a base64 data URL string."""
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG", quality=85)
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return f"data:image/jpeg;base64,{img_str}"

    # -------------------------------------------------------------
    # Module 1: Food Recognition & Nutrition Audit
    # -------------------------------------------------------------
    def analyze_nutrition(self, image: Optional[Image.Image] = None, preset_key: Optional[str] = None) -> Tuple[Dict[str, Any], bool]:
        """
        Multimodal audit of meal/dish.
        Returns (result_dict, is_fallback_used).
        """
        if self.is_demo_mode or image is None:
            key = preset_key if preset_key in NUTRITION_PRESETS else "salmon_bowl"
            return NUTRITION_PRESETS[key], True

        prompt = """
        You are NutriScientist AI, an expert food science and clinical nutrition specialist.
        Analyze this food/dish image and return STRICT, VALID JSON ONLY. No markdown outside JSON.
        
        JSON schema:
        {
            "dish_name": "Full descriptive name of dish",
            "cuisine": "Cuisine type (e.g., Mediterranean, South Asian, Mexican)",
            "serving_size": "Estimated serving size (e.g. 400g)",
            "confidence": 0.95,
            "ingredients": [
                {"name": "Ingredient name", "amount": "Estimated weight/amount", "calories": 150, "protein": 12.0}
            ],
            "nutrition": {
                "calories": 550,
                "protein": 35.0,
                "carbohydrates": 45.0,
                "fats": 22.0,
                "saturated_fats": 4.0,
                "fiber": 7.0,
                "sugar": 4.0,
                "sodium_mg": 450,
                "potassium_mg": 700,
                "cholesterol_mg": 60
            },
            "micronutrients": [
                {"nutrient": "Omega-3 Fatty Acids", "amount": "1,800 mg", "dv_percent": 110},
                {"nutrient": "Vitamin C", "amount": "45 mg", "dv_percent": 50}
            ],
            "allergens": [
                {"name": "Allergen name", "severity": "Critical|Moderate|Trace|Safe", "description": "Specific finding"}
            ],
            "health_score": 88,
            "health_score_grade": "A (Nutrient Dense)",
            "dietary_tags": ["High Protein", "Heart Healthy"],
            "science_audit_summary": "2-3 sentences of food science / clinical nutritional analysis."
        }
        """

        try:
            if self.provider == "Google Gemini":
                if GOOGLE_GENAI_AVAILABLE:
                    client = genai.Client(api_key=self.api_key)
                    # Convert PIL image to bytes
                    img_byte_arr = io.BytesIO()
                    image.save(img_byte_arr, format='JPEG')
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[
                            genai_types.Part.from_bytes(data=img_byte_arr.getvalue(), mime_type='image/jpeg'),
                            prompt
                        ]
                    )
                    return self._clean_json_response(response.text), False
                elif LEGACY_GENAI_AVAILABLE:
                    legacy_genai.configure(api_key=self.api_key)
                    model = legacy_genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content([image, prompt])
                    return self._clean_json_response(response.text), False
                else:
                    raise ImportError("Google GenAI SDK is not installed.")

            elif self.provider == "Groq":
                if not GROQ_AVAILABLE:
                    raise ImportError("Groq SDK is not installed.")
                client = Groq(api_key=self.api_key)
                data_url = self._image_to_base64_data_url(image)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {"type": "image_url", "image_url": {"url": data_url}}
                            ]
                        }
                    ],
                    model="llama-3.2-11b-vision-preview",
                    temperature=0.2,
                    response_format={"type": "json_object"}
                )
                return json.loads(chat_completion.choices[0].message.content), False

        except Exception as e:
            # Automatic graceful fallback to mock data
            fallback = NUTRITION_PRESETS.get(preset_key, NUTRITION_PRESETS["salmon_bowl"]).copy()
            fallback["_error_notice"] = str(e)
            return fallback, True

        return NUTRITION_PRESETS["salmon_bowl"], True

    # -------------------------------------------------------------
    # Module 2: Food Freshness & Spoilage Diagnostic
    # -------------------------------------------------------------
    def diagnose_freshness(self, image: Optional[Image.Image] = None, preset_key: Optional[str] = None) -> Tuple[Dict[str, Any], bool]:
        """
        Vision analysis evaluating surface texture, discoloration, wrinkling, and mold.
        Returns (result_dict, is_fallback_used).
        """
        if self.is_demo_mode or image is None:
            key = preset_key if preset_key in FRESHNESS_PRESETS else "fresh_strawberry"
            return FRESHNESS_PRESETS[key], True

        prompt = """
        You are a Senior Post-Harvest Food Pathologist and Spoilage Diagnostic AI.
        Analyze this perishable food item image (fruits, vegetables, meats, dairy, bread).
        Evaluate surface texture, discoloration, wrinkling/cellular turgor loss, and fungal/bacterial mold.
        
        Return STRICT, VALID JSON ONLY with this schema:
        {
            "item_name": "Full biological / commercial name of the item",
            "category": "Produce | Seafood | Meat | Dairy | Bakery",
            "inspection": {
                "surface_texture": "Detailed texture diagnosis (firmness, slimy exudate, weeping)",
                "discoloration": "Color oxidation, enzymatic browning, or necrosis analysis",
                "wrinkling": "Turgor loss, epidermal collapse percentage",
                "mold_status": "Absence or presence of fungal mycelium/spores (e.g. Botrytis, Penicillium, Aspergillus)"
            },
            "freshness_stage": "Fresh | Moderately Fresh | Spoiled",
            "freshness_score": 85,
            "action_badge": "Safe to consume | Consume within 24h | Discard immediately",
            "action_type": "safe | warning | danger",
            "shelf_life_remaining": "e.g. 3-4 days refrigerated | 0 hours",
            "food_safety_advice": "Actionable food safety, toxicological, or culinary advice.",
            "preservation_tips": [
                "Storage tip 1 (temperature, humidity, container)",
                "Storage tip 2 (ethylene isolation, washing rules)",
                "Storage tip 3"
            ]
        }
        """

        try:
            if self.provider == "Google Gemini":
                if GOOGLE_GENAI_AVAILABLE:
                    client = genai.Client(api_key=self.api_key)
                    img_byte_arr = io.BytesIO()
                    image.save(img_byte_arr, format='JPEG')
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[
                            genai_types.Part.from_bytes(data=img_byte_arr.getvalue(), mime_type='image/jpeg'),
                            prompt
                        ]
                    )
                    return self._clean_json_response(response.text), False
                elif LEGACY_GENAI_AVAILABLE:
                    legacy_genai.configure(api_key=self.api_key)
                    model = legacy_genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content([image, prompt])
                    return self._clean_json_response(response.text), False

            elif self.provider == "Groq":
                if not GROQ_AVAILABLE:
                    raise ImportError("Groq SDK is not installed.")
                client = Groq(api_key=self.api_key)
                data_url = self._image_to_base64_data_url(image)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {"type": "image_url", "image_url": {"url": data_url}}
                            ]
                        }
                    ],
                    model="llama-3.2-11b-vision-preview",
                    temperature=0.2,
                    response_format={"type": "json_object"}
                )
                return json.loads(chat_completion.choices[0].message.content), False

        except Exception as e:
            fallback = FRESHNESS_PRESETS.get(preset_key, FRESHNESS_PRESETS["fresh_strawberry"]).copy()
            fallback["_error_notice"] = str(e)
            return fallback, True

        return FRESHNESS_PRESETS["fresh_strawberry"], True

    # -------------------------------------------------------------
    # Module 3: Kitchen Hygiene & Safety Compliance
    # -------------------------------------------------------------
    def audit_kitchen_hygiene(self, image: Optional[Image.Image] = None, preset_key: Optional[str] = None) -> Tuple[Dict[str, Any], bool]:
        """
        Audit commercial/domestic kitchen environments for HACCP and FDA Food Code compliance.
        Returns (result_dict, is_fallback_used).
        """
        if self.is_demo_mode or image is None:
            key = preset_key if preset_key in HYGIENE_PRESETS else "compliant_kitchen"
            return HYGIENE_PRESETS[key], True

        prompt = """
        You are a Chief Food Safety Inspector and HACCP Compliance AI.
        Inspect this kitchen environment image for commercial food safety indicators:
        1. Chef hat / hairnet compliance and hair containment.
        2. Glove usage & personal protective equipment during food handling.
        3. Workstation sanitization state (surface grease, debris, standing liquids, sanitizer towels).
        4. Cross-contamination hazards (e.g., raw poultry/meat placed near fresh ready-to-eat produce, improper cutting boards).
        
        Return STRICT, VALID JSON ONLY with this schema:
        {
            "scenario_name": "Short descriptive title of the inspected kitchen area",
            "overall_score": 88,
            "compliance_grade": "Grade A | Grade B | Grade C | Grade F (Shutdown Risk)",
            "grade_type": "safe | warning | danger",
            "indicators": {
                "hair_containment": {"status": "Compliant (95%) | Non-Compliant", "details": "Explanation"},
                "glove_usage": {"status": "Compliant | Critical Violation", "details": "Explanation"},
                "workstation_sanitization": {"status": "Compliant | Non-Compliant", "details": "Explanation"},
                "cross_contamination_hazard": {"status": "Zero Hazard | Critical Hazard", "details": "Explanation"}
            },
            "violations": [
                {
                    "id": "VIOL-01",
                    "severity": "Critical Violation | Major Violation | Low Observation",
                    "standard": "FDA Food Code § reference or HACCP CCP",
                    "finding": "Specific violation observation",
                    "corrective_action": "Required immediate corrective action"
                }
            ],
            "haccp_summary": "Comprehensive 2-3 sentence summary of the inspection findings and compliance status."
        }
        """

        try:
            if self.provider == "Google Gemini":
                if GOOGLE_GENAI_AVAILABLE:
                    client = genai.Client(api_key=self.api_key)
                    img_byte_arr = io.BytesIO()
                    image.save(img_byte_arr, format='JPEG')
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[
                            genai_types.Part.from_bytes(data=img_byte_arr.getvalue(), mime_type='image/jpeg'),
                            prompt
                        ]
                    )
                    return self._clean_json_response(response.text), False
                elif LEGACY_GENAI_AVAILABLE:
                    legacy_genai.configure(api_key=self.api_key)
                    model = legacy_genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content([image, prompt])
                    return self._clean_json_response(response.text), False

            elif self.provider == "Groq":
                if not GROQ_AVAILABLE:
                    raise ImportError("Groq SDK is not installed.")
                client = Groq(api_key=self.api_key)
                data_url = self._image_to_base64_data_url(image)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {"type": "image_url", "image_url": {"url": data_url}}
                            ]
                        }
                    ],
                    model="llama-3.2-11b-vision-preview",
                    temperature=0.2,
                    response_format={"type": "json_object"}
                )
                return json.loads(chat_completion.choices[0].message.content), False

        except Exception as e:
            fallback = HYGIENE_PRESETS.get(preset_key, HYGIENE_PRESETS["compliant_kitchen"]).copy()
            fallback["_error_notice"] = str(e)
            return fallback, True

        return HYGIENE_PRESETS["compliant_kitchen"], True

    # -------------------------------------------------------------
    # Module 4: Smart Kitchen Recipe Assistant
    # -------------------------------------------------------------
    def generate_recipes(self, ingredients: list, dietary_style: str = "Any", max_time: int = 30, skill_level: str = "Beginner") -> Tuple[list, bool]:
        """
        Generate creative, nutritious recipes using available pantry ingredients.
        Returns (recipes_list, is_fallback_used).
        """
        if self.is_demo_mode or not ingredients:
            return RECIPE_DATABASE, True

        ingredients_str = ", ".join(ingredients)
        prompt = f"""
        You are a Master Culinary AI and Food Scientist.
        Given available pantry ingredients: [{ingredients_str}],
        Dietary restriction: {dietary_style},
        Max cooking time: {max_time} minutes,
        Skill level: {skill_level}.

        Generate 2 to 3 creative, delicious, nutritionally balanced recipes.
        Return STRICT, VALID JSON ONLY (an ARRAY of recipe objects):
        [
            {{
                "title": "Recipe Title",
                "cuisine": "Cuisine style",
                "prep_time": "10 mins",
                "cook_time": "20 mins",
                "total_time": "30 mins",
                "difficulty": "Easy|Intermediate|MasterChef",
                "servings": 3,
                "calories_per_serving": 420,
                "protein_g": 32,
                "carbs_g": 38,
                "fats_g": 14,
                "matched_ingredients": ["list of user ingredients utilized"],
                "pantry_staples_used": ["salt", "water", "olive oil"],
                "missing_optional": ["optional ingredients"],
                "science_note": "A scientific explanation of culinary reactions involved (e.g. Maillard reaction, emulsification, enzymatic tenderization).",
                "steps": [
                    "Step 1 instruction",
                    "Step 2 instruction"
                ],
                "substitutions": [
                    {{"original": "Ingredient name", "substitute": "Alternative name", "ratio": "1:1", "note": "Culinary behavior difference"}}
                ]
            }}
        ]
        """

        try:
            if self.provider == "Google Gemini":
                if GOOGLE_GENAI_AVAILABLE:
                    client = genai.Client(api_key=self.api_key)
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    return self._clean_json_response(response.text), False
                elif LEGACY_GENAI_AVAILABLE:
                    legacy_genai.configure(api_key=self.api_key)
                    model = legacy_genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    return self._clean_json_response(response.text), False

            elif self.provider == "Groq":
                if not GROQ_AVAILABLE:
                    raise ImportError("Groq SDK is not installed.")
                client = Groq(api_key=self.api_key)
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                    temperature=0.4
                )
                return self._clean_json_response(chat_completion.choices[0].message.content), False

        except Exception as e:
            return RECIPE_DATABASE, True

        return RECIPE_DATABASE, True

    # -------------------------------------------------------------
    # Module 5: Personalized Meal Planner
    # -------------------------------------------------------------
    def generate_meal_plan(self, profile: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
        """
        Generate 7-day adaptive meal schedule and consolidated grocery shopping list.
        Returns (plan_dict, is_fallback_used).
        """
        if self.is_demo_mode:
            return MEAL_PLANS["Balanced Maintenance"], True

        prompt = f"""
        You are a Clinical Sports Nutritionist and Meal Planning AI.
        User Profile:
        - Age: {profile.get('age', 28)} years old
        - Gender: {profile.get('gender', 'Female')}
        - Weight: {profile.get('weight_kg', 65)} kg
        - Height: {profile.get('height_cm', 170)} cm
        - Activity Level: {profile.get('activity_level', 'Moderately Active')}
        - Dietary Constraint: {profile.get('dietary_constraint', 'Omnivore')}
        - Target Calorie Goal: {profile.get('target_calories', 2000)} kcal/day
        - Target Protein: {profile.get('target_protein_g', 130)} g/day
        - Fitness Goal: {profile.get('fitness_goal', 'Fat Loss')}
        - Allergens/Exclusions: {profile.get('allergies', 'None')}

        Generate a complete 7-day meal plan (Monday through Sunday) matching these exact caloric and protein targets,
        plus an organized grocery shopping list categorized by store departments.
        
        Return STRICT, VALID JSON ONLY:
        {{
            "days": [
                {{
                    "day": "Monday",
                    "breakfast": "Meal description (kcal, g Protein)",
                    "lunch": "Meal description (kcal, g Protein)",
                    "dinner": "Meal description (kcal, g Protein)",
                    "snack": "Meal description (kcal, g Protein)",
                    "total_calories": 2010,
                    "total_protein": 132
                }}
            ],
            "shopping_list": {{
                "Produce": ["Item 1 with quantity", "Item 2 with quantity"],
                "Proteins": ["Item 1 with quantity", "Item 2 with quantity"],
                "Dairy & Alternatives": ["Item 1 with quantity"],
                "Pantry & Grains": ["Item 1 with quantity"],
                "Healthy Fats & Seasonings": ["Item 1 with quantity"]
            }}
        }}
        """

        try:
            if self.provider == "Google Gemini":
                if GOOGLE_GENAI_AVAILABLE:
                    client = genai.Client(api_key=self.api_key)
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    return self._clean_json_response(response.text), False
                elif LEGACY_GENAI_AVAILABLE:
                    legacy_genai.configure(api_key=self.api_key)
                    model = legacy_genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    return self._clean_json_response(response.text), False

            elif self.provider == "Groq":
                if not GROQ_AVAILABLE:
                    raise ImportError("Groq SDK is not installed.")
                client = Groq(api_key=self.api_key)
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                    temperature=0.3
                )
                return self._clean_json_response(chat_completion.choices[0].message.content), False

        except Exception as e:
            return MEAL_PLANS["Balanced Maintenance"], True

        return MEAL_PLANS["Balanced Maintenance"], True

