"""
Food Verse AI - Multimodal Food Intelligence Agent
Mock Data & Demonstration Presets Engine
Provides high-fidelity, scientifically validated food science data for standalone demonstration mode.
"""

# Preset Food Recognition Samples
NUTRITION_PRESETS = {
    "salmon_bowl": {
        "dish_name": "Mediterranean Grilled Salmon Quinoa Bowl",
        "cuisine": "Mediterranean / Healthy Contemporary",
        "serving_size": "420g (1 hearty bowl)",
        "confidence": 0.98,
        "ingredients": [
            {"name": "Wild Atlantic Salmon (Grilled)", "amount": "150g", "calories": 280, "protein": 34.0},
            {"name": "Tricolor Organic Quinoa (Cooked)", "amount": "120g", "calories": 145, "protein": 5.0},
            {"name": "Hass Avocado (Sliced)", "amount": "50g", "calories": 80, "protein": 1.0},
            {"name": "Baby Spinach & Arugula", "amount": "40g", "calories": 10, "protein": 1.2},
            {"name": "Cherry Tomatoes & Cucumber", "amount": "50g", "calories": 15, "protein": 0.8},
            {"name": "Tahini Lemon Herb Vinaigrette", "amount": "15g", "calories": 55, "protein": 1.5}
        ],
        "nutrition": {
            "calories": 585,
            "protein": 43.5,
            "carbohydrates": 42.0,
            "fats": 28.5,
            "saturated_fats": 4.2,
            "fiber": 8.5,
            "sugar": 3.8,
            "sodium_mg": 380,
            "potassium_mg": 920,
            "cholesterol_mg": 75
        },
        "micronutrients": [
            {"nutrient": "Omega-3 Fatty Acids (EPA/DHA)", "amount": "2,200 mg", "dv_percent": 137},
            {"nutrient": "Vitamin D", "amount": "14.2 mcg", "dv_percent": 71},
            {"nutrient": "Vitamin B12 (Cobalamin)", "amount": "3.8 mcg", "dv_percent": 158},
            {"nutrient": "Magnesium", "amount": "118 mg", "dv_percent": 28},
            {"nutrient": "Potassium", "amount": "920 mg", "dv_percent": 20}
        ],
        "allergens": [
            {"name": "Fish (Wild Salmon)", "severity": "Critical", "description": "Primary protein component. Severe anaphylactic risk for fish-allergic individuals."},
            {"name": "Sesame (Tahini)", "severity": "Critical", "description": "Major allergen under FDA FASTER Act. Present in dressing."},
            {"name": "Gluten", "severity": "Safe", "description": "Quinoa is naturally 100% gluten-free."}
        ],
        "health_score": 94,
        "health_score_grade": "A+ (Optimal Nutrient Density)",
        "dietary_tags": ["High Protein", "Heart Healthy", "Gluten-Free", "Rich in Omega-3"],
        "science_audit_summary": (
            "Exemplary cardiovascular and metabolic profile. The wild salmon provides bioavailable EPA/DHA "
            "anti-inflammatory fatty acids. Low glycemic complex carbs from tricolor quinoa paired with "
            "monounsaturated fats from avocado maintain steady postprandial glycemic response with zero insulin spikes."
        )
    },
    "chicken_biryani": {
        "dish_name": "Royal Hyderabadi Dum Chicken Biryani",
        "cuisine": "Mughlai / South Asian",
        "serving_size": "480g (1 full plate)",
        "confidence": 0.96,
        "ingredients": [
            {"name": "Aged Long-Grain Basmati Rice", "amount": "220g", "calories": 310, "protein": 6.5},
            {"name": "Skinless Chicken Thigh (Dum Marinated)", "amount": "180g", "calories": 290, "protein": 36.0},
            {"name": "Pure Desi Ghee & Clarified Butter", "amount": "18g", "calories": 160, "protein": 0.0},
            {"name": "Fried Golden Onions (Birista)", "amount": "30g", "calories": 75, "protein": 1.0},
            {"name": "Whole Spices (Cardamom, Clove, Saffron)", "amount": "10g", "calories": 12, "protein": 0.5},
            {"name": "Spiced Yogurt Marinade", "amount": "40g", "calories": 35, "protein": 2.5}
        ],
        "nutrition": {
            "calories": 782,
            "protein": 46.5,
            "carbohydrates": 84.0,
            "fats": 29.0,
            "saturated_fats": 11.5,
            "fiber": 3.4,
            "sugar": 4.1,
            "sodium_mg": 790,
            "potassium_mg": 560,
            "cholesterol_mg": 115
        },
        "micronutrients": [
            {"nutrient": "Niacin (Vitamin B3)", "amount": "10.4 mg", "dv_percent": 65},
            {"nutrient": "Iron", "amount": "3.8 mg", "dv_percent": 21},
            {"nutrient": "Phosphorus", "amount": "340 mg", "dv_percent": 27},
            {"nutrient": "Selenium", "amount": "38 mcg", "dv_percent": 69}
        ],
        "allergens": [
            {"name": "Dairy (Ghee & Curd/Yogurt)", "severity": "Moderate", "description": "Lactose present in yogurt marinade and milk-fat solids in ghee."},
            {"name": "Nuts (Cashews/Almonds - optional garnish)", "severity": "Trace", "description": "Cross-contact possible if prepared in traditional kitchen."},
            {"name": "Gluten", "severity": "Safe", "description": "Pure basmati rice is gluten-free."}
        ],
        "health_score": 72,
        "health_score_grade": "B (Wholesome Energy-Dense)",
        "dietary_tags": ["High Protein", "Calorie Dense", "Gluten-Free", "Rich in Iron"],
        "science_audit_summary": (
            "Nutrient-dense meal with exceptional high-biological-value protein (46.5g) from slow-cooked chicken. "
            "However, moderate to high glycemic index from polished basmati and saturated fats from desi ghee "
            "warrant portion control for diabetic or sedentary individuals. Saffron and whole spices provide "
            "potent polyphenolic antioxidants (crocin and eugenol)."
        )
    },
    "avocado_toast": {
        "dish_name": "Sourdough Avocado Toast with Free-Range Poached Eggs",
        "cuisine": "Modern Brunch / Californian",
        "serving_size": "290g (2 artisanal slices)",
        "confidence": 0.97,
        "ingredients": [
            {"name": "Naturally Fermented Sourdough Bread", "amount": "110g", "calories": 210, "protein": 8.0},
            {"name": "Fresh Hass Avocado (Coarsely Crushed)", "amount": "90g", "calories": 145, "protein": 1.8},
            {"name": "Free-Range Pasture Eggs (Soft Poached)", "amount": "100g (2 large)", "calories": 140, "protein": 12.5},
            {"name": "Extra Virgin Olive Oil & Chili Flakes", "amount": "8g", "calories": 65, "protein": 0.0},
            {"name": "Microgreens & Radish", "amount": "15g", "calories": 8, "protein": 0.5}
        ],
        "nutrition": {
            "calories": 498,
            "protein": 22.8,
            "carbohydrates": 44.0,
            "fats": 27.2,
            "saturated_fats": 5.2,
            "fiber": 9.2,
            "sugar": 2.1,
            "sodium_mg": 460,
            "potassium_mg": 710,
            "cholesterol_mg": 372
        },
        "micronutrients": [
            {"nutrient": "Choline", "amount": "285 mg", "dv_percent": 52},
            {"nutrient": "Lutein & Zeaxanthin", "amount": "520 mcg", "dv_percent": 86},
            {"nutrient": "Folate (Vitamin B9)", "amount": "148 mcg", "dv_percent": 37},
            {"nutrient": "Vitamin E", "amount": "3.6 mg", "dv_percent": 24}
        ],
        "allergens": [
            {"name": "Eggs", "severity": "Critical", "description": "High ovalbumin protein allergen from whole pasture eggs."},
            {"name": "Gluten / Wheat", "severity": "Critical", "description": "Sourdough wheat flour contains active gluten proteins."},
            {"name": "Dairy", "severity": "Safe", "description": "Zero butter or cheese used."}
        ],
        "health_score": 89,
        "health_score_grade": "A- (High Satiety & Micronutrient Rich)",
        "dietary_tags": ["High Fiber", "Brain Health (Choline)", "Vegetarian Friendly"],
        "science_audit_summary": (
            "Outstanding bioavailability profile. Lactic acid fermentation of sourdough breaks down phytates, "
            "significantly improving mineral absorption (zinc, magnesium). Egg yolks furnish critical choline for "
            "neuronal membrane integrity, while oleic acid in avocado stimulates CCK release for prolonged satiety."
        )
    },
    "tofu_stirfry": {
        "dish_name": "Crispy Teriyaki Tofu & Rainbow Edamame Sauté",
        "cuisine": "East Asian / Plant-Based",
        "serving_size": "380g (1 bowl)",
        "confidence": 0.95,
        "ingredients": [
            {"name": "Organic Extra Firm Tofu (Pan-Seared)", "amount": "160g", "calories": 180, "protein": 19.5},
            {"name": "Shelled Edamame Beans", "amount": "60g", "calories": 75, "protein": 6.8},
            {"name": "Broccoli Florets & Bell Peppers", "amount": "110g", "calories": 40, "protein": 2.8},
            {"name": "Toasted Sesame Oil & Low-Sodium Tamari", "amount": "15g", "calories": 85, "protein": 1.5},
            {"name": "Brown Jasmine Rice", "amount": "90g", "calories": 115, "protein": 2.5}
        ],
        "nutrition": {
            "calories": 415,
            "protein": 31.6,
            "carbohydrates": 38.0,
            "fats": 16.5,
            "saturated_fats": 2.4,
            "fiber": 8.0,
            "sugar": 4.5,
            "sodium_mg": 410,
            "potassium_mg": 680,
            "cholesterol_mg": 0
        },
        "micronutrients": [
            {"nutrient": "Calcium", "amount": "380 mg", "dv_percent": 29},
            {"nutrient": "Vitamin C", "amount": "95 mg", "dv_percent": 105},
            {"nutrient": "Iron (Non-Heme)", "amount": "4.6 mg", "dv_percent": 26},
            {"nutrient": "Isoflavones", "amount": "48 mg", "dv_percent": 100}
        ],
        "allergens": [
            {"name": "Soy (Tofu, Edamame, Tamari)", "severity": "Critical", "description": "High concentration of soy protein (glycinin/conglycinin)."},
            {"name": "Sesame (Sesame Oil & Seeds)", "severity": "Moderate", "description": "Sesame seed allergens present."},
            {"name": "Gluten", "severity": "Safe", "description": "Made with gluten-free tamari sauce."}
        ],
        "health_score": 93,
        "health_score_grade": "A (Exceptional Plant Protein)",
        "dietary_tags": ["100% Vegan", "Low Saturated Fat", "Gluten-Free", "Zero Cholesterol"],
        "science_audit_summary": (
            "Complete amino acid score (PDCAAS ~ 1.0) achieved via complementary soy and brown rice proteins. "
            "Rich in glucosinolates from cruciferous broccoli supporting phase II hepatic detoxification. "
            "Zero dietary cholesterol and exceptionally low saturated fat profile make this ideal for lipid optimization."
        )
    }
}

# Preset Freshness & Spoilage Diagnostics
FRESHNESS_PRESETS = {
    "fresh_strawberry": {
        "item_name": "Organic Garden Strawberries (Fragaria × ananassa)",
        "category": "Soft Berry Fruit",
        "inspection": {
            "surface_texture": "Firm, turgid epidermis with taut cell walls. Individual achenes (seeds) intact with no weeping exudate.",
            "discoloration": "None observed. Uniform radiant crimson red coloration (cyanidin-3-glucoside anthocyanin peak).",
            "wrinkling": "0% epidermal collapse. High cellular osmotic pressure maintained.",
            "mold_status": "Completely absent. No mycelial growth, hyphae, or sporulation detected."
        },
        "freshness_stage": "Fresh",
        "freshness_score": 96,
        "action_badge": "Safe to consume",
        "action_type": "safe",
        "shelf_life_remaining": "4 to 6 days",
        "food_safety_advice": (
            "Produce is at peak sensory and nutritional quality. Wash gently with cold water immediately before "
            "consumption (never prior to storage to prevent microbial moisture uptake)."
        ),
        "preservation_tips": [
            "Store unwashed in original ventilated clamshell container at 2°C to 4°C (36°F - 39°F).",
            "Place a dry paper towel at the container base to absorb condensation and inhibit Botrytis.",
            "Keep isolated from high ethylene emitters like ripening bananas and apples."
        ]
    },
    "spoiled_strawberry": {
        "item_name": "Post-Harvest Strawberries with Fungal Pathogen Infection",
        "category": "Soft Berry Fruit",
        "inspection": {
            "surface_texture": "Soft, collapsed parenchymal tissue. Extensive maceration with liquid cellular exudate leaking.",
            "discoloration": "Severe enzymatic browning and necrotic dark brown patches across 65% of fruit surface.",
            "wrinkling": "Severe epidermal collapse and shriveling due to cell wall breakdown by polygalacturonase enzymes.",
            "mold_status": "Severe active contamination: Grey mold mycelium (Botrytis cinerea) with visible fungal conidiophores and spore dust."
        },
        "freshness_stage": "Spoiled",
        "freshness_score": 12,
        "action_badge": "Discard immediately",
        "action_type": "danger",
        "shelf_life_remaining": "0 hours (Immediate biological hazard)",
        "food_safety_advice": (
            "DO NOT CONSUME OR TRIM. Soft porous fruits allow invisible fungal hyphae and mycotoxins to penetrate "
            "the entire fruit interior. Consuming risks respiratory irritation, allergic reaction, and gastrointestinal enteritis."
        ),
        "preservation_tips": [
            "Discard immediately into organic compost or sealed waste disposal to prevent airborne spore propagation.",
            "Sanitize refrigerator drawer with food-contact certified sanitizer (chlorine or quat solution 200ppm).",
            "Inspect neighboring fruits in the same container for micro-infections."
        ]
    },
    "moderate_salmon": {
        "item_name": "Atlantic Salmon Fillet (Salmo salar)",
        "category": "Fresh Seafood / Finfish",
        "inspection": {
            "surface_texture": "Marginal elasticity. Muscle fibers show slight gaping with light surface dehydration along edge borders.",
            "discoloration": "Mild oxidation of astaxanthin pigment. Slight gray-brown tinting at peripheral edges; center remains coral.",
            "wrinkling": "Slight dry pellicle formation on thin tail-end portions.",
            "mold_status": "No mold or fungal growth. Normal marine bacterial microflora approaching threshold limit."
        },
        "freshness_stage": "Moderately Fresh",
        "freshness_score": 68,
        "action_badge": "Consume within 24h",
        "action_type": "warning",
        "shelf_life_remaining": "12 to 24 hours max",
        "food_safety_advice": (
            "Must be cooked thoroughly today. Do not consume raw (not sushi grade). Cook to a minimum internal temperature "
            "of 63°C (145°F) measured with a calibrated digital food thermometer to eliminate potential Listeria monocytogenes."
        ),
        "preservation_tips": [
            "Keep on crushed ice or at coldest refrigeration zone (0°C to 2°C / 32°F - 35°F).",
            "Pat dry with clean single-use paper towel to remove surface moisture containing trimethylamine.",
            "If unable to prepare within 24 hours, vacuum-seal and freeze immediately at -18°C (0°F)."
        ]
    },
    "fresh_avocado": {
        "item_name": "Hass Avocado (Persea americana)",
        "category": "Subtropical Fruit / Lipid Source",
        "inspection": {
            "surface_texture": "Pebbled skin yields gently to light thumb pressure. Pedicel stem intact and green beneath cap.",
            "discoloration": "Uniform dark purplish-green exterior. Pulp interior shows zero enzymatic browning or vascular browning.",
            "wrinkling": "Normal cultivar pebbled texture without dehydration creases.",
            "mold_status": "Completely absent. No stem-end rot (Colletotrichum) or fungal sporulation."
        },
        "freshness_stage": "Fresh",
        "freshness_score": 95,
        "action_badge": "Safe to consume",
        "action_type": "safe",
        "shelf_life_remaining": "2 to 3 days at peak ripeness",
        "food_safety_advice": (
            "Ideal 'ready-to-eat' stage. Oil content and creamy texture are optimized for palatability and nutrient absorption."
        ),
        "preservation_tips": [
            "Transfer immediately to refrigerator (4°C) to halt further ripening and enzymatic softening.",
            "If cutting half, keep pit in residual half, brush surface with citric acid / lemon juice, and wrap tightly in cling film.",
            "Keep away from apples if ripening retardation is desired."
        ]
    }
}

# Preset Kitchen Hygiene & Compliance Audits
HYGIENE_PRESETS = {
    "compliant_kitchen": {
        "scenario_name": "Executive Station A - Commercial Prep Galley",
        "overall_score": 96,
        "compliance_grade": "Grade A (Full HACCP & FDA Compliance)",
        "grade_type": "safe",
        "indicators": {
            "hair_containment": {"status": "Compliant (100%)", "details": "All culinary staff equipped with snug hairnets and beard restraints."},
            "glove_usage": {"status": "Compliant (100%)", "details": "Powder-free food grade nitrile gloves worn during ready-to-eat assembly."},
            "workstation_sanitization": {"status": "Compliant (98%)", "details": "Commercial 304-grade stainless steel surfaces spotless, dry, and sanitized with 200ppm quat."},
            "cross_contamination_hazard": {"status": "Zero Hazard (100%)", "details": "Dedicated color-coded prep boards strictly separated (Blue=Seafood, Green=Produce, Red=Raw Meat)."}
        },
        "violations": [
            {
                "id": "OBS-01",
                "severity": "Low Observation",
                "standard": "FDA Food Code § 4-204.112",
                "finding": "Cold-holding line thermometer located 2 inches higher than optimal airflow channel.",
                "corrective_action": "Reposition dial thermometer to the warmest zone of the sandwich prep cooler."
            }
        ],
        "haccp_summary": (
            "Station operates in exemplary compliance with FDA Food Code and ServSafe sanitation protocols. "
            "Pest management barriers intact, chemical sanitizers stored in locked subterranean locker, and cross-contamination "
            "critical control points (CCPs) completely mitigated."
        )
    },
    "violation_kitchen": {
        "scenario_name": "Line Station B - Commercial Prep & Cook Line",
        "overall_score": 48,
        "compliance_grade": "Grade F - Critical Non-Compliance (Shutdown Risk)",
        "grade_type": "danger",
        "indicators": {
            "hair_containment": {"status": "Non-Compliant (35%)", "details": "Multiple line cooks observed with untamed hair and absent beard guards."},
            "glove_usage": {"status": "Critical Violation (20%)", "details": "Bare hand contact with ready-to-eat burger buns and garnishes after handling raw poultry."},
            "workstation_sanitization": {"status": "Non-Compliant (40%)", "details": "Sanitizer cloth resting on prep table in unmeasured dirty water bucket. Food grease accumulation."},
            "cross_contamination_hazard": {"status": "Critical Hazard (0%)", "details": "Raw unshielded chicken breasts placed on cutting board directly adjacent to freshly cut salad greens."}
        },
        "violations": [
            {
                "id": "CRIT-01",
                "severity": "Critical Violation",
                "standard": "HACCP CCP 2 / FDA Food Code § 3-302.11",
                "finding": "Raw poultry juice dripping within 4 inches of ready-to-eat romaine lettuce. Severe Salmonella and Campylobacter risk.",
                "corrective_action": "Immediately condemn and discard exposed lettuce. Sanitize entire counter with 100ppm sodium hypochlorite."
            },
            {
                "id": "CRIT-02",
                "severity": "Critical Violation",
                "standard": "FDA Food Code § 3-301.11(B)",
                "finding": "Bare hand contact with ready-to-eat foods without single-use barrier gloves.",
                "corrective_action": "Staff re-training in 20-second handwashing protocol and mandatory glove donning before touching finished plates."
            },
            {
                "id": "MAJ-01",
                "severity": "Major Violation",
                "standard": "FDA Food Code § 2-402.11",
                "finding": "Culinary handlers lacking hair restraints and beard nets over prep lines.",
                "corrective_action": "Issue mandatory disposable hairnets and beard guards prior to re-entering kitchen."
            },
            {
                "id": "MAJ-02",
                "severity": "Major Violation",
                "standard": "FDA Food Code § 4-601.11",
                "finding": "Wiping cloths stored on food contact tables instead of designated sanitizer solution bucket at 200ppm.",
                "corrective_action": "Submerge all towels into verified quat sanitizer bucket test-stripped to 200-400 ppm."
            }
        ],
        "haccp_summary": (
            "CRITICAL HAZARD DETECTED: Imminent health hazard due to direct raw poultry-to-produce cross-contamination. "
            "Requires immediate supervisory intervention, food condemnation of contaminated items, and 3-step wash-rinse-sanitize reset."
        )
    }
}

# Preset Recipes for Smart Kitchen Assistant
RECIPE_DATABASE = [
    {
        "title": "One-Skillet Mediterranean Lemon Herb Chicken & Quinoa",
        "cuisine": "Mediterranean",
        "prep_time": "10 mins",
        "cook_time": "20 mins",
        "total_time": "30 mins",
        "difficulty": "Easy",
        "servings": 4,
        "calories_per_serving": 460,
        "protein_g": 38,
        "carbs_g": 36,
        "fats_g": 18,
        "matched_ingredients": ["Chicken Breast", "Quinoa", "Olive Oil", "Garlic", "Lemon", "Spinach"],
        "pantry_staples_used": ["Salt", "Black Pepper", "Oregano"],
        "missing_optional": ["Feta Cheese", "Kalamata Olives"],
        "science_note": (
            "High heat searing initiates the Maillard reaction (reducing sugars reacting with amino acids), "
            "creating hundreds of flavorful pyrazine and furan compounds. Citric acid from lemon tenderizes meat by "
            "denaturing tough surface myofibrillar proteins."
        ),
        "steps": [
            "Season diced chicken breasts with salt, pepper, dried oregano, and minced garlic.",
            "Heat 1 tbsp extra virgin olive oil in a heavy stainless steel skillet over medium-high heat until shimmering.",
            "Sear chicken for 5-6 minutes until golden-brown crust forms. Remove and set aside.",
            "Deglaze skillet with 1 cup chicken broth, add rinsed quinoa, cover and simmer on low for 12 minutes.",
            "Fold in fresh baby spinach until wilted, return chicken, and squeeze fresh lemon juice over the pan before serving."
        ],
        "substitutions": [
            {"original": "Quinoa", "substitute": "Brown Rice or Couscous", "ratio": "1:1", "note": "Adjust simmering broth by +1/4 cup for brown rice."},
            {"original": "Chicken Breast", "substitute": "Firm Tofu or Salmon Fillet", "ratio": "1:1", "note": "Reduce cooking time to 4 mins per side for fish/tofu."},
            {"original": "Fresh Lemon", "substitute": "Apple Cider Vinegar or White Wine", "ratio": "1 tbsp ACV per lemon", "note": "Provides requisite acidic brightness."}
        ]
    },
    {
        "title": "Creamy Tuscan Garlic Butter White Bean & Tomato Ragù",
        "cuisine": "Italian Plant-Forward",
        "prep_time": "5 mins",
        "cook_time": "15 mins",
        "total_time": "20 mins",
        "difficulty": "Beginner",
        "servings": 3,
        "calories_per_serving": 340,
        "protein_g": 16,
        "carbs_g": 42,
        "fats_g": 12,
        "matched_ingredients": ["Cannellini / White Beans", "Garlic", "Cherry Tomatoes", "Spinach", "Olive Oil"],
        "pantry_staples_used": ["Salt", "Crushed Red Pepper", "Italian Seasoning"],
        "missing_optional": ["Parmesan Reggiano", "Crusty Sourdough"],
        "science_note": (
            "Cooking tomatoes breaks down rigid cellular pectin, dramatically increasing the bioavailability "
            "of lycopene—a powerful fat-soluble carotenoid antioxidant. Sautéing with olive oil enhances lycopene "
            "micellar incorporation for maximal intestinal absorption."
        ),
        "steps": [
            "Heat olive oil in a wide sauté pan over medium heat. Add smashed garlic cloves and red pepper flakes.",
            "Add whole cherry tomatoes; blister for 4-5 minutes until skins burst and release sweet pectin-rich juices.",
            "Rinse and drain canned cannellini beans, then stir into the pan with 1/3 cup vegetable broth.",
            "Coarsely mash 1/3 of the beans with a wooden spoon to create a luxurious natural creamy starch sauce.",
            "Fold in baby spinach until just wilted. Season with sea salt, cracked pepper, and fresh basil."
        ],
        "substitutions": [
            {"original": "Cannellini Beans", "substitute": "Chickpeas (Garbanzo) or Butter Beans", "ratio": "1:1", "note": "Mash slightly longer for creaminess."},
            {"original": "Spinach", "substitute": "Kale or Swiss Chard", "ratio": "1:1", "note": "Remove tough stems and sauté 2 minutes longer."},
            {"original": "Cherry Tomatoes", "substitute": "Canned Diced San Marzano Tomatoes", "ratio": "1 cup canned", "note": "Simmer down to reduce water content."}
        ]
    },
    {
        "title": "Ginger Scallion Crispy Sesame Tofu & Broccoli Sauté",
        "cuisine": "Asian Fusion",
        "prep_time": "10 mins",
        "cook_time": "15 mins",
        "total_time": "25 mins",
        "difficulty": "Intermediate",
        "servings": 2,
        "calories_per_serving": 380,
        "protein_g": 24,
        "carbs_g": 28,
        "fats_g": 20,
        "matched_ingredients": ["Tofu", "Broccoli", "Soy Sauce / Tamari", "Sesame Oil", "Ginger", "Garlic"],
        "pantry_staples_used": ["Cornstarch", "Chili Flakes"],
        "missing_optional": ["Toasted Sesame Seeds", "Jasmine Rice"],
        "science_note": (
            "Dredging pressed tofu in cornstarch forms an amylose-rich coating that rapidly gelatinizes and dehydrates "
            "when fried in oil, producing an intensely shatter-crisp exterior while preserving moisture inside."
        ),
        "steps": [
            "Press extra-firm tofu with a paper towel for 10 minutes to expel water. Cut into 2cm cubes.",
            "Toss tofu cubes in 1.5 tbsp cornstarch with a pinch of salt until evenly dusted.",
            "Pan-sear in hot sesame and neutral oil for 3 minutes per side until universally golden and crunchy.",
            "Flash-steam broccoli florets with 2 tbsp water in a covered skillet for 3 minutes.",
            "Whisk soy sauce, minced ginger, grated garlic, and a teaspoon of honey; pour over wok and toss 60 seconds to glaze."
        ],
        "substitutions": [
            {"original": "Cornstarch", "substitute": "Tapioca Starch or Rice Flour", "ratio": "1:1", "note": "Produces equally crisp exterior."},
            {"original": "Tofu", "substitute": "Peeled Shrimp or Paneer Cubes", "ratio": "1:1", "note": "Shrimp cooks in just 3 minutes total."},
            {"original": "Soy Sauce", "substitute": "Coconut Aminos or Tamari", "ratio": "1:1", "note": "Tamari keeps dish 100% gluten-free."}
        ]
    }
]

# Preset 7-Day Meal Plans for Personalized Meal Planner
MEAL_PLANS = {
    "Balanced Maintenance": {
        "days": [
            {
                "day": "Monday",
                "breakfast": "Greek Yogurt Parfait with Mixed Berries, Chia Seeds & Almonds (380 kcal, 28g P)",
                "lunch": "Mediterranean Quinoa Bowl with Grilled Chicken Breast & Tahini (540 kcal, 42g P)",
                "dinner": "Pan-Seared Atlantic Salmon with Roasted Asparagus & Sweet Potato (620 kcal, 44g P)",
                "snack": "Apple slices with 1 tbsp Natural Peanut Butter (190 kcal, 4g P)",
                "total_calories": 1730,
                "total_protein": 118
            },
            {
                "day": "Tuesday",
                "breakfast": "Sourdough Toast with 2 Poached Eggs, Sliced Avocado & Microgreens (460 kcal, 22g P)",
                "lunch": "Turkey & Spinach Wrap with Hummus, Cucumbers & Feta (490 kcal, 38g P)",
                "dinner": "Grass-Fed Lean Beef Stir-Fry with Broccoli, Bell Peppers & Jasmine Rice (590 kcal, 45g P)",
                "snack": "Cottage Cheese with Pineapple chunks (170 kcal, 18g P)",
                "total_calories": 1710,
                "total_protein": 123
            },
            {
                "day": "Wednesday",
                "breakfast": "Overnight Rolled Oats with Whey/Plant Protein, Flaxseeds & Blueberries (420 kcal, 32g P)",
                "lunch": "Tuna Salad Nicoise with Hard-Boiled Eggs, Green Beans & Olive Oil Vinaigrette (510 kcal, 44g P)",
                "dinner": "Lemon Herb Baked Chicken Thighs with Roasted Cauliflower & Wild Rice (580 kcal, 40g P)",
                "snack": "Handful of Raw Walnuts & Dark Chocolate Square (210 kcal, 5g P)",
                "total_calories": 1720,
                "total_protein": 121
            },
            {
                "day": "Thursday",
                "breakfast": "Egg White & Spinach Omelet with Feta Cheese and Whole Grain Toast (390 kcal, 30g P)",
                "lunch": "Lentil & Kale Soup with Grilled Chicken Skewers (530 kcal, 41g P)",
                "dinner": "Seared Cod Fillet with Garlic Sautéed Spinach & Polenta (540 kcal, 43g P)",
                "snack": "Edamame in the pod sprinkled with Sea Salt (160 kcal, 14g P)",
                "total_calories": 1620,
                "total_protein": 128
            },
            {
                "day": "Friday",
                "breakfast": "Protein Smoothie: Spinach, Frozen Banana, Whey/Pea Protein & Almond Milk (370 kcal, 30g P)",
                "lunch": "Mexican Burrito Bowl: Black Beans, Fajita Veggies, Grilled Chicken & Salsa (560 kcal, 42g P)",
                "dinner": "Shrimp Scampi with Zucchini Ribbons & Whole Wheat Linguine (530 kcal, 38g P)",
                "snack": "Carrot and Celery sticks with 3 tbsp Traditional Hummus (150 kcal, 4g P)",
                "total_calories": 1610,
                "total_protein": 114
            },
            {
                "day": "Saturday",
                "breakfast": "Whole Grain Banana Protein Pancakes with Pure Maple Drizzle (440 kcal, 26g P)",
                "lunch": "Grilled Chicken Caesar Salad with Shaved Parmesan & Sourdough Croutons (520 kcal, 45g P)",
                "dinner": "Teriyaki Glazed Salmon with Steamed Bok Choy & Brown Rice (610 kcal, 42g P)",
                "snack": "Roasted Salted Pumpkin Seeds (Pepitas) (180 kcal, 9g P)",
                "total_calories": 1750,
                "total_protein": 122
            },
            {
                "day": "Sunday",
                "breakfast": "Smoked Salmon & Scrambled Eggs with Sliced Tomatoes & English Muffin (430 kcal, 34g P)",
                "lunch": "Warm Quinoa Salad with Roasted Sweet Potato, Chickpeas & Herb Tahini (510 kcal, 20g P)",
                "dinner": "Slow-Roasted Herb Pork Tenderloin with Sautéed Green Beans & Baby Red Potatoes (570 kcal, 46g P)",
                "snack": "Mixed Berry Bowl with Drizzled Raw Honey (120 kcal, 2g P)",
                "total_calories": 1630,
                "total_protein": 102
            }
        ],
        "shopping_list": {
            "Produce": ["Baby Spinach (2 large tubs)", "Organic Blueberries & Strawberries", "Broccoli Crowns (2)", "Avocados (4)", "Lemons & Limes", "Sweet Potatoes (3)", "Asparagus (1 bunch)", "Cherry Tomatoes", "Bananas (1 bunch)"],
            "Proteins": ["Boneless Skinless Chicken Breasts (1.5 kg)", "Wild Atlantic Salmon Fillets (4 count)", "Free-Range Large Eggs (2 dozen)", "Cod / White Fish Fillets (2 count)", "Lean Ground Turkey (500g)", "Shrimp (peeled, 400g)"],
            "Dairy & Refrigerated": ["Non-Fat Greek Yogurt (1 kg)", "Cottage Cheese (500g)", "Feta Cheese crumbles", "Almond Milk (Unsweetened)", "Prepared Hummus (1 tub)"],
            "Pantry & Grains": ["Tricolor Organic Quinoa (500g)", "Rolled Oats (1 bag)", "Brown Jasmine Rice", "Whole Wheat Wrap Tortillas", "Canned Cannellini Beans & Black Beans", "Artisanal Sourdough Loaf"],
            "Healthy Fats & Seasonings": ["Extra Virgin Olive Oil", "Raw Walnuts & Pumpkin Seeds", "Chia Seeds", "Tahini Paste", "Sesame Oil", "Dijon Mustard"]
        }
    }
}

