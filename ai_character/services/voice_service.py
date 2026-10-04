import os
import io
import wave
import base64
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class VoiceService:
    def __init__(self, google_api_key: str = None, tts_model: str = None, edge_voice: str = None, gemini_voice: str = None):
        self.google_api_key = google_api_key or os.getenv("GOOGLE_API_KEY")
        self.tts_model_name = tts_model or os.getenv("GEMINI_TTS_MODEL", "gemini-3.8-flash-tts")
        self.gemini_voice = gemini_voice or os.getenv("GEMINI_TTS_VOICE", "Fenrir")
        self.edge_voice = edge_voice or os.getenv("EDGE_TTS_VOICE", "en-IN-PrabhatNeural")
        self.eleven_api_key = os.getenv("ELEVEN_LABS_API_KEY")

        if self.google_api_key:
            try:
                genai.configure(api_key=self.google_api_key)
            except Exception as e:
                print(f"[VoiceService] Error configuring genai: {e}")

    def text_to_speech(self, text: str) -> tuple:
        """
        Converts text to speech using a robust 4-tier fallback architecture:
        Tier 1 (Primary): Google Gemini AI Text-To-Speech (gemini-3.8-flash-tts / gemini-2.5-flash-preview-tts)
        Tier 2 (Fallback): Microsoft Azure edge-tts (free neural voice, high fidelity)
        Tier 3 (Fallback): Google Translate TTS (gTTS, zero configuration fallback)
        Tier 4 (Fallback): ElevenLabs (if key and credits available)

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

        # ── Tier 1: Gemini AI Text-to-Speech ──────────────────────────────────
        if self.google_api_key:
            try:
                audio_b64 = self._gemini_tts(cleaned_text)
                if audio_b64:
                    return audio_b64, None
            except Exception as e:
                print(f"[VoiceService] Gemini TTS failed ({e}), switching to edge-tts fallback...")

        # ── Tier 2: Microsoft edge-tts (Free, Unlimited, Neural Voice) ─────────
        try:
            audio_b64 = asyncio.run(self._edge_tts(cleaned_text))
            if audio_b64:
                return audio_b64, None
        except Exception as e:
            print(f"[VoiceService] edge-tts fallback failed ({e}), switching to gTTS...")

        # ── Tier 3: gTTS (Google Translate TTS) ───────────────────────────────
        try:
            audio_b64 = self._gtts(cleaned_text)
            if audio_b64:
                return audio_b64, None
        except Exception as e:
            print(f"[VoiceService] gTTS fallback failed ({e})")

        # ── Tier 4: ElevenLabs (Optional) ─────────────────────────────────────
        if self.eleven_api_key:
            try:
                from elevenlabs import ElevenLabs
                eleven = ElevenLabs(api_key=self.eleven_api_key)
                audio_stream = eleven.text_to_speech.convert(
                    voice_id="pNInz6obpgDQGcFmaJgB",
                    text=cleaned_text,
                    model_id="eleven_multilingual_v2",
                    output_format="mp3_44100_128"
                )
                audio_bytes = b''.join(audio_stream)
                if audio_bytes:
                    return base64.b64encode(audio_bytes).decode('utf-8'), None
            except Exception as e:
                print(f"[VoiceService] ElevenLabs failed: {e}")

        return None, "All TTS providers failed"

    def _gemini_tts(self, text: str) -> str:
        """Uses Gemini AI TTS models with male voice (Fenrir) and packages raw 24kHz PCM into valid WAV."""
        genai.configure(api_key=self.google_api_key)

        models_to_try = [self.tts_model_name, "gemini-2.5-flash-preview-tts"]
        raw_pcm_data = None
        last_err = None

        # Explicitly configure male voice (Fenrir)
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

        for model_id in models_to_try:
            try:
                model = genai.GenerativeModel(model_id)
                prompt = f"Read the following text aloud verbatim without adding any commentary or extra words:\n\n{text}"
                response = model.generate_content(prompt, generation_config=config)

                for part in response.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        raw_pcm_data = part.inline_data.data
                        break
                if raw_pcm_data:
                    break
            except Exception as err:
                last_err = err
                continue

        if not raw_pcm_data:
            raise Exception(f"Gemini TTS produced no audio data: {last_err}")

        # Wrap raw PCM (16-bit linear mono 24000Hz) in standard WAV container
        wav_buf = io.BytesIO()
        with wave.open(wav_buf, 'wb') as wf:
            wf.setnchannels(1)      # Mono
            wf.setsampwidth(2)      # 16-bit PCM = 2 bytes per sample
            wf.setframerate(24000)  # 24kHz
            wf.writeframes(raw_pcm_data)

        wav_bytes = wav_buf.getvalue()
        return base64.b64encode(wav_bytes).decode('utf-8')

    def _is_hindi(self, text: str) -> bool:
        """Detects if text contains Devanagari script for Hindi voice selection."""
        import re
        return bool(re.search(r'[\u0900-\u097F]', text))

    async def _edge_tts(self, text: str) -> str:
        import edge_tts
        # If Hindi text, use Microsoft's natural Hindi neural voice
        voice = "hi-IN-MadhurNeural" if self._is_hindi(text) else self.edge_voice
        communicate = edge_tts.Communicate(text, voice)
        buf = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                buf.write(chunk["data"])
        buf.seek(0)
        audio_bytes = buf.read()
        if not audio_bytes:
            raise Exception("edge-tts returned empty audio buffer")
        return base64.b64encode(audio_bytes).decode('utf-8')

    def _gtts(self, text: str) -> str:
        from gtts import gTTS
        buf = io.BytesIO()
        lang = 'hi' if self._is_hindi(text) else 'en'
        tld = 'co.in'
        tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
        tts.write_to_fp(buf)
        buf.seek(0)
        audio_bytes = buf.read()
        return base64.b64encode(audio_bytes).decode('utf-8')
