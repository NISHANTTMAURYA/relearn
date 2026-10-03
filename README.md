# Re:Learn — Adaptive Multimodal Learning Environment

Welcome to the **Re:Learn** repository.

This project is developed to address the limitations of traditional Learning Management Systems (LMS) by inferring the root **misconceptions** behind student mistakes rather than merely marking answers as right or wrong.

---

## 📁 Repository Structure

- [`dataset/`](dataset/README.md): **Class 10 Physics Misconception Dataset**
  - **Authoritative Curriculum**: NCERT Class 10 Science (sole authoritative baseline).
  - **Misconception Taxonomy**: 21 canonical high-school physics fallacies backed by Physics Education Research (PER).
  - **Diagnostic Item Bank**: 16 four-choice items where every distractor maps to a specific cognitive misconception (Eedi / DIRECT model).
  - **Disambiguation Pairs**: Probing questions designed to separate competing misconceptions producing identical errors.
  - **Student Reasoning Logs**: Authentic CBSE candidate errors and explicitly labeled `[SYNTHETIC]` student scratchpads.
  - **Adaptive Interventions & Reassessment**: Predict-Observe-Explain (POE) sequences integrated with PhET simulations and isomorphic pre/post test pairs.
  - **Reference Materials**: Downloaded authentic NCERT textbook chapters, CBSE marking schemes, and NeurIPS research papers (~14 MB total).
  - **Validation & Metrics**: Automated test scripts (`python dataset/scripts/validate_dataset.py`).

For full details, interactive diagrams, and visual screenshots of the inspiring sources, see the **[Master Dataset Documentation](dataset/README.md)**.
