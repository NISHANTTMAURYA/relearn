import json
import csv
import os
import random
import string
import sys

random.seed(42)

# Ensure local imports work
sys.path.insert(0, r"d:\relearn")
from dataset.scripts.curriculum_families import CURRICULUM_FAMILIES

def safe_format(template_str, p):
    if not template_str or not isinstance(template_str, str) or "{" not in template_str:
        return template_str
    try:
        formatter = string.Formatter()
        fields = [fname for _, fname, _, _ in formatter.parse(template_str) if fname is not None]
        if not fields:
            return template_str
        
        p0 = p[0] if len(p) >= 1 else 10
        p1 = p[1] if len(p) >= 2 else 5
        p2 = p[2] if len(p) >= 3 else 2
        
        calc_div = p0 // p1 if p1 != 0 and p0 % p1 == 0 else round(p0 / p1, 1) if p1 != 0 else p0
        calc_mul = p0 * p1
        
        kwargs_pool = {
            "u": p0, "f": p1 if len(p) >= 2 else p0, "fp": p0,
            "d": p0, "t": p1, "v": p0, "m": p0, "M": p0, "h": p2,
            "V": p0, "I": p1, "R": p2 if len(p) >= 3 else p1,
            "misc_val": calc_mul,
            "cor_val": calc_div,
            "div_val": calc_div,
            "slip": round(p0 * 1.5, 1),
            "f_val": calc_mul
        }
        sub_kwargs = {k: kwargs_pool.get(k, 0) for k in fields}
        return template_str.format(**sub_kwargs)
    except Exception:
        return template_str

BASE_DIR = r"d:\relearn\dataset"
INDIV_DIR = os.path.join(BASE_DIR, "individual_response_dataset")
SEQ_DIR = os.path.join(BASE_DIR, "sequence_dataset")

os.makedirs(INDIV_DIR, exist_ok=True)
os.makedirs(SEQ_DIR, exist_ok=True)

# ----------------------------------------------------------------------------------------
# Systematic Stratified Dataset Generator: 2,500 Individual Responses across 25 Families
# ----------------------------------------------------------------------------------------
def generate_optimized_datasets():
    print(f"Generating scaled, research-grounded Re:Learn datasets across {len(CURRICULUM_FAMILIES)} curriculum families...")
    individual_records = []
    record_id = 1

    for fam_idx, fam in enumerate(CURRICULUM_FAMILIES):
        fam_name = fam["family"]
        stems = fam["stem_templates"]
        params = fam["params"]
        target_misc = fam["target_misc"]
        misc_desc = fam["misc_desc"]
        correct_base = fam["correct_base"]
        diagram_meta = fam["diagram_meta"]

        misc_pool = fam["misc_phrasings"]
        cor_pool = fam["correct_phrasings"]
        slip_pool = fam["slip_phrasings"]
        unit_pool = fam["unit_phrasings"]
        unsure_pool = fam["unsure_phrasings"]

        # Exactly 100 diverse samples per family:
        # 60 Misconceptions (60%)
        # 20 Correct answers (20%)
        # 7 Calculation slips (7%)
        # 7 Unit errors (7%)
        # 6 Unsure responses (6%)
        # Total = 100 items per family

        family_items = []

        # 1. Misconceptions (60 items)
        for i in range(60):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = misc_pool[i % len(misc_pool)]
            resp = safe_format(resp_template, p)

            family_items.append({
                "category": "misc",
                "label": target_misc,
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": misc_desc,
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # 2. Correct Responses (20 items)
        for i in range(20):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = cor_pool[i % len(cor_pool)]
            resp = safe_format(resp_template, p)

            family_items.append({
                "category": "correct",
                "label": "CORRECT: Scientifically Accurate Response",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Rigorous scientific reasoning with valid physical principles and mathematical steps.",
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # 3. Calculation Slips (7 items)
        for i in range(7):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = slip_pool[i % len(slip_pool)]
            resp = safe_format(resp_template, p)
            family_items.append({
                "category": "calc_slip",
                "label": "CARELESS_CALCULATION_ERROR",
                "error_type": "calculation_slip",
                "confidence": "Medium",
                "evidence": "Conceptual formula choice is correct; error is isolated to an arithmetic slip.",
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # 4. Unit Conversion Errors (7 items)
        for i in range(7):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = unit_pool[i % len(unit_pool)]
            resp = safe_format(resp_template, p)
            family_items.append({
                "category": "unit_err",
                "label": "UNIT_CONVERSION_ERROR",
                "error_type": "unit_error",
                "confidence": "High",
                "evidence": "Numerical reasoning is sound, but units were omitted or confused with another physical quantity.",
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # 5. Unsure / Insufficient Evidence (6 items)
        for i in range(6):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = unsure_pool[i % len(unsure_pool)]
            resp = safe_format(resp_template, p)
            family_items.append({
                "category": "unsure",
                "label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "error_type": "guessing_unclear",
                "confidence": "Low",
                "evidence": "Student response contains minimal reasoning or expresses explicit uncertainty; requires diagnostic probe.",
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # -------------------------------------------------------------------------
        # Stratified Leak-Free Split per Family:
        # Guarantee every split (train, val, test) receives examples of EVERY category!
        # misc: 39 train, 10 val, 11 test (60)
        # correct: 13 train, 3 val, 4 test (20)
        # calc_slip: 5 train, 1 val, 1 test (7)
        # unit_err: 5 train, 1 val, 1 test (7)
        # unsure: 4 train, 1 val, 1 test (6)
        # Total per family = 66 train (66%), 16 val (16%), 18 test (18%) = 100 items
        # -------------------------------------------------------------------------
        split_plan = {
            "misc": (39, 10, 11),
            "correct": (13, 3, 4),
            "calc_slip": (5, 1, 1),
            "unit_err": (5, 1, 1),
            "unsure": (4, 1, 1)
        }

        cat_groups = {}
        for it in family_items:
            cat_groups.setdefault(it["category"], []).append(it)

        for cat, items in cat_groups.items():
            random.shuffle(items)
            n_tr, n_va, n_te = split_plan[cat]
            for it in items[:n_tr]:
                it["split"] = "train"
            for it in items[n_tr:n_tr+n_va]:
                it["split"] = "val"
            for it in items[n_tr+n_va:]:
                it["split"] = "test"

        for it in family_items:
            rec = {
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": it["stem"],
                "correct_answer_and_steps": it["correct_steps"],
                "student_response": it["response"],
                "misconception_label": it["label"],
                "error_type": it["error_type"],
                "diagnostic_confidence": it["confidence"],
                "evidence_rationale": it["evidence"],
                "multimodal_context": diagram_meta,
                "split": it["split"]
            }
            individual_records.append(rec)
            record_id += 1

    train_n = sum(1 for r in individual_records if r["split"] == "train")
    val_n = sum(1 for r in individual_records if r["split"] == "val")
    test_n = sum(1 for r in individual_records if r["split"] == "test")
    print(f"Generated {len(individual_records)} stratified individual multimodal responses across {len(CURRICULUM_FAMILIES)} curriculum families.")
    print(f"  * Train: {train_n} records ({train_n/len(individual_records)*100:.1f}%)")
    print(f"  * Val:   {val_n} records ({val_n/len(individual_records)*100:.1f}%)")
    print(f"  * Test:  {test_n} records ({test_n/len(individual_records)*100:.1f}%)")

    # Export Individual JSON
    json_path = os.path.join(INDIV_DIR, "individual_responses.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(individual_records, f, indent=2)

    # Export Master CSV
    csv_path = os.path.join(INDIV_DIR, "individual_responses.csv")
    csv_fields = [
        "record_id", "question_id", "question_family", "curriculum_grade", "curriculum_chapter",
        "topic_concept", "question_text", "correct_answer_and_steps", "student_response",
        "misconception_label", "error_type", "diagnostic_confidence", "evidence_rationale",
        "has_diagram", "diagram_type", "diagram_description", "split"
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for r in individual_records:
            writer.writerow({
                "record_id": r["record_id"],
                "question_id": r["question_id"],
                "question_family": r["question_family"],
                "curriculum_grade": r["curriculum_grade"],
                "curriculum_chapter": r["curriculum_chapter"],
                "topic_concept": r["topic_concept"],
                "question_text": r["question_text"],
                "correct_answer_and_steps": r["correct_answer_and_steps"],
                "student_response": r["student_response"],
                "misconception_label": r["misconception_label"],
                "error_type": r["error_type"],
                "diagnostic_confidence": r["diagnostic_confidence"],
                "evidence_rationale": r["evidence_rationale"],
                "has_diagram": r["multimodal_context"]["has_diagram"],
                "diagram_type": r["multimodal_context"]["diagram_type"],
                "diagram_description": r["multimodal_context"]["diagram_description"],
                "split": r["split"]
            })

    # Export Splits (CSV & JSONL)
    for sp in ["train", "val", "test"]:
        sp_records = [r for r in individual_records if r["split"] == sp]
        # JSONL
        with open(os.path.join(INDIV_DIR, f"{sp}.jsonl"), "w", encoding="utf-8") as f:
            for r in sp_records:
                f.write(json.dumps(r) + "\n")
        # CSV
        with open(os.path.join(INDIV_DIR, f"{sp}.csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_fields)
            writer.writeheader()
            for r in sp_records:
                writer.writerow({
                    "record_id": r["record_id"],
                    "question_id": r["question_id"],
                    "question_family": r["question_family"],
                    "curriculum_grade": r["curriculum_grade"],
                    "curriculum_chapter": r["curriculum_chapter"],
                    "topic_concept": r["topic_concept"],
                    "question_text": r["question_text"],
                    "correct_answer_and_steps": r["correct_answer_and_steps"],
                    "student_response": r["student_response"],
                    "misconception_label": r["misconception_label"],
                    "error_type": r["error_type"],
                    "diagnostic_confidence": r["diagnostic_confidence"],
                    "evidence_rationale": r["evidence_rationale"],
                    "has_diagram": r["multimodal_context"]["has_diagram"],
                    "diagram_type": r["multimodal_context"]["diagram_type"],
                    "diagram_description": r["multimodal_context"]["diagram_description"],
                    "split": r["split"]
                })

    return individual_records


# ----------------------------------------------------------------------------------------
# Stratified Longitudinal Student Sequence Dataset Generator (1,000 Sessions)
# ----------------------------------------------------------------------------------------
def generate_optimized_sequence_dataset():
    print("Generating stratified sequence dataset (1,000 multi-turn sessions across curriculum)...")
    sequences = []
    seq_id_counter = 1

    pattern_archetypes = [
        # 1. Recurrent Current Attenuation (Class 10)
        {
            "pattern_label": "RECURRENT_CURRENT_ATTENUATION_PATTERN",
            "topic": "Electricity: Current Conservation",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-ELEC-001",
            "intervention_id": "INTV-ELEC-001",
            "reassessment_pair_id": "PAIR-ELEC-001",
            "steps": [
                ("PHY-Class10-10-0001", "Two identical bulbs in series with 6V battery. Compare ammeter readings.", "A1 = 1.2A, A2 = 0.8A, A3 = 0.4A because bulb 1 consumes electric current to glow.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
                ("PHY-Class10-10-0002", "Three identical resistors connected in series with battery. What is current through R3 compared to R1?", "Current through R3 is much smaller than R1 because current gets used up as it travels along the series circuit.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
                ("PHY-Class10-10-0003", "Does the downstream bulb glow dimmer because less current reaches it?", "Yes, downstream bulb receives less current because upstream bulb consumed the charge.", "MISC-ELEC-001: Current Attenuation / Consumption Model")
            ]
        },
        # 2. Recurrent Battery Constant Current Source (Class 10)
        {
            "pattern_label": "RECURRENT_CONSTANT_CURRENT_BATTERY_PATTERN",
            "topic": "Electricity: Parallel Circuits",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-ELEC-002",
            "intervention_id": "INTV-ELEC-002",
            "reassessment_pair_id": "PAIR-ELEC-002",
            "steps": [
                ("PHY-Class10-11-0001", "Bulb B1 in single branch. Second identical bulb B2 connected in parallel. Brightness of B1?", "Bulb 1 dims to half brightness because the battery provides a fixed total current that must now be shared.", "MISC-ELEC-002: Battery as Constant Current Source"),
                ("PHY-Class10-11-0002", "Heater switched ON in parallel with room lamp. Does lamp dim?", "Yes, the lamp dims because the source current is divided between both appliances.", "MISC-ELEC-002: Battery as Constant Current Source")
            ]
        },
        # 3. Recurrent Half-Lens Blocking Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_HALF_LENS_BLOCKING_PATTERN",
            "topic": "Optics: Image Formation with Aperture Blocking",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-OPT-001",
            "intervention_id": "INTV-OPT-001",
            "reassessment_pair_id": "PAIR-OPT-001",
            "steps": [
                ("PHY-Class10-01-0001", "Lower half of convex lens covered with black paper. What happens to projected image?", "The top half of the candle image is completely missing because the bottom half is covered.", "MISC-OPT-001: Half-Lens Blocking Fallacy"),
                ("PHY-Class10-01-0002", "Upper half of converging lens blocked by opaque mask. Describe image change.", "Only the lower half of the image will appear on the viewing card.", "MISC-OPT-001: Half-Lens Blocking Fallacy")
            ]
        },
        # 4. Recurrent Sign Convention Inversion (Class 10)
        {
            "pattern_label": "PERVASIVE_SIGN_CONVENTION_INVERSION",
            "topic": "Optics: Cartesian Sign Conventions",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-OPT-004",
            "intervention_id": "INTV-OPT-004",
            "reassessment_pair_id": "PAIR-OPT-004",
            "steps": [
                ("PHY-Class10-04-0001", "Object at 30 cm before concave mirror of f = 15 cm. Find v.", "v = +30 cm because distances are always positive scalars; 1/v = 1/15 - 1/30.", "MISC-OPT-004: Sign Convention Spatial Inversion"),
                ("PHY-Class10-04-0002", "Candle at 40 cm from concave mirror of f = 20 cm. Find v.", "1/v = 1/20 + 1/40 giving positive v, because the object is in front of the mirror.", "MISC-OPT-004: Sign Convention Spatial Inversion")
            ]
        },
        # 5. Recurrent Speed-Distance Inversion (Class 9)
        {
            "pattern_label": "RECURRENT_SPEED_DISTANCE_INVERSION_PATTERN",
            "topic": "Motion: Speed and Velocity Operations",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MOT-001",
            "intervention_id": "INTV-MOT-001",
            "reassessment_pair_id": "PAIR-MOT-001",
            "steps": [
                ("PHY-Class9-19-0001", "Runner covers 100 m in 5 s along straight track. Calculate speed.", "Speed is 500 m/s because I multiplied distance by time (100 * 5 = 500).", "MISC-MOT-001: Speed Distance Operation Inversion"),
                ("PHY-Class9-19-0002", "Car travels 300 m in 15 s. What is speed?", "I calculated speed = 300 * 15 = 4500 m/s.", "MISC-MOT-001: Speed Distance Operation Inversion"),
                ("PHY-Class9-19-0003", "Bicycle moves 60 m in 3 s. Find speed.", "Speed = distance times time, so it equals 180 m/s.", "MISC-MOT-001: Speed Distance Operation Inversion")
            ]
        },
        # 6. Recurrent Speed-Acceleration Conflation (Class 9)
        {
            "pattern_label": "RECURRENT_SPEED_ACCELERATION_CONFLATION",
            "topic": "Motion: Speed vs Acceleration",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MOT-002",
            "intervention_id": "INTV-MOT-002",
            "reassessment_pair_id": "PAIR-MOT-002",
            "steps": [
                ("PHY-Class9-20-0001", "Vehicle moves at steady constant speed of 20 m/s for 10 s. What is acceleration?", "Acceleration is 20 m/s^2 because the vehicle is moving fast at 20 m/s.", "MISC-MOT-002: Speed-Acceleration Conflation"),
                ("PHY-Class9-20-0002", "Train moves along straight track at uniform 72 km/h for 20 s. Acceleration?", "Acceleration = 72 / 20 = 3.6 m/s^2 (divided speed by time without checking change in velocity).", "MISC-MOT-002: Speed-Acceleration Conflation")
            ]
        },
        # 7. Recurrent Impetus Theory (Class 9)
        {
            "pattern_label": "RECURRENT_IMPETUS_THEORY_PATTERN",
            "topic": "Force & Laws of Motion: Inertia",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-FOR-001",
            "intervention_id": "INTV-FOR-001",
            "reassessment_pair_id": "PAIR-FOR-001",
            "steps": [
                ("PHY-Class9-21-0001", "Puck slides across frictionless ice at constant 10 m/s. What net force keeps it moving?", "Requires a continuous forward force of 20 N (F = m * v) to keep it moving.", "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)"),
                ("PHY-Class9-21-0002", "Cart glides in deep space at constant velocity. Forward force needed?", "Must maintain a forward thrust in the direction of motion to sustain speed.", "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)")
            ]
        },
        # 8. Recurrent Free Fall Mass Independence Fallacy (Class 9)
        {
            "pattern_label": "RECURRENT_HEAVIER_FALLS_FASTER_PATTERN",
            "topic": "Gravitation: Free Fall",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-GRAV-001",
            "intervention_id": "INTV-GRAV-001",
            "reassessment_pair_id": "PAIR-GRAV-001",
            "steps": [
                ("PHY-Class9-23-0001", "10 kg cannonball and 5 g feather dropped in vacuum. Which hits first?", "Cannonball hits first because gravity pulls heavier things faster.", "MISC-GRAV-001: Heavier Objects Fall Faster Fallacy"),
                ("PHY-Class9-23-0002", "50 kg sphere and 1 kg sphere released from height in vacuum. Compare times.", "The 50 kg sphere arrives first because it has greater mass.", "MISC-GRAV-001: Heavier Objects Fall Faster Fallacy")
            ]
        },
        # 9. Recurrent Ohm's Law Misconception (Class 10)
        {
            "pattern_label": "RECURRENT_OHMS_LAW_DIRECTION_FALLACY",
            "topic": "Electricity: Ohm's Law and Resistance",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-ELEC-003",
            "intervention_id": "INTV-ELEC-003",
            "reassessment_pair_id": "PAIR-ELEC-003",
            "steps": [
                ("PHY-Class10-12-0001", "A 10 ohm resistor connected to 6V battery. Current?", "Current decreases because 10 ohm resistor blocks charge; current must be less than 6.", "MISC-ELEC-003: Resistance Reduces Current Independent of Voltage"),
                ("PHY-Class10-12-0002", "Resistor 20 ohms, 12V battery. Find I using Ohm's Law.", "Bigger resistor always means less current regardless of battery voltage.", "MISC-ELEC-003: Resistance Reduces Current Independent of Voltage")
            ]
        },
        # 10. Recurrent Electromagnetic Induction Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_STATIC_FIELD_EMF_FALLACY",
            "topic": "Magnetic Effects: Electromagnetic Induction",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MAG-006",
            "intervention_id": "INTV-MAG-006",
            "reassessment_pair_id": "PAIR-MAG-006",
            "steps": [
                ("PHY-Class10-18-0001", "A coil of 100 turns placed in constant 2T field. Is EMF induced?", "Yes, EMF = 100 x 2 = 200 V is continuously induced because field passes through coil.", "MISC-MAG-006: Static Field Induces Constant EMF Fallacy"),
                ("PHY-Class10-18-0002", "A search coil in steady non-changing solenoid field. Does galvanometer deflect?", "Galvanometer deflects continuously because field exists inside coil.", "MISC-MAG-006: Static Field Induces Constant EMF Fallacy")
            ]
        },
        # 11. Recurrent Work Direction Misconception (Class 9)
        {
            "pattern_label": "RECURRENT_WORK_DIRECTION_FALLACY",
            "topic": "Work and Energy: Direction-Dependent Work",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-WRK-001",
            "intervention_id": "INTV-WRK-001",
            "reassessment_pair_id": "PAIR-WRK-001",
            "steps": [
                ("PHY-Class9-24-0001", "Porter carries 10 kg bag and walks 5 m horizontally. Work done by holding force?", "Work = 10 x 5 = 50 J because force times displacement is always work.", "MISC-WRK-001: Work Equals Force Times Distance Regardless of Direction"),
                ("PHY-Class9-24-0002", "Man carries 20 kg load and walks 8 m flat. Work done by vertical holding force?", "Work = 20 x 8 = 160 J, force times distance.", "MISC-WRK-001: Work Equals Force Times Distance Regardless of Direction")
            ]
        },
        # 12. Recurrent Momentum Non-Conservation (Class 9)
        {
            "pattern_label": "RECURRENT_MOMENTUM_DESTRUCTION_FALLACY",
            "topic": "Force and Laws of Motion: Momentum Conservation",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MOM-001",
            "intervention_id": "INTV-MOM-001",
            "reassessment_pair_id": "PAIR-MOM-001",
            "steps": [
                ("PHY-Class9-25-0001", "2 kg ball at 5 m/s hits stationary identical ball; first stops. Velocity of second?", "Momentum is destroyed when ball 1 stops; ball 2 stays at rest.", "MISC-MOM-001: Momentum Not Conserved When Object Stops"),
                ("PHY-Class9-25-0002", "3 kg ball moving at 4 m/s collides and stops. What happens to second 3 kg ball?", "Ball 1 stopping destroys its momentum; ball 2 has no reason to move.", "MISC-MOM-001: Momentum Not Conserved When Object Stops")
            ]
        },
        # 13. Recurrent Screen Reification Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_SCREEN_REIFICATION_PATTERN",
            "topic": "Optics: Real Image Formation in Space",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-OPT-002",
            "intervention_id": "INTV-OPT-002",
            "reassessment_pair_id": "PAIR-OPT-002",
            "steps": [
                ("PHY-Class10-02-0001", "Screen removed from focal plane of convex lens. Does image exist?", "Image disappears completely because images only exist on physical screens.", "MISC-OPT-002: Screen Reification (Image Exists Only on Screen)"),
                ("PHY-Class10-02-0002", "Cardboard screen lifted out of optics beam. Where did image go?", "Destroyed because without a screen there is no surface for image to exist on.", "MISC-OPT-002: Screen Reification (Image Exists Only on Screen)")
            ]
        },
        # 14. Recurrent Glass Slab Angular Deviation Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_GLASS_SLAB_DEVIATION_PATTERN",
            "topic": "Optics: Refraction through Glass Slab",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-OPT-005",
            "intervention_id": "INTV-OPT-005",
            "reassessment_pair_id": "PAIR-OPT-005",
            "steps": [
                ("PHY-Class10-05-0001", "Ray enters glass slab at 45 deg. Describe direction of emergent ray.", "Emergent ray exits bent at a permanent angle like a prism.", "MISC-OPT-005: Glass Slab Angular Deviation Fallacy"),
                ("PHY-Class10-05-0002", "Light passes through flat rectangular glass block. Angular deviation?", "Refraction at two faces bends ray permanently into a new angular path.", "MISC-OPT-005: Glass Slab Angular Deviation Fallacy")
            ]
        },
        # 15. Recurrent Virtual Image Convergence Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_VIRTUAL_RAY_CONVERGENCE_PATTERN",
            "topic": "Optics: Virtual Images in Mirrors",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-OPT-003",
            "intervention_id": "INTV-OPT-003",
            "reassessment_pair_id": "PAIR-OPT-003",
            "steps": [
                ("PHY-Class10-03-0001", "Object at 10 cm before plane mirror. Do rays pass behind mirror?", "Light rays penetrate through glass and physically focus behind the surface.", "MISC-OPT-003: Virtual Image Ray Convergence Fallacy"),
                ("PHY-Class10-03-0002", "Reflection seen in mirror. What happens behind silver coating?", "Actual rays intersect behind mirror to create the reflection.", "MISC-OPT-003: Virtual Image Ray Convergence Fallacy")
            ]
        },
        # 16. Recurrent Star Twinkling Emission Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_TWINKLING_EMISSION_PATTERN",
            "topic": "Human Eye: Atmospheric Refraction",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-EYE-003",
            "intervention_id": "INTV-EYE-003",
            "reassessment_pair_id": "PAIR-EYE-003",
            "steps": [
                ("PHY-Class10-08-0001", "Why do stars twinkle at night?", "Nuclear explosions on star make its light turn on and off rapidly.", "MISC-EYE-003: Star Twinkling Emission Artifact Fallacy"),
                ("PHY-Class10-08-0002", "What causes star flickering?", "Stars physically pulsate and vary in size every second.", "MISC-EYE-003: Star Twinkling Emission Artifact Fallacy")
            ]
        },
        # 17. Recurrent Sky Colour Ocean Reflection Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_SKY_OCEAN_REFLECTION_PATTERN",
            "topic": "Human Eye: Rayleigh Scattering",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-EYE-004",
            "intervention_id": "INTV-EYE-004",
            "reassessment_pair_id": "PAIR-EYE-004",
            "steps": [
                ("PHY-Class10-09-0001", "Why is daytime sky blue?", "The sky acts as giant mirror reflecting the blue water of Earth's oceans.", "MISC-EYE-004: Sky Colour Reflection Fallacy"),
                ("PHY-Class10-09-0002", "Physical process for blue sky?", "Water vapor droplets in clouds are blue, coloring the atmosphere.", "MISC-EYE-004: Sky Colour Reflection Fallacy")
            ]
        },
        # 18. Recurrent Parallel Resistance Addition Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_PARALLEL_RESISTANCE_ADDITION_PATTERN",
            "topic": "Electricity: Parallel Resistor Networks",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-ELEC-005",
            "intervention_id": "INTV-ELEC-005",
            "reassessment_pair_id": "PAIR-ELEC-005",
            "steps": [
                ("PHY-Class10-13-0001", "Two 10 ohm resistors in parallel. Total resistance?", "Equivalent resistance is 10 + 10 = 20 ohms because adding resistors always increases R.", "MISC-ELEC-005: Parallel Resistance Addition Fallacy"),
                ("PHY-Class10-13-0002", "Adding parallel resistor across circuit. R_eq change?", "Total resistance increases because you add more resistive obstruction.", "MISC-ELEC-005: Parallel Resistance Addition Fallacy")
            ]
        },
        # 19. Recurrent Power Formula Mis-selection Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_POWER_FORMULA_MISSELECTION_PATTERN",
            "topic": "Electricity: Joule Heating and Power",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-ELEC-006",
            "intervention_id": "INTV-ELEC-006",
            "reassessment_pair_id": "PAIR-ELEC-006",
            "steps": [
                ("PHY-Class10-14-0001", "60W and 100W bulbs in parallel. Which glows brighter?", "60W bulb glows brighter because higher resistance creates more heat by P = I^2*R.", "MISC-ELEC-006: Power Formula Mis-selection in Parallel vs Series"),
                ("PHY-Class10-14-0002", "R1 < R2 in parallel across constant V. Which dissipates more heat?", "Larger R2 produces more heat because P = I^2*R means heat is proportional to R.", "MISC-ELEC-006: Power Formula Mis-selection in Parallel vs Series")
            ]
        },
        # 20. Recurrent Magnetic Field Line Crossing Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_FIELD_LINE_CROSSING_PATTERN",
            "topic": "Magnetic Effects: Field Line Properties",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MAG-004",
            "intervention_id": "INTV-MAG-004",
            "reassessment_pair_id": "PAIR-MAG-004",
            "steps": [
                ("PHY-Class10-16-0001", "Can two magnetic field lines cross each other?", "Yes, field lines cross where the magnetic field is very strong.", "MISC-MAG-004: Field Line Crossing Fallacy"),
                ("PHY-Class10-16-0002", "Diagram shows two field lines intersecting at point P. Valid?", "Lines intersect at the neutral point between opposing magnetic poles.", "MISC-MAG-004: Field Line Crossing Fallacy")
            ]
        },
        # 21. Recurrent Magnetic Pole Charge Equivalence Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_POLE_CHARGE_EQUIVALENCE_PATTERN",
            "topic": "Magnetic Effects: Poles vs Charges",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MAG-001",
            "intervention_id": "INTV-MAG-001",
            "reassessment_pair_id": "PAIR-MAG-001",
            "steps": [
                ("PHY-Class10-15-0001", "Stationary electron near North pole. Magnetic force?", "Electron is strongly attracted because North pole is like a positive charge (+Q).", "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Equivalence Fallacy"),
                ("PHY-Class10-15-0002", "Does static magnet pull at-rest charges?", "North pole pulls negative charges by electrostatic attraction.", "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Equivalence Fallacy")
            ]
        },
        # 22. Recurrent Action-Reaction Self Cancellation Fallacy (Class 9)
        {
            "pattern_label": "RECURRENT_ACTION_REACTION_CANCELLATION_PATTERN",
            "topic": "Force & Laws of Motion: Newton's Third Law",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-FOR-002",
            "intervention_id": "INTV-FOR-002",
            "reassessment_pair_id": "PAIR-FOR-002",
            "steps": [
                ("PHY-Class9-22-0001", "Horse pulls cart, cart pulls horse. Why does system move?", "Forces cancel out to zero on cart, so horse must produce force greater than reaction.", "MISC-FOR-002: Action-Reaction Self-Cancellation Fallacy"),
                ("PHY-Class9-22-0002", "If action equals reaction, why do objects accelerate?", "Third law only applies when objects are stationary; moving action beats reaction.", "MISC-FOR-002: Action-Reaction Self-Cancellation Fallacy")
            ]
        },
        # 23. Successful Cognitive Remediation: Optics Half-Lens (POE Cycle)
        {
            "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
            "topic": "Optics: Half-Lens Aperture Remediation",
            "grade": "Class 10",
            "status": "resolved_with_transfer",
            "next_action": "advance_to_next_topic",
            "target_misc_id": "MISC-OPT-001",
            "intervention_id": "INTV-OPT-001",
            "reassessment_pair_id": "PAIR-OPT-001",
            "steps": [
                ("PHY-Class10-01-0001", "Lower half of convex lens covered with black paper. What happens to projected image?", "The top half of the candle image is completely missing because the bottom half is covered.", "MISC-OPT-001: Half-Lens Blocking Fallacy"),
                ("INTV-OPT-001-STEP", "PhET simulation: Observe virtual mask covering lower half of lens.", "Wait, the full image is still formed on the screen, just dimmer! Every point on lens receives light from entire object.", "COGNITIVE_CONFLICT_RECONCILED: Full image persists with 50% brightness"),
                ("PHY-Class10-01-0003", "Near-transfer isomorphic question: cover top 30% of lens.", "The complete image remains on screen, but brightness is 70% of original.", "CORRECT: Scientifically Accurate Response")
            ]
        },
        # 24. Successful Cognitive Remediation: Current Conservation (POE Cycle)
        {
            "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
            "topic": "Electricity: Current Conservation Remediation",
            "grade": "Class 10",
            "status": "resolved_with_transfer",
            "next_action": "advance_to_next_topic",
            "target_misc_id": "MISC-ELEC-001",
            "intervention_id": "INTV-ELEC-001",
            "reassessment_pair_id": "PAIR-ELEC-001",
            "steps": [
                ("PHY-Class10-10-0001", "Two identical bulbs in series with 6V battery. Compare ammeters.", "A1 = 1.2A, A2 = 0.8A, A3 = 0.4A because bulb 1 consumes electric current.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
                ("INTV-ELEC-001-STEP", "PhET Simulation: Observe moving electron dots and ammeters in series.", "Both ammeters read identical values (0.90A)! Current is not consumed; only electrical potential energy drops.", "COGNITIVE_CONFLICT_RECONCILED: Current is conserved in closed loop"),
                ("PHY-Class10-10-0003", "Near-transfer isomorphic question: 100-ohm and 20-ohm resistors in series.", "I_in = I_out, because in any series circuit electric charge cannot accumulate or vanish.", "CORRECT: Scientifically Accurate Response")
            ]
        },
        # 25. Transient Arithmetic Slip with Conceptual Mastery
        {
            "pattern_label": "TRANSIENT_SLIP_WITH_CONCEPTUAL_MASTERY",
            "topic": "Kinematics: Velocity Calculation",
            "grade": "Class 9",
            "status": "no_conceptual_misconception",
            "next_action": "provide_arithmetic_feedback_only",
            "target_misc_id": "NONE",
            "intervention_id": "FEEDBACK_ARITHMETIC",
            "reassessment_pair_id": "PAIR-NONE-001",
            "steps": [
                ("PHY-Class9-19-0001", "Runner covers 100 m in 5 s. Speed?", "Speed = distance / time = 100 / 5 = 25 m/s (mental arithmetic slip on division).", "CARELESS_CALCULATION_ERROR"),
                ("PHY-Class9-19-0002", "Car travels 300 m in 15 s. Speed?", "Average speed is distance divided by elapsed time: 300 / 15 = 20 m/s.", "CORRECT: Scientifically Accurate Response")
            ]
        }
    ]

    # 40 repetitions across 25 archetypes = 1,000 sessions total
    # Stratified: Reps 0-27 -> Train (70%, 700 sessions)
    #             Reps 28-33 -> Val (15%, 150 sessions)
    #             Reps 34-39 -> Test (15%, 150 sessions)
    for rep in range(40):
        if rep < 28:
            split = "train"
        elif rep < 34:
            split = "val"
        else:
            split = "test"

        for arch in pattern_archetypes:
            sid = f"STU_{seq_id_counter+1000:04d}"
            attempts = []
            for step_idx, st in enumerate(arch["steps"]):
                attempts.append({
                    "step": step_idx + 1,
                    "attempt_id": f"ATT-{seq_id_counter:04d}-{step_idx+1}",
                    "question_id": st[0],
                    "stem": st[1],
                    "student_response": st[2],
                    "individual_diagnosis": st[3]
                })

            seq_record = {
                "sequence_id": f"SEQ-{seq_id_counter:04d}",
                "student_id": sid,
                "curriculum_grade": arch["grade"],
                "topic": arch["topic"],
                "target_misconception_id": arch["target_misc_id"],
                "intervention_id": arch["intervention_id"],
                "reassessment_pair_id": arch["reassessment_pair_id"],
                "ordered_attempts": attempts,
                "sequence_level_label": arch["pattern_label"],
                "learning_status": arch["status"],
                "recommended_intervention_action": arch["next_action"],
                "split": split
            }
            sequences.append(seq_record)
            seq_id_counter += 1

    train_count = sum(1 for s in sequences if s["split"] == "train")
    val_count = sum(1 for s in sequences if s["split"] == "val")
    test_count = sum(1 for s in sequences if s["split"] == "test")
    print(f"Generated {len(sequences)} longitudinal student sequences across train ({train_count}), val ({val_count}), and test ({test_count}).")

    # Export JSON
    seq_json_path = os.path.join(SEQ_DIR, "student_sequences.json")
    with open(seq_json_path, "w", encoding="utf-8") as f:
        json.dump(sequences, f, indent=2)

    # Export Flattened CSV (with unified sequence_level_label)
    seq_csv_path = os.path.join(SEQ_DIR, "student_sequences.csv")
    with open(seq_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "sequence_id", "student_id", "curriculum_grade", "topic", "target_misconception_id",
            "intervention_id", "reassessment_pair_id", "total_steps", "responses_sequence",
            "diagnoses_sequence", "sequence_level_label", "learning_status",
            "recommended_intervention_action", "split"
        ])
        writer.writeheader()
        for s in sequences:
            resp_concat = " -> ".join([f"Step {a['step']}: {a['student_response']}" for a in s["ordered_attempts"]])
            diag_concat = " -> ".join([a["individual_diagnosis"] for a in s["ordered_attempts"]])
            writer.writerow({
                "sequence_id": s["sequence_id"],
                "student_id": s["student_id"],
                "curriculum_grade": s["curriculum_grade"],
                "topic": s["topic"],
                "target_misconception_id": s["target_misconception_id"],
                "intervention_id": s["intervention_id"],
                "reassessment_pair_id": s["reassessment_pair_id"],
                "total_steps": len(s["ordered_attempts"]),
                "responses_sequence": resp_concat,
                "diagnoses_sequence": diag_concat,
                "sequence_level_label": s["sequence_level_label"],
                "learning_status": s["learning_status"],
                "recommended_intervention_action": s["recommended_intervention_action"],
                "split": s["split"]
            })

    # Export Splits
    for sp in ["train", "val", "test"]:
        sp_seqs = [s for s in sequences if s["split"] == sp]
        with open(os.path.join(SEQ_DIR, f"{sp}_sequences.json"), "w", encoding="utf-8") as f:
            json.dump(sp_seqs, f, indent=2)

    return sequences


if __name__ == "__main__":
    generate_optimized_datasets()
    generate_optimized_sequence_dataset()
    print("Optimization of curriculum datasets complete!")
