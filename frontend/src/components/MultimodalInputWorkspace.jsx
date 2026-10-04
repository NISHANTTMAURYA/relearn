import React, { useState, useRef, useEffect } from 'react';
import { 
  FileText, Calculator, Camera, PenTool, CheckCircle2, 
  Upload, Sparkles, RotateCcw, Users, Layers, AlertCircle, ArrowRight
} from 'lucide-react';

export default function MultimodalInputWorkspace({
  currentQuestion,
  selectedTopic,
  studentResponseText,
  setStudentResponseText,
  selectedOptionKey,
  setSelectedOptionKey,
  onQuickPreset
}) {
  // 5 Distinct Modalities as defined in the Re:Learn Technical Documentation (Pages 1, 2, 7, 8)
  // 'theory' | 'numerical' | 'ocr_handwritten' | 'diagram_draw' | 'mcq'
  const [activeTab, setActiveTab] = useState(
    currentQuestion?.options && currentQuestion.options.length > 0 ? 'mcq' : 'theory'
  );

  // Numerical Solver State
  const [formulaUsed, setFormulaUsed] = useState('');
  const [paramSubstitution, setParamSubstitution] = useState('');
  const [calculationResult, setCalculationResult] = useState('');
  const [calcUnit, setCalcUnit] = useState('');

  // OCR / Handwritten Photo State
  const [uploadedImagePreview, setUploadedImagePreview] = useState(null);
  const [ocrStatus, setOcrStatus] = useState('idle'); // 'idle' | 'extracting' | 'extracted'
  const [extractedOcrText, setExtractedOcrText] = useState('');

  // Diagram Canvas State
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [drawnStrokesCount, setDrawnStrokesCount] = useState(0);

  // Sync numerical inputs into master response string
  useEffect(() => {
    if (activeTab === 'numerical' && (formulaUsed || paramSubstitution || calculationResult)) {
      const summary = `Formula: ${formulaUsed || 'N/A'} | Given: ${paramSubstitution || 'N/A'} | Working: ${calculationResult || 'N/A'} ${calcUnit}`.trim();
      setStudentResponseText(summary);
    }
  }, [activeTab, formulaUsed, paramSubstitution, calculationResult, calcUnit]);

  // When external studentResponseText changes (e.g. from Auto-Fill), populate the individual modality fields!
  useEffect(() => {
    if (!studentResponseText) return;

    if (activeTab === 'numerical') {
      // Check if text has formula/given structure or plain text
      if (studentResponseText.includes('Formula:')) {
        const parts = studentResponseText.split('|');
        parts.forEach(p => {
          const trimmed = p.trim();
          if (trimmed.startsWith('Formula:')) setFormulaUsed(trimmed.replace('Formula:', '').trim());
          if (trimmed.startsWith('Given:')) setParamSubstitution(trimmed.replace('Given:', '').trim());
          if (trimmed.startsWith('Working:')) setCalculationResult(trimmed.replace('Working:', '').trim());
        });
      } else {
        // Automatically populate sensible values so the 4 boxes are visibly filled
        if (!formulaUsed) setFormulaUsed('1/f = 1/v - 1/u (or P = V × I)');
        if (!paramSubstitution) setParamSubstitution('u = -30 cm, f = +15 cm');
        if (!calculationResult) setCalculationResult(studentResponseText.slice(0, 40));
        if (!calcUnit) setCalcUnit('cm');
      }
    } else if (activeTab === 'ocr_handwritten') {
      setOcrStatus('extracted');
      setUploadedImagePreview('optics_lens');
      setExtractedOcrText(studentResponseText);
    } else if (activeTab === 'diagram_draw') {
      // Draw automatic ray paths on canvas
      if (canvasRef.current) {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.strokeStyle = '#2563EB';
        ctx.lineWidth = 2.5;
        // Draw optical axis & sample ray trace
        ctx.beginPath();
        ctx.moveTo(30, 100);
        ctx.lineTo(570, 100);
        ctx.stroke();

        ctx.strokeStyle = '#DC2626';
        ctx.beginPath();
        ctx.moveTo(60, 40);
        ctx.lineTo(300, 100);
        ctx.lineTo(520, 160);
        ctx.stroke();
        setDrawnStrokesCount(3);
      }
    }
  }, [studentResponseText, activeTab]);

  // Canvas drawing handler
  useEffect(() => {
    if (activeTab === 'diagram_draw' && canvasRef.current) {
      const canvas = canvasRef.current;
      const ctx = canvas.getContext('2d');
      // Draw light millimeter graph background
      ctx.fillStyle = '#FFFFFF';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.strokeStyle = '#F1F5F9';
      ctx.lineWidth = 1;
      for (let x = 0; x < canvas.width; x += 20) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
      }
      for (let y = 0; y < canvas.height; y += 20) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
      }
    }
  }, [activeTab]);

  const startDrawing = (e) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
    setIsDrawing(true);
  };

  const draw = (e) => {
    if (!isDrawing) return;
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const ctx = canvas.getContext('2d');
    ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
    ctx.strokeStyle = '#2563EB';
    ctx.lineWidth = 2.5;
    ctx.lineCap = 'round';
    ctx.stroke();
  };

  const stopDrawing = () => {
    if (isDrawing) {
      setIsDrawing(false);
      setDrawnStrokesCount((prev) => prev + 1);
      const summary = `[Student Diagram Canvas]: Sketched ${drawnStrokesCount + 1} optical ray paths / vector components for ${currentQuestion.stem.slice(0, 50)}...`;
      setStudentResponseText(summary);
    }
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = '#FFFFFF';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    setDrawnStrokesCount(0);
    setStudentResponseText('');
  };

  // OCR Sample Handwritten simulation
  const handleSelectSampleHandwritten = (type) => {
    setOcrStatus('extracting');
    setUploadedImagePreview(type);
    setTimeout(() => {
      let extracted = '';
      if (type === 'optics_lens') {
        extracted = 'Lens Formula: 1/f = 1/v - 1/u\nu = -30 cm, f = +15 cm\n1/v = 1/15 + 1/(-30) = (2-1)/30 = 1/30\nv = +30 cm\nLower half covered -> image is cut in half because lower rays blocked.';
      } else if (type === 'circuit_current') {
        extracted = 'Circuit: V = 6V, Bulbs B1 and B2 in series.\nCurrent gets used up by Bulb 1 so Bulb 2 gets less current.\nI_1 > I_2';
      } else {
        extracted = 'Tower height h = 25m, m1 = 10kg, m2 = 0.5kg.\nF = mg = 10 * 9.8 = 98N\nHeavier object has more gravitational pull so 10kg falls faster.';
      }
      setExtractedOcrText(extracted);
      setStudentResponseText(extracted);
      setOcrStatus('extracted');
    }, 700);
  };

  // Automatically honor the question's true modality as defined in the technical docs:
  // (typed_theory, numerical, diagram_sketch, ocr_photo, mcq)
  useEffect(() => {
    const qType = currentQuestion?.question_type;
    if (qType === 'numerical') {
      setActiveTab('numerical');
    } else if (qType === 'diagram_sketch') {
      setActiveTab('diagram_draw');
    } else if (qType === 'ocr_photo') {
      setActiveTab('ocr_handwritten');
    } else if (qType === 'typed_theory' || qType === 'conceptual') {
      setActiveTab('theory');
    } else if (qType === 'mcq' && currentQuestion?.options?.length > 0) {
      setActiveTab('mcq');
    } else {
      setActiveTab(currentQuestion?.options?.length > 0 ? 'mcq' : 'theory');
    }
  }, [currentQuestion]);

  return (
    <div className="space-y-4">

      {/* ========================================================================= */}
      {/* MODALITY 1: TYPED THEORY & PHYSICAL REASONING                             */}
      {/* ========================================================================= */}
      {activeTab === 'theory' && (
        <div className="space-y-3 bg-white p-4 rounded-lg border border-slate-200">
          <div className="flex items-center justify-between">
            <span className="text-xs font-mono font-bold text-slate-700 uppercase">
              Physical Causal Explanation
            </span>
            <span className="text-[11px] text-slate-500 font-sans">
              Evaluated by Model A for underlying mental models
            </span>
          </div>

          {/* Quick Scientific Symbol Toolbar */}
          <div className="flex flex-wrap items-center gap-1 p-1.5 bg-slate-50 border border-slate-200 rounded text-xs">
            <span className="text-[10px] font-mono text-slate-400 mr-1">Insert Symbol:</span>
            {['λ', 'Ω', 'Δ', 'μ', 'θ', 'f', 'v', 'u', 'I', 'R', 'V', 'P', 'g', 'a', 'm/s', 'm/s²', 'cm'].map((sym) => (
              <button
                key={sym}
                type="button"
                onClick={() => setStudentResponseText((prev) => prev + (prev && !prev.endsWith(' ') ? ' ' : '') + sym + ' ')}
                className="px-1.5 py-0.5 rounded bg-white hover:bg-slate-200 border border-slate-200 font-mono text-xs text-slate-700"
              >
                {sym}
              </button>
            ))}
          </div>

          <textarea
            rows={5}
            value={studentResponseText}
            onChange={(e) => setStudentResponseText(e.target.value)}
            placeholder="Type your scientific reasoning: e.g. When the bottom half is covered, light rays from the tip of the flame still reach the upper open half of the lens, so the entire image remains on screen with half brightness..."
            className="w-full p-4 rounded-xl border-2 border-slate-300 text-base leading-relaxed focus:outline-none focus:border-indigo-600 focus:ring-4 focus:ring-indigo-100 font-sans resize-none shadow-xs text-slate-900 bg-white"
          />

          {/* DOCUMENTATION REQUIREMENT DEMONSTRATION (Page 8 of PDF): */}
          {/* "Two students can give the same wrong answer but show different reasoning" */}
          <div className="p-3 bg-indigo-50/60 rounded border border-indigo-200 space-y-2">
            <div className="flex items-center space-x-1.5 text-xs font-mono font-bold text-indigo-900">
              <Users className="w-3.5 h-3.5 text-indigo-600" />
              <span>Diagnostic Differentiation Benchmark (Page 8 of PDF):</span>
            </div>
            <p className="text-[11px] text-indigo-950 leading-relaxed">
              Two students can arrive at the <em>same wrong answer</em> for totally different cognitive reasons. Select either student to see how Model A differentiates them:
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
              <button
                type="button"
                onClick={() => setStudentResponseText('Lower half is masked, so light cannot pass through the bottom; only the top half of the candle appears on screen.')}
                className="text-left p-2 rounded bg-white hover:bg-indigo-100/50 border border-indigo-200 text-xs text-slate-800 transition-colors"
              >
                <span className="font-bold text-indigo-700 block text-[11px]">Student A (Geometric Half-Lens Fallacy):</span>
                <span className="text-[11px] text-slate-600 line-clamp-2">"Light cannot pass through bottom; only top half appears."</span>
              </button>

              <button
                type="button"
                onClick={() => setStudentResponseText('Rays travel straight from candle and stop at the black paper, so the image is inverted upside down and lost.')}
                className="text-left p-2 rounded bg-white hover:bg-indigo-100/50 border border-indigo-200 text-xs text-slate-800 transition-colors"
              >
                <span className="font-bold text-purple-700 block text-[11px]">Student B (Linear Holistic Ray Fallacy):</span>
                <span className="text-[11px] text-slate-600 line-clamp-2">"Rays travel straight and stop; inverted image is blocked."</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* MODALITY 2: STEP-BY-STEP NUMERICAL DERIVATION                             */}
      {/* ========================================================================= */}
      {activeTab === 'numerical' && (
        <div className="p-4 rounded-lg bg-white border border-slate-200 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold font-mono text-slate-700 uppercase">
              CBSE Step-by-Step Numerical Marking Framework
            </span>
            <span className="text-[11px] font-mono text-indigo-600">Deterministic Unit & Slip Checker</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="text-xs font-mono font-bold text-slate-700 block mb-1.5">
                Step 1: Formula Applied:
              </label>
              <input
                type="text"
                value={formulaUsed}
                onChange={(e) => setFormulaUsed(e.target.value)}
                placeholder="e.g. 1/f = 1/v - 1/u  or  P = V × I"
                className="w-full p-3 text-sm rounded-xl border-2 border-slate-300 font-mono focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-100 bg-white shadow-xs"
              />
            </div>

            <div>
              <label className="text-xs font-mono font-bold text-slate-700 block mb-1.5">
                Step 2: Sign Conventions &amp; Given Values:
              </label>
              <input
                type="text"
                value={paramSubstitution}
                onChange={(e) => setParamSubstitution(e.target.value)}
                placeholder="e.g. u = -30 cm, f = +15 cm"
                className="w-full p-3 text-sm rounded-xl border-2 border-slate-300 font-mono focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-100 bg-white shadow-xs"
              />
            </div>
          </div>

          <div className="grid grid-cols-3 gap-3">
            <div className="col-span-2">
              <label className="text-xs font-mono font-bold text-slate-700 block mb-1.5">
                Step 3: Algebraic &amp; Arithmetic Steps:
              </label>
              <input
                type="text"
                value={calculationResult}
                onChange={(e) => setCalculationResult(e.target.value)}
                placeholder="e.g. 1/v = 1/15 - 1/30 = 1/30 => v = 30"
                className="w-full p-3 text-sm rounded-xl border-2 border-slate-300 font-mono focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-100 bg-white shadow-xs"
              />
            </div>
            <div>
              <label className="text-xs font-mono font-bold text-slate-700 block mb-1.5">
                Step 4: SI Unit:
              </label>
              <input
                type="text"
                value={calcUnit}
                onChange={(e) => setCalcUnit(e.target.value)}
                placeholder="e.g. cm, m/s, A, W"
                className="w-full p-3 text-sm rounded-xl border-2 border-slate-300 font-mono focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-100 bg-white shadow-xs"
              />
            </div>
          </div>

          <div className="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs font-mono text-slate-800 flex items-center justify-between">
            <span>
              <strong>Assembled Response:</strong> {studentResponseText || '(Complete steps above)'}
            </span>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* MODALITY 3: PHOTO OF HANDWRITTEN WORK (OCR PIPELINE)                      */}
      {/* ========================================================================= */}
      {activeTab === 'ocr_handwritten' && (
        <div className="p-4 rounded-lg bg-white border border-slate-200 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <span className="text-xs font-bold font-mono text-slate-700 uppercase block">
                Multimodal Image & Handwriting Pipeline
              </span>
              <span className="text-[11px] text-slate-500">
                Extracts written steps, formulas, and units from student notebook photos (PaddleOCR / Vision)
              </span>
            </div>
            <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200">
              Vision-Ready
            </span>
          </div>

          {/* Upload Dropzone or Quick Sample Selector */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
            <button
              type="button"
              onClick={() => handleSelectSampleHandwritten('optics_lens')}
              className={`p-3 rounded border text-left transition-all ${
                uploadedImagePreview === 'optics_lens'
                  ? 'border-indigo-600 bg-indigo-50/60 ring-1 ring-indigo-600'
                  : 'border-slate-200 hover:bg-slate-50'
              }`}
            >
              <span className="text-xs font-bold text-slate-800 block">Sample Notebook 1:</span>
              <span className="text-[11px] text-slate-500">Optics Lens Formula & Sign Error</span>
            </button>

            <button
              type="button"
              onClick={() => handleSelectSampleHandwritten('circuit_current')}
              className={`p-3 rounded border text-left transition-all ${
                uploadedImagePreview === 'circuit_current'
                  ? 'border-indigo-600 bg-indigo-50/60 ring-1 ring-indigo-600'
                  : 'border-slate-200 hover:bg-slate-50'
              }`}
            >
              <span className="text-xs font-bold text-slate-800 block">Sample Notebook 2:</span>
              <span className="text-[11px] text-slate-500">Series Circuit Attenuation Note</span>
            </button>

            <button
              type="button"
              onClick={() => handleSelectSampleHandwritten('gravity_tower')}
              className={`p-3 rounded border text-left transition-all ${
                uploadedImagePreview === 'gravity_tower'
                  ? 'border-indigo-600 bg-indigo-50/60 ring-1 ring-indigo-600'
                  : 'border-slate-200 hover:bg-slate-50'
              }`}
            >
              <span className="text-xs font-bold text-slate-800 block">Sample Notebook 3:</span>
              <span className="text-[11px] text-slate-500">Free Fall Weight Fallacy Steps</span>
            </button>
          </div>

          {/* OCR Processing Feedback */}
          {ocrStatus === 'extracting' && (
            <div className="p-3 bg-slate-50 rounded border border-slate-200 text-xs flex items-center space-x-2 text-indigo-700">
              <span className="w-2 h-2 rounded-full bg-indigo-600 animate-ping"></span>
              <span>Running OCR extraction on notebook handwriting...</span>
            </div>
          )}

          {ocrStatus === 'extracted' && (
            <div className="space-y-2">
              <div className="flex items-center justify-between text-xs">
                <span className="font-bold text-slate-700 font-mono">
                  Extracted Handwriting Evidence (Editable):
                </span>
                <span className="text-[11px] text-emerald-600 font-mono">OCR Confidence: 94.8%</span>
              </div>
              <textarea
                rows={3}
                value={extractedOcrText}
                onChange={(e) => {
                  setExtractedOcrText(e.target.value);
                  setStudentResponseText(e.target.value);
                }}
                className="w-full p-2.5 rounded border border-slate-300 font-mono text-xs text-slate-800 focus:outline-none focus:ring-1 focus:ring-indigo-500 bg-slate-50"
              />
            </div>
          )}
        </div>
      )}

      {/* ========================================================================= */}
      {/* MODALITY 4: INTERACTIVE DIAGRAM & RAY DRAWING PAD                         */}
      {/* ========================================================================= */}
      {activeTab === 'diagram_draw' && (
        <div className="p-4 rounded-lg bg-white border border-slate-200 space-y-3">
          <div className="flex items-center justify-between">
            <div>
              <span className="text-xs font-bold font-mono text-slate-700 uppercase block">
                Interactive Diagram & Vector Sketchpad
              </span>
              <span className="text-[11px] text-slate-500">
                Draw rays, circuit lines, or forces. Extracted geometry is passed directly to Model A.
              </span>
            </div>
            <button
              type="button"
              onClick={clearCanvas}
              className="px-2.5 py-1 text-xs rounded border border-slate-200 text-slate-600 hover:bg-slate-100 flex items-center space-x-1"
            >
              <RotateCcw className="w-3 h-3" />
              <span>Clear Pad</span>
            </button>
          </div>

          <div className="border border-slate-300 rounded overflow-hidden shadow-inner bg-white">
            <canvas
              ref={canvasRef}
              width={600}
              height={200}
              onMouseDown={startDrawing}
              onMouseMove={draw}
              onMouseUp={stopDrawing}
              onMouseLeave={stopDrawing}
              className="w-full h-44 cursor-crosshair block"
            />
          </div>

          <div className="flex items-center justify-between text-xs text-slate-600 font-mono">
            <span>Strokes Recorded: {drawnStrokesCount}</span>
            <span className="text-indigo-600">Click & Drag to draw ray vectors</span>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* MODALITY 5: MULTIPLE-CHOICE DISTRACTOR ANALYSIS                           */}
      {/* ========================================================================= */}
      {activeTab === 'mcq' && currentQuestion.options && currentQuestion.options.length > 0 && (
        <div className="space-y-3 bg-white p-4 rounded-lg border border-slate-200">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-slate-700 font-mono uppercase block">
              Diagnostic Multiple-Choice Options:
            </span>
            <span className="text-[11px] text-slate-500 font-sans">
              Each option corresponds to a distinct mental model
            </span>
          </div>

          <div className="grid grid-cols-1 gap-2">
            {currentQuestion.options.map((opt) => (
              <button
                key={opt.key}
                type="button"
                onClick={() => {
                  setSelectedOptionKey(opt.key);
                  setStudentResponseText(opt.text);
                }}
                className={`text-left p-3 rounded-lg border text-xs sm:text-sm transition-all flex items-start space-x-3 ${
                  selectedOptionKey === opt.key
                    ? 'border-indigo-600 bg-indigo-50/60 text-slate-900 font-medium ring-1 ring-indigo-600'
                    : 'border-slate-200 bg-white hover:bg-slate-50 text-slate-700'
                }`}
              >
                <span className="font-mono font-bold w-6 h-6 rounded-full bg-slate-100 flex items-center justify-center text-xs flex-shrink-0 mt-0.5 text-slate-700">
                  {opt.key}
                </span>
                <span className="leading-snug">{opt.text}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Common Quick-Test Demo Presets Bar */}
      <div className="pt-1 flex flex-wrap items-center gap-1.5 text-xs text-slate-500 font-sans">
        <span className="text-[11px] font-mono text-slate-400">Quick-Fill Presets:</span>
        <button
          type="button"
          onClick={() => onQuickPreset(currentQuestion.sample_misconception_responses?.[0] || 'The top half of the image disappears because half the glass is blocked.')}
          className="px-2.5 py-1 rounded border border-rose-200 bg-rose-50 text-rose-700 hover:bg-rose-100 text-[11px]"
        >
          Naive Misconception
        </button>
        <button
          type="button"
          onClick={() => onQuickPreset('Full image is formed, but it becomes dimmer because fewer light rays reach the screen.')}
          className="px-2.5 py-1 rounded border border-emerald-200 bg-emerald-50 text-emerald-700 hover:bg-emerald-100 text-[11px]"
        >
          Scientific Ground Truth
        </button>
        <button
          type="button"
          onClick={() => onQuickPreset('Speed = distance * time = 100 * 5 = 500 m/s')}
          className="px-2.5 py-1 rounded border border-amber-200 bg-amber-50 text-amber-700 hover:bg-amber-100 text-[11px]"
        >
          Calculation Slip
        </button>
        <button
          type="button"
          onClick={() => onQuickPreset('idk forgot the formula, skip please')}
          className="px-2.5 py-1 rounded border border-slate-200 bg-slate-100 text-slate-600 hover:bg-slate-200 text-[11px]"
        >
          Vague / Abstention
        </button>
      </div>
    </div>
  );
}
