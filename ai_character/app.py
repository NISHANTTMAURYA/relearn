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

@app.after_request
def allow_iframe_embedding(response):
    response.headers['X-Frame-Options'] = 'ALLOWALL'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

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
        "service": "prof-vikram",
        "name": "Prof. Vikram — 3D Embodied AI Physics Mentor",
        "system": "Re:Learn Multimodal Diagnostic Engine",
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
            "speaker": "Prof. Vikram"
        })

    except Exception as e:
        print(f"[app] Error in get_response: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/explain_misconception', methods=['POST'])
@app.route('/ai/explain_misconception/', methods=['POST'])
def explain_misconception():
    """
    Physics Misconception Remediation Endpoint:
    Provides real-time verbal 3D character coaching when a student makes a conceptual error.
    """
    try:
        data = request.get_json(silent=True) if request.is_json else request.form.to_dict()
        data = data or {}
        language = data.get('language', 'en').lower()
        misconception_id = data.get('misconception_id', 'UNKNOWN_MISCONCEPTION')
        question_stem = data.get('question_stem', '')
        student_answer = data.get('student_answer', '')

        explanation = text_generation_service.explain_misconception(misconception_id, question_stem, student_answer, language=language)
        audio_base64, _ = voice_service.text_to_speech(explanation)

        return jsonify({
            "response": explanation,
            "audio": audio_base64,
            "language": language,
            "event": "MISCONCEPTION_REMEDIATION",
            "speaker": "Prof. Vikram"
        })
    except Exception as e:
        print(f"[app] Error in explain_misconception: {e}")
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

    print(f"Re:Learn 3D AI Physics Mentor Server")
    print(f"Running at http://localhost:{port}/ ...")
    app.run(host=host, port=port, debug=debug)

