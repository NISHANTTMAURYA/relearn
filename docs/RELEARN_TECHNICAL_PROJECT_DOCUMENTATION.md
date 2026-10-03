# Re:Learn — Technical Project Documentation

> **Document Type:** Project Specification, Architecture & Requirements  
> **Topic:** Dataset, AI Models, Website Integration, and Optional Teaching Features  
> **Source PDF Preserved:** [`docs/ReLearn_Technical_Project_Documentation.pdf`](ReLearn_Technical_Project_Documentation.pdf)

---

## Project in a few lines

**Re:Learn** aims to identify **why** a student gives a wrong answer—not only whether the answer is wrong. It analyses individual responses and patterns across related questions, then provides a targeted intervention and checks whether the misunderstanding has improved.

**Scope note:** This document is based on the problem statement and requirements discussed in this conversation. The central work is misconception diagnosis, personalised intervention, reassessment and evaluation. A full teaching LMS is not the main deliverable; a small website can be used to demonstrate the system.

---

## Recommended End-to-End Plan

```
1. Build and label the dataset
   Questions, answer steps, errors, misconception labels and answer sequences
   ↓
2. Train and test diagnosis models
   Individual response diagnosis plus sequence/pattern analysis
   ↓
3. Connect the diagnosis output
   Combine predictions, confidence and student history
   ↓
4. Generate a targeted intervention
   Select or generate an explanation, hint or follow-up question
   ↓
5. Reassess and record progress
   Check new answers; update unresolved and resolved misconceptions
   ↓
6. Demonstrate through a simple website
   Quiz → diagnosis → intervention → reassessment → progress view
```

---

## Part 1 — Dataset: What to Build First

### Should you use a Class 10 Physics textbook?
**Yes.** Use a textbook as a **content source** to choose chapters, concepts, definitions, formulas and question ideas.
But a textbook alone is not a misconception dataset. You must add realistic wrong answers, the reasoning behind them, and expert-reviewed labels. Check the textbook's usage rights; for a demo, use a permitted source or write original questions aligned to the syllabus.

### Recommended Dataset Structure

| Field | What it contains | Example |
| :--- | :--- | :--- |
| `question_id` | Unique question identifier | `PHY-MOT-001` |
| `topic / concept` | Chapter and concept tested | `Motion / speed` |
| `question + context` | Question wording, units and any diagram context | `Distance = 100 m; time = 5 s. Find speed.` |
| `correct answer + steps` | Expected result and valid solution path | `100 ÷ 5 = 20 m/s` |
| `student response` | Wrong answer and, where possible, working or explanation | `500 m/s; multiplied distance by time` |
| `misconception label` | Specific concept error, not just "wrong" | `Uses multiplication instead of division` |
| `error type / alternative` | Calculation slip, unit error, guess, unclear response, etc. | `Possible arithmetic slip` |
| `confidence / evidence` | How certain the label is and what supports it | `Medium; working not shown` |
| `sequence_id + order` | Links responses from one quiz or learning session | `Quiz-07, Q1 → Q2 → Q3` |
| `sequence-level label` | Pattern or connected misconception supported by the full sequence | `Repeatedly confuses speed and acceleration` |

### Build Two Related Datasets
- **Individual-response dataset:** one record per response. It teaches the model to classify the likely reason for a specific answer.
- **Sequence dataset:** one record per student attempt or ordered group of related responses. It teaches the system to find patterns across questions and concepts.

A sequence can reveal a pattern that one answer cannot. For example, a student may answer several questions in ways that suggest they treat speed and acceleration as the same thing. Store the order of questions and answers, not just a bag of responses.

### How to Create Reliable Labels
- Start with a small concept map for one Physics chapter. List the concepts and common misconceptions for each concept.
- Write original questions that test each concept in more than one way. Include questions where different misconceptions can lead to the same wrong answer.
- Create plausible wrong-answer examples by reasoning through each misconception. Do not invent labels based only on the final number.
- Ask a Physics teacher or knowledgeable reviewer to check the question, answer, misconception label and explanation.
- Include `"insufficient evidence"`, `"careless/calculation error"` and `"other/unknown"` labels. The system must be allowed to say it is unsure.
- Create multi-question quiz examples with known patterns. Keep the full sequence and its reviewed interpretation.
- Split train, validation and test data by question templates or misconception examples—not random near-duplicates—so the test measures generalisation.

> **Important:** The same wrong answer can have multiple causes. If the student's working is unavailable, the model should return likely causes with confidence or ask a short diagnostic follow-up question instead of claiming certainty.

---

## Part 2 — Models and AI Components

You do not need a separate large AI model for every feature. Build one integrated system from specialised components. Some components are trained models; others can be ordinary software or an existing language model.

| Component / Model | Purpose | Train on / Build from | Output |
| :--- | :--- | :--- | :--- |
| **A. Individual misconception classifier** | Predict the likely misconception from one response and its context. | Individual-response dataset: question, topic, student answer, working, correct answer and reviewed label. Start with a baseline such as TF-IDF + Logistic Regression/SVM or text embeddings + a classifier. | Misconception label(s), confidence, or unsure. |
| **B. Sequence/pattern model** | Find recurring or connected misconceptions across ordered answers. | Sequence dataset: ordered questions, responses, per-answer evidence and sequence-level labels. Start with rules/features or a sequence classifier; consider a small Transformer/GRU only if enough data exists. | Pattern-level misconception(s), evidence across questions, confidence. |
| **C. Intervention generator** | Explain the diagnosed issue and create a targeted hint, example or follow-up question. | Usually no new model training is required for a prototype. Use an LLM with a controlled prompt, diagnosis result, approved content and output format. Optionally use a curated intervention bank. | Explanation, worked example, hint and next question. |
| **D. Reassessment / mastery logic** | Check whether the misconception is still present and update the learner record. | Begin with application logic and reviewed follow-up questions. It need not be a trained AI model. Later, use a knowledge-tracing approach if data supports it. | Resolved / still likely / uncertain; updated progress. |
| **E. Optional speech/visual tools** | Speak explanations, animate an avatar or render whiteboard instructions. | Use existing text-to-speech, avatar/animation tools and drawing/rendering code. These are not misconception models. | Audio, avatar motion, diagrams and animation. |

### Suggested Model Strategy
- **Build a baseline first.** A simple classifier and transparent rules give you a measurable starting point. Do not begin by training a large model from scratch.
- **Keep individual and sequence tasks distinct.** They use different input shapes and labels. Their predictions can be combined by a diagnosis service.
- **Use an LLM for teaching, not as proof of diagnosis accuracy.** Feed it the diagnosis and vetted learning material. Constrain it to avoid inventing facts or confidently explaining an uncertain cause.
- **Use confidence and abstention.** When evidence is weak or causes are ambiguous, ask a diagnostic question or show more than one possible explanation.

*Example:* A student gives $500\text{ m/s}$ for $100\text{ m}$ in $5\text{ s}$. The individual classifier may flag *"multiplies instead of divides."* If the student also repeatedly confuses distance, speed and acceleration across the quiz, the sequence component can flag a broader pattern. The intervention engine then selects an explanation and a new question to test that diagnosis.

### Evaluation: How to Know the Models Work
- **Individual model:** Per-class precision, recall and F1; confusion matrix; performance on unseen question forms.
- **Sequence model:** Per-pattern precision/recall/F1; test on unseen sequences and report how often it abstains when evidence is weak.
- **Intervention:** Teacher review for correctness and relevance; check whether students improve on new, related questions.
- **End-to-end:** Measure diagnosis accuracy and the proportion of students who demonstrate improvement after intervention. A correct explanation alone is not proof that learning improved.

---

## Part 3 — Website and Integration Architecture

The website is a demonstration interface, not the main research contribution. Keep it small: one subject, a few topics, a quiz, a diagnosis result, an intervention and reassessment.

### Layer Architecture
1. **Student UI:** Displays the experience and collects input (choose topic, take quiz, enter answer/work, view explanation, answer follow-up and see progress).
2. **API / session service:** Connects the UI to backend services and stores attempts (create quiz session, save ordered responses, fetch diagnosis and intervention).
3. **Content and question store:** Holds reviewed educational content and labels (topics, questions, correct solutions, misconception taxonomy, follow-up questions and intervention resources).
4. **Diagnosis service:** Runs the trained components (individual classifier + sequence model/rules; combines evidence and confidence).
5. **Intervention service:** Chooses the next teaching action (selects a curated resource or calls an LLM to produce a targeted explanation, hint or question).
6. **Reassessment and learner record:** Checks progress and keeps useful history (new question, new response analysis, unresolved/resolved/uncertain status and misconception history).
7. **Optional presentation tools:** Makes the intervention visual or spoken (3D avatar, text-to-speech, whiteboard renderer and animation tool).

### Clean User Flow
```
Student selects a topic and starts a quiz
  Website loads reviewed questions from the content store
↓
Student answers questions in order
  Website saves each answer, working and question order
↓
Individual diagnosis runs
  Model A predicts likely misconception for each response
↓
Sequence analysis runs
  Model B / sequence rules inspect related answers and patterns
↓
Diagnosis service combines evidence
  Returns likely issue(s), evidence and confidence; asks follow-up if unclear
↓
Intervention is selected or generated
  Intervention engine / LLM provides a targeted explanation, hint or example
↓
Optional teaching view presents it
  Text, 3D teacher, whiteboard drawing or generated animation
↓
Student answers a new diagnostic question
  Reassessment logic checks whether the issue remains
↓
Learner record updates
  Stores progress and recurring patterns; student can continue or retry
```

---

## Part 4 — Optional Features & Structured Whiteboard

| Optional Feature | How it works | Where it connects | Practical first version |
| :--- | :--- | :--- | :--- |
| **3D AI teacher** | Turns the intervention text into speech; an avatar plays audio with lip-sync and simple gestures. | After the intervention engine returns an explanation. | Use one ready-made avatar, text-to-speech and basic lip-sync. Avoid building a custom 3D model pipeline first. |
| **AI whiteboard** | Converts an explanation into ordered drawing commands: write text, draw a line, plot a graph, show a formula or diagram. | Intervention output includes a structured visual plan; frontend whiteboard renders it. | Support a small set of Physics primitives: axes, arrows, labels, equations and simple diagrams. Animate strokes in sequence. |
| **Concept animation** | Shows a motion or process over time, such as a moving object or changing force diagram. | Intervention engine requests an animation template based on the misconception. | Use parameterised, prebuilt animations rather than asking a generative model to create arbitrary video live. |
| **Interactive simulation** | Lets a student change a value and observe the result. | Can be offered as an intervention activity or a follow-up exploration. | Build one focused simulation, such as changing distance/time or adjusting an inclined-plane angle. |
| **Pre-quiz chapter lesson** | Shows a brief explanation before the diagnostic quiz. | At the beginning of the website flow; separate from misconception diagnosis. | Use a small amount of reviewed content for the selected topic. |

### Whiteboard Output Should be Structured
Do not rely on a language model to directly draw pixels. Ask it for a limited set of drawing instructions, validate them, and let the website render them. For example:
- `draw_axes(x_label='time', y_label='distance')` → Coordinate axes with labels
- `plot_line(points=[(0,0),(5,100)])` → A distance-time line graph
- `write_equation('speed = distance / time')` → Formula appears on the board
- `highlight('divide distance by time')` → Key step is highlighted

---

## Part 5 — Team Split and Build Order

### Suggested Split for Four Teammates
1. **Teammate 1 — Dataset:** Choose a small Physics scope, write questions, define misconception labels, create individual and sequence examples, arrange expert review. *(Deliverable: Versioned, labelled dataset + taxonomy + data guide).*
2. **Teammate 2 — Individual model:** Build baseline classifier, evaluate per misconception, add confidence/unknown handling. *(Deliverable: Runnable individual diagnosis API or module + evaluation results).*
3. **Teammate 3 — Sequence model:** Represent ordered quiz attempts, build pattern rules/baseline sequence classifier, evaluate sequence-level predictions. *(Deliverable: Sequence analysis module + test results).*
4. **Teammate 4 — Website/integration:** Build quiz flow, backend endpoints, combine model outputs, display intervention and reassessment. *(Deliverable: Working end-to-end demo and integration contract).*

### Suggested Shared Output Format
```yaml
student_attempt_id: "A-014"
predicted_misconception: "speed_time_operation"
confidence: 0.78
evidence: ["Q2: multiplied distance and time", "Q5: repeated same operation"]
status: "likely"
next_action: "targeted_explanation_and_check"
```

---

## Part 6 — Scope, Risks and Common Mistakes to Avoid

### What is Essential vs Optional?
- **Core to the problem:** Labelled misconception dataset, Individual diagnosis, Analysis of answer patterns across related questions, Personalised intervention, Reassessment and progress tracking, Evaluation on unseen examples.
- **Optional demo enhancements:** Full chapter-by-chapter LMS, 3D avatar and lip-sync, Live voice conversation, Animated whiteboard, AI-generated animations/video, Interactive Physics simulations, Large content library.

### Common Mistakes to Avoid:
1. Do not label every wrong answer as a misconception. Separate conceptual errors from arithmetic slips, unit errors, guessing and missing evidence.
2. Do not claim a broad misconception from one response unless the evidence supports it. Use a follow-up question when needed.
3. Do not train and test on near-identical copies of the same question. That can make accuracy look higher than real-world performance.
4. Do not make the LLM the only evaluator. Track measurable model performance and learning outcomes.
5. Do not spend most of the project time building a general LMS or avatar before the diagnosis and reassessment loop works.

---

## Appendix: Expanded Question Formats & Evidence (Supplement)

### Expanded Question Formats for Physics
- **MCQ / select an option:** Common conceptual distinctions and distractor choices.
- **Short conceptual / theory answer:** Definitions, causal explanations, and conceptual models.
- **Numerical problem:** Formula choice, substitution, arithmetic, and units.
- **Assertion–reason:** Whether a learner understands a claim and its explanation.
- **Case / application-based:** Transfer of a concept to a real-world or unfamiliar context.
- **Diagram / circuit / ray-diagram interpretation:** Spatial or visual understanding of a physical setup.
- **Graph / table interpretation:** Relationships, trends, slope, axes, and units.
- **Error analysis / explain a worked solution:** Ability to locate and explain an incorrect step.

### Definition of Done for Core Prototype
> *"A student can submit answers; the system can identify a likely misconception with evidence or express uncertainty; a targeted intervention is delivered; a new question is used to reassess; and the system records whether the misconception appears resolved, remains present or is uncertain. The team can show evaluation results, including a test on responses not used during training."*
