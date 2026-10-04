import os
import re
from typing import Dict, Any, Generator, Optional
from dotenv import load_dotenv

load_dotenv()

# Try importing google.generativeai gracefully
try:
    import google.generativeai as genai
except ImportError:
    genai = None

RELEARN_PHYSICS_TUTOR_SYSTEM_PROMPT = """You are "Prof. Maya / Re:Learn 3D AI Physics Tutor", the 3D Embodied AI Voice Counselor and Physics Educator for the Re:Learn Adaptive Diagnostic Platform (Class 9 & 10 NCERT Physics).

Your mission is to guide students through conceptual physics misconceptions, especially:
1. Light & Optics: Half-lens blocking fallacy (covering half a lens dims the entire image, it does not cut the top or bottom off!), virtual image projection, plane mirror distance doubling.
2. Electricity: Current consumption fallacy (current is conserved in a closed series loop, it does NOT get consumed or attenuated by bulbs!), potential drop vs current.
3. Mechanics: Gravitation & free fall (all objects fall with identical gravitational acceleration g = 9.8 m/s² regardless of mass in vacuum!), action-reaction forces.
4. Human Eye & Vision: Myopia (concave lens needed) vs Hypermetropia (convex lens needed).

Behavioral Rules:
- Voice-First Clarity: Keep answers concise (2 to 4 sentences for voice synthesis clarity), warm, encouraging, and pedagogically grounded.
- Predict-Observe-Explain (POE): Guide the learner to predict what happens, explain the scientific observation, and contrast naive mental models with scientific ground truths.
- Bilingual Support: Speak clearly in English, Hindi, or conversational Hinglish matching the student's prompt.
"""

class TextGenerationService:
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.model_name = model_name or os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        self.model = None

        if self.api_key and genai:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel(
                    model_name=self.model_name,
                    system_instruction=RELEARN_PHYSICS_TUTOR_SYSTEM_PROMPT
                )
            except Exception as e:
                print(f"[TextGenerationService] genai init note: {e}")
                try:
                    self.model = genai.GenerativeModel(self.model_name)
                except Exception:
                    self.model = None

    def generate_response(self, user_input: str, language: str = 'en') -> str:
        text = user_input.strip() if user_input else ""
        if not text:
            if language == 'hi':
                return "नमस्ते! मैं री-लर्न भौतिकी एआई मेंटर हूँ। प्रकाश, विद्युत या गति से जुड़ा अपना सवाल पूछें।"
            return "Hello! I am your Re:Learn 3D AI Physics Mentor. Ask me any question on optics, electricity, gravitation, or your quiz misconceptions!"

        if self.model:
            try:
                lang_rule = "Respond in clear English." if language == 'en' else "Respond in encouraging Hindi/Hinglish."
                prompt = f"{lang_rule}\nUser Question: {text}\nRe:Learn Physics Tutor:"
                res = self.model.generate_content(prompt)
                if res and res.text:
                    return res.text.strip()
            except Exception as e:
                print(f"[TextGenerationService] Gemini generation error: {e}")

        # Intelligent physics knowledge-grounded fallback
        lower_q = text.lower()
        if "lens" in lower_q or "half" in lower_q or "cover" in lower_q:
            return (
                "When you cover the lower half of a convex lens, every point on the object still sends rays through the uncovered upper half. "
                "Therefore, the complete image is still formed on the screen! The only change is that the image brightness is halved because fewer light rays contribute to the focus."
            )
        elif "current" in lower_q or "bulb" in lower_q or "consume" in lower_q or "series" in lower_q:
            return (
                "Remember: electric current is the continuous rate of flow of charge (I = Q/t), which is conserved in a closed series loop! "
                "The current leaving the battery equals the current passing through every single component. Energy is transferred, but electrons are never used up or consumed."
            )
        elif "heavy" in lower_q or "drop" in lower_q or "fall" in lower_q or "gravity" in lower_q:
            return (
                "In a vacuum, both heavy and light objects fall at the exact same rate! As Galileo demonstrated, the acceleration due to gravity g = GM/R² is completely independent of the falling object's mass. Any difference in air is solely due to drag resistance."
            )
        elif "mirror" in lower_q or "distance" in lower_q:
            return (
                "In a plane mirror, the virtual image is formed at the exact same distance behind the mirror as the object is in front of it (v = -u). If you stand 2 meters in front of the mirror, the total distance between you and your image is 4 meters!"
            )
        else:
            return (
                f"Great physics inquiry! When analyzing '{text}', always start from fundamental conservation principles. "
                "Identify the known parameters, check the signs according to Cartesian convention, and verify whether the physical quantity is conserved."
            )

    def stream_response(self, user_input: str, language: str = 'en') -> Generator[str, None, None]:
        full_text = self.generate_response(user_input, language=language)
        sentences = re.split(r'(?<=[.!?])\s+', full_text)
        for s in sentences:
            if s.strip():
                yield s.strip()

    def explain_cas_error(self, error_details: Dict[str, Any], language: str = 'en') -> str:
        return self.generate_response(str(error_details), language=language)
