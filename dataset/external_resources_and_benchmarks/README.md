# External Educational Datasets & Benchmarks Audit

## 1. Objectives of the Landscape Review
To develop the **Re:Learn** Class 10 Physics Misconception Dataset, an exhaustive review of open educational datasets and benchmarks was conducted to identify:
1. **Architectural Best Practices**: What schemas have proven most effective in diagnostic modeling?
2. **Availability of Ground Truth Labels**: Do existing datasets provide distractor-to-misconception mappings or student reasoning traces?
3. **Licensing and Legal Access**: Which resources are freely distributable, which require credentialing, and which are copyright-restricted?

---

## 2. Summary Audit Matrix

| Dataset / Benchmark | Primary Domain | Class 10 Physics? | Misconception Labels? | Free-Text Student Traces? | Access & Download Status in Re:Learn |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NCERT Class 10 Science** | Class 10 Physics (4 Chaps) | **Yes (100%)** | Implicit (Exercises) | No | **Downloaded** (`dataset/reference_materials/textbooks/`) |
| **CBSE Official Papers 2024** | Class 10 Science (Board) | **Yes (100%)** | **Yes (Examiner Notes)** | **Yes (Candidate Errors)** | **Downloaded** (`dataset/reference_materials/cbse_official_papers/`) |
| **NeurIPS 2020 / Eedi** | Secondary Math | No (Math only) | **Yes (Distractor tags)** | No | **Downloaded Paper** (`dataset/reference_materials/research_papers/`) |
| **Kaggle Eedi 2024** | Middle/High Math | No (Math only) | **Yes (MisconceptionId)**| No | Reviewed schema; API token required |
| **DIRECT Test (2004)** | DC Resistive Circuits | **Yes (Physics)** | **Yes (4 Misconception Categories)** | No | Reviewed via Compadre PER / literature |
| **AI2 ARC** | General Science (Grades 3-9)| Yes (Broad) | No (Correct key only) | No | **Sample Downloaded** (`sample_external_records/`) |
| **ScienceQA (NeurIPS 2022)** | Multimodal Science (Grades 1-12)| Yes (Broad) | No (Explanations only)| No | **Sample Downloaded** (`sample_external_records/`) |

---

## 3. Critical Analytical Findings
1. **The Physics Misconception Gap**: Existing large-scale diagnostic datasets with explicit misconception distractor labels (Eedi NeurIPS 2020, Kaggle 2024) are **entirely confined to mathematics**. General science benchmarks (ARC, ScienceQA, OpenBookQA) contain physics questions, but **lack distractor misconception labels**; their distractors are unannotated negative choices.
2. **Need for a Unified Class 10 Physics Benchmark**: Re:Learn fills this critical void by combining the **structural rigor of Eedi** with the **empirical diagnostic depth of the DIRECT test** and the **authoritative curricular foundation of NCERT Class 10 Science**.
