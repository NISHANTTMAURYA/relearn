import os
import io
import wave
import base64
import asyncio
import re
from typing import Dict, List, Any, Tuple, Optional
from dotenv import load_dotenv

load_dotenv()

# Try importing optional TTS dependencies gracefully
try:
    import google.generativeai as genai
except ImportError:
    genai = None

try:
    import edge_tts
except ImportError:
    edge_tts = None

try:
    from gtts import gTTS
except ImportError:
    gTTS = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None


class VoiceService:
    """
    Multi-Tier Text-to-Speech (TTS) & Viseme Generation Engine for Re:Learn.
    Supports:
    - Gemini AI Voice (gemini-3.8-flash-tts / gemini-2.5-flash-preview-tts)
    - Microsoft Edge TTS (Free Neural Voices: en-US-AvaNeural / en-IN-PrabhatNeural)
    - Google Translate TTS (gTTS)
    - pyttsx3 (Offline SAPI5/NSSpeech)
    """

    def __init__(
        self,
        google_api_key: Optional[str] = None,
        gemini_voice: str = "Fenrir",
        edge_voice: str = "en-IN-PrabhatNeural"
    ):
        self.google_api_key = google_api_key or os.getenv("GOOGLE_API_KEY")
        self.gemini_voice = gemini_voice
        self.edge_voice = edge_voice

        if self.google_api_key and genai:
            try:
                genai.configure(api_key=self.google_api_key)
            except Exception as e:
                print(f"[VoiceService] Error configuring genai: {e}")

    def generate_visemes(self, text: str, estimated_duration_sec: float = 3.0) -> List[Dict[str, Any]]:
        """
        Generates simulated viseme timelines for 3D character lip-sync.
        Viseme IDs correspond to standard ReadyPlayerMe morph targets:
        viseme_aa, viseme_E, viseme_I, viseme_O, viseme_U, viseme_PP, viseme_FF, viseme_sil
        """
        words = re.findall(r'\w+', text.lower())
        if not words:
            return [{"time": 0.0, "viseme": "viseme_sil", "weight": 0.0}]

        visemes_seq = []
        time_cursor = 0.0
        sec_per_char = max(0.04, estimated_duration_sec / max(len(text), 1))

        vowel_map = {
            'a': 'viseme_aa',
            'e': 'viseme_E',
            'i': 'viseme_I',
            'o': 'viseme_O',
            'u': 'viseme_U',
            'p': 'viseme_PP',
            'b': 'viseme_PP',
            'm': 'viseme_PP',
            'f': 'viseme_FF',
            'v': 'viseme_FF'
        }

        for word in words:
            for char in word:
                v_type = vowel_map.get(char, 'viseme_aa' if char in 'ydw' else 'jawOpen')
                weight = 0.8 if char in 'aeiou' else 0.4
                visemes_seq.append({
                    "time": round(time_cursor, 3),
                    "viseme": v_type,
                    "weight": weight
                })
                time_cursor += sec_per_char
            
            # Short pause between words
            visemes_seq.append({
                "time": round(time_cursor, 3),
                "viseme": "viseme_sil",
                "weight": 0.0
            })
            time_cursor += sec_per_char * 0.5

        return visemes_seq

    def text_to_speech(self, text: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Converts text to speech audio using multi-tier fallback.
        Returns: (base64_audio_string, error_message)
        """
        if not text or not text.strip():
            return None, "No text provided"

        cleaned_text = (
            text.replace('*', '')
                .replace('#', '')
                .replace('`', '')
                .replace('>', '')
                .strip()
        )

        # Tier 1: Gemini AI TTS
        if self.google_api_key and genai:
            try:
                audio_b64 = self._gemini_tts(cleaned_text)
                if audio_b64:
                    return audio_b64, None
            except Exception as e:
                print(f"[VoiceService] Gemini TTS failed ({e}), trying edge-tts...")

        # Tier 2: Microsoft edge-tts
        if edge_tts:
            try:
                audio_b64 = asyncio.run(self._edge_tts(cleaned_text))
                if audio_b64:
                    return audio_b64, None
            except Exception as e:
                print(f"[VoiceService] edge-tts failed ({e}), trying gTTS...")

        # Tier 3: gTTS
        if gTTS:
            try:
                audio_b64 = self._gtts(cleaned_text)
                if audio_b64:
                    return audio_b64, None
            except Exception as e:
                print(f"[VoiceService] gTTS failed ({e}), trying pyttsx3...")

        # Tier 4: pyttsx3 offline
        if pyttsx3:
            try:
                audio_b64 = self._pyttsx3_tts(cleaned_text)
                if audio_b64:
                    return audio_b64, None
            except Exception as e:
                print(f"[VoiceService] pyttsx3 failed ({e})")

        return None, "All TTS engines failed"

    def _gemini_tts(self, text: str) -> Optional[str]:
        models_to_try = ["gemini-3.8-flash-tts", "gemini-2.5-flash-preview-tts"]
        config = {
            'response_modalities': ['AUDIO'],
            'speech_config': {
                'voice_config': {
                    'prebuilt_voice_config': {
                        'voice_name': self.gemini_voice
                    }
                }
            }
        }
        raw_pcm = None
        for model_id in models_to_try:
            try:
                model = genai.GenerativeModel(model_id)
                prompt = f"Read the following text aloud clearly without adding commentary:\n\n{text}"
                res = model.generate_content(prompt, generation_config=config)
                for part in res.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        raw_pcm = part.inline_data.data
                        break
                if raw_pcm:
                    break
            except Exception:
                continue

        if not raw_pcm:
            return None

        wav_buf = io.BytesIO()
        with wave.open(wav_buf, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            wf.writeframes(raw_pcm)

        return base64.b64encode(wav_buf.getvalue()).decode('utf-8')

    async def _edge_tts(self, text: str) -> Optional[str]:
        communicate = edge_tts.Communicate(text, self.edge_voice)
        buf = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                buf.write(chunk["data"])
        audio_bytes = buf.getvalue()
        if not audio_bytes:
            return None
        return base64.b64encode(audio_bytes).decode('utf-8')

    def _gtts(self, text: str) -> Optional[str]:
        buf = io.BytesIO()
        tts = gTTS(text=text, lang='en', tld='co.in', slow=False)
        tts.write_to_fp(buf)
        audio_bytes = buf.getvalue()
        if not audio_bytes:
            return None
        return base64.b64encode(audio_bytes).decode('utf-8')

    def _pyttsx3_tts(self, text: str) -> Optional[str]:
        engine = pyttsx3.init()
        buf_file = "temp_pyttsx3.wav"
        try:
            engine.save_to_file(text, buf_file)
            engine.runAndWait()
            if os.path.exists(buf_file):
                with open(buf_file, "rb") as f:
                    audio_bytes = f.read()
                os.remove(buf_file)
                return base64.b64encode(audio_bytes).decode('utf-8')
        except Exception as e:
            print(f"[VoiceService] pyttsx3 inner error: {e}")
            if os.path.exists(buf_file):
                os.remove(buf_file)
        return None

    def speak(self, text: str) -> Dict[str, Any]:
        """
        Main helper returning complete audio payload + visemes metadata.
        """
        audio_b64, err = self.text_to_speech(text)
        approx_words = len(text.split())
        est_duration = max(1.5, approx_words * 0.4)
        visemes = self.generate_visemes(text, est_duration)

        return {
            "text": text,
            "audio_base64": audio_b64,
            "visemes": visemes,
            "duration": est_duration,
            "error": err
        }
