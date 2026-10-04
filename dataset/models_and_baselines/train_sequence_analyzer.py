import os
import json
import pickle
import torch
import numpy as np
from collections import Counter

BASE_DIR = r"d:\relearn\dataset\sequence_dataset"
MODEL_DIR = r"d:\relearn\dataset\models_and_baselines"

class SequencePatternAnalyzer:
    """
    Re:Learn Model B: Sequence & Pattern Analysis Component.
    Now uses a trained Machine Learning model.
    """
    def __init__(self):
        # Fallback rules
        import sys
        if r"d:\relearn" not in sys.path:
            sys.path.insert(0, r"d:\relearn")
        if r"d:\relearn\dataset\models_and_baselines" not in sys.path:
            sys.path.insert(0, r"d:\relearn\dataset\models_and_baselines")
        from dataset.scripts.curriculum_families import CURRICULUM_FAMILIES
        
        self.rules = {}
        for fam in CURRICULUM_FAMILIES:
            arch_label = "RECURRENT_" + fam["family"].replace("CLASS9", "").replace("CLASS10", "").strip("_") + "_PATTERN"
            misc_code = fam["target_misc"].split(":")[0].strip()
            self.rules[misc_code] = arch_label
            
        self.model_type = None
        self.model = None
        self.extractor = None
        self.label_encoder = None
        
        # Load ML components
        type_file = os.path.join(MODEL_DIR, "sequence_model_type.txt")
        ext_file = os.path.join(MODEL_DIR, "sequence_feature_extractor.pkl")
        enc_file = os.path.join(MODEL_DIR, "sequence_label_encoder.pkl")
        
        if os.path.exists(type_file) and os.path.exists(ext_file) and os.path.exists(enc_file):
            with open(type_file, "r") as f:
                self.model_type = f.read().strip()
                
            with open(ext_file, "rb") as f:
                self.extractor = pickle.load(f)
                
            with open(enc_file, "rb") as f:
                self.label_encoder = pickle.load(f)
                
            if self.model_type == "sklearn":
                with open(os.path.join(MODEL_DIR, "sequence_model_v2.pkl"), "rb") as f:
                    self.model = pickle.load(f)
            elif self.model_type == "pytorch_gru":
                from dataset.models_and_baselines.train_sequence_model_v2 import SequenceGRU
                input_dim = len(self.extractor.get_feature_names())
                num_classes = len(self.label_encoder.classes_)
                
                self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
                self.model = SequenceGRU(input_dim, 128, num_classes).to(self.device)
                self.model.load_state_dict(torch.load(os.path.join(MODEL_DIR, "sequence_gru_model.pt"), map_location=self.device))
                self.model.eval()

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
            
        if self.model is not None and self.extractor is not None:
            # ML Model Prediction
            X = self.extractor.transform([sequence_record], return_labels=False)
            confidence = 0.0
            
            if self.model_type == "sklearn":
                preds = self.model.predict(X)
                pred_label = self.label_encoder.inverse_transform(preds)[0]
                
                if hasattr(self.model, "predict_proba"):
                    probs = self.model.predict_proba(X)[0]
                    confidence = float(np.max(probs))
                else:
                    confidence = 0.90
                    
            elif self.model_type == "pytorch_gru":
                X_t = torch.tensor(X, dtype=torch.float32).unsqueeze(1).to(self.device)
                with torch.no_grad():
                    outputs = self.model(X_t)
                    probs = torch.softmax(outputs, dim=1)[0]
                    confidence = float(torch.max(probs).item())
                    pred_idx = torch.argmax(probs).item()
                    pred_label = self.label_encoder.inverse_transform([pred_idx])[0]
                    
            status, next_action = self._map_label_to_action(pred_label)
            return {
                "sequence_id": seq_id,
                "student_id": student_id,
                "predicted_pattern": pred_label,
                "confidence": confidence,
                "evidence": [f"Predicted by ML Model: {self.model_type}"],
                "status": status,
                "next_action": next_action
            }
            
        else:
            return self._rule_based_fallback(sequence_record)
            
    def _map_label_to_action(self, label):
        if "SUCCESSFUL" in label:
            return "resolved_with_transfer", "advance_to_next_topic"
        elif "TRANSIENT" in label:
            return "no_conceptual_misconception", "provide_arithmetic_feedback_only"
        elif "RECURRENT" in label:
            return "unresolved_persistent_misconception", "trigger_targeted_multimodal_intervention"
        else:
            return "uncertain", "administer_disambiguation_probe"
            
    def _rule_based_fallback(self, sequence_record):
        attempts = sequence_record.get("ordered_attempts", [])
        student_id = sequence_record.get("student_id", "UNKNOWN_STUDENT")
        seq_id = sequence_record.get("sequence_id", "UNKNOWN_SEQ")
        
        diagnoses = [a.get("individual_diagnosis", a.get("diagnosis", "UNKNOWN")) for a in attempts]
        steps_count = len(attempts)

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
    print("RE:LEARN MODEL B: SEQUENCE & PATTERN ANALYZER (ML MODEL)")
    print("=" * 60)

    seq_path_v2 = os.path.join(BASE_DIR, "test_sequences_v2.json")
    seq_path_v1 = os.path.join(BASE_DIR, "test_sequences.json")
    seq_path = seq_path_v2 if os.path.exists(seq_path_v2) else seq_path_v1
    
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

    accuracy = (correct_matches / len(sequences)) * 100
    print("\n" + "=" * 60)
    print(f"Sequence Pattern Model Accuracy on Test Set: {accuracy:.2f}% ({correct_matches}/{len(sequences)})")
    print("=" * 60)
    
if __name__ == "__main__":
    run_sequence_evaluation()
