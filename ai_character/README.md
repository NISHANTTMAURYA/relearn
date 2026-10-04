# 🌾 Sahakar Sathi (सहकार साथी) — 3D Embodied AI Voice Counselor & ERP Tutor

**Subsystem 8 (SS8) & Innovation 4 of SAHAKAR-SETU**  
**Smart India Hackathon 2026** | **Problem Statement ID:** 26087  
**Ministry:** Ministry of Cooperation, Government of India  
**Apex Organization:** National Council for Cooperative Training (NCCT)  

---

## 📌 Overview

**Sahakar Sathi (सहकार साथी)** is a 3D embodied conversational avatar combining real-time bidirectional voice (Hindi & English), phoneme-to-viseme lip-synchronization in WebGL, strict domain-bounded cooperative RAG, and an active in-sandbox accounting error remediation loop.

It serves **79,630 Primary Agricultural Credit Societies (PACS)** undergoing national computerization and **20 NCCT apex institutions** (VAMNICOM Pune, 5 RICMs, 14 ICMs).

```
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   "SAHAKAR SATHI" 3D EMBODIED CONVERSATIONAL ARCHITECTURE                      │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
 [Trainee Voice Input]     "Hold to Speak" captures vernacular audio via Web Audio API.
            │
            ▼
 [AI4Bharat / Whisper]     High-accuracy Speech-to-Text conversion for Hindi & English.
            │
            ▼
 [Strict RAG & Refusal]    Grounded exclusively in NCCT course catalogs, VAMNICOM curricula,
                           and NABARD Model Byelaws. Refuses out-of-domain queries with zero hallucination.
            │
            ▼
 [Bilingual TTS & Visemes] Generates expressive speech audio + facial blendshape morph targets.
            │
            ▼
 [WebGL 3D Avatar Render]  Real-time Three.js avatar executes lip-synced speech, natural gestures,
                           and blinking (<25 KB/s streaming bandwidth; <3MB cached 3D asset).
            │
            ▼
 [Sandbox Co-Pilot Hook]   Active listener monitors in-browser PACS ERP state;
                           verbally interrupts and coaches trainees when double-entry errors occur.
```

---

## 🎯 4 Core Operational Modes

| Mode | Target User / Context | Key Capabilities |
| :--- | :--- | :--- |
| **1. In-Sandbox Accounting Co-Pilot** | Trainees inside `pacs_erp_sandbox.html` | Actively monitors Common Accounting System (CAS) double-entry bookkeeping. Intervenes verbally when `Debits != Credits` or loan limits are breached. |
| **2. NCCT Career & Skilling Counselor** | Rural Youth, Women SHGs, Farmers | Recommends cooperative diplomas (HDCM, PACS Computerization, FPO Management), eligibility, and career paths. |
| **3. 24/7 Campus Concierge** | Arriving trainees at institute touchscreens | Answers queries on hostel room/bed allotments, mess menus/timings, timetables, and kiosk attendance (TA/DA rules). |
| **4. Strict Refusal Gate** | All Users | Rejects out-of-domain inquiries (crypto, entertainment, unrelated topics) and provides escalation to the human Institute Coordinator. |

---

## 📂 Project Structure

```text
ai_character_standalone/
├── app.py                      # Flask microservice & CAS Co-Pilot endpoints
├── .env                        # Active API keys and environment variables
├── .env.example                # Template for environment variables
├── requirements.txt            # Python dependencies
├── README.md                   # Complete subsystem documentation
├── run.sh                      # One-click startup script
├── services/
│   ├── __init__.py
│   ├── text_generation.py      # Google Gemini LLM with Sahakar Sathi domain prompt
│   └── voice_service.py        # Bilingual TTS (Gemini TTS -> edge-tts -> gTTS -> ElevenLabs)
├── static/
│   └── models/
│       ├── avatar.glb          # Primary 3D avatar model
│       └── avatar_indian_teacher_glasses.glb  # Faculty counselor 3D avatar model
└── templates/
    ├── index.html              # Fullscreen 3D avatar canvas + quick action prompt chips
    └── popup.html              # Draggable floating widget for embedding into portals & sandboxes
```

---

## 🚀 Quick Start

### 1. Create a Virtual Environment & Install Dependencies
```bash
cd ai_character_standalone
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Ensure your `GOOGLE_API_KEY` is present.

### 3. Run the Server
```bash
python app.py
```
Or with gunicorn in production:
```bash
gunicorn -w 2 -b 0.0.0.0:5050 app:app
```

Open your browser at **[http://localhost:5050](http://localhost:5050)**!

---

## 🌐 API Routes & Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` or `/ai/` | Full-screen interactive 3D Sahakar Sathi avatar + cooperative chat interface |
| `GET` | `/popup` or `/ai/popup/` | Draggable floating popup window for embedding into existing portals |
| `POST` | `/get_response` | Text generation with Sahakar Sathi persona: `{"user_input": "..."}` |
| `POST` | `/explain_cas_error` | In-Sandbox Accounting Co-Pilot endpoint for instant debit/credit error explanation |
| `POST` | `/stream_response` | Real-time SSE streaming of text sentences and audio base64 |
| `POST` | `/text-to-speech` | Speech synthesis with automatic Hindi/English neural voice detection |
| `GET` | `/health` | Subsystem health check & SAHAKAR-SETU metadata |

---

## 🔌 How to Embed into PACS ERP Sandbox or Institute Portals

To embed Sahakar Sathi into [`pacs_erp_sandbox.html`](../pacs_erp_sandbox.html) or any HTML/React portal:

```html
<!-- Floating Sahakar Sathi AI Counselor Iframe -->
<iframe 
    src="http://localhost:5050/popup" 
    width="100%" 
    height="740px" 
    style="border: none; border-radius: 16px; box-shadow: 0 16px 48px rgba(0,0,0,0.25);"
    allow="microphone; autoplay" 
    allowfullscreen>
</iframe>
```
