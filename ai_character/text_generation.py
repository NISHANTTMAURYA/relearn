import os
import re
from dotenv import load_dotenv

load_dotenv()

PROF_VIKRAM_SYSTEM_PROMPT = """You are Prof. Vikram, an expert male 3D AI Physics Mentor for the Re:Learn Multimodal AI Platform.
You specialize in secondary school physics (NCERT Class 9-10 standards), specifically diagnosing physics misconceptions, guiding Predict-Observe-Explain (POE) physical demonstrations, and clarifying concepts in optics, electricity, magnetism, and mechanics.

Core Pedagogical Philosophy:
1. Grounded in Physics First-Principles: You do not just give direct answers; you explain underlying physical mechanisms (light ray convergence, wave optics, charge conservation, magnetic flux, free-fall gravitational acceleration invariant g=GM/R^2).
2. Predict-Observe-Explain (POE) Framework: When addressing misconceptions (such as covering half a convex lens, current getting consumed in a series circuit, or heavier objects falling faster), guide the student through:
   - Predict: Acknowledge intuitive/naive predictions.
   - Observe: Explain what actually happens in physical experiments or PhET simulations.
   - Explain: Provide clear mathematical and qualitative explanations.
3. Voice-First Clarity: Keep spoken responses concise (2 to 4 sentences), highly articulate, encouraging, and easy to listen to.
4. Multimodal Integration: Refer to the visual whiteboard, ray diagrams, and interactive simulations available on the Re:Learn platform.
"""

class TextGenerationService:
    def __init__(self, api_key: str = None, model_name: str = None):
        self.system_instruction = PROF_VIKRAM_SYSTEM_PROMPT

    def _fallback_physics_response(self, user_input: str) -> str:
        text = user_input.lower()
        if "lens" in text or "light" in text or "optics" in text or "half" in text or "mirror" in text:
            return "When you cover half of a convex lens, every exposed part still receives light rays from all points of the object. Therefore, the complete image remains intact on the screen, but its overall brightness is reduced by 50%!"
        elif "twinkle" in text or "star" in text or "refraction" in text or "eye" in text or "atmosphere" in text:
            return "Stars twinkle because starlight passes through turbulent layers of the Earth's atmosphere with continuously fluctuating densities and refractive indices, causing the apparent brightness and position to shift rapidly before reaching our eyes."
        elif "current" in text or "bulb" in text or "electric" in text or "circuit" in text or "series" in text:
            return "Electric current is the rate of flow of electric charge. In a series circuit, charge is strictly conserved! Bulbs transform electrical potential energy into heat and light, but they never consume the electric current."
        elif "fall" in text or "gravity" in text or "heavy" in text or "mass" in text:
            return "In vacuum free fall, all objects accelerate at the exact same rate g = GM/R^2 regardless of their mass. The mass of the falling object cancels out completely from the equation of motion!"
        elif "magnet" in text or "field" in text:
            return "Two magnetic field lines can never cross each other because at the point of intersection, a magnetic compass needle would have to point in two different directions at once, which is physically impossible."
        else:
            return f"Hello! I am Prof. Vikram, your 3D AI Physics Mentor. Regarding '{user_input}': in NCERT Physics, we evaluate physical phenomena by examining the underlying forces, field laws, and energy conservation principles!"

    def generate_response(self, user_input: str, language: str = 'en') -> str:
        if not user_input or not user_input.strip():
            return "Hello! I am Prof. Vikram, your 3D AI Physics Mentor for Re:Learn. Ask me any physics question or misconception to begin!"
        return self._fallback_physics_response(user_input)

    def explain_physics_misconception(self, misc_details: dict, language: str = 'en') -> str:
        misc_id = misc_details.get("misconception_id", "MISC-OPT-001")
        misc_name = misc_details.get("name", "Half-Lens Blocking Fallacy")
        return f"Regarding misconception {misc_id} ({misc_name}): Remember that light rays from every point of an object travel across the full aperture of the lens. Blocking part of the lens changes the total light intensity, not the image geometry!"

    def stream_response(self, user_input: str, language: str = 'en'):
        response = self.generate_response(user_input, language)
        sentences = re.split(r'(?<=[.!?])\s+', response)
        for sentence in sentences:
            if sentence.strip():
                yield sentence.strip()
