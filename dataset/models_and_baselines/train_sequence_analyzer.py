import os
import json
from collections import Counter

BASE_DIR = r"d:\relearn\dataset\sequence_dataset"
MODEL_DIR = r"d:\relearn\dataset\models_and_baselines"

class SequencePatternAnalyzer:
    """
    Re:Learn Model B: Sequence & Pattern Analysis Component.
    Analyzes ordered attempts across a student quiz/learning session to identify:
    1. Recurrent single misconceptions (e.g. repeated current attenuation, speed-acceleration conflation)
    2. Misconception shifts or cascades
    3. Transient calculation slips vs genuine misconceptions
    4. Successful resolution after multimodal intervention
    """
    def __init__(self):
        self.rules = {
            "MISC-ELEC-001": "RECURRENT_CURRENT_ATTENUATION_PATTERN",
            "MISC-ELEC-002": "RECURRENT_CONSTANT_CURRENT_BATTERY_PATTERN",
            "MISC-ELEC-003": "RECURRENT_OHMS_LAW_DIRECTION_FALLACY",
            "MISC-ELEC-005": "RECURRENT_PARALLEL_RESISTANCE_ADDITION_PATTERN",
            "MISC-ELEC-006": "RECURRENT_POWER_FORMULA_MISSELECTION_PATTERN",
            "MISC-OPT-001": "RECURRENT_HALF_LENS_BLOCKING_PATTERN",
            "MISC-OPT-002": "RECURRENT_SCREEN_REIFICATION_PATTERN",
            "MISC-OPT-003": "RECURRENT_VIRTUAL_RAY_CONVERGENCE_PATTERN",
            "MISC-OPT-004": "PERVASIVE_SIGN_CONVENTION_INVERSION",
            "MISC-OPT-005": "RECURRENT_GLASS_SLAB_DEVIATION_PATTERN",
            "MISC-EYE-001": "RECURRENT_VISION_DEFECT_PATTERN",
            "MISC-EYE-002": "RECURRENT_PRISM_DEVIATION_PATTERN",
            "MISC-EYE-003": "RECURRENT_TWINKLING_EMISSION_PATTERN",
            "MISC-EYE-004": "RECURRENT_SKY_OCEAN_REFLECTION_PATTERN",
            "MISC-MAG-001": "RECURRENT_POLE_CHARGE_EQUIVALENCE_PATTERN",
            "MISC-MAG-004": "RECURRENT_FIELD_LINE_CROSSING_PATTERN",
            "MISC-MAG-005": "RECURRENT_DIRECTIONAL_HAND_RULE_INVERSION",
            "MISC-MAG-006": "RECURRENT_STATIC_FIELD_EMF_FALLACY",
            "MISC-MOT-001": "RECURRENT_SPEED_DISTANCE_INVERSION_PATTERN",
            "MISC-MOT-002": "RECURRENT_SPEED_ACCELERATION_CONFLATION",
            "MISC-FOR-001": "RECURRENT_IMPETUS_THEORY_PATTERN",
            "MISC-FOR-002": "RECURRENT_ACTION_REACTION_CANCELLATION_PATTERN",
            "MISC-GRAV-001": "RECURRENT_HEAVIER_FALLS_FASTER_PATTERN",
            "MISC-WRK-001": "RECURRENT_WORK_DIRECTION_FALLACY",
            "MISC-MOM-001": "RECURRENT_MOMENTUM_DESTRUCTION_FALLACY"
        }

    def analyze_sequence(self, sequence_record):
        attempts = sequence_record.get("ordered_attempts", [])
        student_id = sequence_record.get("student_id", "UNKNOWN_STUDENT")
        seq_id = sequence_record.get("sequence_id", "UNKNOWN_SEQ")

        if not attempts:
            return {
                "sequence_id": seq_id,
                "student_id": student_id,
                "predicted_pattern": "INSUFFICIENT_DATA",
                "confidence": 0.0,
                "evidence": ["No attempts recorded"],
                "status": "uncertain",
                "next_action": "administer_diagnostic_quiz"
            }

        # Extract per-step diagnoses and confidences
        diagnoses = [a.get("individual_diagnosis", a.get("diagnosis", "UNKNOWN")) for a in attempts]
        steps_count = len(attempts)

        # Detect Post-Intervention Remediation
        has_conflict_reconciled = any("COGNITIVE_CONFLICT" in d for d in diagnoses)
        last_step_correct = ("CORRECT" in diagnoses[-1])
        first_step_error = any("MISC-" in d for d in diagnoses[:-1])

        if first_step_error and (has_conflict_reconciled or last_step_correct):
            evidence = [
                f"Step 1 showed initial error: {diagnoses[0][:40]}...",
                "Intermediate intervention step reconciled conflict",
                f"Final reassessment step achieved correct diagnosis: {diagnoses[-1]}"
            ]
            return {
                "sequence_id": seq_id,
                "student_id": student_id,
                "predicted_pattern": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
                "confidence": 0.94,
                "evidence": evidence,
                "status": "resolved_with_transfer",
                "next_action": "advance_to_next_topic"
            }

        # Check for Recurrent Conceptual Misconceptions
        misc_keys = []
        for d in diagnoses:
            for k in self.rules:
                if k in d:
                    misc_keys.append(k)

        counts = Counter(misc_keys)
        if counts:
            top_misc, freq = counts.most_common(1)[0]
            if freq >= 2:
                evidence = [f"Repeated {top_misc} across {freq}/{steps_count} questions in this session."]
                pattern_name = self.rules.get(top_misc, f"RECURRENT_{top_misc}_PATTERN")
                return {
                    "sequence_id": seq_id,
                    "student_id": student_id,
                    "predicted_pattern": pattern_name,
                    "confidence": min(0.70 + 0.12 * freq, 0.99),
                    "evidence": evidence,
                    "status": "unresolved_persistent_misconception",
                    "next_action": "trigger_targeted_multimodal_intervention"
                }

        # Check for Transient Calculation / Unit Slips
        slip_count = sum(1 for d in diagnoses if ("CALCULATION" in d or "UNIT" in d))
        correct_count = sum(1 for d in diagnoses if "CORRECT" in d)

        if slip_count >= 1 and correct_count >= 1:
            return {
                "sequence_id": seq_id,
                "student_id": student_id,
                "predicted_pattern": "TRANSIENT_SLIP_WITH_CONCEPTUAL_MASTERY",
                "confidence": 0.88,
                "evidence": ["Student demonstrated conceptual accuracy in other steps; error isolated to arithmetic or unit omission."],
                "status": "no_conceptual_misconception",
                "next_action": "provide_arithmetic_feedback_only"
            }

        # Default Fallback / Ambiguous Pattern
        return {
            "sequence_id": seq_id,
            "student_id": student_id,
            "predicted_pattern": "AMBIGUOUS_INCONSISTENT_RESPONSES",
            "confidence": 0.50,
            "evidence": [f"Mixed diagnoses across steps: {', '.join([d[:25] for d in diagnoses])}"],
            "status": "uncertain",
            "next_action": "administer_disambiguation_probe"
        }

def run_sequence_evaluation():
    print("=" * 60)
    print("RE:LEARN MODEL B: SEQUENCE & PATTERN ANALYZER")
    print("=" * 60)

    seq_path = os.path.join(BASE_DIR, "student_sequences.json")
    with open(seq_path, "r", encoding="utf-8") as f:
        sequences = json.load(f)

    analyzer = SequencePatternAnalyzer()
    correct_matches = 0

    for seq in sequences:
        result = analyzer.analyze_sequence(seq)
        expected = seq.get("sequence_level_label")
        predicted = result["predicted_pattern"]
        matched = (expected == predicted)
        if matched:
            correct_matches += 1

        print(f"\n[Sequence: {seq['sequence_id']}] Student: {seq['student_id']} | Topic: {seq.get('topic')}")
        print(f"  Ground Truth Pattern: {expected}")
        print(f"  Predicted Pattern:    {predicted} (Confidence: {result['confidence']:.2f})")
        print(f"  Status:               {result['status']}")
        print(f"  Recommended Action:   {result['next_action']}")
        print(f"  Evidence:             {result['evidence']}")
        print(f"  Match:                {'PASS' if matched else 'FAIL'}")

    accuracy = (correct_matches / len(sequences)) * 100
    print("\n" + "=" * 60)
    print(f"Sequence Pattern Model Accuracy: {accuracy:.2f}% ({correct_matches}/{len(sequences)})")
    print("=" * 60)

if __name__ == "__main__":
    run_sequence_evaluation()
