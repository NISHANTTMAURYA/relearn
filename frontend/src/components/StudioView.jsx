import React, { useState } from 'react';
import TopicQuestionSelector from './TopicQuestionSelector';
import StudentResponseInput from './StudentResponseInput';
import DualDiagnosisPanel from './DualDiagnosisPanel';
import MultimodalRemediation from './MultimodalRemediation';
import ReassessmentCard from './ReassessmentCard';
import { ArrowDown, CheckCircle2, RotateCcw } from 'lucide-react';

export default function StudioView({
  topics = [],
  selectedTopic,
  setSelectedTopic,
  selectedQuestion,
  setSelectedQuestion,
  studentResponse,
  setStudentResponse,
  onDiagnose,
  isLoadingDiagnosis,
  diagnosis,
  sequencePattern,
  attempts = [],
  intervention,
  isLoadingIntervention,
  reassessmentPair,
  isLoadingReassessment,
  onEvaluateReassessment,
  evaluationResult,
  isLoadingEvaluation,
  onResetSession
}) {
  const [showRemediation, setShowRemediation] = useState(false);
  const [showReassessment, setShowReassessment] = useState(false);

  const handleTriggerRemediation = () => {
    setShowRemediation(true);
    // Smooth scroll down to remediation
    setTimeout(() => {
      window.scrollTo({
        top: document.body.scrollHeight / 2,
        behavior: 'smooth'
      });
    }, 100);
  };

  const handleProceedToReassessment = () => {
    setShowReassessment(true);
    setTimeout(() => {
      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
      });
    }, 100);
  };

  return (
    <div className="space-y-6">
      {/* Intro banner */}
      <div className="editorial-card p-5 bg-white border border-border">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 className="text-base font-semibold text-charcoal tracking-tight">
              Interactive Diagnostic Physics Studio
            </h2>
            <p className="text-xs text-charcoal-muted mt-0.5">
              Closed-loop cognitive learning workflow: Question Presentation → Dual Diagnosis (Model A + B) → Multimodal POE Remediation → Isomorphic Reassessment & BKT Mastery Tracking.
            </p>
          </div>

          <div className="flex items-center space-x-2">
            <button
              onClick={onResetSession}
              className="text-xs font-mono px-3 py-1.5 rounded border border-border bg-canvas-subtle hover:bg-slate-100 text-charcoal transition-colors flex items-center space-x-1"
            >
              <RotateCcw className="w-3.5 h-3.5 text-charcoal-muted" />
              <span>Reset Session</span>
            </button>
          </div>
        </div>

        {/* 5-Step Progress Stepper */}
        <div className="mt-4 pt-4 border-t border-border grid grid-cols-2 sm:grid-cols-5 gap-2">
          {[
            { step: '1', title: 'Curriculum & Item', active: true, done: !!selectedQuestion },
            { step: '2', title: 'Student Response', active: !!selectedQuestion, done: !!studentResponse },
            { step: '3', title: 'Dual Diagnosis', active: !!diagnosis, done: !!diagnosis },
            { step: '4', title: 'POE Remediation', active: showRemediation || !!intervention, done: showReassessment },
            { step: '5', title: 'Reassessment & BKT', active: showReassessment, done: !!evaluationResult }
          ].map((s) => (
            <div
              key={s.step}
              className={`p-2 rounded border text-xs font-mono transition-all ${
                s.done
                  ? 'border-emerald-200 bg-emerald-50/50 text-emerald-800'
                  : s.active
                  ? 'border-brand bg-brand-light/40 text-brand font-semibold'
                  : 'border-border bg-slate-50 text-charcoal-subtle'
              }`}
            >
              <div className="flex items-center space-x-1.5">
                <span
                  className={`w-4 h-4 rounded-full flex items-center justify-center text-[10px] font-bold ${
                    s.done
                      ? 'bg-emerald-600 text-white'
                      : s.active
                      ? 'bg-brand text-white'
                      : 'bg-slate-200 text-charcoal-muted'
                  }`}
                >
                  {s.step}
                </span>
                <span className="truncate">{s.title}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Step 1: Topic & Question Selection */}
      <TopicQuestionSelector
        topics={topics}
        selectedTopic={selectedTopic}
        setSelectedTopic={setSelectedTopic}
        selectedQuestion={selectedQuestion}
        setSelectedQuestion={setSelectedQuestion}
        onResetSession={onResetSession}
      />

      {/* Step 2: Student Free-text Input with Presets */}
      <StudentResponseInput
        studentResponse={studentResponse}
        setStudentResponse={setStudentResponse}
        selectedQuestion={selectedQuestion}
        onDiagnose={onDiagnose}
        isLoading={isLoadingDiagnosis}
      />

      {/* Step 3: Real-Time Dual Diagnosis Panel */}
      {diagnosis && (
        <DualDiagnosisPanel
          diagnosis={diagnosis}
          sequencePattern={sequencePattern}
          attempts={attempts}
          onTriggerRemediation={handleTriggerRemediation}
        />
      )}

      {/* Step 4: Targeted Multimodal Remediation (Triggered automatically on misconception diagnosis or manual click) */}
      {(showRemediation || (diagnosis && diagnosis.category === 'misconception')) && intervention && (
        <MultimodalRemediation
          intervention={intervention}
          onProceedToReassessment={handleProceedToReassessment}
        />
      )}

      {/* Step 5: Isomorphic Near-Transfer Reassessment & BKT State */}
      {(showReassessment || (diagnosis && diagnosis.category === 'misconception' && showRemediation)) && reassessmentPair && (
        <ReassessmentCard
          reassessmentPair={reassessmentPair}
          onEvaluateReassessment={onEvaluateReassessment}
          evaluationResult={evaluationResult}
          isLoading={isLoadingEvaluation}
          onResetSession={onResetSession}
        />
      )}
    </div>
  );
}
