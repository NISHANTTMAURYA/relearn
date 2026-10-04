import React, { useState } from 'react';
import {
  Compass,
  Layers,
  ExternalLink,
  ChevronRight,
  Sparkles,
  BookOpen,
  ArrowRight,
  Maximize2
} from 'lucide-react';
import WhiteboardCanvas from './WhiteboardCanvas';
import AICharacterTeacher from './AICharacterTeacher';
import ErrorBoundary from './ErrorBoundary';

export default function MultimodalRemediation({
  intervention,
  onProceedToReassessment
}) {
  const [activeTab, setActiveTab] = useState('3dteacher'); // '3dteacher' | 'whiteboard' | 'phet'

  if (!intervention) return null;

  const seq = intervention.guided_learning_sequence || {};
  const sim = intervention.simulation_reference || {};
  const miscId = intervention.target_misconception_id || '';
  const poeText = intervention.poe_explanation || `${seq.step_1_predict} ${seq.step_3_explain_cognitive_conflict} ${seq.step_4_conceptual_bridge}`;

  return (
    <div className="editorial-card p-4 sm:p-6 bg-white border border-border space-y-5">
      {/* Step Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-border gap-2">
        <div>
          <div className="flex items-center space-x-2">
            <span className="text-xs font-mono font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-brand-light text-brand border border-brand-border">
              Step 4: Targeted Multimodal Remediation
            </span>
            <span className="text-xs font-mono text-charcoal-muted">
              {intervention.target_misconception_id}
            </span>
          </div>
          <h2 className="text-base sm:text-lg font-semibold text-charcoal mt-1">
            {intervention.misconception_name}
          </h2>
          <p className="text-xs text-charcoal-muted">
            Pedagogical Strategy: {intervention.pedagogical_strategy}
          </p>
        </div>

        {/* View Switcher: 3D AI Teacher vs Animated Whiteboard vs PhET Simulation */}
        <div className="flex items-center bg-canvas-subtle p-1 rounded-lg border border-border gap-1">
          <button
            onClick={() => setActiveTab('3dteacher')}
            className={`px-3 py-1 text-xs font-medium rounded-md transition-colors flex items-center space-x-1 ${
              activeTab === '3dteacher'
                ? 'bg-indigo-600 text-white shadow-sm font-semibold'
                : 'text-charcoal-muted hover:text-charcoal'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>3D AI Physics Tutor</span>
          </button>

          <button
            onClick={() => setActiveTab('whiteboard')}
            className={`px-3 py-1 text-xs font-medium rounded-md transition-colors ${
              activeTab === 'whiteboard'
                ? 'bg-white text-charcoal shadow-sm border border-border'
                : 'text-charcoal-muted hover:text-charcoal'
            }`}
          >
            Animated Whiteboard
          </button>

          <button
            onClick={() => setActiveTab('phet')}
            className={`px-3 py-1 text-xs font-medium rounded-md transition-colors flex items-center space-x-1 ${
              activeTab === 'phet'
                ? 'bg-white text-charcoal shadow-sm border border-border'
                : 'text-charcoal-muted hover:text-charcoal'
            }`}
          >
            <span>PhET Simulation</span>
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
          </button>
        </div>
      </div>

      {/* Main Interactive Modality Container */}
      {activeTab === '3dteacher' && (
        <ErrorBoundary message="3D mentor avatar switched to safe mode. You can still use the animated whiteboard and audio explanation.">
          <AICharacterTeacher
            textToSpeak={poeText}
            misconceptionId={miscId}
            title={`3D Avatar Remediation: ${intervention.misconception_name}`}
          />
        </ErrorBoundary>
      )}

      {activeTab === 'whiteboard' && (
        <WhiteboardCanvas
          commands={intervention.whiteboard_commands}
          miscId={miscId}
          title={`Cognitive Reconstruction: ${intervention.misconception_name}`}
        />
      )}

      {activeTab === 'phet' && (
        <div className="editorial-card overflow-hidden bg-white border border-border">
          <div className="bg-canvas-subtle px-4 py-2.5 border-b border-border flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <span className="text-xs font-mono font-semibold uppercase text-charcoal">
                Interactive Lab: {sim.simulation_name}
              </span>
              <span className="text-[10px] font-mono text-charcoal-muted hidden sm:inline">
                (University of Colorado Boulder)
              </span>
            </div>
            <a
              href={sim.url}
              target="_blank"
              rel="noreferrer"
              className="text-xs font-mono text-brand hover:underline flex items-center space-x-1"
            >
              <span>Open in New Tab</span>
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          </div>

          <div className="w-full h-80 sm:h-96 bg-slate-900 relative">
            <iframe
              src={sim.url}
              title={sim.simulation_name}
              className="w-full h-full border-0"
              allow="fullscreen"
            />
          </div>
        </div>
      )}

      {/* 4-Step Predict-Observe-Explain (POE) Learning Cards */}
      <div className="space-y-3">
        <h4 className="text-xs font-mono font-semibold uppercase tracking-wider text-charcoal-muted">
          Predict-Observe-Explain (POE) Cognitive Sequence:
        </h4>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {/* Step 1: Predict */}
          <div className="p-3.5 rounded-lg border border-border bg-canvas-subtle flex flex-col justify-between">
            <div>
              <div className="flex items-center space-x-2 text-xs font-mono font-semibold text-charcoal mb-1">
                <span className="w-5 h-5 rounded-full bg-slate-200 text-charcoal flex items-center justify-center text-[10px]">
                  1
                </span>
                <span>Predict (Cognitive Stance)</span>
              </div>
              <p className="text-xs text-charcoal leading-relaxed">
                {seq.step_1_predict}
              </p>
            </div>
          </div>

          {/* Step 2: Observe */}
          <div className="p-3.5 rounded-lg border border-border bg-canvas-subtle flex flex-col justify-between">
            <div>
              <div className="flex items-center space-x-2 text-xs font-mono font-semibold text-charcoal mb-1">
                <span className="w-5 h-5 rounded-full bg-slate-200 text-charcoal flex items-center justify-center text-[10px]">
                  2
                </span>
                <span>Observe (Empirical Reality)</span>
              </div>
              <p className="text-xs text-charcoal leading-relaxed">
                {seq.step_2_observe}
              </p>
            </div>
          </div>

          {/* Step 3: Explain Cognitive Conflict */}
          <div className="p-3.5 rounded-lg border border-rose-200 bg-rose-50/40 flex flex-col justify-between">
            <div>
              <div className="flex items-center space-x-2 text-xs font-mono font-semibold text-rose-800 mb-1">
                <span className="w-5 h-5 rounded-full bg-rose-200 text-rose-800 flex items-center justify-center text-[10px]">
                  3
                </span>
                <span>Cognitive Conflict Paradox</span>
              </div>
              <p className="text-xs text-rose-900 leading-relaxed font-medium">
                {seq.step_3_explain_cognitive_conflict}
              </p>
            </div>
          </div>

          {/* Step 4: Conceptual Bridge */}
          <div className="p-3.5 rounded-lg border border-emerald-200 bg-emerald-50/40 flex flex-col justify-between">
            <div>
              <div className="flex items-center space-x-2 text-xs font-mono font-semibold text-emerald-800 mb-1">
                <span className="w-5 h-5 rounded-full bg-emerald-200 text-emerald-800 flex items-center justify-center text-[10px]">
                  4
                </span>
                <span>Conceptual Bridge (Invariant Principle)</span>
              </div>
              <p className="text-xs text-emerald-950 leading-relaxed">
                {seq.step_4_conceptual_bridge}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Advance to Step 5 CTA */}
      <div className="pt-2 flex justify-end">
        <button
          onClick={onProceedToReassessment}
          className="px-4 py-2.5 rounded-md bg-brand hover:bg-brand-hover text-white text-xs font-semibold tracking-wide uppercase transition-colors flex items-center space-x-2 shadow-sm"
        >
          <span>Proceed to Isomorphic Near-Transfer Reassessment (Step 5)</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
