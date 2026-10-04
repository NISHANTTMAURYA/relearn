import os
import json
import sys
from typing import Dict, List, Any, Optional

# Ensure relearn root is in path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

try:
    from dataset.scripts.curriculum_families import CURRICULUM_FAMILIES
except ImportError:
    CURRICULUM_FAMILIES = []

def load_json(rel_path: str) -> Any:
    full_path = os.path.join(DATASET_DIR, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

class ReLearnDataService:
    def __init__(self):
        self.taxonomy = load_json(os.path.join("misconception_taxonomy", "master_misconception_index.json"))
        self.item_banks = {
            "optics": load_json(os.path.join("diagnostic_item_bank", "light_reflection_refraction.json")),
            "human_eye": load_json(os.path.join("diagnostic_item_bank", "human_eye_colourful_world.json")),
            "electricity": load_json(os.path.join("diagnostic_item_bank", "electricity.json")),
            "magnetism": load_json(os.path.join("diagnostic_item_bank", "magnetic_effects.json")),
        }
        self.interventions_data = load_json(os.path.join("adaptive_interventions", "intervention_catalogue.json"))
        self.reassessment_data = load_json(os.path.join("adaptive_interventions", "reassessment_item_pairs.json"))
        self.disambiguation_data = load_json(os.path.join("diagnostic_discrimination_pairs", "disambiguation_cases.json"))
        self.curriculum_families = CURRICULUM_FAMILIES

        # Pre-index interventions by target_misconception_id
        self.interventions_map: Dict[str, dict] = {}
        for item in self.interventions_data.get("interventions", []):
            misc_id = item.get("target_misconception_id")
            if misc_id:
                self.interventions_map[misc_id] = item

        # Pre-index reassessment items by target_misconception_id
        self.reassessment_map: Dict[str, dict] = {}
        for pair in self.reassessment_data.get("reassessment_pairs", []):
            misc_id = pair.get("target_misconception_id")
            if misc_id:
                self.reassessment_map[misc_id] = pair

        # Build comprehensive catalog for any remaining curriculum misconceptions
        self._build_expanded_interventions_and_reassessments()

    def _build_expanded_interventions_and_reassessments(self):
        """Ensure all 21 NCERT misconceptions and 42 families have rich POE interventions, PhET references, and whiteboard commands."""
        for fam in self.curriculum_families:
            target_misc = fam.get("target_misc", "")
            misc_id = target_misc.split(":")[0].strip() if ":" in target_misc else target_misc
            if not misc_id:
                continue

            # Extract whiteboard commands and diagram metadata
            diag_meta = fam.get("diagram_meta", {})
            wb_commands = diag_meta.get("whiteboard_commands", [
                "draw_axes(x_label='Domain', y_label='Effect')",
                "plot_concept_boundary()",
                f"write_equation('{fam.get('chapter', 'Physics')}')"
            ])

            # PhET simulation URL heuristics
            chapter = fam.get("chapter", "").lower()
            topic = fam.get("topic", "").lower()
            if "electric" in chapter or "circuit" in topic:
                sim_name = "Circuit Construction Kit: DC"
                sim_url = "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_all.html"
            elif "optic" in chapter or "lens" in topic or "mirror" in topic or "light" in chapter:
                sim_name = "Geometric Optics"
                sim_url = "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_all.html"
            elif "eye" in chapter or "colour" in chapter or "refraction" in topic:
                sim_name = "Bending Light & Prisms"
                sim_url = "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_all.html"
            elif "magnet" in chapter:
                sim_name = "Faraday's Electromagnetic Lab"
                sim_url = "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html"
            elif "gravitat" in chapter or "motion" in chapter:
                sim_name = "Forces and Motion: Basics"
                sim_url = "https://phet.colorado.edu/sims/html/forces-and-motion-basics/latest/forces-and-motion-basics_all.html"
            else:
                sim_name = "Energy Skate Park: Basics"
                sim_url = "https://phet.colorado.edu/sims/html/energy-skate-park-basics/latest/energy-skate-park-basics_all.html"

            if misc_id not in self.interventions_map:
                self.interventions_map[misc_id] = {
                    "intervention_id": f"INTV-{misc_id}",
                    "target_misconception_id": misc_id,
                    "misconception_name": target_misc.split(":", 1)[1].strip() if ":" in target_misc else fam.get("family"),
                    "pedagogical_strategy": "Predict-Observe-Explain (POE) with Dynamic Whiteboard & PhET Simulation",
                    "simulation_reference": {
                        "platform": "PhET Interactive Simulations (Univ. of Colorado Boulder)",
                        "simulation_name": sim_name,
                        "url": sim_url
                    },
                    "guided_learning_sequence": {
                        "step_1_predict": f"Consider the physical configuration: {fam.get('stem_templates', [''])[0].replace('{f}', '15').replace('{v}', '20')}. Predict what will happen before applying formulas.",
                        "step_2_observe": f"Launch the {sim_name} simulation or observe the interactive whiteboard trace below. Notice how the physical field/quantities interact without relying on superficial intuition.",
                        "step_3_explain_cognitive_conflict": f"Notice the contradiction with the naive expectation: {fam.get('misc_desc')}. Why does nature contradict this intuition?",
                        "step_4_conceptual_bridge": fam.get("correct_base", "Ground truth scientific principle: conservation laws and causal mechanics strictly govern the observed phenomenon.")
                    },
                    "whiteboard_commands": wb_commands,
                    "diagram_meta": diag_meta
                }
            else:
                # Augment existing intervention with whiteboard commands if missing
                if "whiteboard_commands" not in self.interventions_map[misc_id]:
                    self.interventions_map[misc_id]["whiteboard_commands"] = wb_commands
                if "diagram_meta" not in self.interventions_map[misc_id]:
                    self.interventions_map[misc_id]["diagram_meta"] = diag_meta

            # Check reassessment item
            if misc_id not in self.reassessment_map:
                # Synthesize high quality near-transfer pair
                stem = fam.get("stem_templates", ["A new isomorphic transfer scenario testing the same core physical law:"])[-1]
                stem = stem.replace("{f}", "25").replace("{v}", "30").replace("{r}", "50")
                correct_opt = fam.get("correct_phrasings", ["Physical conservation law holds; effect is distributed uniformly."])[0]
                distractor_opt = fam.get("misc_phrasings", ["Local component directly cuts the output effect in half."])[0]
                slip_opt = "Calculation results in an unexpected sign reversal due to index convention."

                self.reassessment_map[misc_id] = {
                    "pair_id": f"PAIR-{misc_id}",
                    "target_misconception_id": misc_id,
                    "post_intervention_reassessment_item": {
                        "item_id": f"REASSESS-{misc_id}",
                        "question_type": "isomorphic_near_transfer",
                        "stem": stem,
                        "options": [
                            {
                                "key": "A",
                                "text": distractor_opt,
                                "is_correct": False,
                                "indicates_persistent_misconception": misc_id
                            },
                            {
                                "key": "B",
                                "text": correct_opt,
                                "is_correct": True,
                                "indicates_persistent_misconception": None
                            },
                            {
                                "key": "C",
                                "text": slip_opt,
                                "is_correct": False,
                                "indicates_persistent_misconception": "CARELESS_CALCULATION_SLIP"
                            }
                        ],
                        "correct_answer": "B",
                        "reassessment_diagnostic_rule": f"Selecting Option B confirms conceptual resolution with transfer for {misc_id}. Option A shows persistent naive model."
                    }
                }

    def get_topics_and_questions(self) -> List[dict]:
        """Aggregate curriculum chapters and curated questions for student selection."""
        topics = [
            {
                "id": "optics",
                "grade": "Class 10",
                "chapter": "Light – Reflection and Refraction",
                "summary": "Ray optics, spherical mirrors & lenses, Cartesian sign conventions, and image formation dynamics.",
                "total_items": len(self.item_banks["optics"].get("questions", [])),
                "questions": self._format_items_with_curriculum(self.item_banks["optics"].get("questions", []), "OPTICS")
            },
            {
                "id": "human_eye",
                "grade": "Class 10",
                "chapter": "The Human Eye and Colourful World",
                "summary": "Defects of vision (myopia, hypermetropia), atmospheric refraction, and prism dispersion.",
                "total_items": len(self.item_banks["human_eye"].get("questions", [])),
                "questions": self._format_items_with_curriculum(self.item_banks["human_eye"].get("questions", []), "EYE")
            },
            {
                "id": "electricity",
                "grade": "Class 10",
                "chapter": "Electricity",
                "summary": "Ohm's law, series vs parallel networks, current conservation, and electric power.",
                "total_items": len(self.item_banks["electricity"].get("questions", [])),
                "questions": self._format_items_with_curriculum(self.item_banks["electricity"].get("questions", []), "ELEC")
            },
            {
                "id": "magnetism",
                "grade": "Class 10",
                "chapter": "Magnetic Effects of Electric Current",
                "summary": "Magnetic field lines, solenoid dynamics, Lorentz force, and electromagnetic induction.",
                "total_items": len(self.item_banks["magnetism"].get("questions", [])),
                "questions": self._format_items_with_curriculum(self.item_banks["magnetism"].get("questions", []), "MAG")
            },
            {
                "id": "mechanics",
                "grade": "Class 9",
                "chapter": "Motion, Force & Gravitation",
                "summary": "Speed vs acceleration, Newton's third law pairs, inertia, and free fall gravitational mass invariance.",
                "total_items": 4,
                "questions": self._get_mechanics_sample_items()
            }
        ]
        return topics

    def _format_items_with_curriculum(self, items: list, prefix: str) -> list:
        formatted = []
        modalities = ["mcq", "typed_theory", "numerical", "diagram_sketch", "ocr_photo"]
        
        for idx, it in enumerate(items):
            q_id = it.get("question_id")
            matched_fam = next((f for f in self.curriculum_families if prefix in f.get("family", "")), None)
            formatted.append({
                "question_id": q_id,
                "question_type": modalities[idx % len(modalities)],
                "cognitive_level": it.get("cognitive_level", "Comprehension"),
                "stem": it.get("stem"),
                "options": it.get("options", []),
                "correct_answer": it.get("correct_answer"),
                "authoritative_solution": it.get("authoritative_solution"),
                "diagram_meta": matched_fam.get("diagram_meta") if matched_fam else None,
                "sample_misconception_responses": matched_fam.get("misc_phrasings", [])[:3] if matched_fam else [],
                "sample_correct_responses": matched_fam.get("correct_phrasings", [])[:2] if matched_fam else [],
                "sample_slip_responses": matched_fam.get("slip_phrasings", [])[:2] if matched_fam else []
            })
        
        # Ensure at least 10 questions for full comprehensive exam session
        matching_fams = [f for f in self.curriculum_families if prefix in f.get("family", "")]
        if not matching_fams:
            matching_fams = self.curriculum_families

        while len(formatted) < 10:
            count = len(formatted) + 1
            fam = matching_fams[(count - 1) % len(matching_fams)]
            stem_template = fam.get("stem_templates", ["Explain the physical mechanism in {f}."])[0]
            stem = stem_template.format(f=20, d=15, v=12, slip=30) if "{f}" in stem_template else stem_template

            mod_type = modalities[(count - 1) % len(modalities)]
            formatted.append({
                "question_id": f"DIAG-{prefix}-{count:03d}",
                "question_type": mod_type,
                "cognitive_level": "Analysis" if count % 2 == 0 else "Application",
                "stem": f"Question {count}: {stem}",
                "options": [
                    {"key": "A", "text": fam.get("misc_phrasings", ["Intuitive naive response"])[0], "is_correct": False, "diagnosed_misconception_id": fam.get("target_misc", "").split(":")[0]},
                    {"key": "B", "text": fam.get("correct_phrasings", ["Authoritative NCERT physical law solution"])[0], "is_correct": True, "diagnosed_misconception_id": None},
                    {"key": "C", "text": "Calculation slip due to arithmetic sign convention error.", "is_correct": False, "diagnosed_misconception_id": "MISC-CALC-SLIP"}
                ],
                "correct_answer": "B",
                "authoritative_solution": fam.get("correct_base", "Apply NCERT physics principles."),
                "diagram_meta": fam.get("diagram_meta"),
                "sample_misconception_responses": fam.get("misc_phrasings", [])[:3],
                "sample_correct_responses": fam.get("correct_phrasings", [])[:2],
                "sample_slip_responses": fam.get("slip_phrasings", [])[:2]
            })

        return formatted

    def _get_mechanics_sample_items(self) -> list:
        return [
            {
                "question_id": "DIAG-MECH-001",
                "question_type": "conceptual",
                "cognitive_level": "Analysis",
                "stem": "Two spheres, one made of solid lead (mass 10 kg) and one of hollow aluminum (mass 0.5 kg), are dropped simultaneously from a height of 25 meters in a tall evacuated vacuum cylinder. Which sphere reaches the ground first?",
                "options": [
                    {
                        "key": "A",
                        "text": "The 10 kg lead sphere reaches first because gravity pulls heavier masses with much greater downward force.",
                        "is_correct": False,
                        "diagnosed_misconception_id": "MISC-GRAV-001"
                    },
                    {
                        "key": "B",
                        "text": "Both spheres hit the ground at the exact same instant, because gravitational acceleration g = GM/R^2 is independent of the falling body's mass.",
                        "is_correct": True,
                        "diagnosed_misconception_id": None
                    },
                    {
                        "key": "C",
                        "text": "The 0.5 kg sphere reaches first because lighter objects face lower gravitational inertia.",
                        "is_correct": False,
                        "diagnosed_misconception_id": "MISC-GRAV-002"
                    }
                ],
                "correct_answer": "B",
                "authoritative_solution": "In free fall with negligible air resistance, acceleration a = F/m = (G*M*m/r^2)/m = G*M/r^2. The mass m of the object cancels out identically.",
                "sample_misconception_responses": [
                    "Heavy sphere lands first because larger mass means stronger gravitational pull speeding it up.",
                    "Lead ball is heavier so gravity pulls it down faster to the floor."
                ],
                "sample_correct_responses": [
                    "Both hit simultaneously because acceleration due to gravity is 9.8 m/s^2 for all objects regardless of mass."
                ],
                "sample_slip_responses": [
                    "Both hit simultaneously after exactly 5.1 seconds (miscalculated t = sqrt(2h/g))."
                ]
            },
            {
                "question_id": "DIAG-MECH-002",
                "question_type": "conceptual",
                "cognitive_level": "Application",
                "stem": "A heavy transport truck collides head-on with a small compact car. During the collision, how does the magnitude of the force exerted by the truck on the car compare to the force exerted by the car on the truck?",
                "options": [
                    {
                        "key": "A",
                        "text": "The truck exerts a significantly greater force on the car because it possesses far more mass and momentum.",
                        "is_correct": False,
                        "diagnosed_misconception_id": "MISC-MOT-003"
                    },
                    {
                        "key": "B",
                        "text": "Both vehicles exert forces of exactly equal magnitude on each other, according to Newton's Third Law (action-reaction pairs).",
                        "is_correct": True,
                        "diagnosed_misconception_id": None
                    },
                    {
                        "key": "C",
                        "text": "The car exerts more force on the truck because it experiences greater deceleration.",
                        "is_correct": False,
                        "diagnosed_misconception_id": "MISC-MOT-004"
                    }
                ],
                "correct_answer": "B",
                "authoritative_solution": "By Newton's Third Law, forces always occur in matched interaction pairs of equal magnitude and opposite direction (F_truck_on_car = -F_car_on_truck). The car suffers more damage and acceleration because of its smaller mass (a = F/m), not because the force was larger.",
                "sample_misconception_responses": [
                    "Truck applies way more force because it's massive and moving with heavy momentum.",
                    "The bigger vehicle hits harder so the truck's force is definitely larger."
                ],
                "sample_correct_responses": [
                    "The forces are equal and opposite by Newton's 3rd law; the car accelerates more because of a = F/m."
                ],
                "sample_slip_responses": [
                    "Forces are equal, but impulse is measured in Joules instead of N*s."
                ]
            }
        ]

    def get_taxonomy_index(self) -> dict:
        return self.taxonomy

    def get_disambiguation_cases(self) -> dict:
        return self.disambiguation_data

    def get_intervention(self, misc_id: str) -> Optional[dict]:
        # Handle formats like "MISC-OPT-001" or full strings
        code = misc_id.split(":")[0].strip()
        intv = self.interventions_map.get(code)
        if not intv:
            # Try fuzzy match
            for k, v in self.interventions_map.items():
                if k in code or code in k:
                    return v
            # Fallback to default first intervention
            return list(self.interventions_map.values())[0] if self.interventions_map else None
        return intv

    def get_reassessment(self, misc_id: str) -> Optional[dict]:
        code = misc_id.split(":")[0].strip()
        pair = self.reassessment_map.get(code)
        if not pair:
            for k, v in self.reassessment_map.items():
                if k in code or code in k:
                    return v
            return list(self.reassessment_map.values())[0] if self.reassessment_map else None
        return pair
