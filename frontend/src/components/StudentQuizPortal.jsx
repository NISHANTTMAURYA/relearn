import React, { useState } from 'react';
import { 
  BookOpen, Compass, CheckCircle2, AlertTriangle, ArrowRight, RotateCcw, 
  HelpCircle, Sparkles, ChevronRight, Sliders, ShieldAlert, Award
} from 'lucide-react';
import TeacherAvatar from './TeacherAvatar';
import WhiteboardCanvas from './WhiteboardCanvas';
import InteractiveSimWidget from './InteractiveSimWidget';
import MultimodalInputWorkspace from './MultimodalInputWorkspace';

const API_BASE = 'http://127.0.0.1:8000';

export default function StudentQuizPortal({ topics = [], onUpdateLearnerRecord }) {
  // Phase of Learning Flow:
  // 'select_topic' -> 'pre_quiz_lesson' -> 'taking_quiz' -> 'diagnosis_results' -> 'multimodal_intervention' -> 'isomorphic_reassessment' -> 'mastery_summary'
  const [currentPhase, setCurrentPhase] = useState('select_topic');

  // Selected Topic & Quiz Session State
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [studentResponseText, setStudentResponseText] = useState('');
  const [selectedOptionKey, setSelectedOptionKey] = useState('');

  // Longitudinal Session Attempts
  const [orderedAttempts, setOrderedAttempts] = useState([]);
  
  // Diagnosis State
  const [isDiagnosing, setIsDiagnosing] = useState(false);
  const [quizDiagnoses, setQuizDiagnoses] = useState([]);
  const [sequencePatternResult, setSequencePatternResult] = useState(null);

  // Intervention State
  const [interventionData, setInterventionData] = useState(null);
  const [reassessmentPair, setReassessmentPair] = useState(null);

  // Reassessment State
  const [reassessmentAnswerKey, setReassessmentAnswerKey] = useState('');
  const [reassessmentEvalResult, setReassessmentEvalResult] = useState(null);
  const [isEvaluatingReassessment, setIsEvaluatingReassessment] = useState(false);

  // Fallback demo questions if backend is still initializing
  const activeQuestions = selectedTopic?.questions?.length > 0 
    ? selectedTopic.questions.slice(0, 3)
    : [];

  const currentQ = activeQuestions[currentQuestionIndex];

  // 1. Select Topic
  const handleSelectTopic = (topic) => {
    setSelectedTopic(topic);
    setCurrentPhase('pre_quiz_lesson');
  };

  // 2. Start Quiz from Pre-Quiz Lesson
  const handleStartQuiz = () => {
    setCurrentQuestionIndex(0);
    setOrderedAttempts([]);
    setStudentResponseText('');
    setSelectedOptionKey('');
    setCurrentPhase('taking_quiz');
  };

  // 3. Submit Question in Sequence
  const handleSubmitQuestionAttempt = async () => {
    if (!studentResponseText.trim() && !selectedOptionKey) return;

    const fullResponse = studentResponseText.trim() 
      ? studentResponseText.trim() 
      : `Selected Option [${selectedOptionKey}]`;

    const newAttempt = {
      step: currentQuestionIndex + 1,
      question_id: currentQ.question_id,
      question_stem: currentQ.stem,
      student_response: fullResponse
    };

    const nextAttempts = [...orderedAttempts, newAttempt];
    setOrderedAttempts(nextAttempts);

    if (currentQuestionIndex + 1 < activeQuestions.length) {
      // Move to next question in sequence
      setCurrentQuestionIndex(prev => prev + 1);
      setStudentResponseText('');
      setSelectedOptionKey('');
    } else {
      // Quiz Finished! Run Combined Diagnosis Service (Model A + Model B)
      await runCombinedDiagnosisService(nextAttempts);
    }
  };

  // 4. Run Combined Diagnosis (Model A + Model B)
  const runCombinedDiagnosisService = async (attemptsToDiagnose) => {
    try {
      setIsDiagnosing(true);
      setCurrentPhase('diagnosis_results');

      // Diagnose each attempt via Model A
      const diagPromises = attemptsToDiagnose.map(att =>
        fetch(`${API_BASE}/api/diagnose`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            question_id: att.question_id,
            question_text: att.question_stem,
            student_response: att.student_response,
            topic: selectedTopic?.chapter
          })
        }).then(r => r.json())
      );

      const diagnoses = await Promise.all(diagPromises);
      setQuizDiagnoses(diagnoses);

      // Attach diagnoses to attempts for Model B
      const enrichedAttempts = attemptsToDiagnose.map((att, idx) => ({
        ...att,
        individual_diagnosis: diagnoses[idx]?.label || 'DIAGNOSIS_PENDING',
        confidence: diagnoses[idx]?.confidence || 0.85
      }));

      // Run Model B Sequence Pattern Analyzer
      const seqRes = await fetch(`${API_BASE}/api/sequence-pattern`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sequence_id: `SESSION-${Date.now()}`,
          student_id: 'STU-CBSE-X',
          topic: selectedTopic?.chapter || 'Physics',
          ordered_attempts: enrichedAttempts
        })
      });

      let seqPattern = null;
      if (seqRes.ok) {
        seqPattern = await seqRes.json();
        setSequencePatternResult(seqPattern);
      }

      // Pre-fetch Intervention, Reassessment, and Dynamic Whiteboard Plan
      const primaryMisc = diagnoses.find(d => d.category === 'misconception');
      if (primaryMisc && primaryMisc.misc_id) {
        try {
          const [intvRes, reassessRes, wbRes] = await Promise.all([
            fetch(`${API_BASE}/api/intervention/${primaryMisc.misc_id}`),
            fetch(`${API_BASE}/api/reassessment/${primaryMisc.misc_id}`),
            fetch(`${API_BASE}/api/generate-whiteboard`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                concept: selectedTopic?.chapter || 'Physics',
                misconception_label: primaryMisc.misc_id,
                question_stem: attemptsToDiagnose[0]?.question_stem || '',
                student_response: attemptsToDiagnose[0]?.student_response || ''
              })
            }).catch(e => { console.warn('Dynamic whiteboard fetch notice:', e); return null; })
          ]);

          if (intvRes && intvRes.ok) {
            const intv = await intvRes.json();
            if (wbRes && wbRes.ok) {
              const wbPlan = await wbRes.json();
              intv.dynamic_whiteboard_plan = wbPlan;
            }
            setInterventionData(intv);
          }
          if (reassessRes && reassessRes.ok) {
            setReassessmentPair(await reassessRes.json());
          }
        } catch (fetchErr) {
          console.error('Error prefetching intervention assets:', fetchErr);
        }
      }
    } catch (err) {
      console.error('Diagnosis error:', err);
    } finally {
      setIsDiagnosing(false);
    }
  };

  // 5. Evaluate Reassessment Item
  const handleEvaluateReassessment = async () => {
    if (!reassessmentAnswerKey || !reassessmentPair) return;

    try {
      setIsEvaluatingReassessment(true);
      const evalRes = await fetch(`${API_BASE}/api/evaluate-reassessment`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          misc_id: reassessmentPair.target_misconception_id,
          question_id: reassessmentPair.reassessment_item.item_id,
          student_selection_key: reassessmentAnswerKey,
          correct_key: reassessmentPair.reassessment_item.correct_option_key,
          prior_mastery: 0.20
        })
      });

      if (evalRes.ok) {
        const evalData = await evalRes.json();
        setReassessmentEvalResult(evalData);
        setCurrentPhase('mastery_summary');

        if (onUpdateLearnerRecord) {
          onUpdateLearnerRecord({
            topic: selectedTopic?.chapter,
            misconception_id: reassessmentPair.target_misconception_id,
            status: evalData.resolution_status,
            mastery: evalData.updated_mastery,
            attempts_count: orderedAttempts.length + 1
          });
        }
      }
    } catch (err) {
      console.error('Evaluation error:', err);
    } finally {
      setIsEvaluatingReassessment(false);
    }
  };

  // Quick preset helper for evaluator demo
  const handleQuickPreset = (presetText) => {
    setStudentResponseText(presetText);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* ========================================================================= */}
      {/* PHASE 1: CHOOSE TOPIC                                                     */}
      {/* ========================================================================= */}
      {currentPhase === 'select_topic' && (
        <div className="space-y-6">
          <div className="text-center max-w-2xl mx-auto space-y-2">
            <span className="text-xs uppercase font-mono tracking-wider text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-full border border-indigo-200">
              NCERT Physics Diagnostic Studio
            </span>
            <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-charcoal">
              What concept would you like to explore today?
            </h1>
            <p className="text-sm text-slate-600">
              Select a chapter to begin the diagnostic learning sequence. Re:Learn pinpoints the exact cognitive reason behind any mistake rather than merely scoring answers right or wrong.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-6">
            {topics.map((t) => (
              <div
                key={t.chapter}
                onClick={() => handleSelectTopic(t)}
                className="editorial-card p-5 cursor-pointer hover:border-indigo-400 hover:shadow-md transition-all group bg-white border border-border"
              >
                <div className="flex items-start justify-between">
                  <div className="w-10 h-10 rounded-lg bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold text-lg group-hover:bg-indigo-600 group-hover:text-white transition-colors">
                    {t.chapter.includes('Light') ? '💡' : t.chapter.includes('Electric') ? '⚡' : t.chapter.includes('Magnetic') ? '🧲' : '🏃'}
                  </div>
                  <span className="text-[11px] font-mono text-slate-600 bg-slate-100 px-2 py-0.5 rounded">
                    {t.grade} • {t.questions?.length || 4} Questions
                  </span>
                </div>

                <h3 className="text-base font-semibold text-charcoal mt-3 group-hover:text-indigo-600 transition-colors">
                  {t.chapter}
                </h3>
                <p className="text-xs text-slate-500 mt-1 line-clamp-2">
                  Diagnoses core secondary physics misconceptions in {t.chapter.toLowerCase()}.
                </p>

                <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-indigo-700 font-medium">
                  <span>Start Pre-Quiz Lesson</span>
                  <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* PHASE 2: PRE-QUIZ CHAPTER LESSON (Part 4 of Documentation)                */}
      {/* ========================================================================= */}
      {currentPhase === 'pre_quiz_lesson' && selectedTopic && (
        <div className="editorial-card p-6 sm:p-8 bg-white border border-border space-y-6">
          <div className="flex items-center justify-between border-b border-border pb-4">
            <div>
              <span className="text-xs font-mono uppercase tracking-wider text-slate-600">
                Chapter Overview & Core Principles
              </span>
              <h2 className="text-xl font-bold text-charcoal mt-0.5">
                {selectedTopic.chapter}
              </h2>
            </div>

            <button
              onClick={() => setCurrentPhase('select_topic')}
              className="text-xs font-medium text-slate-600 hover:text-charcoal px-3 py-1.5 rounded border border-border bg-slate-50"
            >
              ← Choose Different Topic
            </button>
          </div>

          {/* Educational Overview Content */}
          <div className="prose prose-slate max-w-none text-sm leading-relaxed space-y-4">
            <div className="p-4 bg-indigo-50/60 rounded border border-indigo-100 text-slate-800">
              <h4 className="text-xs font-bold uppercase tracking-wider text-indigo-800 font-mono mb-1">
                Authoritative NCERT Standard:
              </h4>
              <p className="text-xs text-slate-700 leading-normal">
                This diagnostic quiz assesses whether you truly understand the <em>underlying causal physical mechanisms</em> or whether you are applying naive intuitive shortcuts.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="p-4 rounded border border-slate-200 bg-slate-50">
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-700 font-mono mb-2 flex items-center space-x-1.5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                  <span>Key Principles to Bear in Mind</span>
                </h4>
                <ul className="text-xs text-slate-600 space-y-1.5 list-disc pl-4">
                  {selectedTopic.chapter.includes('Light') ? (
                    <>
                      <li>Every point on a lens receives light rays from every point on an object.</li>
                      <li>Covering part of a lens changes light transmission (brightness), not the image shape.</li>
                      <li>Real images exist in 3D aerial space; a screen merely captures intersecting rays.</li>
                    </>
                  ) : selectedTopic.chapter.includes('Electric') ? (
                    <>
                      <li>Electric current is the rate of flow of charge ($I = Q/t$).</li>
                      <li>Charge is conserved in a closed loop; bulbs do not consume or eat electric current.</li>
                      <li>In a series circuit, current is identical across every component ($I_1 = I_2$).</li>
                    </>
                  ) : (
                    <>
                      <li>Free-fall gravitational acceleration $g = GM/R^2$ is independent of falling mass.</li>
                      <li>Velocity and acceleration are separate quantities; zero velocity does not mean zero force.</li>
                      <li>Distance is scalar total path; displacement is the vector difference.</li>
                    </>
                  )}
                </ul>
              </div>

              <div className="p-4 rounded border border-slate-200 bg-slate-50">
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-700 font-mono mb-2 flex items-center space-x-1.5">
                  <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
                  <span>Common Student Misconceptions</span>
                </h4>
                <ul className="text-xs text-slate-600 space-y-1.5 list-disc pl-4">
                  {selectedTopic.chapter.includes('Light') ? (
                    <>
                      <li>"Covering half the lens cuts off the top or bottom half of the image."</li>
                      <li>"Images exist only as physical drawings stamped onto paper screens."</li>
                    </>
                  ) : selectedTopic.chapter.includes('Electric') ? (
                    <>
                      <li>"Current gets consumed by the first bulb, so downstream bulbs receive less."</li>
                      <li>"Batteries supply a fixed, constant current regardless of circuit resistance."</li>
                    </>
                  ) : (
                    <>
                      <li>"Heavier objects fall faster because Earth attracts them with greater force."</li>
                      <li>"An object at the top of its trajectory has zero acceleration."</li>
                    </>
                  )}
                </ul>
              </div>
            </div>
          </div>

          <div className="pt-4 border-t border-border flex items-center justify-between">
            <span className="text-xs text-slate-500 font-mono">
              Quiz length: 3 sequential questions • Explanations supported
            </span>

            <button
              onClick={handleStartQuiz}
              className="px-5 py-2.5 rounded text-sm font-semibold bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm flex items-center space-x-2 transition-all hover:translate-x-0.5"
            >
              <span>Begin Diagnostic Quiz</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* PHASE 3: TAKING ORDERED QUIZ (Questions in Sequence)                      */}
      {/* ========================================================================= */}
      {currentPhase === 'taking_quiz' && currentQ && (
        <div className="editorial-card p-6 sm:p-8 bg-white border border-border space-y-6">
          {/* Progress Header */}
          <div className="flex items-center justify-between border-b border-border pb-4">
            <div className="flex items-center space-x-3">
              <span className="text-xs font-mono font-bold px-2.5 py-1 rounded bg-slate-100 text-slate-800 border border-slate-200">
                Question {currentQuestionIndex + 1} of {activeQuestions.length}
              </span>
              <span className="text-xs font-mono text-slate-500">
                Session ID: QUIZ-{selectedTopic.chapter.slice(0, 4).toUpperCase()}
              </span>
            </div>

            {/* Stepper Dots */}
            <div className="flex items-center space-x-1.5">
              {activeQuestions.map((_, idx) => (
                <div
                  key={idx}
                  className={`w-2.5 h-2.5 rounded-full transition-all ${
                    idx === currentQuestionIndex
                      ? 'bg-indigo-600 scale-125'
                      : idx < currentQuestionIndex
                      ? 'bg-emerald-500'
                      : 'bg-slate-200'
                  }`}
                />
              ))}
            </div>
          </div>

          {/* Question Stem & Context */}
          <div className="space-y-4">
            <div className="flex items-center space-x-2">
              <span className="text-[11px] font-mono uppercase px-2 py-0.5 rounded bg-indigo-50 text-indigo-700 border border-indigo-200">
                {currentQ.question_type ? currentQ.question_type.replace('_', ' ') : 'Conceptual Inquiry'}
              </span>
              <span className="text-xs text-slate-500 font-mono">
                {currentQ.topic || selectedTopic.chapter}
              </span>
            </div>

            <h3 className="text-base sm:text-lg font-semibold text-charcoal leading-snug">
              {currentQ.stem}
            </h3>

            {/* Visual Diagram Context if present */}
            {currentQ.diagram_metadata?.has_diagram && (
              <div className="p-3 bg-slate-50 border border-slate-200 rounded text-xs text-slate-700 flex items-center space-x-2">
                <span className="font-semibold text-indigo-700 font-mono">[Diagram Context]:</span>
                <span>{currentQ.diagram_metadata.description}</span>
              </div>
            )}
          </div>

          {/* Multimodal Physics Workspace (5 Modalities: Theory, Numerical, Handwritten OCR, Diagram, MCQ) */}
          <MultimodalInputWorkspace
            currentQuestion={currentQ}
            selectedTopic={selectedTopic}
            studentResponseText={studentResponseText}
            setStudentResponseText={setStudentResponseText}
            selectedOptionKey={selectedOptionKey}
            setSelectedOptionKey={setSelectedOptionKey}
            onQuickPreset={handleQuickPreset}
          />

          {/* Navigation Action */}
          <div className="pt-4 border-t border-border flex items-center justify-between">
            <span className="text-xs text-slate-500 font-mono">
              Attempt {currentQuestionIndex + 1} of 3
            </span>

            <button
              onClick={handleSubmitQuestionAttempt}
              disabled={!studentResponseText.trim() && !selectedOptionKey}
              className="px-5 py-2 rounded text-sm font-semibold bg-charcoal hover:bg-slate-800 text-white disabled:opacity-40 flex items-center space-x-1.5 transition-all"
            >
              <span>{currentQuestionIndex + 1 < activeQuestions.length ? 'Submit & Next Question' : 'Complete Quiz & Run Diagnosis'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* PHASE 4: DIAGNOSIS & LONGITUDINAL PATTERN RESULTS (Step 3 & 4 of Docs)    */}
      {/* ========================================================================= */}
      {currentPhase === 'diagnosis_results' && (
        <div className="space-y-6">
          {/* Header Summary */}
          <div className="editorial-card p-6 bg-white border border-border space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-border pb-4">
              <div>
                <span className="text-xs font-mono uppercase tracking-wider text-indigo-700">
                  Diagnosis Complete
                </span>
                <h2 className="text-xl font-bold text-charcoal mt-0.5">
                  Cognitive Analysis & Misconception Report
                </h2>
                <p className="text-xs text-slate-500 mt-1">
                  Re:Learn evaluated each answer individually (Model A) and analyzed longitudinal patterns across your entire session (Model B).
                </p>
              </div>

              <button
                onClick={() => setCurrentPhase('multimodal_intervention')}
                className="px-5 py-2 rounded text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm flex items-center space-x-1.5 self-start sm:self-auto"
              >
                <span>Begin Targeted Intervention</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>

            {/* Model B Longitudinal Sequence Pattern Alert */}
            {sequencePatternResult && (
              <div className="p-4 rounded-lg bg-indigo-50/70 border border-indigo-200 text-slate-800 space-y-2">
                <div className="flex items-center space-x-2">
                  <span className="text-[11px] font-mono uppercase font-bold bg-indigo-600 text-white px-2 py-0.5 rounded">
                    Model B Sequence Pattern Tracker
                  </span>
                  <span className="text-xs font-semibold text-indigo-900">
                    {sequencePatternResult.pattern_detected?.replace(/_/g, ' ')}
                  </span>
                  <span className="text-xs font-mono text-indigo-700">
                    (Confidence: {Math.round(sequencePatternResult.confidence * 100)}%)
                  </span>
                </div>

                <p className="text-xs text-slate-700 leading-relaxed">
                  <strong>Diagnostic Evidence Across Questions:</strong>{' '}
                  {sequencePatternResult.evidence_summary?.join(' • ') || 'Consistent cognitive model observed across sequential attempts.'}
                </p>

                <div className="text-[11px] font-mono text-indigo-800 pt-1">
                  <strong>Prescribed Action:</strong> {sequencePatternResult.recommended_action?.replace(/_/g, ' ')}
                </div>
              </div>
            )}

            {/* Per-Question Model A Diagnostic Cards */}
            <div className="space-y-3 pt-2">
              <h4 className="text-xs font-bold font-mono uppercase text-slate-600">
                Individual Response Diagnoses (Model A - DeBERTa-v3):
              </h4>

              {orderedAttempts.map((att, idx) => {
                const diag = quizDiagnoses[idx];
                const isMisc = diag?.category === 'misconception';
                const isCorrect = diag?.category === 'correct';
                const isSlip = diag?.category === 'calc_slip';
                const isUnsure = diag?.category === 'unsure';

                return (
                  <div
                    key={idx}
                    className={`p-4 rounded border text-xs space-y-2 transition-all ${
                      isMisc
                        ? 'border-rose-200 bg-rose-50/40'
                        : isCorrect
                        ? 'border-emerald-200 bg-emerald-50/40'
                        : isSlip
                        ? 'border-amber-200 bg-amber-50/40'
                        : 'border-slate-200 bg-slate-50'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-slate-700">
                        Question {idx + 1}: {att.question_stem.slice(0, 75)}...
                      </span>
                      <span className="font-mono text-[11px] px-2 py-0.5 rounded bg-white border border-slate-200">
                        Confidence: {diag ? Math.round(diag.confidence * 100) : 85}%
                      </span>
                    </div>

                    <p className="text-slate-600 italic bg-white/70 p-2 rounded border border-slate-100">
                      "{att.student_response}"
                    </p>

                    <div className="flex items-center space-x-2 pt-1">
                      <span className="font-semibold text-slate-700 font-mono">Diagnosis:</span>
                      <span className={`font-semibold ${isMisc ? 'text-rose-700' : isCorrect ? 'text-emerald-700' : 'text-amber-700'}`}>
                        {diag?.label || 'Analyzing...'}
                      </span>
                    </div>

                    {diag?.evidence_rationale && (
                      <p className="text-slate-600 text-[11px] leading-relaxed">
                        <strong>Pedagogical Reason:</strong> {diag.evidence_rationale}
                      </p>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* PHASE 5: TARGETED MULTIMODAL INTERVENTION (Part 4 of Documentation)       */}
      {/* ========================================================================= */}
      {currentPhase === 'multimodal_intervention' && (
        <div className="space-y-6">
          {/* Header */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between border-b border-border pb-3 gap-2">
            <div>
              <span className="text-xs font-mono uppercase text-indigo-700 font-semibold tracking-wider">
                Phase 4 — Targeted Multimodal Remediation
              </span>
              <h2 className="text-xl font-bold text-charcoal mt-0.5">
                Cognitive Reconstruction & Concept Whiteboard
              </h2>
              <p className="text-xs text-slate-500 mt-1">
                Targeted multimodal instruction addressing diagnosed misconception: <span className="font-mono font-medium text-slate-700">{interventionData?.target_misconception_id || 'Active Topic'}</span>
              </p>
            </div>

            <div className="flex items-center space-x-2 text-xs font-mono text-indigo-700 bg-indigo-50 border border-indigo-200 px-3 py-1.5 rounded self-start sm:self-auto">
              <span className="w-2 h-2 rounded-full bg-indigo-600"></span>
              <span>Dynamic AI Whiteboard DSL</span>
            </div>
          </div>

          {/* 1. 3D AI Teacher Avatar (Speech Synthesis + Lip Sync) */}
          <TeacherAvatar
            textToSpeak={
              interventionData?.poe_sequence?.explain?.text ||
              "Notice what actually happens when we cover half of the lens. The full image of the candle is still formed on the screen! Each uncovered point on the lens receives light from all parts of the candle. Only the total brightness decreases by fifty percent."
            }
          />

          {/* 2. Structured AI Whiteboard (Light Mode) */}
          <WhiteboardCanvas
            commands={interventionData?.whiteboard_commands || []}
            plan={interventionData?.dynamic_whiteboard_plan}
            miscId={interventionData?.target_misconception_id || 'MISC-OPT-001'}
            title="Interactive Visual Whiteboard Proof"
          />

          {/* 3. Interactive Physics Mini-Simulation */}
          <InteractiveSimWidget
            simType={
              selectedTopic?.chapter?.toLowerCase().includes('optic')
                ? 'optics'
                : selectedTopic?.chapter?.toLowerCase().includes('electric')
                ? 'electricity'
                : 'mechanics'
            }
          />

          {/* 4. Predict-Observe-Explain (POE) 4-Step Card */}
          {interventionData?.poe_sequence && (
            <div className="editorial-card p-5 bg-white border border-border space-y-4">
              <h4 className="text-xs font-bold font-mono uppercase text-slate-700 flex items-center space-x-2">
                <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
                <span>Predict-Observe-Explain (POE) Cognitive Reconciler</span>
              </h4>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div className="p-3 rounded bg-amber-50/70 border border-amber-200">
                  <span className="font-bold text-amber-900 block mb-1">1. Naive Prediction:</span>
                  <p className="text-amber-800">{interventionData.poe_sequence.predict?.prompt || 'You predicted that half the image would be missing.'}</p>
                </div>

                <div className="p-3 rounded bg-blue-50/70 border border-blue-200">
                  <span className="font-bold text-blue-900 block mb-1">2. Physical Observation:</span>
                  <p className="text-blue-800">{interventionData.poe_sequence.observe?.observation || 'The complete image remains, with 50% reduced illumination.'}</p>
                </div>

                <div className="p-3 rounded bg-emerald-50/70 border border-emerald-200">
                  <span className="font-bold text-emerald-900 block mb-1">3. Scientific Explanation:</span>
                  <p className="text-emerald-800">{interventionData.poe_sequence.explain?.text || 'Rays from every part of the candle pass through the open aperture.'}</p>
                </div>

                <div className="p-3 rounded bg-indigo-50/70 border border-indigo-200">
                  <span className="font-bold text-indigo-900 block mb-1">4. Near-Transfer Law:</span>
                  <p className="text-indigo-800">{interventionData.poe_sequence.generalize?.transfer_principle || 'Aperture area controls light energy, not image geometry.'}</p>
                </div>
              </div>
            </div>
          )}

          {/* Bottom Action */}
          <div className="p-4 bg-slate-50 border border-slate-200 rounded flex items-center justify-between">
            <span className="text-xs text-slate-600 font-sans">
              Have you understood the physical principle? Test your near-transfer understanding.
            </span>

            <button
              onClick={() => setCurrentPhase('isomorphic_reassessment')}
              className="px-5 py-2 rounded text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 text-white flex items-center space-x-1.5"
            >
              <span>Take Reassessment Question →</span>
            </button>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* PHASE 6: ISOMORPHIC REASSESSMENT (Requirement 5 of Problem Statement)     */}
      {/* ========================================================================= */}
      {currentPhase === 'isomorphic_reassessment' && reassessmentPair && (
        <div className="editorial-card p-6 sm:p-8 bg-white border border-border space-y-6">
          <div className="border-b border-border pb-4">
            <span className="text-xs font-mono uppercase text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
              Isomorphic Near-Transfer Reassessment
            </span>
            <h2 className="text-lg font-bold text-charcoal mt-1">
              Verify Mastery in an Unfamiliar Setup
            </h2>
            <p className="text-xs text-slate-500 mt-1">
              A correct follow-up answer alone does not prove learning. This isomorphic question tests whether you can transfer the concept to a new numerical and visual context without relying on memorization.
            </p>
          </div>

          {/* Reassessment Question Stem */}
          <div className="space-y-3">
            <h3 className="text-base font-semibold text-charcoal leading-snug">
              {reassessmentPair.reassessment_item.stem}
            </h3>

            {/* Options */}
            <div className="space-y-2 pt-2">
              {reassessmentPair.reassessment_item.options.map((opt) => (
                <button
                  key={opt.key}
                  type="button"
                  onClick={() => setReassessmentAnswerKey(opt.key)}
                  className={`w-full text-left p-3.5 rounded border text-xs sm:text-sm transition-all flex items-start space-x-3 ${
                    reassessmentAnswerKey === opt.key
                      ? 'border-indigo-600 bg-indigo-50/60 text-slate-900 font-medium ring-1 ring-indigo-600'
                      : 'border-slate-200 bg-white hover:bg-slate-50 text-slate-700'
                  }`}
                >
                  <span className="font-mono font-bold w-5 h-5 rounded-full bg-slate-100 flex items-center justify-center text-xs flex-shrink-0 mt-0.5">
                    {opt.key}
                  </span>
                  <span>{opt.text}</span>
                </button>
              ))}
            </div>
          </div>

          <div className="pt-4 border-t border-border flex items-center justify-between">
            <span className="text-xs text-slate-500 font-mono">
              Transfer Assessment • Bayesian Knowledge Tracing
            </span>

            <button
              onClick={handleEvaluateReassessment}
              disabled={!reassessmentAnswerKey || isEvaluatingReassessment}
              className="px-5 py-2.5 rounded text-xs font-semibold bg-emerald-600 hover:bg-emerald-700 text-white disabled:opacity-40 flex items-center space-x-1.5"
            >
              <span>{isEvaluatingReassessment ? 'Evaluating BKT Transfer...' : 'Submit Reassessment Answer'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* PHASE 7: MASTERY SUMMARY & BKT PROGRESS (Requirement 6 of Problem State)  */}
      {/* ========================================================================= */}
      {currentPhase === 'mastery_summary' && reassessmentEvalResult && (
        <div className="editorial-card p-6 sm:p-8 bg-white border border-border space-y-6">
          <div className="text-center max-w-lg mx-auto space-y-3">
            <div className="w-14 h-14 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center mx-auto text-2xl shadow-inner">
              <Award className="w-8 h-8 text-emerald-600" />
            </div>

            <h2 className="text-2xl font-bold text-charcoal">
              {reassessmentEvalResult.is_correct ? 'Cognitive Misconception Resolved!' : 'Further Practice Recommended'}
            </h2>

            <p className="text-xs text-slate-600 leading-relaxed">
              {reassessmentEvalResult.is_correct
                ? 'You successfully transferred the scientific principle to the new physical setup. The naive model was replaced with genuine understanding.'
                : 'The reassessment reveals that the intuitive fallacy may still be partially active. We have recorded this in your learner profile.'}
            </p>
          </div>

          {/* Bayesian Knowledge Tracing Metric Card */}
          <div className="p-5 rounded-lg bg-slate-50 border border-slate-200 space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-xs font-mono font-bold uppercase text-slate-700">
                Bayesian Knowledge Tracing (BKT) State Update:
              </span>
              <span className="text-xs font-mono font-bold text-emerald-700">
                Resolution: {reassessmentEvalResult.resolution_status}
              </span>
            </div>

            {/* Progress Bar */}
            <div>
              <div className="flex justify-between text-xs text-slate-600 mb-1">
                <span>Prior Mastery: {Math.round((reassessmentEvalResult.prior_mastery || 0.20) * 100)}%</span>
                <span className="font-bold text-indigo-700">Updated Mastery: {Math.round(reassessmentEvalResult.updated_mastery * 100)}%</span>
              </div>
              <div className="w-full h-3 bg-slate-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-emerald-500 transition-all duration-1000"
                  style={{ width: `${Math.round(reassessmentEvalResult.updated_mastery * 100)}%` }}
                />
              </div>
            </div>

            <p className="text-xs text-slate-600 leading-normal border-t border-slate-200 pt-3">
              <strong>Pedagogical Feedback:</strong> {reassessmentEvalResult.explanation}
            </p>
          </div>

          {/* Actions */}
          <div className="pt-4 border-t border-border flex flex-col sm:flex-row items-center justify-between gap-3">
            <button
              onClick={() => setCurrentPhase('select_topic')}
              className="w-full sm:w-auto px-5 py-2.5 rounded text-xs font-semibold bg-charcoal hover:bg-slate-800 text-white"
            >
              Explore Next Chapter / Topic →
            </button>

            <button
              onClick={() => {
                setCurrentQuestionIndex(0);
                setCurrentPhase('taking_quiz');
              }}
              className="w-full sm:w-auto px-4 py-2 rounded text-xs font-medium border border-border bg-white hover:bg-slate-100 text-slate-700 flex items-center justify-center space-x-1"
            >
              <RotateCcw className="w-3.5 h-3.5 text-slate-500" />
              <span>Retry Diagnostic Quiz</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
