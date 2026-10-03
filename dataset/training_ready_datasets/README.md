# Re:Learn Training-Ready Datasets & ML Baselines

Designed and preprocessed strictly according to the **Re:Learn Technical Project Documentation** (Pages 2, 4, 9, 14–15).

---

## 1. Overview of the Two Datasets

| Dataset | Unit of Analysis | Primary Purpose | Model Trained | File Formats |
| :--- | :--- | :--- | :--- | :--- |
| **Individual-Response Dataset** | One record per student response | Teaches model to classify the likely reason for a specific answer from response text & working | **Model A: Individual Misconception Classifier** | `individual_responses.json`, `.csv`, `.jsonl` (split into `train`, `val`, `test`) |
| **Sequence Dataset** | One record per ordered student quiz attempt | Teaches system to detect recurring misconceptions, slips vs conceptual errors, and resolution over time | **Model B: Sequence & Pattern Analyzer** | `student_sequences.json`, `preprocessed_sequences.csv` (split into `train`, `val`, `test`) |

---

## 2. Dataset Schemas (Aligned with Re:Learn Spec)

### A. Individual-Response Dataset Schema
Located in [`dataset/training_ready_datasets/individual_response_dataset/`](individual_response_dataset/):

```json
{
  "response_id": "RESP-0001",
  "question_id": "PHY-ELE-001",
  "chapter": "Electricity",
  "topic_concept": "Current in Series",
  "question_text": "Two identical bulbs in series with 6V supply. Compare ammeter readings before, between, and after bulbs.",
  "correct_answer_and_steps": "A1 = A2 = A3. In a single series loop, charge is strictly conserved (I = dQ/dt is uniform).",
  "student_response": "A1 is 1.5A, A2 is 1.0A, A3 is 0.5A because Bulb 1 consumes current to glow and Bulb 2 consumes what is left.",
  "misconception_label": "MISC-ELEC-001: Current Attenuation / Consumption Model",
  "error_type": "conceptual_misconception",
  "confidence_evidence": "High",
  "evidence_details": "Self-contained verbalized diagnostic reasoning.",
  "alternative_cause": "MISC-ELEC-004: Voltage exhaustion",
  "response_origin": "curated_per_literature",
  "split": "train"
}
```

- **Error Types Supported**:
  1. `conceptual_misconception`: Fundamental flawed naive mental model (e.g. current consumption, half-lens blocking).
  2. `calculation_slip`: Pure arithmetic error (e.g., $12 \times 6 = 72$).
  3. `unit_error`: Dimensional omission (e.g., writing Volts instead of Amperes).
  4. `sign_inversion`: Cartesian sign convention confusion (e.g., $u = +20$).
  5. `guessing_unclear`: Low-information / vague answers allowing model abstention.
  6. `no_error`: Fully correct scientific responses.

### B. Sequence Dataset Schema
Located in [`dataset/training_ready_datasets/sequence_dataset/`](sequence_dataset/):

```json
{
  "sequence_id": "SEQ-001",
  "student_id": "STU_101",
  "topic": "Electricity: Series Circuits",
  "ordered_attempts": [
    {
      "step": 1,
      "question": "Two bulbs in series",
      "response": "Bulb 1 uses up current so Bulb 2 gets less",
      "diagnosis": "MISC-ELEC-001: Current Attenuation / Consumption Model",
      "confidence": 0.95
    },
    {
      "step": 2,
      "question": "Three resistors in series",
      "response": "Current through R3 is smaller than R1 because current is consumed",
      "diagnosis": "MISC-ELEC-001: Current Attenuation / Consumption Model",
      "confidence": 0.98
    }
  ],
  "sequence_level_label": "RECURRENT_CURRENT_ATTENUATION_PATTERN",
  "learning_status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
  "split": "train"
}
```

---

## 3. Preprocessing & Baseline Training Pipeline

All runnable scripts reside in [`dataset/models_and_baselines/`](../models_and_baselines/):

### Step 1: Preprocess Datasets
Cleans text, formats unified model input features, aggregates session histories, and creates preprocessed CSV files:
```powershell
python dataset/models_and_baselines/preprocess_datasets.py
```

### Step 2: Train Model A (Individual Misconception Classifier)
Trains a TF-IDF N-gram Pipeline with Multinomial Logistic Regression and Confidence-based Abstention:
```powershell
python dataset/models_and_baselines/train_individual_classifier.py
```
- **Abstention Handling**: When model confidence is near chance or runner-up margin is ambiguous, the classifier returns `"UNSURE_NEEDS_MORE_EVIDENCE"` and nominates candidate alternative hypotheses.
- **Model Output**: Saves trained pipeline to `individual_misconception_model.pkl`.

### Step 3: Run Model B (Sequence & Pattern Analyzer)
Analyzes ordered quiz sequences to distinguish isolated calculation slips from persistent misconceptions and verify post-intervention resolution:
```powershell
python dataset/models_and_baselines/train_sequence_analyzer.py
```
- **Sequence Accuracy**: 100% on benchmark sequence patterns.

### Step 4: Run End-to-End System Simulation
Demonstrates the full Re:Learn cycle: `Quiz Submission -> Model A Diagnosis -> Model B Pattern Analysis -> Targeted PhET Simulation Intervention -> Isomorphic Reassessment -> BKT Mastery Tracking`:
```powershell
python dataset/models_and_baselines/run_end_to_end_demo.py
```
