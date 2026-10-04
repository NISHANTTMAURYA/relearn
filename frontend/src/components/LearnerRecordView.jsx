import React from 'react';
import { Award, CheckCircle2, AlertTriangle, TrendingUp, Clock, BookOpen, RotateCcw } from 'lucide-react';

export default function LearnerRecordView({ recordHistory = [], onStartNewSession }) {
  // Default sample history if user just opened the tab
  const displayHistory = recordHistory.length > 0 ? recordHistory : [
    {
      topic: 'Light – Reflection and Refraction',
      misconception_id: 'MISC-OPT-001',
      title: 'Half-Lens Blocking Fallacy',
      status: 'RESOLVED_WITH_TRANSFER',
      mastery: 0.85,
      date: 'Just now',
      attempts: 3
    },
    {
      topic: 'Electricity',
      misconception_id: 'MISC-ELEC-001',
      title: 'Current Attenuation in Series Circuits',
      status: 'RESOLVED_WITH_TRANSFER',
      mastery: 0.78,
      date: 'Today',
      attempts: 4
    },
    {
      topic: 'Motion & Kinematics',
      misconception_id: 'MISC-MOT-001',
      title: 'Speed Distance Operation Inversion',
      status: 'NEEDS_REINFORCEMENT',
      mastery: 0.45,
      date: 'Yesterday',
      attempts: 2
    }
  ];

  const resolvedCount = displayHistory.filter(h => h.status === 'RESOLVED_WITH_TRANSFER').length;
  const avgMastery = Math.round(displayHistory.reduce((acc, h) => acc + h.mastery, 0) / displayHistory.length * 100);

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Header Profile Banner */}
      <div className="editorial-card p-6 bg-white border border-border flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div className="flex items-center space-x-4">
          <div className="w-12 h-12 rounded-full bg-indigo-50 border-2 border-indigo-200 text-indigo-700 flex items-center justify-center font-bold text-lg">
            ST
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h2 className="text-lg font-bold text-charcoal">Learner Cognitive Record</h2>
              <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200">
                Active Student
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              Tracks longitudinal conceptual misconceptions and verified near-transfer resolutions.
            </p>
          </div>
        </div>

        <button
          onClick={onStartNewSession}
          className="px-4 py-2 rounded text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm flex items-center space-x-1.5"
        >
          <BookOpen className="w-3.5 h-3.5" />
          <span>Take New Diagnostic Quiz</span>
        </button>
      </div>

      {/* 3 Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="editorial-card p-4 bg-white border border-border">
          <div className="flex items-center justify-between text-slate-500">
            <span className="text-xs font-mono uppercase">Mastery Index (BKT)</span>
            <TrendingUp className="w-4 h-4 text-indigo-600" />
          </div>
          <div className="text-2xl font-bold text-charcoal mt-1">{avgMastery}%</div>
          <p className="text-[11px] text-slate-500 mt-1">Average posterior mastery probability</p>
        </div>

        <div className="editorial-card p-4 bg-white border border-border">
          <div className="flex items-center justify-between text-slate-500">
            <span className="text-xs font-mono uppercase">Misconceptions Resolved</span>
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
          </div>
          <div className="text-2xl font-bold text-emerald-700 mt-1">
            {resolvedCount} / {displayHistory.length}
          </div>
          <p className="text-[11px] text-emerald-600 mt-1">Verified via isomorphic reassessment</p>
        </div>

        <div className="editorial-card p-4 bg-white border border-border">
          <div className="flex items-center justify-between text-slate-500">
            <span className="text-xs font-mono uppercase">Learning Sessions</span>
            <Clock className="w-4 h-4 text-amber-600" />
          </div>
          <div className="text-2xl font-bold text-charcoal mt-1">
            {displayHistory.reduce((acc, h) => acc + (h.attempts || 1), 0)} Attempts
          </div>
          <p className="text-[11px] text-slate-500 mt-1">Total ordered diagnostic interactions</p>
        </div>
      </div>

      {/* Detailed Diagnostic History Timeline */}
      <div className="editorial-card p-6 bg-white border border-border space-y-4">
        <h3 className="text-sm font-bold font-mono uppercase text-slate-700 border-b border-border pb-3">
          Concept Diagnostic & Remediation History
        </h3>

        <div className="divide-y divide-slate-100">
          {displayHistory.map((item, idx) => (
            <div key={idx} className="py-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div className="space-y-1">
                <div className="flex items-center space-x-2">
                  <span className="text-xs font-semibold text-charcoal">{item.topic}</span>
                  <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-100 text-slate-600">
                    {item.misconception_id}
                  </span>
                </div>
                <p className="text-xs text-slate-600">
                  Target Fallacy: <strong>{item.title}</strong>
                </p>
              </div>

              <div className="flex items-center space-x-4">
                <div className="text-right">
                  <span className={`inline-flex items-center text-xs font-semibold px-2 py-0.5 rounded ${
                    item.status === 'RESOLVED_WITH_TRANSFER'
                      ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                      : 'bg-amber-50 text-amber-700 border border-amber-200'
                  }`}>
                    {item.status === 'RESOLVED_WITH_TRANSFER' ? (
                      <>
                        <CheckCircle2 className="w-3 h-3 mr-1" />
                        Resolved with Transfer
                      </>
                    ) : (
                      <>
                        <AlertTriangle className="w-3 h-3 mr-1" />
                        Needs Reinforcement
                      </>
                    )}
                  </span>
                  <span className="text-[11px] text-slate-400 block mt-0.5">
                    Mastery: {Math.round(item.mastery * 100)}%
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
