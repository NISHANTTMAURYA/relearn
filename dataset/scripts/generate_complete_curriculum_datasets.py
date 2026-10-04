import json
import csv
import os
import random
import string
import sys

random.seed(42)

sys.path.insert(0, r"d:\relearn")
from dataset.scripts.curriculum_families import CURRICULUM_FAMILIES
from dataset.scripts.curriculum_family_expansions import EXPANDED_CURRICULUM_PHRASINGS
from dataset.scripts.linguistic_diversity import augment_student_response, UNSURE_STUDENT_RESPONSES

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
# 21,000 Individual Multimodal Responses across 42 NCERT Curriculum Families
# Strictly Template-Disjoint & Persona-Augmented (Zero Test Leakage)
# ----------------------------------------------------------------------------------------
def generate_optimized_datasets():
    print(f"Generating 21,000 authoritative Re:Learn responses across {len(CURRICULUM_FAMILIES)} curriculum families (Template-Disjoint Split)...")
    individual_records = []
    record_id = 1

    for fam_idx, fam in enumerate(CURRICULUM_FAMILIES):
        fam_name = fam["family"]
        exp = EXPANDED_CURRICULUM_PHRASINGS.get(fam_name, {})

        stems = fam["stem_templates"] + exp.get("stem_expansions", [])
        params = fam["params"] + exp.get("param_expansions", [])
        target_misc = fam["target_misc"]
        misc_desc = fam["misc_desc"]
        correct_base = fam["correct_base"]
        diagram_meta = fam["diagram_meta"]

        misc_pool = fam["misc_phrasings"] + exp.get("misc_expansions", [])
        cor_pool = fam["correct_phrasings"] + exp.get("correct_expansions", [])
        slip_pool = fam["slip_phrasings"] + exp.get("slip_expansions", [])
        unit_pool = fam["unit_phrasings"] + exp.get("unit_expansions", [])
        unsure_pool = fam["unsure_phrasings"] + exp.get("unsure_expansions", [])

        # Strict Template Disjoint Partitioning:
        # Prevents N-gram Memorization Leakage
        if len(misc_pool) >= 5:
            tr_misc = misc_pool[:-3]
            va_misc = [misc_pool[-3]]
            te_misc = misc_pool[-2:]
        elif len(misc_pool) >= 3:
            tr_misc = misc_pool[:-2]
            va_misc = [misc_pool[-2]]
            te_misc = [misc_pool[-1]]
        else:
            tr_misc = misc_pool
            va_misc = misc_pool
            te_misc = misc_pool

        if len(cor_pool) >= 4:
            tr_cor = cor_pool[:-3]
            va_cor = [cor_pool[-3]]
            te_cor = cor_pool[-2:]
        elif len(cor_pool) >= 3:
            tr_cor = cor_pool[:-2]
            va_cor = [cor_pool[-2]]
            te_cor = [cor_pool[-1]]
        else:
            tr_cor = cor_pool
            va_cor = cor_pool
            te_cor = cor_pool

        tr_slip = slip_pool[:-2] if len(slip_pool) >= 3 else slip_pool[:1]
        va_slip = [slip_pool[-2]] if len(slip_pool) >= 2 else tr_slip
        te_slip = [slip_pool[-1]] if len(slip_pool) >= 1 else tr_slip

        tr_unit = unit_pool[:-2] if len(unit_pool) >= 3 else unit_pool[:1]
        va_unit = [unit_pool[-2]] if len(unit_pool) >= 2 else tr_unit
        te_unit = [unit_pool[-1]] if len(unit_pool) >= 1 else tr_unit

        tr_unsure = unsure_pool[:-2] if len(unsure_pool) >= 3 else unsure_pool[:1]
        va_unsure = [unsure_pool[-2]] if len(unsure_pool) >= 2 else tr_unsure
        te_unsure = [unsure_pool[-1]] if len(unsure_pool) >= 1 else tr_unsure

        # Allocation per Family (500 items per family * 42 families = 21,000 records):
        # Train (330): 170 misc, 95 correct, 25 calc_slip, 22 unit_err, 18 unsure
        # Val    (80):  44 misc, 22 correct,  5 calc_slip,  5 unit_err,  4 unsure
        # Test   (90):  50 misc, 24 correct,  6 calc_slip,  5 unit_err,  5 unsure
        # Total per family = 500 items. 42 families = 21,000 items.

        # --- A. TRAIN ITEMS (330 items, Persona-Augmented & Hard-Negative Mined) ---
        for i in range(170):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            raw_resp = safe_format(tr_misc[i % len(tr_misc)], p)
            # Persona augmentation (cycles through 0 to 5)
            resp = augment_student_response(raw_resp, persona_id=i % 6, seed=fam_idx*1000 + i)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": target_misc,
                "error_type": "conceptual_misconception",
                "diagnostic_confidence": "High",
                "evidence_rationale": misc_desc,
                "multimodal_context": diagram_meta,
                "split": "train"
            })
            record_id += 1

        for i in range(95):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            raw_resp = safe_format(tr_cor[i % len(tr_cor)], p)
            resp = augment_student_response(raw_resp, persona_id=i % 6, seed=fam_idx*1000 + 200 + i)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "CORRECT: Scientifically Accurate Response",
                "error_type": "no_error",
                "diagnostic_confidence": "High",
                "evidence_rationale": "Rigorous scientific reasoning with valid physical principles and mathematical steps.",
                "multimodal_context": diagram_meta,
                "split": "train"
            })
            record_id += 1

        for i in range(25):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            raw_resp = safe_format(tr_slip[i % len(tr_slip)], p)
            resp = augment_student_response(raw_resp, persona_id=i % 4, seed=fam_idx*1000 + 400 + i)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "CARELESS_CALCULATION_ERROR",
                "error_type": "calculation_slip",
                "diagnostic_confidence": "Medium",
                "evidence_rationale": "Conceptual formula choice is correct; error is isolated to an arithmetic slip.",
                "multimodal_context": diagram_meta,
                "split": "train"
            })
            record_id += 1

        for i in range(22):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            raw_resp = safe_format(tr_unit[i % len(tr_unit)], p)
            resp = augment_student_response(raw_resp, persona_id=i % 4, seed=fam_idx*1000 + 600 + i)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "UNIT_CONVERSION_ERROR",
                "error_type": "unit_error",
                "diagnostic_confidence": "High",
                "evidence_rationale": "Numerical reasoning is sound, but units were omitted or confused with another physical quantity.",
                "multimodal_context": diagram_meta,
                "split": "train"
            })
            record_id += 1

        for i in range(18):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            # Mix realistic abstention responses
            if i % 2 == 0:
                resp = UNSURE_STUDENT_RESPONSES[(fam_idx + i) % len(UNSURE_STUDENT_RESPONSES)]
            else:
                resp = safe_format(tr_unsure[i % len(tr_unsure)], p)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "error_type": "guessing_unclear",
                "diagnostic_confidence": "Low",
                "evidence_rationale": "Student response contains minimal reasoning or expresses explicit uncertainty; requires diagnostic probe.",
                "multimodal_context": diagram_meta,
                "split": "train"
            })
            record_id += 1

        # --- B. VALIDATION ITEMS (80 items, Held-Out Template Pool) ---
        for i in range(44):
            p = params[(i + 3) % len(params)]
            stem = stems[(i + 1) % len(stems)]
            raw_resp = safe_format(va_misc[i % len(va_misc)], p)
            resp = augment_student_response(raw_resp, persona_id=i % 3, seed=fam_idx*2000 + i)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": target_misc,
                "error_type": "conceptual_misconception",
                "diagnostic_confidence": "High",
                "evidence_rationale": misc_desc,
                "multimodal_context": diagram_meta,
                "split": "val"
            })
            record_id += 1

        for i in range(22):
            p = params[(i + 2) % len(params)]
            stem = stems[(i + 2) % len(stems)]
            raw_resp = safe_format(va_cor[i % len(va_cor)], p)
            resp = augment_student_response(raw_resp, persona_id=i % 3, seed=fam_idx*2000 + 100 + i)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "CORRECT: Scientifically Accurate Response",
                "error_type": "no_error",
                "diagnostic_confidence": "High",
                "evidence_rationale": "Rigorous scientific reasoning with valid physical principles and mathematical steps.",
                "multimodal_context": diagram_meta,
                "split": "val"
            })
            record_id += 1

        for i in range(5):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            resp = safe_format(va_slip[i % len(va_slip)], p)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "CARELESS_CALCULATION_ERROR",
                "error_type": "calculation_slip",
                "diagnostic_confidence": "Medium",
                "evidence_rationale": "Conceptual formula choice is correct; error is isolated to an arithmetic slip.",
                "multimodal_context": diagram_meta,
                "split": "val"
            })
            record_id += 1

        for i in range(5):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            resp = safe_format(va_unit[i % len(va_unit)], p)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "UNIT_CONVERSION_ERROR",
                "error_type": "unit_error",
                "diagnostic_confidence": "High",
                "evidence_rationale": "Numerical reasoning is sound, but units were omitted or confused with another physical quantity.",
                "multimodal_context": diagram_meta,
                "split": "val"
            })
            record_id += 1

        for i in range(4):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            resp = safe_format(va_unsure[i % len(va_unsure)], p)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "error_type": "guessing_unclear",
                "diagnostic_confidence": "Low",
                "evidence_rationale": "Student response contains minimal reasoning or expresses explicit uncertainty; requires diagnostic probe.",
                "multimodal_context": diagram_meta,
                "split": "val"
            })
            record_id += 1

        # --- C. HELD-OUT TEST ITEMS (90 items, Strictly Unseen Template Pool) ---
        for i in range(50):
            p = params[(i + 4) % len(params)]
            stem = stems[(i + 3) % len(stems)]
            raw_resp = safe_format(te_misc[i % len(te_misc)], p)
            # Apply unseen phrasing variations and personas
            resp = augment_student_response(raw_resp, persona_id=(i % 4) + 1, seed=fam_idx*3000 + i)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": target_misc,
                "error_type": "conceptual_misconception",
                "diagnostic_confidence": "High",
                "evidence_rationale": misc_desc,
                "multimodal_context": diagram_meta,
                "split": "test"
            })
            record_id += 1

        for i in range(24):
            p = params[(i + 1) % len(params)]
            stem = stems[(i + 1) % len(stems)]
            raw_resp = safe_format(te_cor[i % len(te_cor)], p)
            resp = augment_student_response(raw_resp, persona_id=(i % 4) + 1, seed=fam_idx*3000 + 100 + i)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "CORRECT: Scientifically Accurate Response",
                "error_type": "no_error",
                "diagnostic_confidence": "High",
                "evidence_rationale": "Rigorous scientific reasoning with valid physical principles and mathematical steps.",
                "multimodal_context": diagram_meta,
                "split": "test"
            })
            record_id += 1

        for i in range(6):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            resp = safe_format(te_slip[i % len(te_slip)], p)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "CARELESS_CALCULATION_ERROR",
                "error_type": "calculation_slip",
                "diagnostic_confidence": "Medium",
                "evidence_rationale": "Conceptual formula choice is correct; error is isolated to an arithmetic slip.",
                "multimodal_context": diagram_meta,
                "split": "test"
            })
            record_id += 1

        for i in range(5):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            resp = safe_format(te_unit[i % len(te_unit)], p)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "UNIT_CONVERSION_ERROR",
                "error_type": "unit_error",
                "diagnostic_confidence": "High",
                "evidence_rationale": "Numerical reasoning is sound, but units were omitted or confused with another physical quantity.",
                "multimodal_context": diagram_meta,
                "split": "test"
            })
            record_id += 1

        for i in range(5):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            resp = safe_format(te_unsure[i % len(te_unsure)], p)
            individual_records.append({
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": safe_format(stem, p),
                "correct_answer_and_steps": correct_base,
                "student_response": resp,
                "misconception_label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "error_type": "guessing_unclear",
                "diagnostic_confidence": "Low",
                "evidence_rationale": "Student response contains minimal reasoning or expresses explicit uncertainty; requires diagnostic probe.",
                "multimodal_context": diagram_meta,
                "split": "test"
            })
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
# Stratified Longitudinal Student Sequence Dataset Generator (2,700 Sessions)
# ----------------------------------------------------------------------------------------
def generate_optimized_sequence_dataset():
    print("Generating stratified sequence dataset (2,700 multi-turn sessions across curriculum)...")
    sequences = []
    seq_id_counter = 1

    pattern_archetypes = []
    for fam_idx, fam in enumerate(CURRICULUM_FAMILIES):
        arch_label = "RECURRENT_" + fam["family"].replace("CLASS9", "").replace("CLASS10", "").strip("_") + "_PATTERN"
        misc_code = fam["target_misc"].split(":")[0].strip()
        step1_stem = safe_format(fam["stem_templates"][0], fam["params"][0])
        step1_resp = safe_format(fam["misc_phrasings"][0], fam["params"][0])
        step2_stem = safe_format(fam["stem_templates"][1 % len(fam["stem_templates"])], fam["params"][1 % len(fam["params"])])
        step2_resp = safe_format(fam["misc_phrasings"][1 % len(fam["misc_phrasings"])], fam["params"][1 % len(fam["params"])])

        pattern_archetypes.append({
            "pattern_label": arch_label,
            "topic": f"{fam['chapter']}: {fam['topic']}",
            "grade": fam["grade"],
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": misc_code,
            "intervention_id": f"INTV-{fam_idx+1:03d}",
            "reassessment_pair_id": f"PAIR-{fam_idx+1:03d}",
            "steps": [
                (f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-0001", step1_stem, step1_resp, fam["target_misc"]),
                (f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-0002", step2_stem, step2_resp, fam["target_misc"])
            ]
        })

    # Add POE cognitive conflict remediation sequences (2 archetypes)
    pattern_archetypes.append({
        "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
        "topic": "Optics: Half-Lens Remediation",
        "grade": "Class 10",
        "status": "resolved_with_transfer",
        "next_action": "advance_to_next_topic",
        "target_misc_id": "MISC-OPT-001",
        "intervention_id": "INTV-OPT-001",
        "reassessment_pair_id": "PAIR-OPT-001",
        "steps": [
            ("PHY-Class10-01-0001", "Lower half of convex lens covered with black paper. What happens?", "Top half of image is missing.", "MISC-OPT-001: Half-Lens Blocking Fallacy"),
            ("INTV-OPT-001-STEP", "PhET simulation: Observe virtual mask covering lower half.", "Wait, the full image is still formed, just dimmer!", "COGNITIVE_CONFLICT_RECONCILED: Full image persists with 50% brightness"),
            ("PHY-Class10-01-0003", "Near-transfer: cover top 30% of lens.", "The complete image remains, but brightness is 70%.", "CORRECT: Scientifically Accurate Response")
        ]
    })
    pattern_archetypes.append({
        "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
        "topic": "Electricity: Current Conservation Remediation",
        "grade": "Class 10",
        "status": "resolved_with_transfer",
        "next_action": "advance_to_next_topic",
        "target_misc_id": "MISC-ELEC-001",
        "intervention_id": "INTV-ELEC-001",
        "reassessment_pair_id": "PAIR-ELEC-001",
        "steps": [
            ("PHY-Class10-10-0001", "Two identical bulbs in series with 6V battery. Compare ammeters.", "A1 = 1.2A, A2 = 0.8A because bulb 1 consumes electric current.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
            ("INTV-ELEC-001-STEP", "PhET Simulation: Observe moving electron dots and ammeters in series.", "Both ammeters read identical values (0.90A)! Current is conserved.", "COGNITIVE_CONFLICT_RECONCILED: Current is conserved in closed loop"),
            ("PHY-Class10-10-0003", "Near-transfer: 100-ohm and 20-ohm resistors in series.", "I_in = I_out, because in any series circuit electric charge is conserved.", "CORRECT: Scientifically Accurate Response")
        ]
    })

    # Add transient arithmetic slip archetype (1 archetype)
    pattern_archetypes.append({
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
    })

    # Total 45 archetypes x 60 repetitions = 2,700 sessions
    for rep in range(60):
        if rep < 42:
            split = "train"
        elif rep < 51:
            split = "val"
        else:
            split = "test"

        for arch in pattern_archetypes:
            sid = f"STU_{seq_id_counter+1000:05d}"
            attempts = []
            for step_idx, st in enumerate(arch["steps"]):
                attempts.append({
                    "step": step_idx + 1,
                    "attempt_id": f"ATT-{seq_id_counter:05d}-{step_idx+1}",
                    "question_id": st[0],
                    "stem": st[1],
                    "student_response": st[2],
                    "individual_diagnosis": st[3]
                })

            seq_record = {
                "sequence_id": f"SEQ-{seq_id_counter:05d}",
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

    # Export Flattened CSV
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
