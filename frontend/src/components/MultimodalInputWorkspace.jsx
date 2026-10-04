import React, { useState, useEffect } from 'react';
import { 
  FileText, Calculator, CheckCircle2, 
  Sparkles, Users, Layers, AlertCircle, ArrowRight
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
  // 3 Rock-Solid Diagnostic Modalities: 'mcq' | 'theory' | 'numerical'
  const [activeTab, setActiveTab] = useState(
    currentQuestion?.options && currentQuestion.options.length > 0 ? 'mcq' : 'theory'
  );

  // Step-by-Step Numerical Marking State
  const [formulaUsed, setFormulaUsed] = useState('');
  const [paramSubstitution, setParamSubstitution] = useState('');
  const [calculationResult, setCalculationResult] = useState('');
  const [calcUnit, setCalcUnit] = useState('');

  // Helper to directly update numerical inputs and synthesize the combined answer
  const updateNumerical = (newFormula, newGiven, newWorking, newUnit) => {
    setFormulaUsed(newFormula);
    setParamSubstitution(newGiven);
    setCalculationResult(newWorking);
    setCalcUnit(newUnit);
    
    const parts = [];
    if (newFormula) parts.push(`Formula: ${newFormula}`);
    if (newGiven) parts.push(`Given: ${newGiven}`);
    if (newWorking) parts.push(`Working: ${newWorking}`);
    if (newUnit) parts.push(`Unit: ${newUnit}`);
    setStudentResponseText(parts.join(' | '));
  };

  // When external studentResponseText changes (e.g. via Auto-Fill or Question Navigation),
  // parse the structured fields without circular re-rendering
  useEffect(() => {
    if (!studentResponseText) {
      if (activeTab === 'numerical') {
        setFormulaUsed('');
        setParamSubstitution('');
        setCalculationResult('');
        setCalcUnit('');
      }
      return;
    }

    if (activeTab === 'numerical') {
      if (studentResponseText.includes('Formula:') || studentResponseText.includes('Given:') || studentResponseText.includes('Working:')) {
        const parts = studentResponseText.split('|');
        let f = '', g = '', w = '', u = '';
        parts.forEach(p => {
          const trimmed = p.trim();
          if (trimmed.startsWith('Formula:')) f = trimmed.replace('Formula:', '').trim();
          else if (trimmed.startsWith('Given:')) g = trimmed.replace('Given:', '').trim();
          else if (trimmed.startsWith('Working:')) w = trimmed.replace('Working:', '').trim();
          else if (trimmed.startsWith('Unit:')) u = trimmed.replace('Unit:', '').trim();
        });
        setFormulaUsed(f);
        setParamSubstitution(g);
        setCalculationResult(w);
        setCalcUnit(u || 'cm');
      } else {
        setCalculationResult(studentResponseText);
        setFormulaUsed('1/f = 1/v - 1/u');
        setParamSubstitution('u = -30 cm, f = +15 cm');
        setCalcUnit('cm');
      }
    }
  }, [studentResponseText, activeTab, currentQuestion?.question_id]);

  // Honor the question's modality from curriculum
  useEffect(() => {
    const qType = currentQuestion?.question_type;
    if (qType === 'numerical') {
      setActiveTab('numerical');
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

          {/* Diagnostic Differentiation Benchmark */}
          <div className="p-3 bg-indigo-50/60 rounded border border-indigo-200 space-y-2">
            <div className="flex items-center space-x-1.5 text-xs font-mono font-bold text-indigo-900">
              <Users className="w-3.5 h-3.5 text-indigo-600" />
              <span>Diagnostic Differentiation Benchmark (Page 8 of NCERT Research):</span>
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
                onChange={(e) => updateNumerical(e.target.value, paramSubstitution, calculationResult, calcUnit)}
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
                onChange={(e) => updateNumerical(formulaUsed, e.target.value, calculationResult, calcUnit)}
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
                onChange={(e) => updateNumerical(formulaUsed, paramSubstitution, e.target.value, calcUnit)}
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
                onChange={(e) => updateNumerical(formulaUsed, paramSubstitution, calculationResult, e.target.value)}
                placeholder="e.g. cm, m/s, A, W"
                className="w-full p-3 text-sm rounded-xl border-2 border-slate-300 font-mono focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-100 bg-white shadow-xs"
              />
            </div>
          </div>

          <div className="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs font-mono text-slate-800 flex items-center justify-between">
            <span>
              <strong>Assembled Derivation:</strong> {studentResponseText || '(Complete steps above)'}
            </span>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* MODALITY 3: MULTIPLE-CHOICE DISTRACTOR ANALYSIS                           */}
      {/* ========================================================================= */}
      {activeTab === 'mcq' && currentQuestion.options && currentQuestion.options.length > 0 && (
        <div className="space-y-3 bg-white p-4 rounded-lg border border-slate-200">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-slate-700 font-mono uppercase block">
              Diagnostic Multiple-Choice Options:
            </span>
            <span className="text-[11px] text-slate-500 font-sans">
              Each distractor corresponds to an engineered mental model
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
          onClick={() => onQuickPreset('Formula: 1/f = 1/v + 1/u | Given: u = -30 cm, f = +15 cm | Working: 1/v = 1/15 - 1/30 = 1/30 => v = 30 | Unit: cm')}
          className="px-2.5 py-1 rounded border border-amber-200 bg-amber-50 text-amber-700 hover:bg-amber-100 text-[11px]"
        >
          Calculation Slip
        </button>
        <button
          type="button"
          onClick={() => onQuickPreset('Formula: 1/f = 1/v - 1/u | Given: u = -30 cm, f = +15 cm | Working: 1/v = 1/15 + 1/(-30) = 1/30 => v = +30 | Unit: cm')}
          className="px-2.5 py-1 rounded border border-slate-200 bg-slate-100 text-slate-600 hover:bg-slate-200 text-[11px]"
        >
          Step-by-Step Numerical
        </button>
      </div>
    </div>
  );
}
