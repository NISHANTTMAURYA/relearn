# Diagnostic Discrimination & Disambiguation Protocol

## 1. The Core Adaptive Challenge
A classic deficiency in traditional computerized learning systems is **observational equivalence**: two students can submit the exact same wrong answer for completely different underlying cognitive reasons.

For example, if a student claims a downstream series bulb glows dimmer:
- **Explanation A (`MISC-ELEC-001`)**: The student thinks electric current is a substance that is consumed by upstream bulbs (*Current Attenuation*).
- **Explanation B (`MISC-ELEC-004`)**: The student understands that current is conserved, but believes potential difference (*voltage*) is an energy fluid that gets exhausted inside the first bulb.

Simply providing a standard explanation or grading the answer wrong fails to remediate the underlying mental model. If the tutor provides a lecture on current conservation to Student B, Student B is not helped, because Student B already believed current was conserved!

---

## 2. The Re:Learn Disambiguation Strategy
1. **Ambiguity Flagging**: When a student response maps to multiple plausible misconceptions, the system flags the state as `DIAGNOSTIC_AMBIGUITY`.
2. **Targeted Probe Question Administration**: The system immediately administers an orthogonal probe question specifically engineered to yield divergent responses under the competing hypotheses.
3. **Discriminative Branching**: Based on the probe item response, the engine decisively identifies the active misconception and triggers the appropriate multimodal intervention.
