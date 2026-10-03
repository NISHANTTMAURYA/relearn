# Re:Learn — Adaptive Multimodal Learning Environment

Welcome to the **Re:Learn** repository.

This project addresses the limitations of traditional Learning Management Systems (LMS) by inferring the root **misconceptions** behind student mistakes rather than merely marking answers as right or wrong.

---

## 📁 Repository Structure & Dataset Summary

- [`dataset/`](dataset/README.md): **Class 10 & Secondary Physics Misconception Dataset**
  - **Individual Response Dataset**: 2,500 stratified multimodal responses (Train: 1,650, Val: 400, Test: 450) across 25 curriculum families with 100 items per family.
  - **Sequence Dataset**: 1,000 longitudinal multi-step student learning sessions (Train: 700, Val: 150, Test: 150) across 25 temporal pattern archetypes.
  - **Authoritative Curriculum**: NCERT Class 10 & Class 9 Science (sole authoritative baseline) + Class 11 & 12 reference benchmarks.
  - **Misconception Taxonomy**: 21 canonical secondary physics fallacies backed by Physics Education Research (PER).
  - **Diagnostic Item Bank**: 16 four-choice items where every distractor maps to a specific cognitive misconception (Eedi / DIRECT model).
  - **Disambiguation Pairs**: Probing questions designed to separate competing misconceptions producing identical errors.
  - **Adaptive Interventions & Reassessment**: Predict-Observe-Explain (POE) sequences integrated with PhET simulations and isomorphic pre/post test pairs.
  - **Reference Materials**: 15 downloaded authentic NCERT textbook chapters, CBSE marking schemes, and NeurIPS research papers (~28 MB total).
  - **Models & Baselines**: Model A (Individual Classifier: 82.2% held-out test accuracy, 95% macro recall) and Model B (Sequence Pattern Analyzer: 100% accuracy on 1,000 sessions).

For complete data schemas, field descriptions, AI ingestion specifications, and visual screenshots of the inspiring sources, see the **[Master Dataset Documentation](dataset/README.md)**.
