import json
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_json(rel_path):
    full_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Missing required file: {full_path}")
    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_validation():
    print("=" * 60)
    print("RE:LEARN DATASET VALIDATION PROTOCOL")
    print("=" * 60)

    errors = []
    warnings = []

    # 1. Load Master Taxonomy
    try:
        master_tax = load_json("misconception_taxonomy/master_misconception_index.json")
        tax_ids = {m["id"]: m for m in master_tax.get("misconceptions_index", [])}
        print(f"[OK] Master Misconception Index loaded: {len(tax_ids)} codified misconceptions.")
    except Exception as e:
        errors.append(f"Failed to load master taxonomy: {e}")
        return False

    # 2. Validate Diagnostic Item Bank Files
    bank_files = [
        "diagnostic_item_bank/light_reflection_refraction.json",
        "diagnostic_item_bank/human_eye_colourful_world.json",
        "diagnostic_item_bank/electricity.json",
        "diagnostic_item_bank/magnetic_effects.json"
    ]

    total_questions = 0
    for bf in bank_files:
        try:
            data = load_json(bf)
            questions = data.get("questions", [])
            total_questions += len(questions)
            for q in questions:
                qid = q.get("question_id")
                correct_count = 0
                for opt in q.get("options", []):
                    if opt.get("is_correct"):
                        correct_count += 1
                    else:
                        misc_id = opt.get("diagnosed_misconception_id")
                        if misc_id and misc_id not in tax_ids:
                            errors.append(f"Question {qid} option {opt.get('key')} references unknown misconception ID: {misc_id}")
                if correct_count != 1:
                    errors.append(f"Question {qid} must have exactly 1 correct option, found {correct_count}")
            print(f"[OK] {bf} passed integrity check ({len(questions)} items).")
        except Exception as e:
            errors.append(f"Error checking {bf}: {e}")

    # 3. Validate Disambiguation Pairs
    try:
        disambig = load_json("diagnostic_discrimination_pairs/disambiguation_cases.json")
        cases = disambig.get("cases", [])
        for c in cases:
            cid = c.get("case_id")
            for comp in c.get("competing_explanations", []):
                mid = comp.get("misconception_id")
                if mid not in tax_ids:
                    errors.append(f"Disambiguation Case {cid} references unknown misconception {mid}")
        print(f"[OK] Disambiguation cases validated ({len(cases)} cases).")
    except Exception as e:
        errors.append(f"Error in disambiguation validation: {e}")

    # 4. Validate Interventions & Reassessment Pairs
    try:
        intv_data = load_json("adaptive_interventions/intervention_catalogue.json")
        intvs = intv_data.get("interventions", [])
        for inv in intvs:
            target = inv.get("target_misconception_id")
            if target not in tax_ids:
                errors.append(f"Intervention {inv.get('intervention_id')} targets unknown misconception {target}")
        print(f"[OK] Intervention catalogue validated ({len(intvs)} interventions).")

        reassess_data = load_json("adaptive_interventions/reassessment_item_pairs.json")
        pairs = reassess_data.get("reassessment_pairs", [])
        for p in pairs:
            mid = p.get("target_misconception_id")
            if mid not in tax_ids:
                errors.append(f"Reassessment pair {p.get('pair_id')} targets unknown misconception {mid}")
        print(f"[OK] Reassessment item pairs validated ({len(pairs)} pairs).")
    except Exception as e:
        errors.append(f"Error in adaptive interventions validation: {e}")

    # 5. Check Reference Materials Downloads
    ref_files = [
        "reference_materials/textbooks/jesc110.pdf",
        "reference_materials/textbooks/jesc111.pdf",
        "reference_materials/textbooks/jesc112.pdf",
        "reference_materials/textbooks/jesc113.pdf",
        "reference_materials/cbse_official_papers/CBSE_Class10_Science_SQP_2024.pdf",
        "reference_materials/cbse_official_papers/CBSE_Class10_Science_MS_2024.pdf",
        "reference_materials/research_papers/NeurIPS_2020_Education_Challenge_Eedi.pdf"
    ]

    for rf in ref_files:
        full_rf = os.path.join(BASE_DIR, rf)
        if os.path.exists(full_rf):
            size_kb = os.path.getsize(full_rf) / 1024
            print(f"[OK] Reference material present: {rf} ({size_kb:.1f} KB)")
        else:
            warnings.append(f"Reference file not downloaded locally: {rf}")

    # Report Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print(f"Total Questions Verified: {total_questions}")
    print(f"Total Codified Misconceptions: {len(tax_ids)}")
    print(f"Errors Found: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\nERRORS:")
        for err in errors:
            print(" - " + err)
        return False
    else:
        print("\nSUCCESS: All schema definitions and cross-references are 100% valid!")
        return True

if __name__ == "__main__":
    success = run_validation()
    sys.exit(0 if success else 1)
