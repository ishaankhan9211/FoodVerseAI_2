"""
Comprehensive Unit & Integration Test Suite for Food Verse AI
"""

import unittest
from PIL import Image
import os
import json

from modules.ai_service import AIService
from modules.mock_data import (
    NUTRITION_PRESETS,
    FRESHNESS_PRESETS,
    HYGIENE_PRESETS,
    RECIPE_DATABASE,
    MEAL_PLANS
)
from modules.meal_planner import calculate_bmr_tdee
from modules.food_recognition import render_macro_donut, render_health_score_gauge
from modules.freshness_diagnostic import render_freshness_gauge
from modules.kitchen_hygiene import render_compliance_gauge


class TestFoodVerseAI(unittest.TestCase):

    def setUp(self):
        self.ai_service = AIService(provider="Demo Mode", api_key="")

    def test_nutrition_audit_demo(self):
        result, is_fallback = self.ai_service.analyze_nutrition(preset_key="salmon_bowl")
        self.assertTrue(is_fallback)
        self.assertIn("dish_name", result)
        self.assertIn("nutrition", result)
        nutr = result["nutrition"]
        self.assertGreater(nutr["calories"], 0)
        self.assertGreater(nutr["protein"], 0)
        self.assertIn("health_score", result)
        self.assertTrue(0 <= result["health_score"] <= 100)
        self.assertIn("allergens", result)
        self.assertTrue(len(result["allergens"]) > 0)

    def test_freshness_diagnostic_demo(self):
        # Test Fresh
        fresh_res, _ = self.ai_service.diagnose_freshness(preset_key="fresh_strawberry")
        self.assertEqual(fresh_res["freshness_stage"], "Fresh")
        self.assertEqual(fresh_res["action_badge"], "Safe to consume")
        self.assertGreaterEqual(fresh_res["freshness_score"], 75)

        # Test Spoiled
        spoiled_res, _ = self.ai_service.diagnose_freshness(preset_key="spoiled_strawberry")
        self.assertEqual(spoiled_res["freshness_stage"], "Spoiled")
        self.assertEqual(spoiled_res["action_badge"], "Discard immediately")
        self.assertLess(spoiled_res["freshness_score"], 40)

    def test_kitchen_hygiene_demo(self):
        comp_res, _ = self.ai_service.audit_kitchen_hygiene(preset_key="compliant_kitchen")
        self.assertGreaterEqual(comp_res["overall_score"], 85)
        self.assertIn("indicators", comp_res)
        self.assertIn("hair_containment", comp_res["indicators"])
        self.assertIn("glove_usage", comp_res["indicators"])
        self.assertIn("workstation_sanitization", comp_res["indicators"])
        self.assertIn("cross_contamination_hazard", comp_res["indicators"])

        viol_res, _ = self.ai_service.audit_kitchen_hygiene(preset_key="violation_kitchen")
        self.assertLess(viol_res["overall_score"], 60)
        self.assertTrue(len(viol_res["violations"]) > 0)

    def test_recipe_assistant_demo(self):
        recipes, _ = self.ai_service.generate_recipes(ingredients=["Chicken Breast", "Quinoa", "Spinach"])
        self.assertTrue(len(recipes) > 0)
        first = recipes[0]
        self.assertIn("title", first)
        self.assertIn("cook_time", first)
        self.assertIn("steps", first)
        self.assertTrue(len(first["steps"]) > 0)
        self.assertIn("substitutions", first)
        self.assertIn("science_note", first)

    def test_bmr_tdee_calculation(self):
        # Male, 70kg, 175cm, 25 years old
        # BMR = 10*70 + 6.25*175 - 5*25 + 5 = 700 + 1093.75 - 125 + 5 = 1673.75
        metrics_male = calculate_bmr_tdee(70.0, 175.0, 25, "Male", "Moderately Active (3-5 days/week)", "Maintenance (Weight Stability)")
        self.assertEqual(metrics_male["bmr"], 1673)
        self.assertEqual(metrics_male["tdee"], int(1673.75 * 1.55))
        self.assertGreater(metrics_male["target_protein"], 100)

        # Female, 60kg, 165cm, 30 years old
        # BMR = 10*60 + 6.25*165 - 5*30 - 161 = 600 + 1031.25 - 150 - 161 = 1320.25
        metrics_female = calculate_bmr_tdee(60.0, 165.0, 30, "Female", "Sedentary (Desk job, little exercise)", "Moderate Fat Loss (-300 kcal)")
        self.assertEqual(metrics_female["bmr"], 1320)
        self.assertEqual(metrics_female["target_calories"], int(1320.25 * 1.2 - 300))

    def test_meal_plan_demo(self):
        profile = {
            "age": 28, "gender": "Female", "weight_kg": 65, "height_cm": 170,
            "activity_level": "Moderately Active", "dietary_constraint": "Balanced",
            "target_calories": 1800, "target_protein_g": 120, "fitness_goal": "Maintenance"
        }
        plan_data, _ = self.ai_service.generate_meal_plan(profile)
        self.assertIn("days", plan_data)
        self.assertEqual(len(plan_data["days"]), 7)
        self.assertIn("shopping_list", plan_data)
        self.assertTrue(len(plan_data["shopping_list"]) > 0)

    def test_plotly_chart_rendering(self):
        donut = render_macro_donut(35.0, 45.0, 20.0, 6.0)
        self.assertIsNotNone(donut)
        gauge1 = render_health_score_gauge(88, "A")
        self.assertIsNotNone(gauge1)
        gauge2 = render_freshness_gauge(95, "Fresh")
        self.assertIsNotNone(gauge2)
        gauge3 = render_compliance_gauge(96, "Grade A")
        self.assertIsNotNone(gauge3)


if __name__ == '__main__':
    unittest.main()

