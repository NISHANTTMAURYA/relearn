import React from 'react';
import { Send, Zap, HelpCircle, Check, AlertTriangle, ArrowRight } from 'lucide-react';

export default function StudentResponseInput({
  studentResponse,
  setStudentResponse,
  selectedQuestion,
  onDiagnose,
  isLoading
}) {
  // Collect presets based on active question or generic archetypes
  const presets = [
    {
      category: 'Misconception',
      type: 'misc',
      text: selectedQuestion?.sample_misconception_responses?.[0] ||
        "The top half of the candle image is completely missing because the bottom half of the lens is covered with black paper."
    },
    {
      category: 'Alternate Misconception',
      type: 'misc',
      text: selectedQuestion?.sample_misconception_responses?.[1] ||
        "Current gets consumed by Bulb 1 to produce light, so Bulb 2 receives significantly less amperage."
    },
    {
      category: 'Scientific Ground Truth',
      type: 'correct',
      text: selectedQuestion?.sample_correct_responses?.[0] ||
        "The entire image remains intact on the screen; only the intensity/brightness is halved because all exposed lens points collect light from every object point."
    },
    {
      category: 'Calculation Slip',
      type: 'slip',
      text: selectedQuestion?.sample_slip_responses?.[0] ||
        "Full image forms with focal length miscalculated as 30 cm instead of 15 cm due to arithmetic sign inversion."
    },
    {
      category: 'Unsure / Vague (Abstain Test)',
      type: 'unsure',
      text: "idk forgot the formula skip please"
    }
  ];

  return (
    <div className="editorial-card p-4 bg-white border border-border space-y-3">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1">
        <div>
          <label className="block text-xs font-mono font-semibold uppercase tracking-wider text-charcoal">
            Step 2: Student Reasoning & Qualitative Response
          </label>
          <p className="text-xs text-charcoal-muted">
            Enter the student's authentic written thought process or select an evaluation preset.
          </p>
        </div>

        {/* Evaluation Presets Dropdown / Quick bar */}
        <div className="flex items-center space-x-1 text-xs">
          <Zap className="w-3.5 h-3.5 text-amber-500" />
          <span className="font-mono text-[11px] text-charcoal-muted">Quick-Test Presets:</span>
        </div>
      </div>

      {/* Preset Chips */}
      <div className="flex flex-wrap gap-1.5">
        {presets.map((preset, idx) => {
          let badgeClass = 'border-slate-200 text-charcoal hover:bg-slate-100';
          if (preset.type === 'misc') badgeClass = 'border-red-200 text-rose-700 bg-rose-50/50 hover:bg-rose-100/60';
          if (preset.type === 'correct') badgeClass = 'border-emerald-200 text-emerald-700 bg-emerald-50/50 hover:bg-emerald-100/60';
          if (preset.type === 'slip') badgeClass = 'border-amber-200 text-amber-700 bg-amber-50/50 hover:bg-amber-100/60';
          if (preset.type === 'unsure') badgeClass = 'border-slate-300 text-slate-700 bg-slate-100 hover:bg-slate-200';

          return (
            <button
              key={idx}
              onClick={() => setStudentResponse(preset.text)}
              className={`text-xs px-2.5 py-1 rounded-md border text-left font-mono transition-colors flex items-center space-x-1.5 ${badgeClass}`}
            >
              <span className="font-semibold text-[10px] uppercase opacity-75">
                [{preset.category}]
              </span>
              <span className="truncate max-w-[200px] sm:max-w-[280px]">
                "{preset.text}"
              </span>
            </button>
          );
        })}
      </div>

      {/* Text Area Input */}
      <div className="relative">
        <textarea
          rows={3}
          value={studentResponse}
          onChange={(e) => setStudentResponse(e.target.value)}
          placeholder="e.g. I think covering half the lens cuts off the top half of the candle image because light rays are physically blocked from reaching the screen..."
          className="w-full text-sm font-sans p-3 bg-canvas-subtle border border-border rounded-lg text-charcoal placeholder-charcoal-subtle focus:bg-white focus:outline-none focus:ring-1 focus:ring-brand focus:border-brand transition-all"
        />
        <div className="flex items-center justify-between mt-1 text-[11px] text-charcoal-subtle font-mono">
          <span>{studentResponse.length} characters</span>
          {studentResponse && (
            <button
              onClick={() => setStudentResponse('')}
              className="text-charcoal-muted hover:text-charcoal underline"
            >
              Clear
            </button>
          )}
        </div>
      </div>

      {/* Submit Diagnosis Button */}
      <div className="flex justify-end pt-1">
        <button
          onClick={onDiagnose}
          disabled={!studentResponse.trim() || isLoading}
          className="px-4 py-2 rounded-md bg-brand hover:bg-brand-hover text-white text-xs font-semibold tracking-wide uppercase transition-colors flex items-center space-x-2 disabled:opacity-40 disabled:cursor-not-allowed shadow-sm"
        >
          {isLoading ? (
            <>
              <div className="w-3.5 h-3.5 border-2 border-white border-t-transparent rounded-full animate-spin" />
              <span>Running Neural Diagnosis...</span>
            </>
          ) : (
            <>
              <span>Run Dual Diagnosis (Model A + B)</span>
              <ArrowRight className="w-4 h-4" />
            </>
          )}
        </button>
      </div>
    </div>
  );
}
