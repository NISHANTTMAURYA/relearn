import os
import sys
import json
from typing import Dict, List, Any, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from pydantic import BaseModel, Field

from fastapi.staticfiles import StaticFiles

from data_service import ReLearnDataService
from models_service import ReLearnModelEngine
from whiteboard_generator import generate_dynamic_whiteboard_plan
from voice_service import VoiceService
from text_generation import TextGenerationService

app = FastAPI(
    title="Re:Learn AI Diagnostic Physics Platform API",
    description="Backend microservices for NCERT Physics misconception diagnosis, POE remediation, and sequence pattern analysis.",
    version="1.0.0"
)

# Enable CORS for local Vite development & production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static asset directory for 3D character models (static/models)
static_models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
if not os.path.exists(os.path.join(static_models_dir, "models")):
    os.makedirs(os.path.join(static_models_dir, "models"), exist_ok=True)
app.mount("/static", StaticFiles(directory=static_models_dir), name="static")

templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

data_service = ReLearnDataService()
model_engine = ReLearnModelEngine()
voice_service = VoiceService()
text_generation_service = TextGenerationService()

# Pydantic Request Models
class DiagnoseRequest(BaseModel):
    question_id: str
    question_text: str
    student_response: str
    topic: Optional[str] = None

class SequentialAttempt(BaseModel):
    step: int
    question_id: str
    question_stem: str
    student_response: str
    individual_diagnosis: Optional[str] = None
    confidence: Optional[float] = None

class SequenceAnalysisRequest(BaseModel):
    sequence_id: Optional[str] = "SESSION-LIVE-01"
    student_id: Optional[str] = "STUDENT-LIVE"
    topic: Optional[str] = "Physics"
    ordered_attempts: List[Dict[str, Any]]

class ReassessmentEvalRequest(BaseModel):
    misc_id: str
    question_id: str
    student_selection_key: str
    correct_key: str
    prior_mastery: Optional[float] = 0.15

class WhiteboardPlanRequest(BaseModel):
    concept: Optional[str] = "Optics"
    question_stem: Optional[str] = ""
    student_response: Optional[str] = ""
    misconception_label: Optional[str] = ""

class CharacterSpeakRequest(BaseModel):
    text: Optional[str] = None
    misconception_id: Optional[str] = None
    voice: Optional[str] = None

# Routes
@app.get("/")
def root():
    return {
        "platform": "Re:Learn AI Diagnostic Physics Platform",
        "status": "operational",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "model_a_deberta_loaded": model_engine.deberta_model is not None,
        "model_a_device": model_engine.device,
        "model_a_baseline_loaded": model_engine.baseline_pipeline is not None,
        "model_b_sequence_analyzer_loaded": model_engine.sequence_analyzer is not None,
        "curriculum_families_count": len(data_service.curriculum_families),
        "total_misconceptions": len(data_service.taxonomy.get("misconceptions_index", []))
    }

@app.get("/api/topics")
def get_topics():
    """Returns curriculum chapters (Optics, Human Eye, Electricity, Magnetism, Mechanics) and questions."""
    try:
        topics = data_service.get_topics_and_questions()
        return {"topics": topics}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/diagnose")
def diagnose_response(req: DiagnoseRequest):
    """Predicts underlying misconception using Model A (DeBERTa / Baseline Pipeline) with abstention logic."""
    try:
        diagnosis = model_engine.diagnose_individual_response(
            question_id=req.question_id,
            question_stem=req.question_text,
            student_response=req.student_response,
            topic=req.topic
        )
        return diagnosis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/sequence-pattern")
def analyze_sequence(req: SequenceAnalysisRequest):
    """Accepts sequential attempts, running Model B (Sequence Analyzer) to classify learning patterns."""
    try:
        session_data = {
            "sequence_id": req.sequence_id,
            "student_id": req.student_id,
            "topic": req.topic,
            "ordered_attempts": req.ordered_attempts
        }
        result = model_engine.analyze_sequence_patterns(session_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/intervention/{misc_id}")
def get_intervention(misc_id: str):
    """Returns targeted Predict-Observe-Explain (POE) remediation, PhET simulation links, and whiteboard instructions."""
    intervention = data_service.get_intervention(misc_id)
    if not intervention:
        raise HTTPException(status_code=404, detail=f"No intervention found for misconception {misc_id}")
    return intervention

@app.get("/api/reassessment/{misc_id}")
def get_reassessment(misc_id: str):
    """Returns isomorphic near-transfer question for post-intervention testing."""
    reassessment_pair = data_service.get_reassessment(misc_id)
    if not reassessment_pair:
        raise HTTPException(status_code=404, detail=f"No reassessment pair found for misconception {misc_id}")
    return reassessment_pair

@app.post("/api/evaluate-reassessment")
def evaluate_reassessment(req: ReassessmentEvalRequest):
    """Evaluates student's follow-up answer, updating BKT learner state."""
    try:
        eval_result = model_engine.evaluate_bkt_reassessment(
            misc_id=req.misc_id,
            question_id=req.question_id,
            student_choice=req.student_selection_key,
            correct_choice=req.correct_key,
            prior_mastery=req.prior_mastery or 0.15
        )
        return eval_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-whiteboard")
def generate_whiteboard(req: WhiteboardPlanRequest):
    """Dynamically generates structured drawing commands and narration for any physics misconception."""
    try:
        plan = generate_dynamic_whiteboard_plan(
            concept=req.concept or "Physics",
            question_stem=req.question_stem or "",
            student_response=req.student_response or "",
            misconception_label=req.misconception_label or ""
        )
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/analytics")
def get_analytics():
    """Returns comprehensive dataset metrics (12,600 responses, 2,700 sequences, 42 families) and model metrics."""
    return {
        "dataset_summary": {
            "total_individual_responses": 21000,
            "total_longitudinal_sequences": 2700,
            "total_codified_misconceptions": 21,
            "total_curriculum_families": 42,
            "diagnostic_items_in_bank": 16,
            "disambiguation_cases": 4,
            "remediation_catalog_entries": len(data_service.interventions_map),
            "reassessment_pairs": len(data_service.reassessment_map)
        },
        "individual_dataset_splits": {
            "train": 13860,
            "val": 3360,
            "test": 3780
        },
        "sequence_dataset_splits": {
            "train": 1890,
            "val": 405,
            "test": 405
        },
        "model_performance_benchmarks": {
            "model_a_deberta_primary": {
                "architecture": "DeBERTa-v3-small + HuggingFace PyTorch",
                "test_accuracy": 0.8859,
                "macro_f1": 0.8678,
                "ood_generalization_accuracy": 0.8889,
                "latency_gpu_ms": 12.4
            },
            "model_a_baseline": {
                "architecture": "TF-IDF N-grams (1-3) + Multinomial Naive Bayes / Logistic Regression",
                "test_accuracy": 0.825,
                "macro_f1": 0.812,
                "latency_cpu_ms": 0.8
            },
            "model_b_sequence_analyzer": {
                "architecture": "Stateful Sequence Transition Rule Engine & Temporal Classifier",
                "pattern_accuracy": 1.000,
                "classes_tracked": [
                    "RECURRENT_PERSISTENT_MISCONCEPTION",
                    "TRANSIENT_SLIP_WITH_CONCEPTUAL_MASTERY",
                    "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
                    "AMBIGUOUS_INCONSISTENT_RESPONSES"
                ]
            }
        },
        "chapters_covered": [
            {"chapter": "Light – Reflection and Refraction", "grade": "Class 10", "items": 4, "families": 6},
            {"chapter": "The Human Eye and Colourful World", "grade": "Class 10", "items": 4, "families": 4},
            {"chapter": "Electricity", "grade": "Class 10", "items": 4, "families": 6},
            {"chapter": "Magnetic Effects of Electric Current", "grade": "Class 10", "items": 4, "families": 5},
            {"chapter": "Motion, Force and Gravitation", "grade": "Class 9", "items": 4, "families": 21}
        ]
    }

@app.get("/api/taxonomy")
def get_taxonomy():
    """Returns the 21 codified NCERT physics misconceptions, naive mental models, and ground truths."""
    return data_service.get_taxonomy_index()

@app.get("/api/disambiguation-cases")
def get_disambiguation():
    """Returns competing misconception disambiguation cases."""
    return data_service.get_disambiguation_cases()

@app.get("/api/benchmark-history")
def get_benchmark_history():
    """Returns official benchmark optimization timeline across all loop iterations."""
    history_path = os.path.join(ROOT_DIR, "dataset", "models_and_baselines", "benchmark_history.json")
    if os.path.exists(history_path):
        try:
            with open(history_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []

@app.post("/api/character/speak")
@app.post("/api/text-to-speech")
def character_speak(req: CharacterSpeakRequest):
    """
    Generates TTS audio & viseme lip-sync markers for 3D AI Physics Tutor avatar.
    Accepts text directly, or misconception_id to fetch target POE explanation.
    """
    try:
        text = req.text
        if not text and req.misconception_id:
            intervention = data_service.get_intervention(req.misconception_id)
            if intervention:
                m_name = intervention.get("misconception_name", "this concept")
                poe = intervention.get("poe_explanation", "")
                strat = intervention.get("pedagogical_strategy", "")
                text = f"Hello! Let's address misconception {req.misconception_id}: {m_name}. {poe} {strat}"
        
        if not text:
            text = "Welcome to Re:Learn AI Physics Studio! I am your 3D Embodied AI Physics Tutor."

        payload = voice_service.speak(text)
        return payload
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ai/", response_class=HTMLResponse)
@app.get("/ai-character", response_class=HTMLResponse)
@app.get("/ai-character/", response_class=HTMLResponse)
def get_ai_character_standalone():
    """Serves the standalone 3D embodied character canvas."""
    index_path = os.path.join(templates_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    raise HTTPException(status_code=404, detail="AI Character template not found")

@app.get("/ai/popup/", response_class=HTMLResponse)
@app.get("/ai-character/popup", response_class=HTMLResponse)
def get_ai_character_popup():
    """Serves the draggable floating 3D avatar popup modal."""
    popup_path = os.path.join(templates_dir, "popup.html")
    if os.path.exists(popup_path):
        with open(popup_path, "r", encoding="utf-8") as f:
            return f.read()
    raise HTTPException(status_code=404, detail="Popup template not found")

@app.post("/get_response")
@app.post("/ai/get_response/")
async def ai_get_response(request: Request):
    """Generates conversational responses and audio for the standalone 3D avatar interface."""
    try:
        data = await request.json() if request.headers.get("content-type") == "application/json" else {}
        user_input = data.get("user_input", "") or ""
        include_audio = data.get("include_audio", False)
        language = data.get("language", "en")

        resp_text = text_generation_service.generate_response(user_input, language=language)
        audio_b64 = None
        if include_audio:
            try:
                audio_payload = voice_service.speak(resp_text)
                audio_b64 = audio_payload.get("audio_base64")
            except Exception:
                pass

        return {
            "response": resp_text,
            "audio": audio_b64,
            "language": language,
            "speaker": "Prof. Maya (Re:Learn AI Physics Mentor)"
        }
    except Exception as e:
        return {"response": f"Let's explore that physics concept together! {e}", "audio": None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
