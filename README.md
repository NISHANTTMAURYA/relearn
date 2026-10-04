# Re:Learn — AI-Powered Diagnostic Physics Learning Platform

Re:Learn is an AI-powered diagnostic physics learning system designed for Class 9 and 10 students and educators. Grounded in NCERT Science Class 10/9 standards, CBSE authentic error patterns, and classic physics education research (McDermott & Shaffer 1992, Viennot 1979, Driver 1994), Re:Learn identifies **why** a student formulated a wrong answer, differentiates competing misconceptions for identical wrong answers, detects multi-step sequence patterns, provides targeted multimodal remediation (Predict-Observe-Explain sequences, structured AI whiteboard vector animations, interactive PhET simulations, and voice AI explanations), and evaluates schema generalization through isomorphic near-transfer reassessment with Bayesian Knowledge Tracing (BKT).

---

## 🏛️ System Architecture

### 1. Backend Microservices (`backend/`)
- **Framework:** Python FastAPI (`backend/main.py`)
- **Model A (Individual Misconception Classifier):**
  - **Primary Model:** Fine-tuned `DeBERTa-v3-small` running on PyTorch CUDA GPU (`dataset/models_and_baselines/deberta_primary_model/`) with 92.36%+ validation accuracy and high Out-of-Distribution (OOD) generalization across 12,600 records and 21 misconception classes.
  - **Baseline Pipeline:** TF-IDF (1–3 n-grams) + Multinomial Logistic Regression (`dataset/models_and_baselines/individual_misconception_model.pkl`).
  - **Abstention Logic:** Abstains to `UNSURE_INSUFFICIENT_EVIDENCE` when inputs express explicit doubt or low diagnostic confidence (<40%), prescribing an active diagnostic probe.
- **Model B (Sequence Pattern Analyzer):**
  - Stateful temporal sequence analyzer (`dataset/models_and_baselines/train_sequence_analyzer.py`) tracking 2,700 longitudinal student sessions across 45 trajectory archetypes (recurrent misconceptions, transient slips, and post-intervention remediation shifts).
- **Dynamic Whiteboard Generator (`backend/whiteboard_generator.py`):**
  - REST Endpoint: `POST /api/generate-whiteboard`
  - Generates structured, step-by-step vector drawing commands and narration in a JSON Drawing DSL (optical axes, lenses, rays, paper masks, circuits, ammeters, callouts). Zero video fine-tuning needed.
- **Remediation & Mastery Engine:**
  - 4-step Predict-Observe-Explain (POE) guided learning sequence.
  - PhET Interactive Simulation embed references (University of Colorado Boulder).
  - Bayesian Knowledge Tracing (BKT) updating prior mastery $P(L_t) \to P(L_{t+1})$ upon post-intervention reassessment.

### 2. Frontend Web Application (`frontend/`)
- **Framework:** React 18 + Vite + Tailwind CSS + Lucide React
- **Design Read:** High-calibre, calm academic publication UI (#FBFBFA canvas, #0F172A charcoal typography, slate borders, indigo accents, emerald mastery indicators).
- **5 Question Input Modalities (PDF Specification):**
  1. **📝 Theory & Physical Reasoning:** Typed explanation with quick physics math symbol toolbar ($\lambda, \Omega, \Delta, \mu, \theta, f, v, u, I, R, V, P, g, a$) and a live benchmark demonstrating how **Two Students with the Same Wrong Answer** receive different diagnoses.
  2. **🔢 Step-by-Step Numerical Derivation:** Formatted to CBSE marking schemes (Formula Used, Sign Conventions & Given Values, Algebraic Steps, Final SI Unit).
  3. **📷 Handwritten Solution Photo (OCR):** Upload photo or select notebook scans; PaddleOCR/Vision pipeline extracts handwritten formulas for confirmation before diagnosis.
  4. **✏️ Diagram & Ray Drawing Pad:** Interactive canvas where students sketch ray paths or circuits; vector coordinates are extracted as diagnostic evidence.
  5. **🔘 Multiple-Choice (MCQ) Distractor Analysis:** Option selection mapped to specific NCERT mental models with mandatory justification.
- **Core Views:**
  1. **Interactive Diagnostic Studio:** Complete 6-step diagnostic and remediation loop.
  2. **Technical Whiteboard Player with DSL Inspector:** Light mode graph paper whiteboard displaying step-by-step ray and circuit tracing, with a live JSON DSL Inspector drawer.
  3. **Learner Cognitive Record:** Persistent BKT history and cognitive trajectory tracker.
  4. **Disambiguation Lab (Requirement 3):** Dedicated interactive tool separating competing misconceptions that produce identical wrong answers.
  5. **Taxonomy Browser:** 21 codified NCERT physics misconceptions and naive mental models.
  6. **Research & Benchmarks Dashboard:** Analytics for the 12,600 record dataset, 2,700 sequences, and model performance.

---

## 📊 Dataset & Model Benchmarks

| Metric / Dataset Component | Value / Benchmark |
| :--- | :--- |
| **Total Individual Response Dataset** | **12,600 authoritative records** across 42 NCERT curriculum families |
| **Dataset Partitioning** | 8,232 Train / 2,016 Val / 2,352 Held-Out Test (100% Template-Disjoint) |
| **Longitudinal Student Sequences** | **2,700 sessions** across 45 trajectory archetypes |
| **Primary Model A (DeBERTa-v3 GPU)** | **87.37% Held-Out Test Acc** (Macro F1: 0.8378) | **90.48% OOD Challenge Benchmark** |
| **Secondary Model B (Sequence Tracker)** | **100.0% Pattern Recognition Accuracy** |
| **Schema Validation** | 100% Passed (`validate_dataset.py`, 0 errors, 0 warnings) |

---

## 🚀 Quickstart & Launcher Instructions

### Unified Launcher
Run both Backend and Frontend together:
```bash
python run_app.py
```

### Manual Commands

**Backend (FastAPI):**
```bash
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
- API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Health Check: [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)
- Whiteboard API: [http://127.0.0.1:8000/api/generate-whiteboard](http://127.0.0.1:8000/api/generate-whiteboard)

**Frontend (Vite React):**
```bash
cd frontend
npm install
npm run dev
```
- Application UI: [http://localhost:5173](http://localhost:5173)

---

## 🧪 Verification & Build Tests

**API Endpoint Test Suite:**
```bash
cd backend
python test_api_endpoints.py
```

**Frontend Production Build:**
```bash
cd frontend
npm run build
```

**Dataset Validation:**
```bash
python dataset/scripts/validate_dataset.py
```
