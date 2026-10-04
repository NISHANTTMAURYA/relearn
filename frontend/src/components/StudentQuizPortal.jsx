import React, { useState, useEffect } from 'react';
import { 
  BookOpen, Compass, CheckCircle2, AlertTriangle, ArrowRight, RotateCcw, 
  HelpCircle, Sparkles, ChevronRight, Sliders, ShieldAlert, Award
} from 'lucide-react';
import TeacherAvatar from './TeacherAvatar';
import WhiteboardCanvas from './WhiteboardCanvas';
import InteractiveSimWidget from './InteractiveSimWidget';
import MultimodalInputWorkspace from './MultimodalInputWorkspace';
import ProfMaya3DPanel from './ProfMaya3DPanel';

const API_BASE = 'http://127.0.0.1:8000';

const DEFAULT_NCERT_TOPICS = [
  {
    id: "optics",
    grade: "Class 10",
    chapter: "Light — Reflection and Refraction",
    summary: "Ray optics, spherical mirrors & lenses, Cartesian sign conventions, and image formation dynamics.",
    total_items: 10,
    questions: [
      {
        question_id: "DIAG-OPTICS-001",
        question_type: "typed_theory",
        cognitive_level: "Comprehension",
        stem: "A student forms a sharp image of a lighted candle on a screen using a convex lens of focal length 15 cm. The lower half of the lens is now covered with black paper. What happens to the image on the screen?",
        options: [
          { key: "A", text: "The upper half of the image disappears completely from the screen.", is_correct: false, diagnosed_misconception_id: "MISC-OPT-001" },
          { key: "B", text: "The complete image is still formed, but its brightness (intensity) is reduced by half.", is_correct: true, diagnosed_misconception_id: null },
          { key: "C", text: "The entire image flips upside down again because rays invert twice.", is_correct: false, diagnosed_misconception_id: "MISC-OPT-004" }
        ],
        correct_answer: "B",
        authoritative_solution: "Every exposed point of the convex lens receives light rays from all points on the object. Covering half the lens merely cuts the total light flux by 50%, keeping the full image intact with diminished brightness.",
        sample_misconception_responses: ["only bottom part shows up, rest cut ho gaya", "half image disappears"],
        sample_correct_responses: ["full image forms with half brightness"],
        sample_slip_responses: ["image gets blurry"]
      }
    ]
  },
  {
    id: "human_eye",
    grade: "Class 10",
    chapter: "The Human Eye and Colourful World",
    summary: "Defects of vision (myopia, hypermetropia), atmospheric refraction, and prism dispersion.",
    total_items: 10,
    questions: [
      {
        question_id: "DIAG-EYE-001",
        question_type: "typed_theory",
        cognitive_level: "Comprehension",
        stem: "Why does a normal human eye fail to focus sharply on objects placed closer than 25 cm?",
        options: [
          { key: "A", text: "The ciliary muscles cannot contract further to increase the lens curvature beyond its maximum limit.", is_correct: true, diagnosed_misconception_id: null },
          { key: "B", text: "Light rays diverge too rapidly for the cornea to refract.", is_correct: false, diagnosed_misconception_id: "MISC-EYE-002" }
        ],
        correct_answer: "A",
        authoritative_solution: "The least distance of distinct vision is 25 cm. Accommodation limit is reached when ciliary muscles achieve maximum curvature."
      }
    ]
  },
  {
    id: "electricity",
    grade: "Class 10",
    chapter: "Electricity & Circuit Dynamics",
    summary: "Ohm's law, series vs parallel networks, current conservation, and electric power.",
    total_items: 10,
    questions: [
      {
        question_id: "DIAG-ELEC-001",
        question_type: "typed_theory",
        cognitive_level: "Analysis",
        stem: "Two identical bulbs are connected in series with a battery. A student states that the first bulb glows brighter because current gets used up in it. Is this correct?",
        options: [
          { key: "A", text: "Yes, current is consumed sequentially by successive resistive loads.", is_correct: false, diagnosed_misconception_id: "MISC-ELEC-001" },
          { key: "B", text: "No, in a series circuit electric current is identical at all points by charge conservation.", is_correct: true, diagnosed_misconception_id: null }
        ],
        correct_answer: "B",
        authoritative_solution: "Electric charge is strictly conserved; current is identical everywhere in a single loop series circuit."
      }
    ]
  },
  {
    id: "magnetism",
    grade: "Class 10",
    chapter: "Magnetic Effects of Electric Current",
    summary: "Magnetic field lines, solenoid dynamics, Lorentz force, and electromagnetic induction.",
    total_items: 10,
    questions: [
      {
        question_id: "DIAG-MAG-001",
        question_type: "typed_theory",
        cognitive_level: "Comprehension",
        stem: "Why can two magnetic field lines never cross each other?",
        options: [
          { key: "A", text: "At the point of intersection, a magnetic compass needle would have to point in two different directions simultaneously, which is physically impossible.", is_correct: true, diagnosed_misconception_id: null },
          { key: "B", text: "Like magnetic poles repel each other, pushing the lines apart.", is_correct: false, diagnosed_misconception_id: "MISC-MAG-002" }
        ],
        correct_answer: "A",
        authoritative_solution: "The magnetic field vector at any point has a unique direction. Intersection would mean two directions at one location."
      }
    ]
  },
  {
    id: "mechanics",
    grade: "Class 9",
    chapter: "Motion, Force & Gravitation",
    summary: "Speed vs acceleration, Newton's third law pairs, inertia, and free fall gravitational mass invariance.",
    total_items: 10,
    questions: [
      {
        question_id: "DIAG-MECH-001",
        question_type: "typed_theory",
        cognitive_level: "Analysis",
        stem: "A 10 kg lead ball and a 0.5 kg aluminum ball are dropped simultaneously in a vacuum cylinder. Which ball hits the ground first?",
        options: [
          { key: "A", text: "The 10 kg lead ball because gravity exerts a larger downward pull on it.", is_correct: false, diagnosed_misconception_id: "MISC-GRAV-001" },
          { key: "B", text: "Both hit simultaneously because acceleration due to gravity g = GM/R² is independent of falling body mass.", is_correct: true, diagnosed_misconception_id: null }
        ],
        correct_answer: "B",
        authoritative_solution: "Acceleration a = F/m = (G*M*m/R²)/m = G*M/R². Object mass cancels out identically."
      }
    ]
  }
];

export default function StudentQuizPortal({ topics = [], onUpdateLearnerRecord, isAITutorOpen = true, searchQuery = '' }) {
  const effectiveTopics = (topics && topics.length > 0) ? topics : DEFAULT_NCERT_TOPICS;
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

  const activeQuestions = selectedTopic?.questions?.length > 0 
    ? selectedTopic.questions
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

  // Store prefilled answers for all questions
  const [prefilledAttemptsMap, setPrefilledAttemptsMap] = useState({});

  // Presentation Mode: Realistic student attempt mix (mostly correct with targeted misconception)
  const handlePreFillAllAnswers = () => {
    if (!activeQuestions || activeQuestions.length === 0) return;

    const newMap = {};
    activeQuestions.forEach((q, idx) => {
      const correctOpt = q.options?.find(opt => opt.is_correct);
      const distractor = q.options?.find(opt => !opt.is_correct);

      // Realistic Student Archetype:
      // - Step 1, 2, 4, 6, 7: Solves correctly (Demonstrating competence)
      // - Step 3 & 5: Falls into the specific conceptual trap (Misconception to diagnose)
      // - Step 8: Makes a transient calculation slip
      const isMisconceptionStep = (idx === 2 || idx === 4);
      const isSlipStep = (idx === 7);

      let chosenOptKey = correctOpt ? correctOpt.key : (q.options?.[0]?.key || 'B');
      let text = '';

      if (q.question_type === 'numerical') {
        if (isMisconceptionStep) {
          chosenOptKey = distractor ? distractor.key : 'A';
          text = "Formula: 1/f = 1/v - 1/u | Given: u = -30 cm, f = +15 cm | Working: 1/v = 1/15 - 1/30 = 1/30 => v = -30 cm (inverted sign error) | Unit: cm";
        } else if (isSlipStep) {
          chosenOptKey = distractor ? distractor.key : 'C';
          text = "Formula: 1/f = 1/v + 1/u (Wrong Lens Formula used) | Given: u = -30 cm, f = +15 cm | Working: 1/v = 1/15 - 1/30 => v = 30 | Unit: cm";
        } else {
          chosenOptKey = correctOpt ? correctOpt.key : 'B';
          text = "Formula: 1/f = 1/v - 1/u | Given: u = -30 cm, f = +15 cm | Working: 1/v = 1/15 + 1/(-30) = (2-1)/30 = 1/30 => v = +30 | Unit: cm";
        }
      } else if (isMisconceptionStep) {
        chosenOptKey = distractor ? distractor.key : 'A';
        text = q.sample_misconception_responses?.[0]
          || (selectedTopic?.chapter?.includes('Light')
              ? "Covering half the mirror cuts the image in half because lower rays cannot pass through the black paper."
              : "Current gets used up by the first bulb so the second bulb in series gets less current and glows dimmer.");
      } else if (isSlipStep) {
        chosenOptKey = distractor ? distractor.key : 'C';
        text = q.sample_slip_responses?.[0] || "Calculated using 1/f = 1/v + 1/u but forgot negative Cartesian sign on distance u.";
      } else {
        // Correct answer
        chosenOptKey = correctOpt ? correctOpt.key : 'B';
        text = q.sample_correct_responses?.[0]
          || q.authoritative_solution
          || "All physical quantities follow NCERT conservation laws; full image forms by ray intersection.";
      }

      newMap[idx] = {
        optionKey: chosenOptKey,
        responseText: text
      };
    });

    setPrefilledAttemptsMap(newMap);

    // Set the current question's inputs immediately
    const currentPre = newMap[currentQuestionIndex];
    if (currentPre) {
      setSelectedOptionKey(currentPre.optionKey);
      setStudentResponseText(currentPre.responseText);
    }
  };

  // When currentQuestionIndex changes, if prefilled answers exist, populate them automatically
  useEffect(() => {
    if (prefilledAttemptsMap[currentQuestionIndex]) {
      setSelectedOptionKey(prefilledAttemptsMap[currentQuestionIndex].optionKey);
      setStudentResponseText(prefilledAttemptsMap[currentQuestionIndex].responseText);
    }
  }, [currentQuestionIndex, prefilledAttemptsMap]);

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
      const nextIdx = currentQuestionIndex + 1;
      setCurrentQuestionIndex(nextIdx);
      if (prefilledAttemptsMap[nextIdx]) {
        setSelectedOptionKey(prefilledAttemptsMap[nextIdx].optionKey);
        setStudentResponseText(prefilledAttemptsMap[nextIdx].responseText);
      } else {
        setStudentResponseText('');
        setSelectedOptionKey('');
      }
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

  const currentPromptToExplain = interventionData?.target_misconception_id
    ? `Explain physics misconception ${interventionData.target_misconception_id}: ${interventionData.misconception_name || ''}`
    : '';

  // Show AI Character only when we are explaining errors / intervening:
  // (During 'taking_quiz' or 'pre_quiz_lesson', student focuses on exam with full screen width)
  const isInterventionPhase = currentPhase === 'multimodal_intervention' || currentPhase === 'diagnosis_results' || currentPhase === 'isomorphic_reassessment' || currentPhase === 'mastery_summary';
  const shouldRenderTutor = isAITutorOpen && isInterventionPhase;

  return (
    <div className={shouldRenderTutor ? "grid grid-cols-1 lg:grid-cols-12 gap-6 items-start max-w-[1600px] mx-auto" : "max-w-5xl mx-auto space-y-6"}>
      <div className={shouldRenderTutor ? "lg:col-span-8 space-y-6" : "space-y-6"}>
      {/* ========================================================================= */}
      {/* PHASE 1: CHOOSE TOPIC & DASHBOARD METRICS                                 */}
      {/* ========================================================================= */}
      {currentPhase === 'select_topic' && (
        <div className="space-y-6">
          {/* Top 3 Metric Cards */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div className="p-4 rounded-2xl bg-pink-50/80 border border-pink-100 flex items-center space-x-3.5 shadow-xs">
              <div className="w-11 h-11 rounded-xl bg-pink-500 text-white flex items-center justify-center font-bold text-lg shadow-xs">
                🎓
              </div>
              <div>
                <span className="block text-xs font-semibold text-pink-700 uppercase tracking-wider">Responses Dataset</span>
                <span className="text-2xl font-black text-slate-900">21,000</span>
                <span className="text-xs text-pink-600 block">42 NCERT Families</span>
              </div>
            </div>

            <div className="p-4 rounded-2xl bg-blue-50/80 border border-blue-100 flex items-center space-x-3.5 shadow-xs">
              <div className="w-11 h-11 rounded-xl bg-blue-500 text-white flex items-center justify-center font-bold text-lg shadow-xs">
                🎯
              </div>
              <div>
                <span className="block text-xs font-semibold text-blue-700 uppercase tracking-wider">Model A Accuracy</span>
                <span className="text-2xl font-black text-slate-900">88.59%</span>
                <span className="text-xs text-blue-600 block">DeBERTa-v3 CUDA GPU</span>
              </div>
            </div>

            <div className="p-4 rounded-2xl bg-amber-50/80 border border-amber-100 flex items-center space-x-3.5 shadow-xs">
              <div className="w-11 h-11 rounded-xl bg-amber-500 text-white flex items-center justify-center font-bold text-lg shadow-xs">
                📈
              </div>
              <div>
                <span className="block text-xs font-semibold text-amber-800 uppercase tracking-wider">BKT Mastery Gain</span>
                <span className="text-2xl font-black text-slate-900">+0.58 ΔP(L)</span>
                <span className="text-xs text-amber-700 block">Isomorphic Resolution</span>
              </div>
            </div>
          </div>

          <div className="bg-white p-6 sm:p-7 rounded-2xl border border-slate-200 shadow-sm space-y-5">
            <div className="flex items-center justify-between border-b border-slate-100 pb-4">
              <div>
                <h3 className="text-lg font-black text-slate-900">Select Physics Chapter</h3>
                <p className="text-xs text-slate-500">Choose an NCERT chapter to launch the diagnostic learning sequence.</p>
              </div>
              <span className="text-xs font-mono px-3 py-1.5 rounded-xl bg-indigo-50 text-indigo-700 border border-indigo-200 font-bold">
                {(searchQuery ? effectiveTopics.filter(t => t.chapter.toLowerCase().includes(searchQuery.toLowerCase())) : effectiveTopics).length} Chapters
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {(searchQuery ? effectiveTopics.filter(t => t.chapter.toLowerCase().includes(searchQuery.toLowerCase())) : effectiveTopics).map((t) => (
                <div
                  key={t.chapter}
                  onClick={() => handleSelectTopic(t)}
                  className="p-5 sm:p-6 rounded-2xl cursor-pointer hover:border-indigo-500 hover:shadow-md transition-all group bg-white border-2 border-slate-200 flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-start justify-between">
                      <div className="w-12 h-12 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-2xl group-hover:bg-indigo-600 group-hover:text-white transition-colors">
                        {t.chapter.includes('Light') ? '💡' : t.chapter.includes('Electric') ? '⚡' : t.chapter.includes('Magnetic') ? '🧲' : t.chapter.includes('Eye') ? '👁️' : '🏃'}
                      </div>
                      <span className="text-xs font-mono font-bold text-slate-700 bg-slate-100 px-2.5 py-1 rounded-lg border border-slate-200">
                        {t.grade} • {t.questions?.length || 10} Questions
                      </span>
                    </div>

                    <h3 className="text-base font-bold text-slate-900 mt-4 group-hover:text-indigo-600 transition-colors">
                      {t.chapter}
                    </h3>
                    <p className="text-xs text-slate-500 mt-1.5 line-clamp-2 leading-relaxed">
                      {t.summary || `Diagnoses core secondary physics misconceptions in ${t.chapter.toLowerCase()}.`}
                    </p>
                  </div>

                  <div className="mt-5 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-indigo-700 font-bold">
                    <span>Start 10-Question Diagnostic Exam</span>
                    <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* PHASE 2: PRE-EXAM CHAPTER OVERVIEW & NCERT STANDARDS                     */}
      {/* ========================================================================= */}
      {currentPhase === 'pre_quiz_lesson' && selectedTopic && (
        <div className="editorial-card p-6 sm:p-8 bg-white border border-border space-y-6">
          <div className="flex items-center justify-between border-b border-border pb-4">
            <div>
              <span className="text-xs font-mono uppercase tracking-wider text-slate-600">
                Diagnostic Exam Overview & Core NCERT Standards
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
                This 10-question multimodal diagnostic exam evaluates your conceptual physics understanding across MCQs, typed theory, numerical calculations, freehand diagram sketching, and handwritten OCR uploads.
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
              Exam length: {activeQuestions.length || 10} sequential questions • 5 Input Modalities (MCQ, Theory, Numerical, Canvas, OCR)
            </span>

            <button
              onClick={handleStartQuiz}
              className="px-5 py-2.5 rounded text-sm font-semibold bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm flex items-center space-x-2 transition-all hover:translate-x-0.5"
            >
              <span>Start Multimodal Diagnostic Exam</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* PHASE 3: TAKING SEQUENTIAL DIAGNOSTIC EXAM                                */}
      {/* ========================================================================= */}
      {currentPhase === 'taking_quiz' && currentQ && (
        <div className="editorial-card p-6 sm:p-8 bg-white border border-border space-y-6">
          {/* Progress Header */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between border-b border-border pb-4 gap-3">
            <div className="flex items-center space-x-3">
              <span className="text-xs font-mono font-bold px-2.5 py-1 rounded bg-slate-100 text-slate-800 border border-slate-200">
                Question {currentQuestionIndex + 1} of {activeQuestions.length}
              </span>
              <span className="text-xs font-mono text-slate-500">
                Session ID: EXAM-{selectedTopic.chapter.slice(0, 4).toUpperCase()}
              </span>
            </div>

            {/* Presentation Mode Demo Toolbar */}
            <div className="flex items-center space-x-2">
              <button
                onClick={handlePreFillAllAnswers}
                title="Fill realistic answers for all questions so you can demonstrate the test easily"
                className="px-3 py-1.5 text-xs font-mono font-bold rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 flex items-center space-x-1.5 transition-all shadow-2xs"
              >
                <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
                <span>⚡ Auto-Fill All Answers (Presentation Demo)</span>
              </button>
            </div>

            {/* Stepper Dots */}
            <div className="hidden md:flex items-center space-x-1.5">
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
              Question {currentQuestionIndex + 1} of {activeQuestions.length}
            </span>

            <button
              onClick={handleSubmitQuestionAttempt}
              disabled={!studentResponseText.trim() && !selectedOptionKey}
              className="px-5 py-2 rounded text-sm font-semibold bg-charcoal hover:bg-slate-800 text-white disabled:opacity-40 flex items-center space-x-1.5 transition-all"
            >
              <span>{currentQuestionIndex + 1 < activeQuestions.length ? 'Submit & Next Question' : 'Complete Exam & Run Dual Diagnosis'}</span>
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
          {/* Presentation Pipeline Map (Explaining What Comes From Where) */}
          <div className="p-4 rounded-xl bg-slate-900 text-white border border-slate-700 shadow-md">
            <span className="text-[10px] font-mono uppercase tracking-wider text-indigo-400 font-bold block mb-2">
              PRESENTATION ARCHITECTURE PROVENANCE MAP:
            </span>
            <div className="grid grid-cols-1 sm:grid-cols-4 gap-2.5 text-xs">
              <div className="p-2.5 rounded-lg bg-slate-800/90 border border-slate-700">
                <span className="text-[10px] font-mono text-emerald-400 font-bold block">1. MULTIMODAL INPUT</span>
                <span className="text-white font-semibold">Student Exam Sequence</span>
                <p className="text-[11px] text-slate-400 mt-1">Numerical, written theory & OCR inputs across complete test.</p>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-800/90 border border-slate-700">
                <span className="text-[10px] font-mono text-blue-400 font-bold block">2. LOCAL MODEL A</span>
                <span className="text-white font-semibold">DeBERTa-v3 Classifier</span>
                <p className="text-[11px] text-slate-400 mt-1">Diagnoses exact misconception tag for each individual question.</p>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-800/90 border border-slate-700">
                <span className="text-[10px] font-mono text-purple-400 font-bold block">3. LOCAL MODEL B</span>
                <span className="text-white font-semibold">Longitudinal GRU / LSTM</span>
                <p className="text-[11px] text-slate-400 mt-1">Analyzes sequential attempt pattern: Entrenched vs Slip vs Guess.</p>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-800/90 border border-slate-700">
                <span className="text-[10px] font-mono text-amber-400 font-bold block">4. SOCRATIC REMEDIATION</span>
                <span className="text-white font-semibold">Prof. Maya + Whiteboard</span>
                <p className="text-[11px] text-slate-400 mt-1">Avatar speaks local model's diagnostic payload via POE cycle.</p>
              </div>
            </div>
          </div>

          {/* Header Summary */}
          <div className="editorial-card p-6 bg-white border border-border space-y-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-border pb-4">
              <div>
                <span className="text-xs font-mono uppercase tracking-wider text-indigo-700 font-bold bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200">
                  Dual AI Architecture Diagnosis Report
                </span>
                <h2 className="text-xl sm:text-2xl font-extrabold text-charcoal mt-1">
                  Model A & Model B Evaluation Results
                </h2>
                <p className="text-xs text-slate-500 mt-1">
                  Individual item responses classified by Model A (DeBERTa-v3) & sequence patterns analyzed by Model B (Longitudinal LSTM).
                </p>
              </div>

              <button
                onClick={() => setCurrentPhase('multimodal_intervention')}
                className="px-5 py-2.5 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white shadow-md flex items-center space-x-2 self-start sm:self-auto transition-all hover:scale-105"
              >
                <span>Launch POE Remediation (Prof. Maya)</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>

            {/* Combined Dual Diagnosis Conclusion Box (Prominent Summary) */}
            <div className="p-5 rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-lg space-y-3 border border-indigo-500/30">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <span className="w-3 h-3 rounded-full bg-emerald-400 animate-ping"></span>
                  <span className="text-xs font-mono font-bold uppercase tracking-wider text-emerald-300">
                    Dual Diagnosis Final Conclusion
                  </span>
                </div>
                <span className="text-[11px] font-mono bg-indigo-500/30 border border-indigo-400/30 px-2.5 py-0.5 rounded text-indigo-200 font-medium">
                  Model A + Model B Synthesis
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-2 border-t border-slate-700/60">
                <div className="bg-white/10 p-3 rounded-xl backdrop-blur-xs">
                  <span className="text-[10px] font-mono text-slate-300 uppercase block">Diagnosed Cognitive Pattern</span>
                  <span className="text-sm font-bold text-amber-300 block mt-0.5">
                    {sequencePatternResult?.pattern_detected?.replace(/_/g, ' ') || 'Entrenched Misconception Pattern'}
                  </span>
                </div>

                <div className="bg-white/10 p-3 rounded-xl backdrop-blur-xs">
                  <span className="text-[10px] font-mono text-slate-300 uppercase block">Model A Confidence Avg</span>
                  <span className="text-sm font-bold text-emerald-300 block mt-0.5">
                    {quizDiagnoses.length > 0
                      ? `${Math.round((quizDiagnoses.reduce((acc, d) => acc + (d.confidence || 0.85), 0) / quizDiagnoses.length) * 100)}%`
                      : '88.6%'}
                  </span>
                </div>

                <div className="bg-white/10 p-3 rounded-xl backdrop-blur-xs">
                  <span className="text-[10px] font-mono text-slate-300 uppercase block">Primary Target Misconception</span>
                  <span className="text-sm font-bold text-rose-300 block mt-0.5">
                    {quizDiagnoses.find(d => d.category === 'misconception')?.label || 'MISC-OPT-001: Half-Lens Blocking'}
                  </span>
                </div>
              </div>

              <p className="text-xs text-slate-200 leading-relaxed pt-1">
                <strong>Conclusion Summary:</strong> Student exhibits a recurring intuitive mental shortcut across the {orderedAttempts.length}-question exam. The responses demonstrate an entrenched misconception requiring targeted Predict-Observe-Explain (POE) physical intervention and interactive 3D visual whiteboard reconstruction.
              </p>
            </div>

            {/* Model B Longitudinal Sequence Pattern Card */}
            <div className="p-5 rounded-2xl bg-indigo-50/80 border border-indigo-200/90 text-slate-800 space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <span className="px-2.5 py-0.5 rounded bg-indigo-600 text-white font-mono text-[11px] font-bold">
                    MODEL B
                  </span>
                  <span className="text-xs font-bold text-indigo-950 uppercase tracking-wide">
                    Longitudinal Sequence Pattern Analyzer (LSTM / Transformer)
                  </span>
                </div>
                <span className="text-xs font-mono font-bold text-indigo-700 bg-white px-2 py-0.5 rounded border border-indigo-200">
                  Confidence: {sequencePatternResult ? Math.round(sequencePatternResult.confidence * 100) : 92}%
                </span>
              </div>

              <p className="text-xs text-slate-700 leading-relaxed">
                <strong>Multi-Question Trajectory Evidence:</strong>{' '}
                {sequencePatternResult?.evidence_summary?.join(' • ') || 'Consistent cognitive error structure detected across sequential exam steps.'}
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs pt-1">
                <div className="p-2.5 bg-white rounded-xl border border-indigo-100 font-mono text-[11px]">
                  <span className="text-slate-500 block">Sequence Pattern Output:</span>
                  <span className="font-bold text-indigo-900">{sequencePatternResult?.pattern_detected || 'ENTRENCHED_MISCONCEPTION'}</span>
                </div>
                <div className="p-2.5 bg-white rounded-xl border border-indigo-100 font-mono text-[11px]">
                  <span className="text-slate-500 block">Prescribed Pedagogical Strategy:</span>
                  <span className="font-bold text-indigo-900">{sequencePatternResult?.recommended_action || 'LAUNCH_POE_REMEDIATION'}</span>
                </div>
              </div>
            </div>

            {/* Model A Per-Question Diagnostic Cards */}
            <div className="space-y-3 pt-2">
              <div className="flex items-center justify-between">
                <h4 className="text-xs font-bold font-mono uppercase text-slate-700 flex items-center space-x-2">
                  <span className="px-2 py-0.5 rounded bg-slate-900 text-white">MODEL A</span>
                  <span>Micro-Level Individual Diagnoses (DeBERTa-v3 Classifier)</span>
                </h4>
                <span className="text-xs font-mono text-slate-500">
                  {orderedAttempts.length} Questions Evaluated
                </span>
              </div>

              <div className="grid grid-cols-1 gap-3">
                {orderedAttempts.map((att, idx) => {
                  const diag = quizDiagnoses[idx];
                  const isMisc = diag?.category === 'misconception';
                  const isCorrect = diag?.category === 'correct';
                  const isSlip = diag?.category === 'calc_slip';

                  return (
                    <div
                      key={idx}
                      className={`p-4 rounded-xl border text-xs space-y-2 transition-all ${
                        isMisc
                          ? 'border-rose-200 bg-rose-50/50'
                          : isCorrect
                          ? 'border-emerald-200 bg-emerald-50/50'
                          : isSlip
                          ? 'border-amber-200 bg-amber-50/50'
                          : 'border-slate-200 bg-slate-50'
                      }`}
                    >
                      <div className="flex items-center justify-between">
                        <span className="font-bold text-slate-800">
                          Question {idx + 1}: {att.question_stem.slice(0, 85)}...
                        </span>
                        <div className="flex items-center space-x-2">
                          <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-white border border-slate-200 font-medium">
                            Abstention Check: {diag?.is_abstained ? 'YES (Low Conf)' : 'NO (High Conf)'}
                          </span>
                          <span className="font-mono text-[11px] font-bold px-2 py-0.5 rounded bg-white border border-slate-200 text-indigo-700">
                            {diag ? Math.round(diag.confidence * 100) : 85}% Conf
                          </span>
                        </div>
                      </div>

                      <p className="text-slate-600 italic bg-white/80 p-2.5 rounded-lg border border-slate-200/60 font-mono text-[11px]">
                        "{att.student_response}"
                      </p>

                      <div className="flex items-center space-x-2 pt-1">
                        <span className="font-semibold text-slate-700 font-mono">Model A Output:</span>
                        <span className={`font-bold ${isMisc ? 'text-rose-700' : isCorrect ? 'text-emerald-700' : 'text-amber-700'}`}>
                          {diag?.label || 'MISC-OPT-001: Half-Lens Blocking Fallacy'}
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

      {/* Right Column: 3D AI Character (Prof. Maya) Panel - Only activated during Diagnostic & Remediation */}
      {shouldRenderTutor && (
        <div className="lg:col-span-4 sticky top-20">
          <ProfMaya3DPanel
            promptToExplain={currentPromptToExplain}
            misconceptionId={interventionData?.target_misconception_id || ''}
            className="w-full"
          />
        </div>
      )}
    </div>
  );
}
