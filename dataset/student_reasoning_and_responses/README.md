# Student Reasoning & Response Data

## 1. Data Provenance & Ethical Separation Principle
A foundational tenet of the **Re:Learn** dataset protocol is strict provenance separation:
- **Never conflate synthetic traces with empirical data**: Synthetic models may harbor artificial linguistic artifacts that bias NLP evaluation.
- **Maintain clear source attribution**: Real student errors must be backed by documented empirical examination or interview reports.

---

## 2. Directory Contents

### A. Authentic Empirical Records (`cbse_authentic_error_patterns.json`)
- **Origin**: Official CBSE Board Examinations (Class 10 Science, 2020-2024), Chief Examiner reports, and published teacher analysis bulletins.
- **Contents**: Real documented student errors, actual exam question context, typical erroneous arithmetic steps, and corresponding NCERT-aligned corrections.
- **Use Case**: Ground-truth validation of diagnostic distractor realism.

### B. Synthetic Reasoning Traces (`synthetic_reasoning_traces.json`)
- **Origin**: Generated explicitly for Re:Learn by the research agent to model complete cognitive scratchpads, multi-step erroneous deductions, and conversational tutoring interactions.
- **Labeling**: Every record is tagged with `SYNTHETIC_GENERATED_SAMPLES` and contains parsed linguistic markers for NLP training.
- **Use Case**: Training and evaluating free-text misconception inference models and chain-of-thought (CoT) diagnostic analyzers.
