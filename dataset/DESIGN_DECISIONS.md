# Re:Learn — Dataset Design Decisions & Architectural Log

This document records the foundational research, pedagogical, and technical decisions made in constructing the **Re:Learn Class 10 Physics Misconception Datasets**, strictly following the requirements outlined in the *Re:Learn Technical Project Documentation*.

---

## 1. Decision 1: Dual Dataset Architecture (Individual vs. Sequence)

### Rationale:
As specified on **Page 2** of the project documentation:
> *"Build two related datasets:*
> *• Individual-response dataset: one record per response. It teaches the model to classify the likely reason for a specific answer.*
> *• Sequence dataset: one record per student attempt or ordered group of related responses. It teaches the system to find patterns across questions and concepts."*

## 1. Decision 1: Dual Dataset Architecture (Individual vs. Sequence)

### Rationale:
As specified on **Page 2** of the project documentation:
> *"Build two related datasets:*
> *• Individual-response dataset: one record per response. It teaches the model to classify the likely reason for a specific answer.*
> *• Sequence dataset: one record per student attempt or ordered group of related responses. It teaches the system to find patterns across questions and concepts."*

### Implementation in Re:Learn:
1. **`dataset/individual_response_dataset/`**:
   - Total Records: **2,240 multimodal samples** across Class 9, 10, 11, and 12 Physics (2.29 MB CSV, 4.42 MB JSON, 4.54 MB preprocessed CSV)
   - Splits: **Train (1,580 records)**, **Validation (440 records)**, **Test (220 records)**
   - Formats: Tabular CSV (`individual_responses.csv`, `train.csv`, `val.csv`, `test.csv`), structured JSON (`individual_responses.json`), and preprocessed ML-ready files (`preprocessed_individual_responses.csv`, `train.jsonl`, `val.jsonl`, `test.jsonl`).
   - Unit of Observation: A single student answer, including their scratchpad calculation, written explanation, and multimodal diagram context.
   - Model Target: Trains **Model A (Individual Misconception Classifier)** to predict the root cause from a single response.
2. **`dataset/sequence_dataset/`**:
   - Total Records: **320 complete student sessions** (~1,000 ordered steps)
   - Splits: **Train (224 sessions)**, **Validation (64 sessions)**, **Test (32 sessions)**
   - Formats: Structured JSON (`student_sequences.json`, `train_sequences.json`, `val_sequences.json`, `test_sequences.json`), CSV (`student_sequences.csv`), and preprocessed ML-ready file (`preprocessed_sequences.csv`).
   - Unit of Observation: An ordered sequence of questions ($Q_1 \rightarrow Q_2 \rightarrow Q_3$) answered by the same student during a learning session.
   - Model Target: Trains **Model B (Sequence / Pattern Analyzer)** to distinguish between an isolated slip and a deeply held persistent misconception.

---

## 2. Decision 2: Single Authoritative Textbook Baseline (NCERT Secondary & Senior Secondary Physics)

### Rationale:
The project guidelines require using **one primary textbook only** as the authoritative source.
- Mixing textbooks across different educational boards (e.g. US AP Physics vs. UK GCSE vs. Indian NCERT) introduces severe contradictions in sign conventions (such as Cartesian vs. "Real-is-Positive" conventions in optics) and symbol standards.
- NCERT Science & Physics (*Classes 9, 10, 11, and 12*, published by NCERT, Government of India) serves as the unified national curriculum benchmark, ensuring complete internal consistency in definitions, formulas, and diagrams across all secondary and higher secondary physics tiers.

### Artifacts Downloaded & Preserved:
The complete original chapter PDFs are stored in `reference_materials/textbooks/` (21.9 MB total):
- **Class 9 Physics**: `iesc108.pdf` (Motion, 706 KB), `iesc109.pdf` (Force & Laws, 4.42 MB), `iesc110.pdf` (Gravitation, 573 KB).
- **Class 10 Physics**: `jesc110.pdf` (Light, 2.08 MB), `jesc111.pdf` (Human Eye, 1.44 MB), `jesc112.pdf` (Electricity, 2.05 MB), `jesc113.pdf` (Magnetism, 2.47 MB).
- **Class 11 Physics**: `keph102_class11_kinematics.pdf` (1.39 MB), `keph104_class11_work_energy.pdf` (2.06 MB), `keph107_class11_gravitation.pdf` (1.76 MB).
- **Class 12 Physics**: `leph103_class12_current_elec.pdf` (2.11 MB), `leph201_class12_ray_optics.pdf` (3.31 MB).

---

## 3. Decision 3: Multimodal Representation & Structured Whiteboard Primitives

### Rationale:
To support multimodal vision-language models (VLM), the dataset cannot be limited to plain text. As outlined on **Page 8 & 14**:
- Students interpret diagrams (circuit schematics, ray paths, field lines, V-I graphs).
- The system must support structured whiteboard primitives rather than unstructured pixel guessing.

### Implementation:
Every record in the individual dataset contains rich multimodal metadata:
- `has_diagram`: Boolean indicator.
- `diagram_type`: Categorized into `circuit_schematic`, `ray_diagram`, `eye_defect_diagram`, `prism_dispersion`, `field_lines`, and `v_i_graph`.
- `diagram_description`: Exhaustive spatial descriptions of components, ray intersections, and current flow paths.
- `visual_elements`: Component connection tokens (e.g. `Battery(12V)`, `Branch1(R1=6_ohm)`, `Ammeter(pos_side)`).
- `whiteboard_commands`: Structured drawing instructions compatible with Page 8:
  ```python
  draw_axes(x_label='Distance from mirror', origin='Pole P')
  draw_concave_mirror(pole=(300, 150))
  plot_point(label='F', x=225, y=150, text='-15 cm')
  draw_object(label='AB', x=200, y=150, height=40)
  write_equation('1/f = 1/v + 1/u')
  ```

---

## 4. Decision 4: Taxonomy & Separation of Errors from Misconceptions

### Rationale:
Page 3 & 10 explicitly warn:
> *"Do not label every wrong answer as a misconception. Separate conceptual errors from arithmetic slips, unit errors, guessing and missing evidence."*

### Implementation:
The dataset codifies 24 mutually exclusive target classes categorized by `error_type`:
1. **`conceptual_misconception`**: 21 codified fallacies from Physics Education Research (e.g. *Current Attenuation*, *Battery as Constant Current Source*, *Half-Lens Blocking*, *Sign Convention Inversion*).
2. **`calculation_slip`**: Dedicated class `CARELESS_CALCULATION_ERROR` (e.g. arithmetic multiplication errors with correct formula).
3. **`unit_error`**: Dedicated class `UNIT_CONVERSION_ERROR` (e.g. reporting Volts for Current, or omitting time conversion from minutes to seconds).
4. **`sign_inversion`**: Substituted positive scalar distances in Cartesian formulas.
5. **`guessing_unclear`**: Dedicated class `UNSURE_INSUFFICIENT_EVIDENCE` for low-information responses.
6. **`no_error`**: Dedicated class `CORRECT: Scientifically Accurate Response`.

---

## 5. Decision 5: Calibrated Confidence & Abstention Protocol

### Rationale:
Pages 3 & 4 mandate that when evidence is ambiguous, the system must be allowed to abstain and request diagnostic follow-up rather than claiming unearned certainty:
> *"Important: The same wrong answer can have multiple causes. If the student's working is unavailable, the model should return likely causes with confidence or ask a short diagnostic follow-up question instead of claiming certainty."*

### Implementation in Model A:
- Calibrated probability output relative to chance level ($1/24 \approx 0.0416$).
- When the margin between the top prediction and runner-up is negligible, the model returns `UNSURE_NEEDS_MORE_EVIDENCE` and outputs `alternative_cause` as a candidate hypothesis.

---

## 6. Decision 6: Leak-Free Group-Based Splitting

### Rationale:
Page 3 & 15 state:
> *"Split train, validation and test data by question templates or misconception examples—not random near-duplicates—so the test measures generalisation."*

### Implementation:
The dataset organizes items into 15 distinct `question_family` groups (e.g. `SERIES_CIRCUIT_CONSERVATION`, `PARALLEL_BATTERY_DELIVERY`, `LENS_APERTURE_AND_IMAGE`). Splitting enforces held-out question variants so that model evaluation measures true generalization to unseen response phrasings and question forms rather than memorization.

---

## 7. Decision 7: Remediation & Reassessment Loop Verification

### Rationale:
Page 11 & 12 emphasize that a single correct follow-up does not prove mastery. The system must verify transfer through isomorphic questions:
> *"Make the resolution rule explicit: use new evidence across suitable questions/attempts; allow unresolved or uncertain; avoid declaring mastery from one answer alone."*

### Implementation in Model B:
Model B explicitly parses sequences into:
- `UNRESOLVED_PERSISTENT_MISCONCEPTION`: Repeated error across multiple questions triggers targeted intervention.
- `SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE`: Pre-test error followed by reconciled conflict in PhET simulation followed by correct answer on near-transfer reassessment updates BKT mastery state ($0.15 \rightarrow 0.88$).
- `TRANSIENT_SLIP_WITH_CONCEPTUAL_MASTERY`: Single slip accompanied by correct conceptual working triggers arithmetic feedback only without unnecessary remediation.
