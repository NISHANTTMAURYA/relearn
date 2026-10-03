# Diagnostic Item Bank: Class 10 Physics

## 1. Item Design Methodology
Traditional assessment banks design multiple-choice distractors to act as simple "traps" or random calculation errors. In **Re:Learn**, every item is constructed as a **Diagnostic Question** (inspired by the *Eedi / NeurIPS 2020 Diagnostic Questions framework* and the *DIRECT Concept Inventory*):
1. **Four Valid Options**: Exactly one scientifically correct option and three distractors.
2. **Explicit Cognitive Attribution**: Each distractor maps to a specific, pre-codified misconception from `misconception_taxonomy/`.
3. **No Gratuitous Distractors**: An option is included only if it represents an empirically documented naive mental model or procedural confusion.
4. **Authoritative Ground Truth**: All answers and explanations are directly verified against the single authoritative syllabus baseline: **NCERT Class 10 Science**.

---

## 2. Item Bank Composition

| Chapter File | NCERT Domain | Question Types | Key Tested Misconceptions |
| :--- | :--- | :--- | :--- |
| `light_reflection_refraction.json` | Light: Reflection & Refraction | Conceptual, Numerical, Ray Diagram, Application | Half-lens fallacy (`MISC-OPT-001`), Screen reification (`MISC-OPT-002`), Virtual ray convergence (`MISC-OPT-003`), Cartesian sign convention (`MISC-OPT-004`), Glass slab deviation (`MISC-OPT-005`), Special ray exclusivity (`MISC-OPT-006`) |
| `human_eye_colourful_world.json` | Human Eye & Colourful World | Conceptual, Theory-based, Application | Vision defect lens inversion (`MISC-EYE-001`), Prism dispersion inversion (`MISC-EYE-002`), Star twinkling artifact (`MISC-EYE-003`), Sky color reflection (`MISC-EYE-004`) |
| `electricity.json` | Electricity | Conceptual, Circuit Analysis, Numerical, Application | Current attenuation (`MISC-ELEC-001`), Battery constant current (`MISC-ELEC-002`), Parallel equal current (`MISC-ELEC-003`), Voltage-current conflation (`MISC-ELEC-004`), Parallel resistance addition (`MISC-ELEC-005`), Power formula mis-selection (`MISC-ELEC-006`) |
| `magnetic_effects.json` | Magnetic Effects of Current | Conceptual, Application | Magnetic pole = charge (`MISC-MAG-001`), Universal metallic magnetism (`MISC-MAG-002`), Magnetic force collinearity (`MISC-MAG-003`), Field line crossing (`MISC-MAG-004`), Hand rule inversion (`MISC-MAG-005`) |

---

## 3. Schema Structure

```json
{
  "question_id": "DIAG-<DOMAIN>-<NNN>",
  "question_type": "conceptual | numerical | ray_diagram | circuit_analysis | application | theory_based",
  "cognitive_level": "Comprehension | Application | Analysis | Evaluation",
  "stem": "Full, self-contained problem statement",
  "options": [
    {
      "key": "A",
      "text": "Option text",
      "is_correct": false,
      "diagnosed_misconception_id": "MISC-ELEC-001",
      "distractor_rationale": "Why a student holding this misconception selects this option"
    }
  ],
  "correct_answer": "C",
  "authoritative_solution": "Exhaustive step-by-step NCERT scientific solution",
  "source": "Bibliographic provenance (NCERT, CBSE exam, PER paper)"
}
```
