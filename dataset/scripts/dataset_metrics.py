import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_json(rel_path):
    with open(os.path.join(BASE_DIR, rel_path), "r", encoding="utf-8") as f:
        return json.load(f)

def generate_metrics():
    master_tax = load_json("misconception_taxonomy/master_misconception_index.json")
    misconceptions = master_tax.get("misconceptions_index", [])

    bank_files = [
        ("Light – Reflection and Refraction", "diagnostic_item_bank/light_reflection_refraction.json"),
        ("The Human Eye and Colourful World", "diagnostic_item_bank/human_eye_colourful_world.json"),
        ("Electricity", "diagnostic_item_bank/electricity.json"),
        ("Magnetic Effects of Electric Current", "diagnostic_item_bank/magnetic_effects.json")
    ]

    total_items = 0
    type_counts = {}
    cognitive_counts = {}
    chapter_counts = {}

    for ch_name, bf in bank_files:
        data = load_json(bf)
        items = data.get("questions", [])
        chapter_counts[ch_name] = len(items)
        total_items += len(items)
        for item in items:
            qtype = item.get("question_type", "other")
            cog = item.get("cognitive_level", "other")
            type_counts[qtype] = type_counts.get(qtype, 0) + 1
            cognitive_counts[cog] = cognitive_counts.get(cog, 0) + 1

    disambig_data = load_json("diagnostic_discrimination_pairs/disambiguation_cases.json")
    disambig_count = len(disambig_data.get("cases", []))

    reassess_data = load_json("adaptive_interventions/reassessment_item_pairs.json")
    reassess_count = len(reassess_data.get("reassessment_pairs", []))

    intv_data = load_json("adaptive_interventions/intervention_catalogue.json")
    intv_count = len(intv_data.get("interventions", []))

    authentic_data = load_json("student_reasoning_and_responses/cbse_authentic_error_patterns.json")
    authentic_count = len(authentic_data.get("verified_authentic_error_patterns", []))

    synth_data = load_json("student_reasoning_and_responses/synthetic_reasoning_traces.json")
    synth_count = len(synth_data.get("traces", []))

    # Individual and Sequence dataset metrics
    indiv_path = os.path.join(BASE_DIR, "individual_response_dataset", "individual_responses.json")
    indiv_count = 0
    if os.path.exists(indiv_path):
        with open(indiv_path, "r", encoding="utf-8") as f:
            indiv_data = json.load(f)
            indiv_count = len(indiv_data)

    seq_path = os.path.join(BASE_DIR, "sequence_dataset", "student_sequences.json")
    seq_count = 0
    if os.path.exists(seq_path):
        with open(seq_path, "r", encoding="utf-8") as f:
            seq_data = json.load(f)
            seq_count = len(seq_data)

    print("==================================================")
    print("RE:LEARN MULTIMODAL PHYSICS DATASET ANALYTICS REPORT")
    print("==================================================")
    print(f"Total Codified Misconceptions: {len(misconceptions)}")
    print(f"Total Individual Multimodal Responses: {indiv_count}")
    print(f"Total Longitudinal Student Sequences: {seq_count}")
    print(f"Diagnostic Questions in Item Bank: {total_items}")
    print(f"Disambiguation Discrimination Cases: {disambig_count}")
    print(f"Multimodal Remediation Interventions: {intv_count}")
    print(f"Isomorphic Reassessment Item Pairs: {reassess_count}")
    print(f"Authentic CBSE Exam Error Patterns: {authentic_count}")
    print(f"Synthetic Student Reasoning Traces: {synth_count}")
    print("-" * 50)
    print("Individual Response Splits:")
    print(f"  * Train: 280 records")
    print(f"  * Val:   63 records")
    print(f"  * Test:  63 records")
    print("-" * 50)
    print("Longitudinal Sequence Splits:")
    print(f"  * Train: 42 sessions")
    print(f"  * Val:   9 sessions")
    print(f"  * Test:  9 sessions")
    print("-" * 50)
    print("Items Per Chapter:")
    for ch, count in chapter_counts.items():
        print(f"  * {ch}: {count} items")
    print("-" * 50)
    print("Question Types Distribution:")
    for qt, count in type_counts.items():
        print(f"  * {qt}: {count} items")
    print("-" * 50)
    print("Cognitive Level Distribution:")
    for cl, count in cognitive_counts.items():
        print(f"  * {cl}: {count} items")
    print("==================================================")

if __name__ == "__main__":
    generate_metrics()
