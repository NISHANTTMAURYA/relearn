import React, { useState, useEffect, useRef } from 'react';
import { Volume2, VolumeX, RotateCcw, Sparkles } from 'lucide-react';

export default function TeacherAvatar({ textToSpeak = '', teacherName = 'Prof. Vikram (3D AI Physics Mentor)' }) {
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isMuted, setIsMuted] = useState(false);
  const [mouthOpen, setMouthOpen] = useState(0);
  const [eyeBlink, setEyeBlink] = useState(false);
  const animFrameRef = useRef(null);

  // Blinking timer
  useEffect(() => {
    const blinkInterval = setInterval(() => {
      setEyeBlink(true);
      setTimeout(() => setEyeBlink(false), 150);
    }, 4000);
    return () => clearInterval(blinkInterval);
  }, []);

  // Web Speech API Integration
  useEffect(() => {
    if (!textToSpeak || isMuted || typeof window === 'undefined' || !('speechSynthesis' in window)) {
      return;
    }

    window.speechSynthesis.cancel();
    const cleanText = textToSpeak.replace(/\[.*?\]/g, '').replace(/https?:\/\/\S+/g, '');
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.rate = 1.0;
    utterance.pitch = 1.05;

    // Pick English female/natural voice if available
    const voices = window.speechSynthesis.getVoices();
    const preferredVoice = voices.find(v => v.lang.includes('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Zira')));
    if (preferredVoice) {
      utterance.voice = preferredVoice;
    }

    utterance.onstart = () => setIsSpeaking(true);
    utterance.onend = () => {
      setIsSpeaking(false);
      setMouthOpen(0);
    };
    utterance.onerror = () => {
      setIsSpeaking(false);
      setMouthOpen(0);
    };

    window.speechSynthesis.speak(utterance);

    return () => {
      window.speechSynthesis.cancel();
    };
  }, [textToSpeak, isMuted]);

  // Mouth animation during speech
  useEffect(() => {
    let interval;
    if (isSpeaking) {
      interval = setInterval(() => {
        setMouthOpen(Math.random() * 8 + 2);
      }, 120);
    } else {
      setMouthOpen(0);
    }
    return () => clearInterval(interval);
  }, [isSpeaking]);

  const handleToggleMute = () => {
    if (isSpeaking) {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
    }
    setIsMuted(!isMuted);
  };

  const handleReplay = () => {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window && textToSpeak) {
      window.speechSynthesis.cancel();
      setIsMuted(false);
      const cleanText = textToSpeak.replace(/\[.*?\]/g, '').replace(/https?:\/\/\S+/g, '');
      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.rate = 1.0;
      utterance.pitch = 1.05;
      utterance.onstart = () => setIsSpeaking(true);
      utterance.onend = () => setIsSpeaking(false);
      window.speechSynthesis.speak(utterance);
    }
  };

  return (
    <div className="editorial-card p-4 bg-white border border-border flex flex-col sm:flex-row items-center gap-4">
      {/* 3D / Vector Avatar Canvas */}
      <div className="relative w-24 h-24 sm:w-28 sm:h-28 rounded-full bg-slate-50 border-2 border-indigo-100 flex-shrink-0 flex items-center justify-center overflow-hidden shadow-inner">
        <svg viewBox="0 0 120 120" className="w-full h-full">
          {/* Background aura */}
          <circle cx="60" cy="60" r="58" fill="#F8FAFC" />
          
          {/* Hair back */}
          <path d="M30 45 C20 60, 20 95, 35 110 L85 110 C100 95, 100 60, 90 45 Z" fill="#334155" />
          
          {/* Shoulders & Lab Coat */}
          <path d="M22 120 C25 98, 42 90, 60 90 C78 90, 95 98, 98 120 Z" fill="#FFFFFF" stroke="#CBD5E1" strokeWidth="2" />
          <path d="M50 90 L60 108 L70 90 Z" fill="#4F46E5" />
          <path d="M54 90 L60 120 L66 90 Z" fill="#E2E8F0" />

          {/* Neck */}
          <rect x="52" y="75" width="16" height="18" fill="#FBCFE8" rx="4" />

          {/* Head */}
          <ellipse cx="60" cy="55" rx="26" ry="30" fill="#FDE047" opacity="0.1" />
          <ellipse cx="60" cy="55" rx="24" ry="28" fill="#FED7AA" />

          {/* Hair front */}
          <path d="M36 45 C40 30, 80 30, 84 45 C80 35, 40 35, 36 45 Z" fill="#1E293B" />
          <path d="M36 45 C35 55, 38 65, 40 70 C38 60, 37 50, 38 45 Z" fill="#1E293B" />
          <path d="M84 45 C85 55, 82 65, 80 70 C82 60, 83 50, 82 45 Z" fill="#1E293B" />

          {/* Glasses */}
          <rect x="42" y="47" width="14" height="10" rx="3" fill="none" stroke="#475569" strokeWidth="1.5" />
          <rect x="64" y="47" width="14" height="10" rx="3" fill="none" stroke="#475569" strokeWidth="1.5" />
          <line x1="56" y1="52" x2="64" y2="52" stroke="#475569" strokeWidth="1.5" />

          {/* Eyes (Blinking support) */}
          {eyeBlink ? (
            <>
              <line x1="45" y1="52" x2="53" y2="52" stroke="#0F172A" strokeWidth="2" strokeLinecap="round" />
              <line x1="67" y1="52" x2="75" y2="52" stroke="#0F172A" strokeWidth="2" strokeLinecap="round" />
            </>
          ) : (
            <>
              <circle cx="49" cy="52" r="3" fill="#0F172A" />
              <circle cx="50" cy="51" r="1" fill="#FFFFFF" />
              <circle cx="71" cy="52" r="3" fill="#0F172A" />
              <circle cx="72" cy="51" r="1" fill="#FFFFFF" />
            </>
          )}

          {/* Nose */}
          <path d="M59 56 L58 63 L62 63" fill="none" stroke="#F97316" strokeWidth="1.2" strokeLinecap="round" />

          {/* Mouth (Speech animated) */}
          <ellipse
            cx="60"
            cy="71"
            rx={isSpeaking ? 5 : 4}
            ry={mouthOpen}
            fill="#BE123C"
            stroke="#9F1239"
            strokeWidth="0.8"
          />
        </svg>

        {/* Live Audio Waves Badge */}
        {isSpeaking && (
          <div className="absolute bottom-1 right-1 flex items-center space-x-0.5 bg-indigo-600 px-1.5 py-0.5 rounded-full shadow">
            <span className="w-1 h-2 bg-white rounded-full animate-pulse"></span>
            <span className="w-1 h-3 bg-white rounded-full animate-pulse delay-75"></span>
            <span className="w-1 h-2 bg-white rounded-full animate-pulse delay-150"></span>
          </div>
        )}
      </div>

      {/* Teacher speech caption & controls */}
      <div className="flex-1 text-center sm:text-left">
        <div className="flex items-center justify-center sm:justify-between gap-2">
          <div className="flex items-center space-x-1.5">
            <span className="text-xs font-semibold text-charcoal">{teacherName}</span>
            <span className="inline-flex items-center px-1.5 py-0.2 rounded-full text-[10px] font-mono bg-indigo-50 text-indigo-700 border border-indigo-200">
              <Sparkles className="w-2.5 h-2.5 mr-0.5 text-indigo-500" />
              Interactive Voice
            </span>
          </div>

          <div className="flex items-center space-x-1">
            <button
              onClick={handleToggleMute}
              className={`p-1.5 rounded text-xs transition-colors ${
                isMuted ? 'text-rose-600 bg-rose-50 hover:bg-rose-100' : 'text-slate-600 hover:bg-slate-100'
              }`}
              title={isMuted ? 'Unmute Teacher' : 'Mute Teacher'}
            >
              {isMuted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
            </button>
            <button
              onClick={handleReplay}
              className="p-1.5 rounded text-xs text-slate-600 hover:bg-slate-100 transition-colors"
              title="Replay Voice Explanation"
            >
              <RotateCcw className="w-4 h-4" />
            </button>
          </div>
        </div>

        <p className="text-xs text-slate-700 mt-1.5 leading-relaxed bg-slate-50 p-2.5 rounded border border-slate-100 font-sans">
          "{textToSpeak}"
        </p>
      </div>
    </div>
  );
}
