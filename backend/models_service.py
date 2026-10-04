import os
import re
import sys
import pickle
import numpy as np
from typing import Dict, List, Any, Optional, Tuple

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")
MODELS_DIR = os.path.join(DATASET_DIR, "models_and_baselines")

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if MODELS_DIR not in sys.path:
    sys.path.insert(0, MODELS_DIR)

try:
    from train_sequence_analyzer import SequencePatternAnalyzer
except ImportError:
    SequencePatternAnalyzer = None

# Vague / uninformative student inputs that should trigger abstention
VAGUE_KEYWORDS = [
    "idk", "dont know", "don't know", "not sure", "skip", "no idea",
    "forgot", "dunno", "guess", "maybe", "confused", "no clue", "haven't learned"
]


class ReLearnModelEngine:
    def __init__(self):
        self.deberta_model = None
        self.deberta_tokenizer = None
        self.deberta_classes = None
        self.device = "cpu"
        self.baseline_pipeline = None

        # 1. Load Baseline Classifier Pipeline
        baseline_path = os.path.join(MODELS_DIR, "individual_misconception_model.pkl")
        if os.path.exists(baseline_path):
            try:
                with open(baseline_path, "rb") as f:
                    self.baseline_pipeline = pickle.load(f)
                print(f"[ModelEngine] Baseline Pipeline loaded with {len(self.baseline_pipeline.classes_)} classes.")
            except Exception as e:
                print(f"[ModelEngine] Warning: Could not load baseline pipeline: {e}")

        # 2. Try loading DeBERTa fine-tuned primary model
        deberta_dir = os.path.join(MODELS_DIR, "deberta_primary_model")
        if os.path.exists(deberta_dir) and os.path.exists(os.path.join(deberta_dir, "model.safetensors")):
            try:
                import torch
                from transformers import AutoTokenizer, AutoModelForSequenceClassification

                self.device = "cuda" if torch.cuda.is_available() else "cpu"
                print(f"[ModelEngine] Attempting to load DeBERTa on {self.device}...")
                self.deberta_tokenizer = AutoTokenizer.from_pretrained(deberta_dir)
                self.deberta_model = AutoModelForSequenceClassification.from_pretrained(deberta_dir)
                self.deberta_model.to(self.device)
                self.deberta_model.eval()

                classes_path = os.path.join(deberta_dir, "label_classes.npy")
                if os.path.exists(classes_path):
                    self.deberta_classes = np.load(classes_path, allow_pickle=True)
                print(f"[ModelEngine] DeBERTa Primary Model loaded successfully on {self.device} ({len(self.deberta_classes)} classes)!")
            except Exception as e:
                print(f"[ModelEngine] Note: DeBERTa load bypassed ({e}), using baseline pipeline.")
                self.deberta_model = None

        # 3. Model B: Sequence Pattern Analyzer
        if SequencePatternAnalyzer:
            self.sequence_analyzer = SequencePatternAnalyzer()
        else:
            self.sequence_analyzer = None

    def diagnose_individual_response(
        self,
        question_id: str,
        question_stem: str,
        student_response: str,
        topic: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Diagnose a single student response using Model A.
        Includes abstention logic for low confidence, vague text, or uninformative responses.
        """
        clean_resp = (student_response or "").strip()

        # Step 1: Abstention check on vague or uninformative phrasing
        resp_lower = clean_resp.lower()
        is_vague = (
            len(clean_resp.split()) < 2 or
            any(k in resp_lower for k in VAGUE_KEYWORDS) or
            clean_resp in ["?", "??", "...", "-", "pass"]
        )
        if is_vague:
            return {
                "question_id": question_id,
                "label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "misc_id": "UNSURE",
                "confidence": 0.20,
                "category": "unsure",
                "evidence_rationale": "Student response contains insufficient conceptual reasoning (e.g. vague, monosyllabic, or statement of uncertainty). The system abstains from making an ungrounded diagnostic attribution and recommends administering an active disambiguation probe.",
                "competing_hypotheses": ["Incomplete recall", "Careless guess", "Language barrier"],
                "suggested_action": "administer_disambiguation_probe"
            }

        # Step 2: Format input prompt for Model A
        # "Question: <stem> | Student Response: <resp>"
        input_text = f"Question: {question_stem} | Student Response: {clean_resp}"
        if topic:
            input_text_with_topic = f"Topic: {topic} | Question: {question_stem} | Student Response: {clean_resp}"
        else:
            input_text_with_topic = input_text

        pred_label = None
        conf = 0.0
        top_candidates = []

        # Run DeBERTa if available
        if self.deberta_model is not None and self.deberta_tokenizer is not None:
            try:
                import torch
                inputs = self.deberta_tokenizer(
                    input_text,
                    return_tensors="pt",
                    truncation=True,
                    max_length=256
                ).to(self.device)

                with torch.no_grad():
                    logits = self.deberta_model(**inputs).logits
                    probs = torch.softmax(logits, dim=-1).cpu().numpy()[0]
                    top_indices = np.argsort(probs)[::-1][:3]
                    pred_idx = top_indices[0]
                    pred_label = str(self.deberta_classes[pred_idx])
                    conf = float(probs[pred_idx])

                    for idx in top_indices:
                        top_candidates.append({
                            "label": str(self.deberta_classes[idx]),
                            "prob": round(float(probs[idx]), 3)
                        })
            except Exception as e:
                print(f"[ModelEngine] DeBERTa inference error ({e}), falling back to baseline.")
                pred_label = None

        # Fallback to Baseline Pipeline if DeBERTa was not run or failed
        if pred_label is None and self.baseline_pipeline is not None:
            try:
                preds = self.baseline_pipeline.predict([input_text_with_topic])
                probs = self.baseline_pipeline.predict_proba([input_text_with_topic])[0]
                pred_label = preds[0]
                conf = float(np.max(probs))

                top_indices = np.argsort(probs)[::-1][:3]
                top_candidates = [
                    {"label": str(self.baseline_pipeline.classes_[i]), "prob": round(float(probs[i]), 3)}
                    for i in top_indices
                ]
            except Exception as e:
                print(f"[ModelEngine] Baseline inference error: {e}")
                pred_label = "UNSURE_INSUFFICIENT_EVIDENCE"
                conf = 0.30

        # Step 3: Low confidence threshold check (< 0.40)
        if conf < 0.40 and pred_label != "UNSURE_INSUFFICIENT_EVIDENCE":
            return {
                "question_id": question_id,
                "label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "misc_id": "UNSURE",
                "confidence": round(conf, 3),
                "category": "unsure",
                "evidence_rationale": f"Prediction confidence ({conf:.1%}) falls below the reliable diagnostic threshold (40%). The student may hold a hybrid intuitive mental model or an unclassified error.",
                "competing_hypotheses": [c["label"] for c in top_candidates],
                "suggested_action": "administer_disambiguation_probe"
            }

        # Step 4: Classify category & extract ID
        misc_id = None
        category = "misconception"
        if "CORRECT" in pred_label:
            category = "correct"
            misc_id = "CORRECT"
        elif "CALCULATION" in pred_label or "SLIP" in pred_label or "UNIT" in pred_label:
            category = "slip"
            misc_id = "SLIP"
        elif "MISC-" in pred_label:
            parts = pred_label.split(":")
            misc_id = parts[0].strip()
            category = "misconception"
        else:
            misc_id = "OTHER"
            category = "other"

        # Construct evidence rationale
        evidence = self._generate_evidence_rationale(clean_resp, pred_label, category, conf)

        return {
            "question_id": question_id,
            "label": pred_label,
            "misc_id": misc_id,
            "confidence": round(conf, 3),
            "category": category,
            "evidence_rationale": evidence,
            "competing_hypotheses": [c["label"] for c in top_candidates if c["label"] != pred_label][:2],
            "suggested_action": "trigger_multimodal_intervention" if category == "misconception" else (
                "advance_to_next_topic" if category == "correct" else "provide_arithmetic_feedback"
            )
        }

    def _generate_evidence_rationale(self, response: str, label: str, category: str, conf: float) -> str:
        if category == "correct":
            return f"The student demonstrates correct physical reasoning aligned with standard scientific conservation principles. Confidence: {conf:.1%}."
        elif category == "slip":
            return f"The underlying concept appears correctly grasped; error is isolated to an arithmetic slip, unit mismatch, or sign inversion. Confidence: {conf:.1%}."
        elif "MISC-OPT-001" in label:
            return "Student models the lens as a geometric stencil/window where blocking glass physically blocks corresponding parts of the object's picture, neglecting that every lens point receives rays from every object point."
        elif "MISC-ELEC-001" in label:
            return "Student applies a consumable fuel model to electric current, predicting current decreases sequentially after passing through resistive loads."
        elif "MISC-ELEC-002" in label:
            return "Student treats the voltage source as an invariant current supply, assuming total amperage remains constant regardless of parallel branch additions."
        elif "MISC-MAG-001" in label:
            return "Student conflates magnetic poles with static electrostatic charges, expecting stationary charges to experience static attractive or repulsive forces from magnetic poles."
        elif "MISC-GRAV-001" in label:
            return "Student associates gravitational acceleration with object weight/mass, neglecting that inertial mass cancels gravitational mass in free fall."
        else:
            return f"Diagnosed conceptual error: '{label}' based on semantic markers in student response '{response[:60]}...'. Confidence: {conf:.1%}."

    def analyze_sequence_patterns(self, session_data: Dict[str, Any]) -> Dict[str, Any]:
        """Run Model B (Sequence Pattern Analyzer) across ordered attempts."""
        if not self.sequence_analyzer:
            attempts = session_data.get("ordered_attempts", [])
            return {
                "sequence_id": session_data.get("sequence_id", "SEQ-001"),
                "student_id": session_data.get("student_id", "STUDENT"),
                "predicted_pattern": "SEQUENCE_ANALYZER_DEFAULT",
                "confidence": 0.85,
                "evidence": [f"Processed {len(attempts)} sequential quiz attempts."],
                "status": "persistent_misconception" if len(attempts) > 1 else "single_attempt",
                "next_action": "administer_intervention"
            }

        return self.sequence_analyzer.analyze_sequence(session_data)

    def evaluate_bkt_reassessment(
        self,
        misc_id: str,
        question_id: str,
        student_choice: str,
        correct_choice: str,
        prior_mastery: float = 0.15
    ) -> Dict[str, Any]:
        """
        Bayesian Knowledge Tracing (BKT) State Updater.
        Parameters:
          P(L0) = prior_mastery (typically 0.15 for diagnosed misconception)
          P(T)  = 0.35 (transition probability after guided POE intervention)
          P(S)  = 0.10 (slip probability)
          P(G)  = 0.20 (guess probability for 3-4 option MCQ)
        """
        is_correct = (student_choice.strip().upper() == correct_choice.strip().upper())
        p_l = max(0.01, min(0.99, float(prior_mastery)))
        p_t = 0.35
        p_s = 0.10
        p_g = 0.20

        if is_correct:
            # P(L | correct) = P(L)*(1 - S) / [P(L)*(1 - S) + (1 - P(L))*G]
            num = p_l * (1.0 - p_s)
            den = num + (1.0 - p_l) * p_g
            p_l_given_obs = num / den if den > 0 else 0.85
            # State transition: P(L_next) = P(L|obs) + (1 - P(L|obs))*P(T)
            posterior_mastery = p_l_given_obs + (1.0 - p_l_given_obs) * p_t
            verdict = "RESOLVED_WITH_TRANSFER"
            explanation = (
                f"Student successfully solved the near-transfer question! Misconception {misc_id} is marked "
                f"as RESOLVED. Bayesian Knowledge Tracing updates concept mastery probability from "
                f"{p_l:.2f} to {posterior_mastery:.2f}."
            )
            recommended_next_step = "advance_to_next_topic"
        else:
            # P(L | incorrect) = P(L)*S / [P(L)*S + (1 - P(L))*(1 - G)]
            num = p_l * p_s
            den = num + (1.0 - p_l) * (1.0 - p_g)
            p_l_given_obs = num / den if den > 0 else 0.05
            posterior_mastery = p_l_given_obs + (1.0 - p_l_given_obs) * 0.05
            verdict = "UNRESOLVED_PERSISTENT"
            explanation = (
                f"Student selected an answer indicating persistence of {misc_id}. "
                f"Mastery probability remains low at {posterior_mastery:.2f}. Recommend scheduling secondary "
                f"mechanical analogy or interactive physical simulation."
            )
            recommended_next_step = "trigger_secondary_analog_intervention"

        return {
            "misc_id": misc_id,
            "question_id": question_id,
            "is_correct": is_correct,
            "verdict": verdict,
            "explanation": explanation,
            "bkt_update": {
                "prior_mastery": round(p_l, 3),
                "posterior_mastery": round(posterior_mastery, 3),
                "delta": round(posterior_mastery - p_l, 3),
                "parameters": {
                    "p_transition": p_t,
                    "p_slip": p_s,
                    "p_guess": p_g
                }
            },
            "recommended_next_step": recommended_next_step
        }
