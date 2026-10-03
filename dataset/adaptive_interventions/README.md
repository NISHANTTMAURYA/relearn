# Adaptive Interventions & Reassessment Module

## 1. Pedagogical Architecture
The ultimate value of a diagnostic system in **Re:Learn** is its capacity to close the learning loop:
1. **Misconception Detection**: An incorrect distractor or erroneous reasoning step identifies a specific node in the misconception taxonomy.
2. **Targeted Remediation**: Rather than generic answer keys, the system delivers an intervention tailored to the specific cognitive failure mode using **Predict-Observe-Explain (POE)** or **Cognitive Conflict** simulations.
3. **Isomorphic Reassessment**: The student is administered a near-transfer reassessment item to determine whether the cognitive shift is robust or merely superficial recall.
4. **Longitudinal Mastery Tracking**: Bayesian Knowledge Tracing (BKT) records update the student's mastery probability vector across sessions.

---

## 2. Directory Contents
- `intervention_catalogue.json`: Structured intervention sequences mapped to each misconception, incorporating interactive tools like **PhET Interactive Simulations** (University of Colorado Boulder).
- `reassessment_item_pairs.json`: Formally paired pre-diagnostic and post-reassessment items with explicit diagnosis and evaluation criteria.
