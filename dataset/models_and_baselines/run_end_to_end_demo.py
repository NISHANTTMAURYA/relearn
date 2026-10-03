import os
import pickle
import json
from train_sequence_analyzer import SequencePatternAnalyzer

BASE_DIR = r"d:\relearn\dataset"
MODEL_PATH = os.path.join(BASE_DIR, "models_and_baselines", "individual_misconception_model.pkl")
INTERVENTIONS_PATH = os.path.join(BASE_DIR, "adaptive_interventions", "intervention_catalogue.json")
REASSESS_PATH = os.path.join(BASE_DIR, "adaptive_interventions", "reassessment_item_pairs.json")

def run_relearn_simulation():
    print("=" * 70)
    print("RE:LEARN END-TO-END DEMO: QUIZ -> DIAGNOSIS -> INTERVENTION -> REASSESSMENT")
    print("=" * 70)

    # 1. Load Trained Individual Model (Model A)
    with open(MODEL_PATH, "rb") as f:
        model_a = pickle.load(f)

    # 2. Load Sequence Analyzer (Model B)
    model_b = SequencePatternAnalyzer()

    # 3. Load Multimodal Interventions & Reassessment Pairs
    with open(INTERVENTIONS_PATH, "r", encoding="utf-8") as f:
        interventions = json.load(f)["interventions"]
    with open(REASSESS_PATH, "r", encoding="utf-8") as f:
        reassessment_pairs = json.load(f)["reassessment_pairs"]

    # Simulated Student Session: Student "Priya" tackling Electric Circuits
    student_name = "Priya (Student ID: STU-804)"
    print(f"\n[Step 1: Student Session Initialized]")
    print(f"Learner: {student_name}")
    print(f"Topic: NCERT Class 10 Physics - Chapter 11 (Electricity)")

    quiz_attempts = [
        {
            "step": 1,
            "question_id": "PHY-ELEC-001",
            "question_stem": "Two identical bulbs in series with a 6V battery. Compare ammeter readings before, between, and after the bulbs.",
            "student_response": "A1 = 1.2A, A2 = 0.8A, A3 = 0.4A. Bulb 1 consumes current to glow, and Bulb 2 consumes what is left."
        },
        {
            "step": 2,
            "question_id": "PHY-ELEC-001-VAR",
            "question_stem": "Three identical resistors connected in series with battery. What is current through R3 compared to R1?",
            "student_response": "Current through R3 is much smaller than R1 because current gets used up as it travels along the series circuit."
        }
    ]

    print("\n[Step 2: Student Submits Quiz Responses]")
    diagnosed_steps = []
    for att in quiz_attempts:
        inp_text = f"Topic: Current Conservation in Series | Question: {att['question_stem']} | Student Response: {att['student_response']}"
        pred_label = model_a.predict([inp_text])[0]
        probs = model_a.predict_proba([inp_text])[0]
        conf = float(max(probs))

        print(f"\n  Question {att['step']}: {att['question_stem']}")
        print(f"  Student Response: \"{att['student_response']}\"")
        print(f"  --> Model A (Individual Diagnosis): {pred_label} (Confidence: {conf:.2f})")

        att_copy = att.copy()
        att_copy["individual_diagnosis"] = pred_label
        att_copy["confidence"] = conf
        diagnosed_steps.append(att_copy)

    # Step 3: Run Model B (Sequence Analyzer)
    print("\n" + "-" * 70)
    print("[Step 3: Model B Sequence & Pattern Analysis]")
    sequence_input = {
        "sequence_id": "SESSION-PRIYA-01",
        "student_id": "STU-804",
        "topic": "Electricity: Current Conservation",
        "ordered_attempts": diagnosed_steps
    }
    seq_result = model_b.analyze_sequence(sequence_input)
    print(f"  Detected Pattern:    {seq_result['predicted_pattern']}")
    print(f"  Session Status:      {seq_result['status']}")
    print(f"  Pattern Confidence:  {seq_result['confidence']:.2f}")
    print(f"  Synthesized Evidence: {seq_result['evidence']}")
    print(f"  System Action:       {seq_result['next_action']}")

    # Step 4: Trigger Targeted Multimodal Intervention
    print("\n" + "-" * 70)
    print("[Step 4: Targeted Multimodal Intervention Triggered]")
    # Find matching intervention
    active_intv = next((i for i in interventions if i["target_misconception_id"] == "MISC-ELEC-001"), interventions[0])
    print(f"  Pedagogical Strategy: {active_intv['pedagogical_strategy']}")
    print(f"  Interactive Tool:     {active_intv['simulation_reference']['simulation_name']} ({active_intv['simulation_reference']['url']})")
    seq = active_intv["guided_learning_sequence"]
    print(f"  1. Predict:           {seq['step_1_predict']}")
    print(f"  2. Observe (PhET):    {seq['step_2_observe']}")
    print(f"  3. Cognitive Conflict: {seq['step_3_explain_cognitive_conflict']}")
    print(f"  4. Conceptual Bridge: {seq['step_4_conceptual_bridge']}")

    # Step 5: Post-Intervention Isomorphic Reassessment
    print("\n" + "-" * 70)
    print("[Step 5: Post-Intervention Isomorphic Reassessment]")
    pair = next((p for p in reassessment_pairs if p["target_misconception_id"] == "MISC-ELEC-001"), reassessment_pairs[0])
    reassess_item = pair["post_intervention_reassessment_item"]
    print(f"  New Transfer Question: {reassess_item['stem']}")
    print("  Options Presented to Student:")
    for opt in reassess_item["options"]:
        print(f"    [{opt['key']}] {opt['text']}")

    # Student after POE intervention submits answer
    student_reassess_choice = "B"
    chosen_opt = next(o for o in reassess_item["options"] if o["key"] == student_reassess_choice)
    print(f"\n  Priya selects: [{student_reassess_choice}] \"{chosen_opt['text']}\"")

    if chosen_opt["is_correct"]:
        print(f"\n[Step 6: Learner Record & Mastery Tracking]")
        print("  VERDICT: Misconception MISC-ELEC-001 successfully RESOLVED with transfer.")
        print("  Mastery Probability: Increased from 0.15 -> 0.88 (BKT Update)")
        print("  Next Recommendation: Advance learner to parallel resistor dynamics.")
    else:
        print("  VERDICT: Misconception persists. Secondary mechanical analog scheduled.")
    print("=" * 70)

if __name__ == "__main__":
    run_relearn_simulation()
