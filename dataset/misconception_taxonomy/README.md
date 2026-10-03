# Misconception Taxonomy: Class 10 Physics

## 1. Pedagogical and Research Foundations
The taxonomy codified in this directory is grounded in over four decades of rigorous **Physics Education Research (PER)**, notably:
- **Electric Circuits**: McDermott & Shaffer (1992), Engelhardt & Beichner (DIRECT, 2004), Cohen et al. (1983).
- **Geometrical Optics**: Goldberg & McDermott (1987), Galili & Hazan (2000), Driver et al. (1994).
- **Electromagnetism**: Maloney et al. (CSEM, 2001), Guisasola et al. (2004).
- **Board Examination Empirical Diagnostics**: Central Board of Secondary Education (CBSE) annual reports on *Common Errors Committed by Candidates in Secondary School Examinations (Science - Physics)*.

---

## 2. Taxonomy Schema and Coding Convention
Each misconception record adheres to the following formal structure:

```json
{
  "misconception_id": "MISC-<DOMAIN>-<NNN>",
  "name": "Standardized Descriptive Label",
  "naive_mental_model": "Description of the student's internal flawed model",
  "scientific_ground_truth": "Authoritative NCERT physical principle",
  "cognitive_trigger": "Cognitive, perceptual, or linguistic origin of the error",
  "distinguishing_signature": "Measurable behavioural/choice pattern identifying this specific misconception",
  "competing_misconceptions": ["Other misconceptions that produce superficially identical errors"],
  "literature_citations": ["Primary PER peer-reviewed literature references"]
}
```

### Domain Codes
- `MISC-OPT-xxx`: Light – Reflection and Refraction (Chapter 9)
- `MISC-EYE-xxx`: The Human Eye and the Colourful World (Chapter 10)
- `MISC-ELEC-xxx`: Electricity (Chapter 11)
- `MISC-MAG-xxx`: Magnetic Effects of Electric Current (Chapter 12)

---

## 3. Addressing the Core Re:Learn Problem Statement
A naive LMS classifies answers as binary (0/1). However:
- A student choosing an incorrect current value might do so because they think the battery current is constant (`MISC-ELEC-002`) or because current is consumed by upstream resistors (`MISC-ELEC-001`).
- A student failing an optics ray question might be adhering to the "half lens blocks half image" fallacy (`MISC-OPT-001`) or the "only textbook rays exist" fallacy (`MISC-OPT-006`).

This taxonomy provides the formal diagnostic labels required by **Re:Learn**'s Bayesian Knowledge Tracing and LLM diagnostic inference engines to disambiguate, target interventions, and verify cognitive change.
