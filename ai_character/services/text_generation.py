import os
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Generation settings for Gemini
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
}

SAHAKAR_SATHI_SYSTEM_PROMPT = """You are "Sahakar Sathi" (सहकार साथी), the official 3D Embodied AI Voice Counselor, Campus Concierge, and PACS ERP Tutor for SAHAKAR-SETU (सहकार-सेतु) — an initiative under the Ministry of Cooperation, Government of India and the National Council for Cooperative Training (NCCT) (Smart India Hackathon 2026, Problem Statement 26087).

Your mission is to empower rural youth, farmers, women Self-Help Groups (SHGs), PACS Secretaries, and cooperative trainees across India's 79,630 computerizing Primary Agricultural Credit Societies (PACS) and 20 NCCT apex institutions (VAMNICOM Pune, 5 RICMs, and 14 ICMs).

You operate in three core roles:
1. In-Sandbox PACS ERP Accounting Tutor:
   - Guide trainees through NABARD Model Byelaws (25+ economic activities) and the Common Accounting System (CAS) double-entry bookkeeping rules.
   - Enforce fundamental accounting law: Total Debits must equal Total Credits (कुल डेबिट = कुल क्रेडिट).
   - Explain Daybook reconciliation, Kisan Credit Card (KCC) Kharif/Rabi crop loan disbursements, cash vault retention limits, fertilizer sales, dairy pooling, and custom hiring center accounts.
   - When a student unbalances debits/credits, clearly point out the exact mismatched amount and ledger accounts to balance it.

2. NCCT Career & Skilling Counselor:
   - Guide candidates on cooperative management courses: Higher Diploma in Cooperative Management (HDCM), Diploma in Cooperative Banking, Certificate Course in PACS Computerization, and FPO Management.
   - Explain eligibility (10+2, Graduates, PACS staff), fee waivers, stipend entitlements (verified TA/DA tied to biometric door scans), and career paths in the cooperative sector.

3. 24/7 Campus Concierge:
   - Answer arriving trainees' questions regarding hostel room and bed allocations, mess timings and daily menus, lecture timetables, and campus facilities across NCCT institutions.
   - Clarify edge biometric kiosk attendance rules (contactless INT8 MobileFaceNet face match, anti-spoofing, and dynamic QR fallback).

Behavioral Rules:
- Voice-First Clarity: Keep answers concise (2 to 4 sentences for voice clarity), warm, encouraging, and authoritative.
- Bilingual Mastery: Respond fluently in Hindi (हिंदी), English, or conversational Hinglish matching the user's spoken or written language.
- Domain-Bounded Refusal Gate: You strictly specialize in cooperatives, PACS ERP, and NCCT training. If a user asks about unrelated topics (crypto, movie gossip, entertainment, general coding unrelated to cooperatives), politely decline and redirect:
  * Hindi: "क्षमा करें, मैं केवल सहकारिता, पैक्स (PACS) ईआरपी लेखांकन, और एनसीटी (NCCT) प्रशिक्षण कार्यक्रमों में सहायता कर सकता हूँ। क्या आप पैक्स डे-बुक या सहकारिता डिप्लोमा के बारे में कुछ जानना चाहते हैं?"
  * English: "I specialize strictly in cooperative skilling, PACS ERP accounting, and NCCT training. For campus administrative escalations, please consult your NCCT Institute Coordinator."
- Never hallucinate fake government stipends, non-existent job guarantees, or unauthorized loan sanctions.
"""

class TextGenerationService:
    def __init__(self, api_key: str = None, model_name: str = None):
        api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables or .env")
        
        genai.configure(api_key=api_key)
        self.model_name = model_name or os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        
        # System instructional prompt grounded in Sahakar Sathi domain
        self.system_instruction = os.getenv("AI_CHARACTER_PROMPT", SAHAKAR_SATHI_SYSTEM_PROMPT)
        
        try:
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                system_instruction=self.system_instruction
            )
        except Exception:
            # Fallback if system_instruction parameter isn't supported by the chosen model
            self.model = genai.GenerativeModel(self.model_name)

    def generate_response(self, user_input: str, language: str = 'en') -> str:
        try:
            if not user_input or not user_input.strip():
                if language == 'hi':
                    return "नमस्ते! मैं सहकार साथी हूँ। पैक्स ईआरपी या एनसीटी प्रशिक्षण से जुड़ा अपना सवाल पूछें।"
                return "Hello! I am Sahakar Sathi. Please ask your question regarding PACS ERP, Common Accounting System, or NCCT training."
            
            lang_instruction = "Respond in clear, professional English." if language == 'en' else "Respond in clear, encouraging Hindi (हिंदी)."
            context = f"User preferred language: {lang_instruction}\nUser: {user_input.strip()}\nSahakar Sathi:"
            response = self.model.generate_content(
                context,
                generation_config=generation_config
            )
            
            if not response or not response.text:
                return "I apologize, but I was unable to generate a response. Please ask again." if language == 'en' else "क्षमा करें, मैं उत्तर तैयार नहीं कर सका। कृपया अपना प्रश्न पुनः पूछें।"
            
            return response.text.strip()
        except Exception as e:
            print(f"[TextGenerationService] Error in generate_response: {str(e)}")
            return "An error occurred while processing your request. Please try again." if language == 'en' else "तकनीकी त्रुटि के कारण उत्तर नहीं मिल सका। कृपया पुनः प्रयास करें।"

    def explain_cas_error(self, error_details: dict, language: str = 'en') -> str:
        """
        Specialized co-pilot remediation: generates instant spoken advice
        when a trainee violates Common Accounting System (CAS) rules in the PACS ERP Sandbox.
        """
        try:
            error_type = error_details.get("error_type", "CAS_BALANCE_ERROR")
            debit = error_details.get("debit", 0)
            credit = error_details.get("credit", 0)
            activity = error_details.get("activity", "KCC Kharif Loan")
            diff = abs(float(debit) - float(credit))
            
            lang_rule = "in clear English" if language == 'en' else "in Hindi with key accounting terms"
            prompt = (
                f"A trainee in the PACS ERP Sandbox made an accounting error during '{activity}'. "
                f"Error type: {error_type}. Total Debit: ₹{debit}, Total Credit: ₹{credit}. Difference: ₹{diff}. "
                f"Provide an immediate, spoken verbal remediation {lang_rule} explaining why "
                "debits and credits must balance under NABARD Common Accounting System (CAS) rules and how to fix this Daybook entry. "
                "Keep it to 2-3 spoken sentences."
            )
            return self.generate_response(prompt, language=language)
        except Exception as e:
            print(f"[TextGenerationService] Error in explain_cas_error: {e}")
            if language == 'en':
                return (
                    f"Attention! Under the Common Accounting System (CAS), Total Debits and Total Credits must always balance. "
                    f"Your Daybook currently has ₹{error_details.get('debit', 0)} Debit and ₹{error_details.get('credit', 0)} Credit. "
                    "Please adjust the cash vault or corresponding ledger account to balance the entry."
                )
            return (
                f"ध्यान दें! सामान्य लेखा प्रणाली (CAS) के तहत कुल डेबिट और क्रेडिट हमेशा बराबर होने चाहिए। "
                f"आपके डे-बुक में ₹{error_details.get('debit', 0)} डेबिट और ₹{error_details.get('credit', 0)} क्रेडिट है। "
                "अंतर को रोकड़ या संबंधित खाते में दर्ज कर संतुलित करें।"
            )

    def stream_response(self, user_input: str, language: str = 'en'):
        """Stream the response sentence by sentence using Gemini streaming API."""
        try:
            if not user_input or not user_input.strip():
                yield "Hello! Please ask your question." if language == 'en' else "नमस्ते! कृपया अपना प्रश्न पूछें।"
                return

            lang_instruction = "Respond in clear English." if language == 'en' else "Respond in natural Hindi (हिंदी)."
            context = f"User preferred language: {lang_instruction}\nUser: {user_input.strip()}\nSahakar Sathi:"
            response = self.model.generate_content(
                context,
                generation_config=generation_config,
                stream=True
            )

            buffer = ""
            sentence_end = re.compile(r'(?<=[.!?।])\s+|(?<=[.!?।])$')

            for chunk in response:
                if chunk.text:
                    buffer += chunk.text
                    parts = sentence_end.split(buffer)
                    for part in parts[:-1]:
                        part = part.strip()
                        if part:
                            yield part
                    buffer = parts[-1]

            if buffer.strip():
                yield buffer.strip()

        except Exception as e:
            print(f"[TextGenerationService] Error in stream_response: {str(e)}")
            yield "An error occurred while processing your request." if language == 'en' else "तकनीकी त्रुटि के कारण उत्तर नहीं मिल सका।"
