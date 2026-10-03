# Dataset Automation & Validation Utilities

## 1. Scripts Overview

### A. `validate_dataset.py`
A comprehensive dataset integrity test that executes programmatic sanity checks:
- **Schema Validation**: Ensures all question and misconception JSON structures adhere to specified data types.
- **Relational Integrity**: Cross-checks every `diagnosed_misconception_id` against `master_misconception_index.json` to eliminate dangling or invalid references.
- **Single Correct Option Rule**: Verifies that every diagnostic item contains exactly one `is_correct: true` option.
- **Reference Assets Verification**: Confirms local presence and byte integrity of downloaded reference textbooks, CBSE papers, and research PDFs.

#### Running the Validator
```bash
python dataset/scripts/validate_dataset.py
```

### B. `dataset_metrics.py`
An analytical utility generating tabular reports on dataset distribution:
- Misconception count per physics chapter.
- Question type distribution (conceptual, numerical, ray-diagram, application).
- Bloom's taxonomy cognitive levels (Comprehension, Application, Analysis, Evaluation).

#### Running the Metrics Reporter
```bash
python dataset/scripts/dataset_metrics.py
```
