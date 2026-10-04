import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from flask_cors import CORS

from services.text_generation import TextGenerationService
from services.voice_service import VoiceService

# Resolve absolute base directory of the standalone module
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load environment configuration (first from module dir, then fallback to current dir)
load_dotenv(os.path.join(BASE_DIR, ".env"))
load_dotenv()

app = Flask(
    __name__,
    root_path=BASE_DIR,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static"
)
app.secret_key = os.getenv("SECRET_KEY", "ai-character-standalone-secret-key")

# Enable CORS for cross-origin embedding & frontend access
CORS(app)

# Initialize AI and Voice services
text_generation_service = TextGenerationService()
voice_service = VoiceService()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE ROUTES
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/')
@app.route('/ai/')
def index():
    """Main interactive 3D character canvas & chat interface."""
    return render_template('index.html')


@app.route('/popup')
@app.route('/ai/popup/')
def popup():
    """Draggable floating modal popup embedding the AI assistant."""
    return render_template('popup.html')


@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "service": "sahakar-sathi",
        "name": "Sahakar Sathi (सहकार साथी) — 3D Embodied AI Voice Counselor & ERP Tutor",
        "ecosystem": "SAHAKAR-SETU",
        "ministry": "Ministry of Cooperation, Government of India",
        "apex_organization": "NCCT (National Council for Cooperative Training)",
        "sih_problem_id": "26087",
        "version": "2.0.0"
    })


# ─────────────────────────────────────────────────────────────────────────────
# API ENDPOINTS
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/get_response', methods=['POST'])
@app.route('/ai/get_response/', methods=['POST'])
def get_response():
    """Generates an AI character response to the user's input."""
    try:
        user_input = ""
        include_audio = False
        language = "en"
        if request.is_json:
            data = request.get_json(silent=True) or {}
            user_input = data.get('user_input', '').strip()
            include_audio = data.get('include_audio', False)
            language = data.get('language', 'en').lower()
        else:
            user_input = request.form.get('user_input', '').strip()
            include_audio = request.form.get('include_audio', 'false').lower() in ('true', '1')
            language = request.form.get('language', 'en').lower()

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        response_text = text_generation_service.generate_response(user_input, language=language)
        
        audio_base64 = None
        if include_audio:
            audio_base64, _ = voice_service.text_to_speech(response_text)

        return jsonify({
            "response": response_text,
            "audio": audio_base64,
            "language": language,
            "speaker": "Sahakar Sathi (सहकार साथी)"
        })

    except Exception as e:
        print(f"[app] Error in get_response: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/explain_cas_error', methods=['POST'])
@app.route('/ai/explain_cas_error/', methods=['POST'])
def explain_cas_error():
    """
    In-Sandbox Accounting Co-Pilot endpoint:
    Provides real-time verbal coaching when a trainee violates NABARD Common Accounting System (CAS) rules.
    """
    try:
        data = request.get_json(silent=True) if request.is_json else request.form.to_dict()
        data = data or {}
        language = data.get('language', 'en').lower()
        
        explanation = text_generation_service.explain_cas_error(data, language=language)
        audio_base64, _ = voice_service.text_to_speech(explanation)

        return jsonify({
            "response": explanation,
            "audio": audio_base64,
            "language": language,
            "event": "CAS_COACH_REMEDIATION",
            "speaker": "Sahakar Sathi (सहकार साथी)"
        })
    except Exception as e:
        print(f"[app] Error in explain_cas_error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/text-to-speech', methods=['POST'])
@app.route('/text_to_speech', methods=['POST'])
@app.route('/ai/text_to_speech/', methods=['POST'])
def text_to_speech():
    """Converts input text into speech base64 audio."""
    try:
        text = ""
        if request.is_json:
            data = request.get_json(silent=True) or {}
            text = data.get('text', '').strip()
        else:
            text = request.form.get('text', '').strip()

        if not text:
            return jsonify({"error": "No text provided"}), 400

        audio_base64, error = voice_service.text_to_speech(text)
        if audio_base64:
            return jsonify({"audio": audio_base64, "error": None})
        
        # Audio failure shouldn't crash the frontend chat experience
        return jsonify({"audio": None, "error": error or "TTS unavailable"}), 200

    except Exception as e:
        print(f"[app] Error in text_to_speech: {e}")
        return jsonify({"audio": None, "error": str(e)}), 500


@app.route('/stream_response', methods=['POST'])
@app.route('/ai/stream_response/', methods=['POST'])
def stream_response():
    """
    Server-Sent Events (SSE) streaming endpoint:
    Yields sentence-by-sentence text and its corresponding TTS audio in real-time.
    """
    try:
        user_input = ""
        language = "en"
        if request.is_json:
            data = request.get_json(silent=True) or {}
            user_input = data.get('user_input', '').strip()
            language = data.get('language', 'en').lower()
        else:
            user_input = request.form.get('user_input', '').strip()
            language = request.form.get('language', 'en').lower()

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        def event_stream():
            full_text = []
            for sentence in text_generation_service.stream_response(user_input, language=language):
                full_text.append(sentence)
                audio_b64, error = voice_service.text_to_speech(sentence)
                payload = json.dumps({
                    "sentence": sentence,
                    "audio": audio_b64 if not error else None,
                    "language": language,
                    "speaker": "Sahakar Sathi"
                })
                yield f"data: {payload}\n\n"
            
            yield f"data: {json.dumps({'done': True, 'full_text': ' '.join(full_text)})}\n\n"

        return Response(
            stream_with_context(event_stream()),
            mimetype='text/event-stream',
            headers={
                'Cache-Control': 'no-cache',
                'X-Accel-Buffering': 'no'
            }
        )

    except Exception as e:
        print(f"[app] Error in stream_response: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5050))
    host = os.getenv("HOST", "0.0.0.0")
    debug = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

    print(f"🌾 Sahakar Sathi (सहकार साथी) — SAHAKAR-SETU AI Assistant")
    print(f"🏛️ Ministry of Cooperation | NCCT | SIH-26087")
    print(f"🚀 Running at http://localhost:{port}/ (http://{host}:{port}/) ...")
    app.run(host=host, port=port, debug=debug)
