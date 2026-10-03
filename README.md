# Re:Learn — Adaptive Multimodal Learning Environment

Welcome to the **Re:Learn** repository.

This project addresses the limitations of traditional Learning Management Systems (LMS) by inferring the root **misconceptions** behind student mistakes rather than merely marking answers as right or wrong.

---

## 📁 Repository Structure & Dataset Summary

- [`dataset/`](dataset/README.md): **Class 10 & Secondary Physics Misconception Dataset**
  - **Individual Response Dataset**: 900 stratified multimodal responses (Train: 585, Val: 150, Test: 165) across 15 curriculum families with 15 balanced target classes.
  - **Sequence Dataset**: 390 longitudinal multi-step student learning sessions (Train: 270, Val: 60, Test: 60) across 13 temporal pattern archetypes.
  - **Authoritative Curriculum**: NCERT Class 10 & Class 9 Science (sole authoritative baseline).
  - **Misconception Taxonomy**: 21 canonical secondary physics fallacies backed by Physics Education Research (PER).
  - **Diagnostic Item Bank**: 16 four-choice items where every distractor maps to a specific cognitive misconception (Eedi / DIRECT model).
  - **Disambiguation Pairs**: Probing questions designed to separate competing misconceptions producing identical errors.
  - **Adaptive Interventions & Reassessment**: Predict-Observe-Explain (POE) sequences integrated with PhET simulations and isomorphic pre/post test pairs.
  - **Reference Materials**: 15 downloaded authentic NCERT textbook chapters, CBSE marking schemes, and NeurIPS research papers (~28 MB total).
  - **Models & Baselines**: Model A (Individual Classifier) and Model B (Sequence Pattern Analyzer) with 100% automated validation pass rate.

For complete data schemas, field descriptions, AI ingestion specifications, and visual screenshots of the inspiring sources, see the **[Master Dataset Documentation](dataset/README.md)**.
