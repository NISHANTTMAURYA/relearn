import React from 'react';
import {
  AlertCircle,
  CheckCircle,
  HelpCircle,
  Clock,
  ArrowRight,
  TrendingUp,
  Cpu,
  Layers,
  ChevronRight,
  BrainCircuit
} from 'lucide-react';

export default function DualDiagnosisPanel({
  diagnosis,
  sequencePattern,
  attempts = [],
  onTriggerRemediation
}) {
  if (!diagnosis) return null;

  const isMisconception = diagnosis.category === 'misconception';
  const isCorrect = diagnosis.category === 'correct';
  const isSlip = diagnosis.category === 'slip';
  const isUnsure = diagnosis.category === 'unsure';

  // Badge styling based on category
  let badgeBorder = 'border-rose-200 bg-rose-50 text-rose-800';
  let icon = <AlertCircle className="w-5 h-5 text-rose-600 flex-shrink-0" />;
  if (isCorrect) {
    badgeBorder = 'border-emerald-200 bg-emerald-50 text-emerald-800';
    icon = <CheckCircle className="w-5 h-5 text-emerald-600 flex-shrink-0" />;
  } else if (isSlip) {
    badgeBorder = 'border-amber-200 bg-amber-50 text-amber-800';
    icon = <AlertCircle className="w-5 h-5 text-amber-600 flex-shrink-0" />;
  } else if (isUnsure) {
    badgeBorder = 'border-slate-300 bg-slate-100 text-slate-800';
    icon = <HelpCircle className="w-5 h-5 text-slate-600 flex-shrink-0" />;
  }

  // Confidence gauge color
  const confPct = Math.round((diagnosis.confidence || 0) * 100);
  let gaugeColor = 'bg-rose-500';
  if (isCorrect) gaugeColor = 'bg-emerald-500';
  else if (isSlip) gaugeColor = 'bg-amber-500';
  else if (isUnsure) gaugeColor = 'bg-slate-400';

  return (
    <div className="space-y-4">
      <div className="flex items-center space-x-2">
        <BrainCircuit className="w-4 h-4 text-brand" />
        <h3 className="text-xs font-mono font-semibold uppercase tracking-wider text-charcoal">
          Step 3: Dual Real-Time Cognitive Diagnosis
        </h3>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-4">
        {/* MODEL A: Individual Diagnosis (7 cols) */}
        <div className="lg:col-span-7 editorial-card p-4 bg-white border border-border flex flex-col justify-between">
          <div>
            {/* Header */}
            <div className="flex items-center justify-between pb-3 border-b border-border">
              <div className="flex items-center space-x-2">
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-brand-light text-brand font-semibold border border-brand-border">
                  MODEL A (DeBERTa-v3 Primary)
                </span>
                <span className="text-xs text-charcoal-muted font-mono">
                  Individual Response Classifier
                </span>
              </div>
              <span className="text-[11px] font-mono text-charcoal-subtle">
                Latency: ~12ms
              </span>
            </div>

            {/* Diagnosis Result Banner */}
            <div className={`mt-3 p-3 rounded-lg border ${badgeBorder} flex items-start space-x-3`}>
              {icon}
              <div className="flex-1">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-mono font-bold uppercase tracking-wider">
                    {diagnosis.category.toUpperCase()}
                  </span>
                  <span className="text-xs font-mono font-semibold">
                    {confPct}% Confidence
                  </span>
                </div>
                <h4 className="text-sm font-semibold mt-0.5 leading-snug">
                  {diagnosis.label}
                </h4>
              </div>
            </div>

            {/* Confidence Gauge */}
            <div className="mt-3">
              <div className="flex items-center justify-between text-[11px] font-mono text-charcoal-muted mb-1">
                <span>Posterior Likelihood</span>
                <span>{confPct}%</span>
              </div>
              <div className="w-full h-2 rounded-full bg-slate-100 overflow-hidden border border-border">
                <div
                  className={`h-full rounded-full transition-all duration-500 ${gaugeColor}`}
                  style={{ width: `${confPct}%` }}
                />
              </div>
            </div>

            {/* Evidence Rationale */}
            <div className="mt-3 p-2.5 rounded bg-canvas-subtle border border-border">
              <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-charcoal-muted block mb-1">
                Cognitive Evidence Rationale:
              </span>
              <p className="text-xs text-charcoal leading-relaxed font-sans">
                {diagnosis.evidence_rationale}
              </p>
            </div>

            {/* Competing Hypotheses if present */}
            {diagnosis.competing_hypotheses && diagnosis.competing_hypotheses.length > 0 && (
              <div className="mt-2 text-[11px] font-mono text-charcoal-muted">
                <span className="text-charcoal-subtle">Alternative Hypotheses Considered: </span>
                {diagnosis.competing_hypotheses.join(' | ')}
              </div>
            )}
          </div>

          {/* Action Trigger */}
          {isMisconception && (
            <div className="mt-4 pt-3 border-t border-border flex items-center justify-between">
              <span className="text-xs text-charcoal-muted font-mono">
                Prescription: Targeted Multimodal Remediation
              </span>
              <button
                onClick={onTriggerRemediation}
                className="px-3 py-1.5 rounded bg-brand text-white text-xs font-semibold hover:bg-brand-hover transition-colors flex items-center space-x-1.5 shadow-sm"
              >
                <span>Deploy POE Remediation (Step 4)</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>
          )}
        </div>

        {/* MODEL B: Sequence Pattern Analyzer (5 cols) */}
        <div className="lg:col-span-5 editorial-card p-4 bg-white border border-border flex flex-col justify-between">
          <div>
            {/* Header */}
            <div className="flex items-center justify-between pb-3 border-b border-border">
              <div className="flex items-center space-x-2">
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-100 text-charcoal font-semibold border border-border">
                  MODEL B (Sequence Analyzer)
                </span>
                <span className="text-xs text-charcoal-muted font-mono">
                  Longitudinal Temporal Rules
                </span>
              </div>
            </div>

            {/* Longitudinal Session History */}
            <div className="mt-3">
              <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-charcoal-muted block mb-1.5">
                Session Attempt Stream ({attempts.length} attempts):
              </span>
              <div className="space-y-1.5 max-h-24 overflow-y-auto pr-1">
                {attempts.map((att, idx) => (
                  <div
                    key={idx}
                    className="p-1.5 rounded bg-canvas-subtle border border-border text-[11px] font-mono flex items-center justify-between"
                  >
                    <div className="flex items-center space-x-1.5 truncate">
                      <span className="text-charcoal-subtle">#{att.step || idx + 1}</span>
                      <span className="text-charcoal truncate max-w-[150px]">
                        {att.question_id}: "{att.student_response}"
                      </span>
                    </div>
                    <span className="text-[10px] px-1 py-0.2 rounded bg-slate-200 text-charcoal font-semibold">
                      {att.individual_diagnosis?.split(':')[0] || 'DIAGNOSED'}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Pattern Result Card */}
            {sequencePattern && (
              <div className="mt-3 p-3 rounded-lg border border-border bg-canvas-subtle">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-charcoal-muted">
                    Detected Longitudinal Pattern:
                  </span>
                  <span className="text-xs font-mono font-semibold text-brand">
                    {Math.round((sequencePattern.confidence || 0.9) * 100)}% Match
                  </span>
                </div>
                <h5 className="text-xs font-mono font-bold text-charcoal mt-1">
                  {sequencePattern.predicted_pattern}
                </h5>

                <div className="mt-2 text-[11px] text-charcoal-muted">
                  <span className="font-semibold text-charcoal font-mono uppercase text-[10px]">Session Status: </span>
                  <span className="font-mono text-charcoal">{sequencePattern.status}</span>
                </div>

                {sequencePattern.evidence && sequencePattern.evidence.length > 0 && (
                  <div className="mt-2 text-[11px] text-charcoal-muted border-t border-border pt-1.5">
                    <span className="font-semibold text-charcoal font-mono uppercase text-[10px]">Evidence Synthesis: </span>
                    <p className="mt-0.5 text-xs text-charcoal">{sequencePattern.evidence[0]}</p>
                  </div>
                )}
              </div>
            )}
          </div>

          <div className="mt-4 pt-3 border-t border-border flex items-center justify-between text-xs font-mono text-charcoal-muted">
            <span>Next Pedagogical Action:</span>
            <span className="font-semibold text-charcoal">
              {sequencePattern?.next_action || 'administer_intervention'}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
