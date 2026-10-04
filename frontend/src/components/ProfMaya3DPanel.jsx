import React, { useState, useEffect, useRef } from 'react';
import AICharacterTeacher from './AICharacterTeacher';
import ErrorBoundary from './ErrorBoundary';
import { Sparkles, Maximize2, Minimize2, RefreshCw, Monitor, Server } from 'lucide-react';

export default function ProfMaya3DPanel({ 
  promptToExplain = '',
  misconceptionId = '',
  compact = false,
  className = ''
}) {
  const iframeRef = useRef(null);
  const [useIframe, setUseIframe] = useState(true); // Default to real 3D AI character server on port 5050
  const [isExpanded, setIsExpanded] = useState(false);
  const [iframeLoaded, setIframeLoaded] = useState(false);
  const [iframeError, setIframeError] = useState(false);

  const targetUrl = promptToExplain 
    ? `http://127.0.0.1:5050/?explain=${encodeURIComponent(promptToExplain)}`
    : `http://127.0.0.1:5050/`;

  useEffect(() => {
    if (useIframe && promptToExplain && iframeRef.current) {
      try {
        iframeRef.current.contentWindow?.postMessage({
          type: 'EXPLAIN_MISCONCEPTION',
          explanation: promptToExplain,
          spoken_text: promptToExplain,
          prompt: promptToExplain,
          misconception_id: misconceptionId
        }, '*');
      } catch (err) {
        console.warn('ProfMaya3DPanel postMessage notice:', err);
      }
    }
  }, [useIframe, promptToExplain, misconceptionId]);

  return (
    <div className={`bg-white rounded-2xl border border-slate-200/90 shadow-sm flex flex-col overflow-hidden transition-all duration-300 ${
      isExpanded ? 'fixed inset-4 z-50 shadow-2xl ring-1 ring-slate-900/10' : className
    }`}>
      {/* Header Bar */}
      <div className="bg-slate-900 text-white px-4 py-3 flex items-center justify-between flex-shrink-0">
        <div className="flex items-center space-x-2.5">
          <div className="w-7 h-7 rounded-xl bg-indigo-500 flex items-center justify-center text-white shadow-xs">
            <Sparkles className="w-4 h-4 animate-pulse" />
          </div>
          <div>
            <h3 className="text-xs font-bold tracking-tight text-white flex items-center space-x-2">
              <span>Prof. Vikram</span>
              <span className="text-[10px] bg-indigo-500/30 text-indigo-200 border border-indigo-400/30 px-1.5 py-0.5 rounded-md font-mono font-medium">
                3D AI Mentor
              </span>
            </h3>
          </div>
        </div>

        <div className="flex items-center space-x-1.5">
          <button
            type="button"
            onClick={() => setUseIframe(!useIframe)}
            title={useIframe ? "Switch to Native WebGL 3D Avatar" : "Switch to Flask Server 3D Avatar (:5050)"}
            className="flex items-center space-x-1 text-[10px] font-semibold bg-slate-800 hover:bg-slate-700 text-indigo-300 px-2 py-1 rounded-lg border border-slate-700 transition-colors"
          >
            {useIframe ? <Monitor className="w-3 h-3" /> : <Server className="w-3 h-3" />}
            <span className="hidden sm:inline">{useIframe ? '3D Server (:5050)' : 'Native WebGL'}</span>
          </button>

          <button
            type="button"
            onClick={() => setIsExpanded(!isExpanded)}
            title={isExpanded ? "Collapse Panel" : "Expand Panel"}
            className="p-1 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition-colors"
          >
            {isExpanded ? <Minimize2 className="w-3.5 h-3.5" /> : <Maximize2 className="w-3.5 h-3.5" />}
          </button>
        </div>
      </div>

      {/* Main 3D Avatar Render Body */}
      <div className="flex-1 relative min-h-[820px] h-[820px] bg-slate-900">
        {useIframe ? (
          <div className="w-full h-full relative min-h-[820px]">
            {!iframeLoaded && !iframeError && (
              <div className="absolute inset-0 flex flex-col items-center justify-center bg-slate-900 text-slate-300 z-10 space-y-2">
                <Sparkles className="w-6 h-6 text-indigo-400 animate-spin" />
                <span className="text-xs font-medium text-slate-300">Connecting to 3D Server (:5050)...</span>
              </div>
            )}
            {iframeError ? (
              <div className="absolute inset-0 flex flex-col items-center justify-center bg-slate-800 text-white p-6 text-center space-y-3">
                <p className="text-xs font-semibold text-amber-300">Port 5050 Server Offline</p>
                <p className="text-[11px] text-slate-400">Switching back to Native WebGL Avatar...</p>
                <button
                  onClick={() => setUseIframe(false)}
                  className="px-3 py-1.5 text-xs bg-indigo-600 text-white font-medium rounded-lg"
                >
                  Use Native WebGL Avatar
                </button>
              </div>
            ) : (
              <iframe
                ref={iframeRef}
                src={targetUrl}
                title="Prof Vikram 3D AI Physics Mentor"
                className="w-full h-full border-0 absolute inset-0 min-h-[820px]"
                onLoad={() => setIframeLoaded(true)}
                onError={() => setIframeError(true)}
                allow="microphone; autoplay; clipboard-write; encrypted-media; picture-in-picture"
              />
            )}
          </div>
        ) : (
          <ErrorBoundary message="Native 3D Avatar canvas ready.">
            <AICharacterTeacher
              textToSpeak={promptToExplain || "Hello! I am Prof. Vikram, your 3D AI Physics Mentor for Re:Learn. Ask me any physics question or misconception to begin!"}
              misconceptionId={misconceptionId}
              compact={compact}
              title="Prof. Vikram — 3D AI Physics Mentor"
            />
          </ErrorBoundary>
        )}
      </div>
    </div>
  );
}
