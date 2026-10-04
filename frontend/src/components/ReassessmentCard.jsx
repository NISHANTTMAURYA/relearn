import React, { useState } from 'react';
import {
  CheckCircle2,
  XCircle,
  TrendingUp,
  Award,
  ArrowRight,
  RotateCcw,
  Sparkles,
  HelpCircle
} from 'lucide-react';

export default function ReassessmentCard({
  reassessmentPair,
  onEvaluateReassessment,
  evaluationResult,
  isLoading,
  onResetSession
}) {
  const [selectedKey, setSelectedKey] = useState('');

  if (!reassessmentPair) return null;

  const item = reassessmentPair.post_intervention_reassessment_item || {};
  const options = item.options || [];

  const handleSubmit = () => {
    if (!selectedKey) return;
    onEvaluateReassessment({
      misc_id: reassessmentPair.target_misconception_id,
      question_id: item.item_id,
      student_selection_key: selectedKey,
      correct_key: item.correct_answer || 'B',
      prior_mastery: 0.15
    });
  };

  return (
    <div className="editorial-card p-4 sm:p-6 bg-white border border-border space-y-5">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-border gap-2">
        <div>
          <div className="flex items-center space-x-2">
            <span className="text-xs font-mono font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200">
              Step 5: Isomorphic Near-Transfer Reassessment
            </span>
            <span className="text-xs font-mono text-charcoal-muted">
              {item.item_id}
            </span>
          </div>
          <h3 className="text-sm sm:text-base font-semibold text-charcoal mt-1">
            Verifying Conceptual Resolution & Schema Generalization
          </h3>
          <p className="text-xs text-charcoal-muted">
            Tests whether the underlying physical law transfers to an isomorphic physical setup without rote recall.
          </p>
        </div>
      </div>

      {/* Question Stem */}
      <div className="p-3.5 rounded-lg bg-canvas-subtle border border-border">
        <p className="text-sm text-charcoal font-medium leading-relaxed">
          {item.stem}
        </p>
      </div>

      {/* Options Selection */}
      <div className="space-y-2">
        <span className="text-xs font-mono font-semibold uppercase tracking-wider text-charcoal-muted block">
          Select Student Response:
        </span>
        <div className="space-y-2">
          {options.map((opt) => {
            const isSelected = selectedKey === opt.key;
            return (
              <label
                key={opt.key}
                onClick={() => !evaluationResult && setSelectedKey(opt.key)}
                className={`p-3 rounded-lg border text-xs sm:text-sm flex items-start space-x-3 cursor-pointer transition-all ${
                  isSelected
                    ? 'border-brand bg-brand-light/30 ring-1 ring-brand'
                    : 'border-border bg-white hover:bg-slate-50'
                } ${evaluationResult ? 'cursor-default' : ''}`}
              >
                <div
                  className={`w-5 h-5 rounded-full border flex items-center justify-center text-xs font-mono font-semibold flex-shrink-0 mt-0.5 ${
                    isSelected
                      ? 'border-brand bg-brand text-white'
                      : 'border-slate-300 text-charcoal-muted'
                  }`}
                >
                  {opt.key}
                </div>
                <div className="flex-1">
                  <span className="text-charcoal leading-snug block">
                    {opt.text}
                  </span>
                  {evaluationResult && opt.key === item.correct_answer && (
                    <span className="text-[11px] font-mono text-emerald-600 font-semibold mt-1 block">
                      ✓ Authoritative Ground Truth Answer
                    </span>
                  )}
                  {evaluationResult && opt.indicates_persistent_misconception && (
                    <span className="text-[11px] font-mono text-rose-600 mt-1 block">
                      ⚠ Distractor reflecting: {opt.indicates_persistent_misconception}
                    </span>
                  )}
                </div>
              </label>
            );
          })}
        </div>
      </div>

      {/* Submit Evaluation Button */}
      {!evaluationResult && (
        <div className="flex justify-end pt-2">
          <button
            onClick={handleSubmit}
            disabled={!selectedKey || isLoading}
            className="px-4 py-2.5 rounded-md bg-brand hover:bg-brand-hover text-white text-xs font-semibold tracking-wide uppercase transition-colors flex items-center space-x-2 disabled:opacity-40 disabled:cursor-not-allowed shadow-sm"
          >
            {isLoading ? (
              <>
                <div className="w-3.5 h-3.5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                <span>Evaluating Transfer Verification...</span>
              </>
            ) : (
              <>
                <span>Submit & Update Mastery (BKT)</span>
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>
      )}

      {/* Step 6: BKT Mastery & Resolution Result Card */}
      {evaluationResult && (
        <div className="mt-5 pt-5 border-t border-border space-y-4">
          <div className="flex items-center space-x-2">
            <Award className="w-4 h-4 text-emerald-600" />
            <h4 className="text-xs font-mono font-semibold uppercase tracking-wider text-charcoal">
              Step 6: Longitudinal Mastery Tracking & Knowledge Tracing
            </h4>
          </div>

          <div
            className={`p-4 rounded-lg border ${
              evaluationResult.is_correct
                ? 'border-emerald-200 bg-emerald-50/60'
                : 'border-rose-200 bg-rose-50/60'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-mono font-bold uppercase tracking-wider text-charcoal">
                Diagnostic Verdict:
              </span>
              <span
                className={`text-xs font-mono font-bold px-2 py-0.5 rounded ${
                  evaluationResult.is_correct
                    ? 'bg-emerald-600 text-white'
                    : 'bg-rose-600 text-white'
                }`}
              >
                {evaluationResult.verdict}
              </span>
            </div>

            <p className="text-xs sm:text-sm text-charcoal font-medium mt-2 leading-relaxed">
              {evaluationResult.explanation}
            </p>

            {/* BKT Probability Visualizer */}
            {evaluationResult.bkt_update && (
              <div className="mt-4 p-3 rounded bg-white border border-border space-y-2">
                <div className="flex items-center justify-between text-xs font-mono">
                  <span className="text-charcoal-muted">Bayesian Knowledge Tracing State:</span>
                  <span className="font-bold text-charcoal">
                    {Math.round(evaluationResult.bkt_update.prior_mastery * 100)}% →{' '}
                    <span className="text-emerald-600">
                      {Math.round(evaluationResult.bkt_update.posterior_mastery * 100)}%
                    </span>
                  </span>
                </div>

                {/* Progress bar comparison */}
                <div className="w-full h-3 rounded-full bg-slate-100 overflow-hidden border border-border relative">
                  <div
                    className="h-full bg-slate-300 absolute left-0 top-0"
                    style={{
                      width: `${Math.round(evaluationResult.bkt_update.prior_mastery * 100)}%`
                    }}
                  />
                  <div
                    className={`h-full absolute left-0 top-0 transition-all duration-700 ${
                      evaluationResult.is_correct ? 'bg-emerald-500' : 'bg-rose-400'
                    }`}
                    style={{
                      width: `${Math.round(evaluationResult.bkt_update.posterior_mastery * 100)}%`
                    }}
                  />
                </div>

                <div className="flex items-center justify-between text-[10px] font-mono text-charcoal-subtle pt-1">
                  <span>P(Init)=0.15</span>
                  <span>P(Transit)=0.35</span>
                  <span>P(Slip)=0.10</span>
                  <span>P(Guess)=0.20</span>
                </div>
              </div>
            )}
          </div>

          {/* Action to restart or explore another question */}
          <div className="flex items-center justify-between pt-2">
            <span className="text-xs text-charcoal-muted font-mono">
              Recommended Next Step: {evaluationResult.recommended_next_step}
            </span>
            <button
              onClick={onResetSession}
              className="px-3.5 py-2 rounded border border-border bg-white hover:bg-slate-50 text-charcoal text-xs font-mono font-medium transition-colors flex items-center space-x-1.5"
            >
              <RotateCcw className="w-3.5 h-3.5 text-charcoal-muted" />
              <span>Start Next Diagnostic Quiz</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
