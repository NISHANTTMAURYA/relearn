import React, { useState, useEffect, useRef } from 'react';
import {
  Brain, Database, BarChart2, Sparkles, ChevronRight,
  CheckCircle, XCircle, ArrowRight, ArrowDown, BookOpen, Zap, Target,
  Activity, Users, Shield, Cpu, Award, TrendingUp, AlertTriangle,
  Monitor, PenLine, FlaskConical, Home, HelpCircle, FileText, Layers, Eye,
  RefreshCw, GitCommit, Split
} from 'lucide-react';
import {
  LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer, ReferenceLine, RadarChart,
  PolarGrid, PolarAngleAxis, Radar, Cell
} from 'recharts';

// ── Palette ──────────────────────────────────────────────────────────────────
const C = {
  indigo: { bg: 'bg-indigo-50', text: 'text-indigo-700', border: 'border-indigo-200', badge: 'bg-indigo-100 text-indigo-700', dot: 'bg-indigo-500', hex: '#4F46E5' },
  violet: { bg: 'bg-violet-50', text: 'text-violet-700', border: 'border-violet-200', badge: 'bg-violet-100 text-violet-700', dot: 'bg-violet-500', hex: '#7C3AED' },
  emerald:{ bg: 'bg-emerald-50', text: 'text-emerald-700', border: 'border-emerald-200', badge: 'bg-emerald-100 text-emerald-700', dot: 'bg-emerald-500', hex: '#059669' },
  amber:  { bg: 'bg-amber-50', text: 'text-amber-700', border: 'border-amber-200', badge: 'bg-amber-100 text-amber-700', dot: 'bg-amber-500', hex: '#D97706' },
  rose:   { bg: 'bg-rose-50', text: 'text-rose-700', border: 'border-rose-200', badge: 'bg-rose-100 text-rose-700', dot: 'bg-rose-500', hex: '#E11D48' },
  pink:   { bg: 'bg-pink-50', text: 'text-pink-700', border: 'border-pink-200', badge: 'bg-pink-100 text-pink-700', dot: 'bg-pink-500', hex: '#EC4899' },
  slate:  { bg: 'bg-slate-50', text: 'text-slate-700', border: 'border-slate-200', badge: 'bg-slate-100 text-slate-700', dot: 'bg-slate-500', hex: '#64748B' },
};

// ── Data ─────────────────────────────────────────────────────────────────────
const benchmarkData = [
  { iter: 'Iter 1', records: 2500, testAcc: 100, oodAcc: 0, macroF1: 1.0, status: 'fail' },
  { iter: 'Iter 2', records: 8400, testAcc: 74.34, oodAcc: 73.41, macroF1: 70.94, status: 'partial' },
  { iter: 'Iter 3', records: 12600, testAcc: 87.37, oodAcc: 90.48, macroF1: 83.78, status: 'pass' },
  { iter: 'Iter 4', records: 16800, testAcc: 88.59, oodAcc: 88.89, macroF1: 86.78, status: 'pass' },
  { iter: 'Iter 5', records: 21000, testAcc: 85.00, oodAcc: 85.32, macroF1: 82.82, status: 'pass' },
];

const datasetGrowth = [
  { iter: 'Iter 1', records: 2500, families: 25 },
  { iter: 'Iter 2', records: 8400, families: 42 },
  { iter: 'Iter 3', records: 12600, families: 42 },
  { iter: 'Iter 4', records: 16800, families: 42 },
  { iter: 'Iter 5', records: 21000, families: 42 },
];

const radarData = [
  { metric: 'Test Accuracy', value: 88.59 },
  { metric: 'OOD Accuracy', value: 90.48 },
  { metric: 'Macro F1', value: 86.78 },
  { metric: 'Abstention Cal.', value: 98.8 },
  { metric: 'Seq. Pattern', value: 100 },
  { metric: 'Differentiation', value: 95.8 },
];

// Interactive Hero Prompts demonstrating genuine student reasoning
const HERO_EXAMPLES = [
  {
    id: 'optics-standard',
    category: 'Ray Optics (Standard)',
    query: 'If top half of a convex lens is covered with black paper, only the bottom half of the image will form on the screen.',
    badge: 'MISC-OPT-001 · Stencil Model',
    conf: '99.7%',
    topic: 'Ray Optics · NCERT Class 10',
    questionAsked: 'What happens to the image formed by a convex lens when its top half is covered with black paper?',
    studentMindset: 'The student views the lens like an opaque window shutter, believing covering half the glass blocks half of the image.',
    scientificTruth: 'Every point on the lens gathers light from every point on the object. The complete image is still formed—it simply has half the brightness (light intensity).',
    color: 'indigo'
  },
  {
    id: 'optics-vernacular',
    category: 'CBSE Vernacular (Hinglish)',
    query: 'bro only bottom part shows up, rest cut ho gaya',
    badge: 'MISC-OPT-001 · Vernacular Parsing',
    conf: '99.7%',
    topic: 'Ray Optics · Colloquial Shorthand',
    questionAsked: 'Classroom answer in Hinglish: "Bro only bottom part shows up, rest got cut off!"',
    studentMindset: 'Expresses the same geometric stencil misconception using conversational student slang ("rest cut ho gaya").',
    scientificTruth: 'Re:Learn’s DeBERTa model parses informal Hinglish without penalty, correctly isolating the root physics misunderstanding.',
    color: 'violet'
  },
  {
    id: 'electricity',
    category: 'Current Electricity',
    query: 'Current is used up in the first bulb, so the second bulb in series receives less electricity and glows dimmer.',
    badge: 'MISC-ELEC-001 · Fuel Attenuation',
    conf: '97.2%',
    topic: 'Electricity · Series Circuits',
    questionAsked: 'Why do two identical bulbs connected in series have the same brightness?',
    studentMindset: 'Models electric current as consumable fuel that diminishes sequentially after passing through each resistor.',
    scientificTruth: 'Conservation of charge dictates that electric current is identical at all points in a single-loop series circuit.',
    color: 'amber'
  },
  {
    id: 'kinematics-slip',
    category: 'Kinematics (Slip vs Flaw)',
    query: 'Distance = 100 m, time = 5 s. Speed = 100 × 5 = 500 m/s.',
    badge: 'CARELESS_CALCULATION_ERROR · Slip',
    conf: '98.4%',
    topic: 'Motion · Formula Application',
    questionAsked: 'Calculate the speed of an object covering 100 m in 5 seconds.',
    studentMindset: 'The student understands speed links distance and time, but multiplied instead of dividing.',
    scientificTruth: 'The system differentiates arithmetic slips from deep conceptual flaws, avoiding unnecessary conceptual lectures.',
    color: 'emerald'
  }
];

const personas = [
  { name: 'Standard Concept', example: '"If top half of lens is covered, only bottom half shows"', label: 'MISC-OPT-001' },
  { name: 'CBSE Vernacular', example: '"bro only bottom part shows up, rest cut ho gaya"', label: 'MISC-OPT-001' },
  { name: 'WhatsApp Shorthand', example: '"idk mybe crrnt used up in 1st bulb"', label: 'MISC-ELEC-001' },
  { name: 'Terse Formula-First', example: '"v²=u²+2as → a=0 so v=u always"', label: 'MISC-MOT-001' },
  { name: 'Calculation Slip', example: '"100×5 = 500 m/s, speed = 500"', label: 'CARELESS_CALCULATION_ERROR' },
  { name: 'Abstention', example: '"idk forgot formula"', label: 'UNSURE_INSUFFICIENT_EVIDENCE' },
];

// PDF Page 10 Flow Steps
const PIPELINE_STEPS = [
  {
    step: '1',
    title: 'Student Answers Quiz',
    model: 'Quiz Engine / LMS',
    color: 'indigo',
    desc: 'Collects student MCQ, typed text, numerical steps, or uploaded diagram photo.',
    simpleWords: 'The student answers in their own natural way—not just guessing A, B, C, or D.'
  },
  {
    step: '2',
    title: 'Multimodal Preprocessing',
    model: 'PaddleOCR + Vision Parser',
    color: 'violet',
    desc: 'Extracts handwriting, equations, circuit schematics, and ray vectors into structured features.',
    simpleWords: 'Reads handwritten scribbles and sketches into clear digital text and numbers for the AI.'
  },
  {
    step: '3',
    title: 'Model 1: Individual Diagnosis',
    model: 'DeBERTa-v3 Text Classifier',
    color: 'blue',
    desc: 'Predicts which of 46 misconception classes or slips explains the student’s specific response.',
    simpleWords: 'Finds the exact reason WHY the answer was wrong (e.g., treating a lens like a window).'
  },
  {
    step: '4',
    title: 'Model 2: Sequence Pattern Analysis',
    model: 'GRU Sequence Model',
    color: 'emerald',
    desc: 'Inspects ordered answers across the quiz to uncover persistent vs. transient error patterns.',
    simpleWords: 'Looks across multiple questions to see if the student is repeating the same mistake.'
  },
  {
    step: '5',
    title: 'Combine Diagnoses & Confidence Gate',
    model: 'Synthesis Rules + Abstention',
    color: 'amber',
    desc: 'Combines individual & sequence evidence. If uncertain, asks a targeted follow-up question.',
    simpleWords: 'If the AI is unsure, it admits it and asks a quick check question instead of guessing.'
  },
  {
    step: '6',
    title: 'Generate Targeted Remediation',
    model: 'POE + Prof. Maya (Gemini Flash)',
    color: 'rose',
    desc: 'Predict-Observe-Explain cycle with 3D WebGL avatar, SVG whiteboard, and PhET simulation.',
    simpleWords: 'Gives a friendly interactive explanation that directly disproves the student’s wrong theory.'
  },
  {
    step: '7',
    title: 'Isomorphic Reassessment',
    model: 'Question Bank Engine',
    color: 'pink',
    desc: 'Presents a fresh near-transfer question with different numbers to verify genuine mastery.',
    simpleWords: 'Asks a brand new question on the same idea to prove the student truly understands now.'
  },
  {
    step: '8',
    title: 'Track Learner Mastery',
    model: 'Bayesian Knowledge Tracing (BKT)',
    color: 'teal',
    desc: 'Updates probability of mastery P(L), storing resolved vs. unresolved misconceptions.',
    simpleWords: 'Updates the student’s mastery score so future lessons know what they have mastered.'
  }
];

// PDF Page 1-2 & Page 10: System Architecture Table
const ARCHITECTURE_TABLE = [
  {
    part: 'Model 1: Multimodal Response Diagnosis',
    role: 'Main diagnosis model predicting root misconceptions from student answers & evidence',
    tech: 'Fine-tuned DeBERTa-v3-small + PaddleOCR image extractor',
    output: 'Misconception Class (46 classes) + Confidence % + Evidence Rationale',
    simpleWords: 'Finds the exact mental error in a single typed answer or handwritten calculation.'
  },
  {
    part: 'Model 2: Sequence Pattern Analysis',
    role: 'Tracks ordered question history to find repeated or connected misconceptions',
    tech: 'GRU (Gated Recurrent Unit) neural network + Trajectory Rules',
    output: 'Sequence Pattern Archetype (45 classes) + Persistence Score',
    simpleWords: 'Watches how the student answers across several questions to detect recurring habits.'
  },
  {
    part: 'Intervention Engine: Predict-Observe-Explain',
    role: 'Delivers personalized multimodal remediation confronting the diagnosed error',
    tech: 'Gemini 1.5 Flash (NCERT RAG prompt) + 3D WebGL Avatar Prof. Maya',
    output: 'POE Interactive Card + Bilingual Audio (EN/HI) + SVG Diagram',
    simpleWords: 'Shows the student an interactive experiment that clearly proves why their intuition was wrong.'
  },
  {
    part: 'Reassessment Engine: Near-Transfer Check',
    role: 'Selects an isomorphic new question for the same concept to test understanding',
    tech: 'Curated NCERT Question Bank + Context Variation Logic',
    output: 'Isomorphic Test Item + Transfer Difficulty Level',
    simpleWords: 'Gives a new question with different numbers so the student can’t just recite the answer.'
  },
  {
    part: 'Learner Record & Mastery Tracking',
    role: 'Updates conceptual mastery and logs persistent vs. resolved misconceptions',
    tech: 'Bayesian Knowledge Tracing (BKT) Engine with Slip & Guess params',
    output: 'Updated Mastery P(L), Retention Probability, Diagnostic History',
    simpleWords: 'A live report card showing which physics concepts are mastered and which need practice.'
  }
];

// PDF Page 2 & Page 7: Multimodal Input Matrix
const INPUT_MATRIX_TABLE = [
  {
    type: 'Typed Theory / Explanation',
    input: 'Free-text reasoning in plain English or vernacular slang',
    pipeline: 'Direct DeBERTa-v3 NLP classification with confidence gating',
    simpleWords: 'The student types how they think in normal words. The AI detects the hidden misconception.'
  },
  {
    type: 'Selected MCQ Option',
    input: 'Question identifier + selected choice letter',
    pipeline: 'Option mapped to candidate misconceptions (partial evidence signal)',
    simpleWords: 'Picking an option gives a hint, but the AI asks for working before claiming 100% certainty.'
  },
  {
    type: 'Numerical Calculation',
    input: 'Final numerical value + formula substitution steps',
    pipeline: 'Deterministic math/unit parser + concept diagnosis',
    simpleWords: 'Separates simple math calculation slips from fundamental misunderstanding of physics formulas.'
  },
  {
    type: 'Photo of Handwritten Working',
    input: 'Snapshot of written formulas, scratchpad steps, or exam paper',
    pipeline: 'PaddleOCR extracts symbols, equations, and steps into text',
    simpleWords: 'Students can take a picture of their notebook; the AI reads the steps and finds where they slipped.'
  },
  {
    type: 'Physics Diagram / Ray Sketch',
    input: 'Student-drawn ray diagram, circuit schematic, or force vector',
    pipeline: 'Vision-Language parser extracts component labels, directions, and axes',
    simpleWords: 'The student draws arrows or lenses; the AI checks if light rays or forces point the right way.'
  }
];

// PDF Page 11: Detection vs Differentiation
const DIFFERENTIATION_EXAMPLES = [
  {
    task: 'Detection (Stage 1)',
    question: 'Determine IF the student made an error and whether it is a concept flaw or arithmetic slip.',
    example: 'Student writes "100 × 5 = 500 m/s" for speed = distance / time.',
    result: 'CARELESS_CALCULATION_ERROR (Slip detected · no conceptual misconception intervention required)',
    simpleWords: 'Like a teacher checking: "Did they understand the physics but make a quick calculation mistake?"'
  },
  {
    task: 'Differentiation (Stage 2)',
    question: 'Distinguish BETWEEN two completely different wrong mental models that both lead to the same wrong answer.',
    example: 'Question: "Covering top half of convex lens." Student A says "only bottom half forms". Student B says "inverted image flips upside down again".',
    result: 'Differentiates MISC-OPT-001 (Stencil window model) from MISC-OPT-004 (Flipping inversion model).',
    simpleWords: 'Two students can give the same wrong answer for totally different reasons. The AI figures out each student’s unique logic.'
  }
];

const layers = [
  { num: '01', title: 'Student UI', sub: 'React + Vite :5173', icon: Monitor, color: 'indigo', desc: 'Topic selection, free-text answer input, 5-step diagnostic flow, BKT progress.' },
  { num: '02', title: 'API / Session', sub: 'FastAPI :8000', icon: Zap, color: 'violet', desc: 'REST endpoints: diagnose, sequence-pattern, intervention, reassessment, analytics.' },
  { num: '03', title: 'Content Store', sub: 'JSON / CSV', icon: Database, color: 'blue', desc: '42 curriculum families, 21 misconceptions, 16 diagnostic items, POE catalogues.' },
  { num: '04', title: 'Diagnosis Service', sub: 'DeBERTa-v3 + GRU', icon: Brain, color: 'emerald', desc: 'Model A: 46-class individual classifier. Model B: 45 trajectory archetypes.' },
  { num: '05', title: 'Intervention', sub: 'POE + Gemini Flash', icon: Target, color: 'amber', desc: 'Predict-Observe-Explain remediation + Prof. Maya bilingual LLM explanations.' },
  { num: '06', title: 'Reassessment', sub: 'BKT Engine', icon: TrendingUp, color: 'rose', desc: 'Isomorphic near-transfer questions + Bayesian Knowledge Tracing mastery update.' },
  { num: '07', title: 'Presentation', sub: '3D Avatar + PhET', icon: Sparkles, color: 'pink', desc: 'Three.js WebGL avatar Prof. Maya, structured SVG whiteboard, PhET simulations.' },
];

const features = [
  { icon: FlaskConical, title: '5-Step Diagnostic Studio', color: 'indigo', desc: 'Topic → Input → Dual Diagnosis → POE Remediation → Reassessment loop.' },
  { icon: Brain, title: 'DeBERTa-v3 Classifier', color: 'violet', desc: '88.59% test, 90.48% OOD peak. 46 classes, confidence gating, abstention.' },
  { icon: Activity, title: 'Sequence Pattern Analyser', color: 'emerald', desc: 'GRU model, 45 trajectory archetypes, 100% sequence pattern accuracy.' },
  { icon: Sparkles, title: '3D AI Mentor Prof. Maya', color: 'amber', desc: 'Three.js WebGL avatar, lip-sync, bilingual Gemini 1.5 Flash reasoning.' },
  { icon: PenLine, title: 'Structured SVG Whiteboard', color: 'rose', desc: 'Ray diagrams, circuit schematics, force vectors via drawing commands.' },
  { icon: Monitor, title: 'PhET Simulations', color: 'pink', desc: 'Embedded UC Boulder interactive Physics simulations for hands-on exploration.' },
  { icon: BookOpen, title: 'Taxonomy Browser', color: 'slate', desc: '21 codified NCERT misconceptions with naive models, ground truths, disambiguation.' },
  { icon: Award, title: 'BKT Mastery Tracking', color: 'indigo', desc: 'Per-concept Bayesian Knowledge Tracing updated on every reassessment.' },
];

// ── Utility Components ────────────────────────────────────────────────────────
function useInView() {
  const ref = useRef(null);
  const [inView, setInView] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(([e]) => { if (e.isIntersecting) { setInView(true); obs.disconnect(); } }, { threshold: 0.1 });
    obs.observe(el);
    return () => obs.disconnect();
  }, []);
  return [ref, inView];
}

function Fade({ children, className = '' }) {
  const [ref, v] = useInView();
  return <div ref={ref} className={`transition-all duration-700 ${v ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-6'} ${className}`}>{children}</div>;
}

function Tag({ children }) {
  return (
    <span className="inline-flex items-center gap-1.5 text-[11px] font-mono font-semibold uppercase tracking-widest text-indigo-600 bg-indigo-50 border border-indigo-200 px-3 py-1 rounded-full mb-4">
      <span className="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse" />{children}
    </span>
  );
}

// Animated Flow Arrow SVG Component
function FlowArrow({ direction = 'right', className = '' }) {
  if (direction === 'down') {
    return (
      <div className={`flex flex-col items-center justify-center my-1.5 ${className}`}>
        <svg className="w-5 h-8 text-indigo-500 overflow-visible" viewBox="0 0 20 32" fill="none">
          <path d="M10 0 L10 26" stroke="currentColor" strokeWidth="2.5" className="animate-arrow-flow" strokeLinecap="round" />
          <path d="M5 21 L10 28 L15 21" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </div>
    );
  }
  return (
    <div className={`hidden lg:flex items-center justify-center mx-1 flex-shrink-0 ${className}`}>
      <svg className="w-7 h-5 text-indigo-500 overflow-visible" viewBox="0 0 28 20" fill="none">
        <path d="M0 10 L22 10" stroke="currentColor" strokeWidth="2.5" className="animate-arrow-flow" strokeLinecap="round" />
        <path d="M17 5 L24 10 L17 15" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </div>
  );
}

const CustomTooltip = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-white border border-slate-200 rounded-xl shadow-lg p-3 text-xs font-mono">
        <p className="font-bold text-slate-800 mb-1">{label}</p>
        {payload.map(p => (
          <p key={p.name} style={{ color: p.color }}>{p.name}: <strong>{typeof p.value === 'number' ? p.value.toFixed(2) : p.value}</strong></p>
        ))}
      </div>
    );
  }
  return null;
};

// ── Hero Section ─────────────────────────────────────────────────────────────
function HeroSection({ onEnterApp }) {
  const [selectedExample, setSelectedExample] = useState(HERO_EXAMPLES[0]);

  return (
    <section className="relative overflow-hidden w-full min-h-[calc(100vh-64px)] flex items-center bg-gradient-to-b from-[#F0F2FD] via-[#F6F8FE] to-white py-12 lg:py-16">
      {/* Background subtle dots */}
      <div
        className="absolute inset-0 pointer-events-none opacity-30"
        style={{
          backgroundImage: 'radial-gradient(circle, #818cf8 1.2px, transparent 1.2px)',
          backgroundSize: '32px 32px'
        }}
      />

      <div className="relative max-w-[1550px] w-full mx-auto px-6 sm:px-10 lg:px-16">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
          
          {/* Left Column (7 cols) */}
          <div className="lg:col-span-7 flex flex-col justify-center">
            <div className="mb-5">
              <span className="inline-flex items-center space-x-2 text-xs font-mono font-semibold uppercase tracking-wider text-indigo-700 bg-indigo-100/70 border border-indigo-200/80 px-3.5 py-1.5 rounded-full shadow-sm">
                <span className="w-2 h-2 rounded-full bg-indigo-600 animate-pulse" />
                <span>NCERT Physics Class 9 & 10 · AI Diagnostic System</span>
              </span>
            </div>

            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-slate-900 leading-[1.08] mb-5">
              AI That Finds<br />
              What You<br />
              <span className="text-indigo-600">Don't Know</span>
            </h1>

            <p className="text-base sm:text-lg text-slate-600 mb-6 max-w-2xl leading-relaxed font-normal">
              Re:Learn diagnoses the exact conceptual misconception behind every wrong Physics answer — delivering targeted multimodal remediation and tracking mastery with Bayesian Knowledge Tracing.
            </p>

            {/* Interactive Example Selector Tabs */}
            <div className="mb-3">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-mono font-bold text-slate-500 uppercase tracking-wider">
                  Select A Student Response Scenario:
                </span>
                <span className="text-[11px] font-mono text-indigo-600 font-medium">Click to test diagnosis</span>
              </div>
              <div className="flex flex-wrap gap-2">
                {HERO_EXAMPLES.map((ex) => {
                  const isActive = selectedExample.id === ex.id;
                  return (
                    <button
                      key={ex.id}
                      onClick={() => setSelectedExample(ex)}
                      className={`text-xs font-mono font-semibold px-3 py-1.5 rounded-lg border transition-all ${
                        isActive
                          ? 'bg-indigo-600 text-white border-indigo-600 shadow-sm'
                          : 'bg-white text-slate-600 border-slate-200 hover:border-indigo-300 hover:bg-indigo-50/50'
                      }`}
                    >
                      {ex.category}
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Interactive Search-style Input Bar */}
            <div className="flex flex-col sm:flex-row items-stretch sm:items-center bg-white border-2 border-indigo-200 rounded-2xl p-2 shadow-lg shadow-indigo-100/60 max-w-2xl mb-4 transition-all focus-within:border-indigo-500">
              <div className="flex-1 px-3 py-2 text-sm sm:text-base text-slate-800 font-mono flex items-center space-x-2.5">
                <span className="text-indigo-600 font-bold text-lg">›</span>
                <span className="truncate select-all text-slate-900 font-medium">
                  "{selectedExample.query}"
                </span>
              </div>
              <button
                onClick={onEnterApp}
                className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm px-6 py-3 rounded-xl shadow-md transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5 flex items-center justify-center space-x-2 whitespace-nowrap"
              >
                <span>Diagnose Now</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>

            {/* In Plain Words Explainer Card for Selected Example */}
            <div className="bg-white/95 border border-indigo-100 rounded-2xl p-4 shadow-sm max-w-2xl mb-8">
              <div className="flex items-center justify-between border-b border-slate-100 pb-2 mb-2.5">
                <div className="flex items-center space-x-2">
                  <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                  <span className="text-xs font-mono font-bold text-slate-700 uppercase">
                    Diagnosed: <span className="text-indigo-600">{selectedExample.badge}</span>
                  </span>
                </div>
                <span className="text-xs font-mono font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                  Confidence: {selectedExample.conf}
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div className="bg-slate-50 rounded-xl p-3 border border-slate-200/60">
                  <div className="text-[11px] font-bold font-mono text-rose-600 uppercase mb-1">
                    Student's Wrong Mental Model
                  </div>
                  <p className="text-slate-600 leading-relaxed font-normal">
                    {selectedExample.studentMindset}
                  </p>
                </div>
                <div className="bg-emerald-50/60 rounded-xl p-3 border border-emerald-200/60">
                  <div className="text-[11px] font-bold font-mono text-emerald-700 uppercase mb-1">
                    In Simple Words (Scientific Truth)
                  </div>
                  <p className="text-slate-700 leading-relaxed font-normal">
                    {selectedExample.scientificTruth}
                  </p>
                </div>
              </div>
            </div>

            {/* Stats Row */}
            <div className="flex flex-wrap items-center gap-6 sm:gap-10 pt-4 border-t border-slate-200/70">
              <div>
                <div className="text-3xl lg:text-4xl font-black text-slate-900 leading-tight">21,000</div>
                <div className="text-xs font-mono text-slate-500 uppercase tracking-wider mt-0.5">Responses Trained</div>
              </div>
              <div className="w-px h-10 bg-slate-200 hidden sm:block" />
              <div>
                <div className="text-3xl lg:text-4xl font-black text-slate-900 leading-tight">42</div>
                <div className="text-xs font-mono text-slate-500 uppercase tracking-wider mt-0.5">Curriculum Families</div>
              </div>
              <div className="w-px h-10 bg-slate-200 hidden sm:block" />
              <div>
                <div className="text-3xl lg:text-4xl font-black text-indigo-600 leading-tight">88.59%</div>
                <div className="text-xs font-mono text-slate-500 uppercase tracking-wider mt-0.5">Test Accuracy</div>
              </div>
            </div>
          </div>

          {/* Right Column (5 cols) — Character Illustration & Explanatory Callouts with Animated Flow Arrows */}
          <div className="lg:col-span-5 relative flex items-center justify-center pt-8 pb-4">
            <div className="absolute w-80 h-80 sm:w-96 sm:h-96 rounded-full bg-indigo-200/40 blur-3xl -z-10" />

            <div className="relative w-full max-w-lg flex flex-col items-center">
              
              {/* Isolated Character Illustration */}
              <div className="relative flex items-center justify-center w-full">
                <img
                  src="/student_illustration.png"
                  alt="Student learning physics with Re:Learn"
                  className="w-full max-w-[420px] h-auto object-contain drop-shadow-xl select-none"
                  onError={(e) => {
                    e.target.src = '/landing_hero.jpg';
                  }}
                />

                {/* Callout 1: Top-Left pointing to Student typing with animated dashed arrow */}
                <div className="absolute -top-6 -left-4 sm:-left-8 max-w-[210px] bg-white/95 backdrop-blur-md border border-indigo-200 shadow-xl rounded-2xl p-3 z-20">
                  <div className="flex items-center space-x-1.5 mb-1">
                    <span className="w-2 h-2 rounded-full bg-indigo-600"></span>
                    <span className="text-[11px] font-bold text-indigo-900 uppercase font-mono">1. Student Input</span>
                  </div>
                  <p className="text-xs text-slate-600 leading-snug font-medium">
                    Enters physics reasoning in plain English or Hinglish slang
                  </p>
                  <svg className="absolute -bottom-4 right-4 w-7 h-7 text-indigo-500 overflow-visible" viewBox="0 0 28 28" fill="none">
                    <path d="M4 2 C 14 2, 22 10, 22 22" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" className="animate-arrow-flow" />
                    <path d="M17 18 L 22 23 L 26 17" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                </div>

                {/* Callout 2: Top-Right pointing to AI Diagnosis with animated dashed arrow */}
                <div className="absolute -top-4 -right-2 sm:-right-8 max-w-[210px] bg-white/95 backdrop-blur-md border border-emerald-200 shadow-xl rounded-2xl p-3 z-20">
                  <div className="flex items-center space-x-1.5 mb-1">
                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span className="text-[11px] font-bold text-emerald-900 uppercase font-mono">2. Model Diagnosis</span>
                  </div>
                  <p className="text-xs text-slate-600 leading-snug font-medium">
                    DeBERTa-v3 classifies the exact misconception, not just right or wrong
                  </p>
                  <svg className="absolute -bottom-4 left-4 w-7 h-7 text-emerald-500 overflow-visible" viewBox="0 0 28 28" fill="none">
                    <path d="M24 2 C 14 2, 6 10, 6 22" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" className="animate-arrow-flow" />
                    <path d="M11 18 L 6 23 L 2 17" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                </div>

                {/* Callout 3: Bottom-Left pointing to Pattern Tracking */}
                <div className="absolute -bottom-6 -left-4 sm:-left-8 max-w-[210px] bg-white/95 backdrop-blur-md border border-amber-200 shadow-xl rounded-2xl p-3 z-20">
                  <div className="flex items-center space-x-1.5 mb-1">
                    <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                    <span className="text-[11px] font-bold text-amber-900 uppercase font-mono">3. Pattern Tracking</span>
                  </div>
                  <p className="text-xs text-slate-600 leading-snug font-medium">
                    Model B detects persistent flaws vs. transient calculation slips
                  </p>
                  <svg className="absolute -top-4 right-4 w-7 h-7 text-amber-500 overflow-visible" viewBox="0 0 28 28" fill="none">
                    <path d="M4 26 C 14 26, 22 18, 22 6" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" className="animate-arrow-flow" />
                    <path d="M17 10 L 22 5 L 26 11" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                </div>

                {/* Callout 4: Bottom-Right pointing to Remediation & Reassessment */}
                <div className="absolute -bottom-6 -right-2 sm:-right-8 max-w-[210px] bg-white/95 backdrop-blur-md border border-violet-200 shadow-xl rounded-2xl p-3 z-20">
                  <div className="flex items-center space-x-1.5 mb-1">
                    <span className="w-2 h-2 rounded-full bg-violet-500"></span>
                    <span className="text-[11px] font-bold text-violet-900 uppercase font-mono">4. Multimodal Remediation</span>
                  </div>
                  <p className="text-xs text-slate-600 leading-snug font-medium">
                    Predict-Observe-Explain with 3D Mentor, Whiteboard &amp; BKT test
                  </p>
                  <svg className="absolute -top-4 left-4 w-7 h-7 text-violet-500 overflow-visible" viewBox="0 0 28 28" fill="none">
                    <path d="M24 26 C 14 26, 6 18, 6 6" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" className="animate-arrow-flow" />
                    <path d="M11 10 L 6 5 L 2 11" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                </div>

              </div>

            </div>
          </div>

        </div>
      </div>
    </section>
  );
}

// ── SECTION 01: End-to-End Component Flow (Direct from PDF Page 10) ───────────
function EndToEndFlowSection() {
  const [activeStep, setActiveStep] = useState(0);

  return (
    <section id="flow" className="py-20 bg-slate-50 border-y border-slate-200">
      <div className="max-w-[1550px] mx-auto px-6 lg:px-12">
        <Fade className="mb-12">
          <Tag>01 — End-to-End Component Flow</Tag>
          <h2 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-3">
            How The 8 Components Connect — <span className="text-indigo-600">In Simple Words</span>
          </h2>
          <p className="text-slate-600 max-w-2xl text-base leading-relaxed">
            Follows the exact 8-step pipeline specified on <strong>Page 10 of the Technical Project Documentation</strong>. Animated arrows indicate real-time signal flow from student input to mastery tracking.
          </p>
        </Fade>

        {/* Desktop 8-Step Interactive Pipeline with Animated Flow Arrows */}
        <div className="hidden xl:grid grid-cols-8 gap-2 items-center mb-8 relative">
          {PIPELINE_STEPS.map((s, idx) => {
            const isSelected = activeStep === idx;
            return (
              <React.Fragment key={s.step}>
                <div
                  onClick={() => setActiveStep(idx)}
                  className={`cursor-pointer rounded-2xl p-4 transition-all duration-200 border flex flex-col justify-between h-44 ${
                    isSelected
                      ? 'bg-white border-indigo-500 shadow-md ring-2 ring-indigo-200 scale-105'
                      : 'bg-white/80 border-slate-200 hover:border-indigo-300 hover:bg-white shadow-sm'
                  }`}
                >
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span className={`w-6 h-6 rounded-lg ${C[s.color].bg} ${C[s.color].text} font-mono font-black text-xs flex items-center justify-center`}>
                        {s.step}
                      </span>
                      <span className="text-[10px] font-mono text-slate-400">Step {idx + 1}</span>
                    </div>
                    <h4 className="text-xs font-bold text-slate-900 leading-snug line-clamp-2 mb-1">{s.title}</h4>
                    <span className={`text-[9px] font-mono font-medium ${C[s.color].badge} px-1.5 py-0.5 rounded block truncate`}>
                      {s.model}
                    </span>
                  </div>
                  <div className="text-[10px] text-slate-500 line-clamp-2 mt-2 leading-tight">
                    {s.simpleWords}
                  </div>
                </div>
              </React.Fragment>
            );
          })}
        </div>

        {/* Mobile / Tablet Step Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:hidden gap-4 mb-8">
          {PIPELINE_STEPS.map((s, idx) => (
            <div
              key={s.step}
              onClick={() => setActiveStep(idx)}
              className={`cursor-pointer rounded-2xl p-5 border transition-all ${
                activeStep === idx
                  ? 'bg-white border-indigo-500 shadow-md ring-2 ring-indigo-200'
                  : 'bg-white border-slate-200 hover:border-indigo-200'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <span className={`w-7 h-7 rounded-xl ${C[s.color].bg} ${C[s.color].text} font-mono font-black text-xs flex items-center justify-center`}>
                  {s.step}
                </span>
                <span className={`text-[10px] font-mono ${C[s.color].badge} px-2 py-0.5 rounded-full`}>
                  {s.model}
                </span>
              </div>
              <h4 className="text-sm font-bold text-slate-900 mb-1">{s.title}</h4>
              <p className="text-xs text-slate-600 mb-3">{s.desc}</p>
              <div className="bg-slate-50 p-2.5 rounded-xl border border-slate-100 text-[11px] text-slate-700">
                <span className="font-bold text-indigo-700">In simple words: </span>{s.simpleWords}
              </div>
            </div>
          ))}
        </div>

        {/* Highlighted Step In-Depth Explainer with Animated Arrow Flow */}
        <Fade>
          <div className="bg-white border-2 border-indigo-200 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-100 pb-4 mb-6">
              <div className="flex items-center space-x-3">
                <span className={`w-10 h-10 rounded-xl ${C[PIPELINE_STEPS[activeStep].color].bg} ${C[PIPELINE_STEPS[activeStep].color].text} font-mono font-black text-lg flex items-center justify-center`}>
                  {PIPELINE_STEPS[activeStep].step}
                </span>
                <div>
                  <div className="flex items-center space-x-2">
                    <h3 className="text-xl font-black text-slate-900">{PIPELINE_STEPS[activeStep].title}</h3>
                    <span className={`text-xs font-mono font-semibold ${C[PIPELINE_STEPS[activeStep].color].badge} px-2.5 py-0.5 rounded-full`}>
                      {PIPELINE_STEPS[activeStep].model}
                    </span>
                  </div>
                  <span className="text-xs font-mono text-slate-400">Step {activeStep + 1} of 8 in Documentation Flow</span>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <button
                  disabled={activeStep === 0}
                  onClick={() => setActiveStep(prev => prev - 1)}
                  className="px-3 py-1.5 text-xs font-mono font-semibold bg-slate-100 text-slate-600 rounded-lg hover:bg-slate-200 disabled:opacity-40"
                >
                  ← Previous Step
                </button>
                <button
                  disabled={activeStep === PIPELINE_STEPS.length - 1}
                  onClick={() => setActiveStep(prev => prev + 1)}
                  className="px-3 py-1.5 text-xs font-mono font-semibold bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 disabled:opacity-40"
                >
                  Next Step →
                </button>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
              <div>
                <h4 className="text-xs font-mono font-bold text-slate-500 uppercase tracking-wider mb-2">Technical Description (From PDF)</h4>
                <p className="text-sm text-slate-700 leading-relaxed mb-4">
                  {PIPELINE_STEPS[activeStep].desc}
                </p>
                
                {/* In Simple Words Callout Box */}
                <div className="bg-indigo-50/70 border border-indigo-200 rounded-xl p-4">
                  <div className="flex items-center space-x-2 mb-1">
                    <Sparkles className="w-4 h-4 text-indigo-600" />
                    <span className="text-xs font-bold font-mono text-indigo-900 uppercase">In Simple Words</span>
                  </div>
                  <p className="text-sm text-indigo-950 font-medium leading-relaxed">
                    {PIPELINE_STEPS[activeStep].simpleWords}
                  </p>
                </div>
              </div>

              {/* Animated Mini Flowchart for this step */}
              <div className="bg-slate-900 rounded-xl p-5 text-white">
                <div className="flex items-center justify-between text-xs font-mono text-slate-400 mb-3 border-b border-slate-800 pb-2">
                  <span>LIVE SIGNAL FLOW</span>
                  <span className="text-emerald-400">Step {activeStep + 1} ACTIVE</span>
                </div>
                <div className="flex items-center justify-between text-xs font-mono space-x-2">
                  <div className="bg-slate-800 p-2.5 rounded-lg border border-slate-700 text-center flex-1">
                    <span className="text-[10px] text-slate-400 block mb-0.5">FROM</span>
                    <span className="text-indigo-300 font-bold">
                      {activeStep === 0 ? 'Student' : PIPELINE_STEPS[activeStep - 1].title}
                    </span>
                  </div>
                  <div className="flex flex-col items-center">
                    <svg className="w-8 h-4 text-indigo-400 overflow-visible" viewBox="0 0 32 16" fill="none">
                      <path d="M0 8 L24 8" stroke="currentColor" strokeWidth="2" className="animate-arrow-flow" />
                      <path d="M18 4 L26 8 L18 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                  </div>
                  <div className="bg-indigo-950 p-2.5 rounded-lg border border-indigo-500 text-center flex-1 ring-1 ring-indigo-400">
                    <span className="text-[10px] text-indigo-300 block mb-0.5">CURRENT</span>
                    <span className="text-white font-bold">{PIPELINE_STEPS[activeStep].model}</span>
                  </div>
                  <div className="flex flex-col items-center">
                    <svg className="w-8 h-4 text-indigo-400 overflow-visible" viewBox="0 0 32 16" fill="none">
                      <path d="M0 8 L24 8" stroke="currentColor" strokeWidth="2" className="animate-arrow-flow" />
                      <path d="M18 4 L26 8 L18 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                  </div>
                  <div className="bg-slate-800 p-2.5 rounded-lg border border-slate-700 text-center flex-1">
                    <span className="text-[10px] text-slate-400 block mb-0.5">NEXT</span>
                    <span className="text-emerald-300 font-bold">
                      {activeStep === PIPELINE_STEPS.length - 1 ? 'Mastery DB' : PIPELINE_STEPS[activeStep + 1].title}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Fade>
      </div>
    </section>
  );
}

// ── SECTION 02: Architecture & Models Table (From PDF Page 1-2 & 10) ─────────
function ArchitectureTableSection() {
  return (
    <section id="models-table" className="py-20 bg-white">
      <div className="max-w-[1550px] mx-auto px-6 lg:px-12">
        <Fade className="mb-12">
          <Tag>02 — System Architecture</Tag>
          <h2 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-3">
            AI Models &amp; Component Specification — <span className="text-indigo-600">Table Overview</span>
          </h2>
          <p className="text-slate-600 max-w-2xl text-base leading-relaxed">
            As outlined in <strong>Pages 1–2 of the System Implementation Plan</strong>, Re:Learn does not train one monolithic black-box chatbot. Instead, it couples specialized modular components with clear division of responsibility.
          </p>
        </Fade>

        {/* Formatted Architecture Table */}
        <Fade className="mb-10">
          <div className="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="bg-slate-900 text-white font-mono text-xs">
                    <th className="px-5 py-4 font-semibold uppercase tracking-wider w-1/5">Component</th>
                    <th className="px-5 py-4 font-semibold uppercase tracking-wider w-1/4">Role in System</th>
                    <th className="px-5 py-4 font-semibold uppercase tracking-wider w-1/5">AI Model / Implementation</th>
                    <th className="px-5 py-4 font-semibold uppercase tracking-wider w-1/3">In Simple Words</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {ARCHITECTURE_TABLE.map((row, i) => (
                    <tr key={row.part} className={i % 2 === 0 ? 'bg-white' : 'bg-slate-50/60'}>
                      <td className="px-5 py-4 font-bold text-slate-900 font-mono text-xs">
                        {row.part}
                      </td>
                      <td className="px-5 py-4 text-xs text-slate-600 leading-relaxed">
                        {row.role}
                      </td>
                      <td className="px-5 py-4 text-xs font-mono font-semibold text-indigo-700">
                        {row.tech}
                      </td>
                      <td className="px-5 py-4 text-xs text-slate-800 font-medium bg-indigo-50/30">
                        <span className="inline-flex items-center space-x-1.5 text-slate-700">
                          <CheckCircle className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0" />
                          <span>{row.simpleWords}</span>
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </Fade>

        {/* 3 Main Models Cards */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
          {[
            {
              tag: 'Model 1', color: 'indigo', icon: Brain,
              title: 'DeBERTa-v3-small',
              desc: 'Fine-tuned on 13,860 student responses across 46 misconception classes. Calibrated abstention gates ambiguous answers.',
              stats: [{ l: 'Test Accuracy', v: '88.59%', c: 'indigo' }, { l: 'OOD Accuracy', v: '90.48%', c: 'emerald' }, { l: 'Macro F1', v: '0.8678', c: 'violet' }, { l: 'Classes', v: '46', c: 'amber' }],
              simpleWords: 'Acts as the primary diagnostician, identifying why a student got an answer wrong in a fraction of a second.'
            },
            {
              tag: 'Model 2', color: 'emerald', icon: Activity,
              title: 'Sequence Pattern Analyser',
              desc: 'GRU neural network classifies 2,700 student trajectory sequences across 45 archetypes. Distinguishes slips from real flaws.',
              stats: [{ l: 'Sequence Acc.', v: '100%', c: 'emerald' }, { l: 'Sequences', v: '2,700', c: 'indigo' }, { l: 'Archetypes', v: '45', c: 'violet' }, { l: 'BKT Gain', v: '+0.58', c: 'amber' }],
              simpleWords: 'Watches if the student repeatedly makes the same mistake or if it was just a one-time calculation slip.'
            },
            {
              tag: 'Intervention', color: 'amber', icon: Sparkles,
              title: 'Prof. Maya (Gemini Flash)',
              desc: 'Gemini 1.5 Flash with strict NCERT-constrained prompt. Bilingual EN+HI. Generates POE lessons for 3D avatar & whiteboard.',
              stats: [{ l: 'Base Model', v: 'Gemini Flash', c: 'amber' }, { l: 'Language', v: 'EN + HI', c: 'indigo' }, { l: 'Abstention', v: '98.8%', c: 'emerald' }, { l: 'Avatar', v: '3D WebGL', c: 'violet' }],
              simpleWords: 'The 3D teacher who steps in with interactive experiments and whiteboard sketches to reteach the concept.'
            },
          ].map(m => {
            const Icon = m.icon;
            return (
              <Fade key={m.tag}>
                <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm flex flex-col justify-between h-full">
                  <div>
                    <div className="flex items-center justify-between mb-4">
                      <div className={`w-10 h-10 rounded-xl ${C[m.color].bg} flex items-center justify-center`}>
                        <Icon className={`w-5 h-5 ${C[m.color].text}`} />
                      </div>
                      <span className={`text-[10px] font-mono font-semibold ${C[m.color].badge} px-2.5 py-0.5 rounded-full`}>{m.tag}</span>
                    </div>
                    <h3 className="text-lg font-black text-slate-900 mb-1">{m.title}</h3>
                    <p className="text-xs text-slate-500 mb-4 leading-relaxed">{m.desc}</p>
                    
                    <div className="grid grid-cols-2 gap-2 mb-4">
                      {m.stats.map(s => (
                        <div key={s.l} className="bg-slate-50 rounded-lg p-2 border border-slate-100">
                          <div className="text-[10px] font-mono text-slate-500">{s.l}</div>
                          <div className={`text-sm font-black ${C[s.c].text}`}>{s.v}</div>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div className="bg-slate-50 rounded-xl p-3 border border-slate-100 text-xs text-slate-700">
                    <span className="font-bold text-slate-900">In simple words: </span>{m.simpleWords}
                  </div>
                </div>
              </Fade>
            );
          })}
        </div>
      </div>
    </section>
  );
}

// ── SECTION 03: Multimodal Input Handling Matrix (From PDF Page 2 & 7) ────────
function MultimodalInputSection() {
  return (
    <section id="inputs" className="py-20 bg-slate-50 border-t border-slate-200">
      <div className="max-w-[1550px] mx-auto px-6 lg:px-12">
        <Fade className="mb-12">
          <Tag>03 — Multimodal Modalities</Tag>
          <h2 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-3">
            How Re:Learn Processes <span className="text-indigo-600">5 Input Modalities</span>
          </h2>
          <p className="text-slate-600 max-w-2xl text-base leading-relaxed">
            Directly from <strong>Page 2 &amp; Page 7 of the System Plan</strong>: students do not think solely in multiple choice questions. Here is how each modality is converted into diagnostic evidence.
          </p>
        </Fade>

        {/* Input Matrix Table */}
        <Fade className="mb-10">
          <div className="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="bg-slate-900 text-white font-mono text-xs">
                    <th className="px-5 py-4 font-semibold uppercase tracking-wider w-1/5">Input Modality</th>
                    <th className="px-5 py-4 font-semibold uppercase tracking-wider w-1/4">What the Student Provides</th>
                    <th className="px-5 py-4 font-semibold uppercase tracking-wider w-1/4">Processing Pipeline</th>
                    <th className="px-5 py-4 font-semibold uppercase tracking-wider w-1/3">In Simple Words</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {INPUT_MATRIX_TABLE.map((row, i) => (
                    <tr key={row.type} className={i % 2 === 0 ? 'bg-white' : 'bg-slate-50/60'}>
                      <td className="px-5 py-4 font-bold text-slate-900 font-mono text-xs">
                        {row.type}
                      </td>
                      <td className="px-5 py-4 text-xs text-slate-600 leading-relaxed">
                        {row.input}
                      </td>
                      <td className="px-5 py-4 text-xs font-mono text-indigo-700">
                        {row.pipeline}
                      </td>
                      <td className="px-5 py-4 text-xs text-slate-800 font-medium bg-emerald-50/30">
                        <span className="inline-flex items-center space-x-1.5 text-slate-700">
                          <CheckCircle className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0" />
                          <span>{row.simpleWords}</span>
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </Fade>

        {/* Visual Modality Grid with Flow Arrows */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          <Fade>
            <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-mono font-bold text-indigo-600 uppercase">Text / Speech</span>
                <span className="text-[10px] font-mono bg-indigo-50 text-indigo-700 px-2 py-0.5 rounded">Direct NLP</span>
              </div>
              <h4 className="font-bold text-slate-900 mb-1 text-sm">Natural Language &amp; Slang</h4>
              <p className="text-xs text-slate-500 mb-3">Students type their reasoning in informal words. DeBERTa classifies without requiring textbook phrasing.</p>
              <div className="bg-slate-50 rounded-xl p-2.5 font-mono text-xs text-slate-600 italic">
                › "current gets used up in bulb 1"
              </div>
            </div>
          </Fade>

          <Fade>
            <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-mono font-bold text-violet-600 uppercase">Handwriting Photo</span>
                <span className="text-[10px] font-mono bg-violet-50 text-violet-700 px-2 py-0.5 rounded">PaddleOCR</span>
              </div>
              <h4 className="font-bold text-slate-900 mb-1 text-sm">Exam Scratchpad Photos</h4>
              <p className="text-xs text-slate-500 mb-3">OCR reads equations, fractions, and intermediate algebra steps directly from camera snapshots.</p>
              <div className="bg-slate-50 rounded-xl p-2.5 font-mono text-xs text-slate-600 italic">
                › [Image → Text: v = 100/5 = 20 m/s]
              </div>
            </div>
          </Fade>

          <Fade>
            <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-mono font-bold text-emerald-600 uppercase">Diagram Sketches</span>
                <span className="text-[10px] font-mono bg-emerald-50 text-emerald-700 px-2 py-0.5 rounded">Vision Parser</span>
              </div>
              <h4 className="font-bold text-slate-900 mb-1 text-sm">Ray &amp; Force Vectors</h4>
              <p className="text-xs text-slate-500 mb-3">Parses arrows, focal points, and normals to detect whether vector directions were inverted.</p>
              <div className="bg-slate-50 rounded-xl p-2.5 font-mono text-xs text-slate-600 italic">
                › [Ray: Top Object → Lens Center]
              </div>
            </div>
          </Fade>
        </div>
      </div>
    </section>
  );
}

// ── SECTION 04: Detection vs Differentiation (From PDF Page 11) ───────────────
function DetectionDifferentiationSection() {
  return (
    <section id="differentiation" className="py-20 bg-white border-t border-slate-200">
      <div className="max-w-[1550px] mx-auto px-6 lg:px-12">
        <Fade className="mb-12">
          <Tag>04 — Diagnostic Engine Core</Tag>
          <h2 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-3">
            Model A: Detection vs. Differentiation — <span className="text-indigo-600">In Simple Words</span>
          </h2>
          <p className="text-slate-600 max-w-2xl text-base leading-relaxed">
            As explained on <strong>Page 11 of the Documentation</strong>, Model A does not simply mark an answer right or wrong. It handles two distinct diagnostic challenges.
          </p>
        </Fade>

        {/* Side by Side Comparison Cards with Animated Arrows */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-10">
          {DIFFERENTIATION_EXAMPLES.map((item, idx) => (
            <Fade key={item.task}>
              <div className="bg-white border-2 border-slate-200 hover:border-indigo-300 rounded-2xl p-6 sm:p-8 shadow-sm h-full flex flex-col justify-between transition-all">
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <span className={`text-xs font-mono font-bold px-3 py-1 rounded-full ${idx === 0 ? 'bg-indigo-100 text-indigo-700' : 'bg-emerald-100 text-emerald-700'}`}>
                      {item.task}
                    </span>
                    <span className="text-xs font-mono text-slate-400">Challenge {idx + 1}</span>
                  </div>

                  <h3 className="text-lg font-bold text-slate-900 mb-2">{item.question}</h3>
                  <div className="bg-slate-50 rounded-xl p-3.5 border border-slate-100 mb-4">
                    <span className="text-[11px] font-mono font-bold text-slate-500 uppercase block mb-1">Realistic Scenario</span>
                    <p className="text-xs text-slate-700 italic">"{item.example}"</p>
                  </div>

                  <div className="bg-indigo-50/50 rounded-xl p-3.5 border border-indigo-100 mb-6">
                    <span className="text-[11px] font-mono font-bold text-indigo-800 uppercase block mb-1">Model Output</span>
                    <p className="text-xs text-indigo-900 font-semibold">{item.result}</p>
                  </div>
                </div>

                <div className="bg-emerald-50 rounded-xl p-4 border border-emerald-200">
                  <div className="flex items-center space-x-2 mb-1">
                    <CheckCircle className="w-4 h-4 text-emerald-600" />
                    <span className="text-xs font-bold font-mono text-emerald-900 uppercase">In Simple Words</span>
                  </div>
                  <p className="text-xs text-emerald-950 font-medium leading-relaxed">
                    {item.simpleWords}
                  </p>
                </div>
              </div>
            </Fade>
          ))}
        </div>

        {/* Visual Differentiation Flowchart with Animated Arrows */}
        <Fade>
          <div className="bg-slate-900 rounded-2xl p-6 sm:p-8 text-white">
            <div className="flex items-center space-x-2 mb-6">
              <Split className="w-5 h-5 text-indigo-400" />
              <h3 className="font-bold text-white text-base">How Differentiation Works In Practice</h3>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 items-center">
              <div className="bg-slate-800 p-4 rounded-xl border border-slate-700 text-center">
                <span className="text-[10px] font-mono text-slate-400 uppercase block mb-1">Input Response</span>
                <p className="text-xs text-white font-mono">"Image only shows half"</p>
                <div className="text-[11px] text-rose-400 font-bold mt-2">Wrong Answer</div>
              </div>

              <div className="flex flex-col items-center justify-center">
                <div className="text-[10px] font-mono text-indigo-300 bg-indigo-950 px-3 py-1 rounded-full border border-indigo-800 mb-1.5">
                  DeBERTa Reasoner
                </div>
                <svg className="w-12 h-6 text-indigo-400 overflow-visible" viewBox="0 0 48 24" fill="none">
                  <path d="M0 12 L38 12" stroke="currentColor" strokeWidth="2.5" className="animate-arrow-flow" />
                  <path d="M30 6 L40 12 L30 18" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </div>

              <div className="space-y-2">
                <div className="bg-indigo-950/80 p-3 rounded-xl border border-indigo-500/80">
                  <div className="text-[10px] font-mono text-indigo-300 font-bold">MISC-OPT-001 (Stencil Flaw)</div>
                  <div className="text-xs text-slate-300">Believes glass blocks light physically like cardboard window.</div>
                </div>
                <div className="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
                  <div className="text-[10px] font-mono text-slate-400 font-bold">Alternative Hypothesis (Intensity)</div>
                  <div className="text-xs text-slate-400">If student mentioned dimmer light, flagged as correct intensity insight.</div>
                </div>
              </div>
            </div>
          </div>
        </Fade>
      </div>
    </section>
  );
}

// ── SECTION 05: Dataset & Anti-Memorisation (From PDF Page 4) ────────────────
function DatasetSection() {
  const [ref, inView] = useInView();
  return (
    <section id="dataset" ref={ref} className={`py-20 bg-slate-50 border-t border-slate-200 transition-all duration-700 ${inView ? 'opacity-100' : 'opacity-0 translate-y-6'}`}>
      <div className="max-w-[1550px] mx-auto px-6 lg:px-12">
        <div className="mb-12">
          <Tag>05 — Dataset Architecture</Tag>
          <h2 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-3">
            21,000 Responses.<br />
            <span className="text-indigo-600">Anti-Memorisation Template Splits.</span>
          </h2>
          <p className="text-slate-600 max-w-2xl text-base leading-relaxed">
            Curated across 42 NCERT Physics curriculum families with strict template-disjoint splitting. The model is tested on question templates it never saw during training, proving it learned physics principles rather than sentence memorization.
          </p>
        </div>

        {/* Stat cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
          {[
            { icon: Database, val: '21,000', label: 'Training Responses', sub: '13,860 train / 3,780 test', color: 'indigo', bg: '#EEF2FF' },
            { icon: BookOpen, val: '42', label: 'Curriculum Families', sub: '500 responses / family', color: 'emerald', bg: '#ECFDF5' },
            { icon: Users, val: '2,700', label: 'Longitudinal Sequences', sub: '45 trajectory archetypes', color: 'violet', bg: '#F5F3FF' },
            { icon: Shield, val: '252', label: 'OOD Challenge Items', sub: 'Real-world messy slang', color: 'amber', bg: '#FFFBEB' },
          ].map(s => {
            const Icon = s.icon;
            return (
              <div key={s.val} className="rounded-2xl p-5 border flex flex-col justify-between" style={{ background: s.bg, borderColor: s.bg }}>
                <div className="flex items-center justify-between mb-3">
                  <div className={`w-9 h-9 rounded-xl ${C[s.color].bg} flex items-center justify-center`}>
                    <Icon className={`w-4.5 h-4.5 ${C[s.color].text}`} />
                  </div>
                  <span className={`text-[10px] font-mono ${C[s.color].badge} px-2 py-0.5 rounded-full font-semibold`}>Dataset</span>
                </div>
                <div>
                  <div className={`text-3xl font-black ${C[s.color].text} mb-1`}>{s.val}</div>
                  <div className="text-sm font-semibold text-slate-700">{s.label}</div>
                  <div className="text-[11px] font-mono text-slate-400 mt-0.5">{s.sub}</div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Dataset Growth Chart + Split Bar */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-5 mb-8">
          {/* Growth Bar Chart */}
          <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <h3 className="font-bold text-slate-900 text-sm">Dataset Growth Across Iterations</h3>
              <span className="text-[10px] font-mono text-slate-400 bg-slate-50 border border-slate-200 px-2 py-1 rounded-lg">Records</span>
            </div>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={datasetGrowth} margin={{ top: 5, right: 10, left: -10, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                <XAxis dataKey="iter" tick={{ fontSize: 11, fontFamily: 'monospace', fill: '#94A3B8' }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11, fontFamily: 'monospace', fill: '#94A3B8' }} axisLine={false} tickLine={false} />
                <Tooltip content={<CustomTooltip />} />
                <Bar dataKey="records" name="Records" radius={[6, 6, 0, 0]}>
                  {datasetGrowth.map((e, i) => <Cell key={i} fill={i === 0 ? '#FDA4AF' : i === 1 ? '#A78BFA' : '#818CF8'} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Split breakdown */}
          <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center space-x-2">
                <Shield className="w-4 h-4 text-slate-600" />
                <h3 className="font-bold text-slate-900 text-sm">Template-Disjoint Splits</h3>
              </div>
              <span className="text-[10px] font-mono bg-emerald-100 text-emerald-700 px-2 py-1 rounded-lg font-semibold">Zero Leakage</span>
            </div>
            <div className="space-y-4 mb-5">
              {[
                { label: 'Train', pct: 66, count: '13,860', color: '#818CF8' },
                { label: 'Validation', pct: 16, count: '3,360', color: '#A78BFA' },
                { label: 'Test (Disjoint)', pct: 18, count: '3,780', color: '#10B981' },
              ].map(s => (
                <div key={s.label}>
                  <div className="flex justify-between text-xs font-mono text-slate-600 mb-1">
                    <span>{s.label}</span><span>{s.count}</span>
                  </div>
                  <div className="h-2.5 bg-slate-100 rounded-full overflow-hidden">
                    <div className="h-full rounded-full transition-all duration-1000" style={{ width: `${s.pct}%`, background: s.color }} />
                  </div>
                </div>
              ))}
            </div>
            <div className="grid grid-cols-2 gap-3 mt-4">
              {personas.slice(0, 4).map(p => (
                <div key={p.name} className="bg-slate-50 border border-slate-200 rounded-xl p-2.5">
                  <div className="text-[10px] font-semibold text-slate-700 mb-1">{p.name}</div>
                  <p className="text-[10px] font-mono text-slate-400 italic truncate">"{p.example}"</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

// ── SECTION 06: Empirical Benchmarks & Stress Tests ──────────────────────────
function BenchmarksSection() {
  return (
    <section id="benchmarks" className="py-20 bg-white border-t border-slate-200">
      <div className="max-w-[1550px] mx-auto px-6 lg:px-12">
        <Fade className="mb-12">
          <Tag>06 — Empirical Benchmarks</Tag>
          <h2 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-3">
            5 Iterations.<br /><span className="text-indigo-600">From 0% OOD to 90.48%.</span>
          </h2>
          <p className="text-slate-600 max-w-xl text-base leading-relaxed">
            Iterative dataset scaling + hyperparameter refinement. The model transitioned from catastrophic template memorisation to robust real-world generalisation.
          </p>
        </Fade>

        {/* Main accuracy chart */}
        <Fade className="mb-5">
          <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm mb-5">
            <div className="flex items-center justify-between mb-4">
              <h3 className="font-bold text-slate-900">Accuracy Evolution — Test vs OOD</h3>
              <div className="flex items-center space-x-4 text-xs font-mono">
                <span className="flex items-center space-x-1"><span className="w-3 h-0.5 bg-indigo-500 inline-block rounded" /><span className="text-slate-500">Test Acc</span></span>
                <span className="flex items-center space-x-1"><span className="w-3 h-0.5 bg-emerald-500 inline-block rounded" /><span className="text-slate-500">OOD Acc</span></span>
                <span className="flex items-center space-x-1"><span className="w-3 h-0.5 bg-violet-400 inline-block rounded border-dashed border-t-2" /><span className="text-slate-500">Target 85%</span></span>
              </div>
            </div>
            <ResponsiveContainer width="100%" height={260}>
              <LineChart data={benchmarkData} margin={{ top: 10, right: 20, left: -10, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                <XAxis dataKey="iter" tick={{ fontSize: 11, fontFamily: 'monospace', fill: '#94A3B8' }} axisLine={false} tickLine={false} />
                <YAxis domain={[0, 105]} tick={{ fontSize: 11, fontFamily: 'monospace', fill: '#94A3B8' }} axisLine={false} tickLine={false} />
                <Tooltip content={<CustomTooltip />} />
                <ReferenceLine y={85} stroke="#A78BFA" strokeDasharray="6 3" strokeWidth={1.5} label={{ value: 'Target 85%', fontSize: 10, fill: '#7C3AED', fontFamily: 'monospace' }} />
                <Line type="monotone" dataKey="testAcc" name="Test Accuracy" stroke="#4F46E5" strokeWidth={2.5} dot={{ r: 5, fill: '#4F46E5', stroke: '#fff', strokeWidth: 2 }} activeDot={{ r: 7 }} />
                <Line type="monotone" dataKey="oodAcc" name="OOD Accuracy" stroke="#10B981" strokeWidth={2.5} dot={{ r: 5, fill: '#10B981', stroke: '#fff', strokeWidth: 2 }} activeDot={{ r: 7 }} />
                <Line type="monotone" dataKey="macroF1" name="Macro F1 ×100" stroke="#F59E0B" strokeWidth={1.5} strokeDasharray="4 2" dot={{ r: 4, fill: '#F59E0B' }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </Fade>

        {/* Radar + Stress-Test Table */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-5 mb-5">
          {/* Radar */}
          <Fade>
            <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm h-full flex flex-col justify-between">
              <div>
                <h3 className="font-bold text-slate-900 text-sm mb-4">Multi-Metric Verification</h3>
                <ResponsiveContainer width="100%" height={230}>
                  <RadarChart data={radarData}>
                    <PolarGrid stroke="#E2E8F0" />
                    <PolarAngleAxis dataKey="metric" tick={{ fontSize: 10, fontFamily: 'monospace', fill: '#64748B' }} />
                    <Radar name="Performance" dataKey="value" stroke="#4F46E5" fill="#4F46E5" fillOpacity={0.15} strokeWidth={2} dot={{ r: 4, fill: '#4F46E5' }} />
                    <Tooltip content={<CustomTooltip />} />
                  </RadarChart>
                </ResponsiveContainer>
              </div>
              <div className="text-xs text-slate-500 bg-slate-50 p-2.5 rounded-xl border border-slate-100 font-mono mt-3">
                Abstention Calibration: 98.8% · Sequence Pattern: 100%
              </div>
            </div>
          </Fade>

          {/* Qualitative Stress Tests */}
          <Fade>
            <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
              <h3 className="font-bold text-slate-900 text-sm mb-4">Qualitative Stress-Test Responses</h3>
              <div className="space-y-3">
                {[
                  { q: '"If top half covered, only bottom half shows up"', label: 'MISC-OPT-001', conf: '99.7%', color: 'indigo', note: 'Standard phrasing' },
                  { q: '"bro only bottom part shows up, rest cut ho gaya"', label: 'MISC-OPT-001', conf: '99.7%', color: 'violet', note: 'Vernacular Hinglish slang' },
                  { q: '"idk forgot formula"', label: 'UNSURE_INSUFFICIENT_EVIDENCE', conf: '100%', color: 'emerald', note: 'Correctly abstains' },
                  { q: '"current gets used up in first bulb"', label: 'MISC-ELEC-001', conf: '97.2%', color: 'amber', note: 'Circuit fuel model' },
                ].map(t => (
                  <div key={t.q} className="bg-slate-50 border border-slate-100 rounded-xl p-3 flex items-start space-x-3">
                    <div className={`mt-1 w-2 h-2 rounded-full flex-shrink-0 ${C[t.color].dot}`} />
                    <div className="flex-1 min-w-0">
                      <p className="text-xs font-mono text-slate-700 italic mb-1 leading-relaxed">{t.q}</p>
                      <div className="flex items-center justify-between">
                        <span className={`text-[10px] font-mono font-semibold ${C[t.color].badge} px-2 py-0.5 rounded`}>{t.label}</span>
                        <div className="flex items-center space-x-2">
                          <span className="text-[10px] text-slate-400 font-mono">{t.note}</span>
                          <span className="text-xs font-black text-emerald-600">{t.conf}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </Fade>
        </div>

        {/* Iteration table */}
        <Fade>
          <div className="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm mb-5">
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="bg-slate-900 text-white">
                    {['Iteration', 'Records', 'Families', 'Test Acc', 'OOD Acc', 'Macro F1', 'Status'].map(h => (
                      <th key={h} className="text-left px-5 py-3.5 font-mono text-xs font-semibold tracking-wide">{h}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {benchmarkData.map((row, i) => (
                    <tr key={row.iter} className={`border-t border-slate-100 ${i % 2 ? 'bg-slate-50/50' : 'bg-white'}`}>
                      <td className="px-5 py-3.5 font-bold text-slate-800 text-xs font-mono">{row.iter}</td>
                      <td className="px-5 py-3.5 font-mono text-xs text-slate-500">{row.records.toLocaleString()}</td>
                      <td className="px-5 py-3.5 font-mono text-xs text-slate-500">{row.iter === 'Iter 1' ? 25 : 42}</td>
                      <td className="px-5 py-3.5 font-black text-sm" style={{ color: row.status === 'fail' ? '#E11D48' : row.status === 'partial' ? '#D97706' : '#059669' }}>{row.testAcc}%</td>
                      <td className="px-5 py-3.5 font-black text-sm" style={{ color: row.status === 'fail' ? '#E11D48' : row.status === 'partial' ? '#D97706' : '#059669' }}>{row.oodAcc}%</td>
                      <td className="px-5 py-3.5 font-mono text-xs text-slate-500">{(row.macroF1 / 100).toFixed(4)}</td>
                      <td className="px-5 py-3.5">
                        {row.status === 'fail' && <XCircle className="w-4 h-4 text-rose-500" />}
                        {row.status === 'partial' && <AlertTriangle className="w-4 h-4 text-amber-500" />}
                        {row.status === 'pass' && <CheckCircle className="w-4 h-4 text-emerald-500" />}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </Fade>

        <Fade>
          <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-4 flex items-center space-x-3">
            <CheckCircle className="w-5 h-5 text-emerald-600 flex-shrink-0" />
            <div>
              <div className="font-bold text-emerald-800 text-sm">All Research Benchmark Targets Achieved</div>
              <div className="text-xs text-emerald-700 font-mono">≥85% held-out test accuracy · ≥80% OOD challenge · 100% sequence accuracy · 98.8% abstention calibration</div>
            </div>
          </div>
        </Fade>
      </div>
    </section>
  );
}

// ── SECTION 07: 7-Layer Engineering Architecture ─────────────────────────────
function ArchitectureSection() {
  return (
    <section id="architecture" className="py-20 bg-slate-50 border-t border-slate-200">
      <div className="max-w-[1550px] mx-auto px-6 lg:px-12">
        <Fade className="mb-12">
          <Tag>07 — Engineering Stack</Tag>
          <h2 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-3">
            7-Layer<br /><span className="text-indigo-600">Production Architecture.</span>
          </h2>
          <p className="text-slate-600 max-w-xl text-base leading-relaxed">
            Each layer owns a single responsibility — connecting the React frontend through FastAPI to the AI diagnosis core and 3D avatar.
          </p>
        </Fade>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 mb-8">
          {layers.map(layer => {
            const Icon = layer.icon;
            const c = C[layer.color] || C.indigo;
            return (
              <Fade key={layer.num}>
                <div className="bg-white border border-slate-200 rounded-2xl p-5 hover:shadow-md hover:-translate-y-0.5 transition-all duration-200 h-full">
                  <div className="flex items-center justify-between mb-3">
                    <div className={`w-9 h-9 rounded-xl ${c.bg} flex items-center justify-center`}>
                      <Icon className={`w-4.5 h-4.5 ${c.text}`} />
                    </div>
                    <span className="text-[10px] font-mono text-slate-400 font-semibold">{layer.num}</span>
                  </div>
                  <h3 className="font-bold text-slate-900 text-sm mb-1">{layer.title}</h3>
                  <span className={`text-[10px] font-mono ${c.badge} px-2 py-0.5 rounded-full inline-block mb-2`}>{layer.sub}</span>
                  <p className="text-xs text-slate-500 leading-relaxed">{layer.desc}</p>
                </div>
              </Fade>
            );
          })}
        </div>

        {/* Live Flow Bar with Animated Arrows */}
        <Fade>
          <div className="bg-slate-900 rounded-2xl p-6 overflow-x-auto">
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-2 h-2 rounded-full bg-indigo-500 animate-pulse" />
              <span className="text-xs font-mono text-slate-300 font-semibold">End-to-End Execution Flow</span>
            </div>
            <div className="flex items-center gap-2 min-w-max">
              {[
                { l: 'Student UI', s: 'React :5173', c: 'text-indigo-400' },
                { l: 'FastAPI', s: ':8000 REST', c: 'text-violet-400' },
                { l: '/api/diagnose', s: 'DeBERTa-v3', c: 'text-blue-400' },
                { l: 'Intervention', s: 'POE + LLM', c: 'text-amber-400' },
                { l: 'Reassessment', s: 'BKT Engine', c: 'text-emerald-400' },
                { l: 'Learner Record', s: 'Mastery DB', c: 'text-rose-400' },
              ].map((n, i) => (
                <React.Fragment key={n.l}>
                  <div className="bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-center flex-shrink-0">
                    <div className={`text-xs font-mono font-semibold ${n.c}`}>{n.l}</div>
                    <div className="text-[10px] text-slate-500 mt-0.5">{n.s}</div>
                  </div>
                  {i < 5 && (
                    <svg className="w-6 h-4 text-indigo-400 flex-shrink-0 overflow-visible" viewBox="0 0 24 16" fill="none">
                      <path d="M0 8 L18 8" stroke="currentColor" strokeWidth="2" className="animate-arrow-flow" />
                      <path d="M12 4 L20 8 L12 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                  )}
                </React.Fragment>
              ))}
            </div>
          </div>
        </Fade>
      </div>
    </section>
  );
}

// ── Features & Launch Section ────────────────────────────────────────────────
function FeaturesSection({ onEnterApp }) {
  return (
    <section id="features" className="py-20 bg-white border-t border-slate-200">
      <div className="max-w-[1550px] mx-auto px-6 lg:px-12">
        <Fade className="mb-12">
          <Tag>08 — Features &amp; Demo</Tag>
          <h2 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-3">
            Everything In<br /><span className="text-indigo-600">One Integrated Platform.</span>
          </h2>
          <p className="text-slate-600 max-w-xl text-base leading-relaxed">
            All 7 mandatory features from the problem statement are fully integrated into a real-time interactive workspace.
          </p>
        </Fade>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-12">
          {features.map(f => {
            const Icon = f.icon;
            const c = C[f.color] || C.indigo;
            return (
              <Fade key={f.title}>
                <div className="bg-white border border-slate-200 rounded-2xl p-5 hover:shadow-md hover:-translate-y-0.5 transition-all duration-200 h-full">
                  <div className={`w-9 h-9 rounded-xl ${c.bg} flex items-center justify-center mb-3`}>
                    <Icon className={`w-4.5 h-4.5 ${c.text}`} />
                  </div>
                  <h3 className="font-bold text-slate-900 text-sm mb-2 leading-snug">{f.title}</h3>
                  <p className="text-xs text-slate-500 leading-relaxed">{f.desc}</p>
                </div>
              </Fade>
            );
          })}
        </div>

        {/* CTA Banner */}
        <Fade>
          <div className="rounded-3xl border border-indigo-200 p-8 lg:p-12 flex flex-col lg:flex-row items-center justify-between gap-6 bg-gradient-to-r from-indigo-50 via-purple-50 to-indigo-100">
            <div>
              <h3 className="text-2xl font-black text-slate-900 mb-2">Try the Diagnostic Studio Now</h3>
              <p className="text-slate-600 max-w-md text-sm">Select any NCERT Physics topic, submit free-text reasoning or calculation steps, and observe DeBERTa-v3 diagnose the underlying misconception in real-time.</p>
            </div>
            <div className="flex gap-3">
              <button onClick={onEnterApp} className="flex items-center space-x-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm px-7 py-3.5 rounded-xl shadow-md transition-all hover:-translate-y-0.5 whitespace-nowrap">
                <Zap className="w-4 h-4" /><span>Launch Diagnostic Studio</span>
              </button>
              <a href="https://github.com/NISHANTTMAURYA/relearn" target="_blank" rel="noopener noreferrer" className="flex items-center justify-center bg-white border border-slate-200 text-slate-700 font-semibold text-sm px-6 py-3.5 rounded-xl hover:bg-slate-50 transition-colors whitespace-nowrap">
                GitHub Repository →
              </a>
            </div>
          </div>
        </Fade>
      </div>
    </section>
  );
}

// ── Main Component ────────────────────────────────────────────────────────────
export default function LandingPage({ onEnterApp }) {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const fn = () => setScrolled(window.scrollY > 30);
    window.addEventListener('scroll', fn);
    return () => window.removeEventListener('scroll', fn);
  }, []);

  const scrollTo = id => { const el = document.getElementById(id); if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' }); };

  return (
    <div className="min-h-screen bg-white font-sans text-slate-900 antialiased">
      {/* Floating navigation header */}
      <header className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'bg-white/95 backdrop-blur shadow-sm border-b border-slate-200' : 'bg-transparent'}`}>
        <div className="max-w-[1550px] mx-auto px-6 lg:px-12 h-16 flex items-center justify-between">
          <div className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white font-black text-xs shadow-sm">Re:</div>
            <span className="font-black text-slate-900 text-base">Re:Learn</span>
            <span className="text-[10px] font-mono font-semibold bg-indigo-50 text-indigo-700 border border-indigo-200/80 px-2 py-0.5 rounded-full">NCERT Physics</span>
          </div>
          <nav className="hidden lg:flex items-center space-x-1">
            {[
              ['flow', '01 Flow'],
              ['models-table', '02 Models'],
              ['inputs', '03 Modalities'],
              ['differentiation', '04 Differentiation'],
              ['dataset', '05 Dataset'],
              ['benchmarks', '06 Benchmarks'],
              ['architecture', '07 Architecture']
            ].map(([id, label]) => (
              <button key={id} onClick={() => scrollTo(id)} className="px-3 py-1.5 text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-colors">{label}</button>
            ))}
          </nav>
          <button onClick={onEnterApp} className="flex items-center space-x-1.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs px-4.5 py-2 rounded-xl shadow transition-all hover:-translate-y-0.5">
            <Zap className="w-3.5 h-3.5" /><span>Enter Studio</span>
          </button>
        </div>
      </header>

      <div className="h-16" />

      {/* Hero Section */}
      <HeroSection onEnterApp={onEnterApp} />

      {/* 01: End-to-End Component Flow (Direct from PDF Page 10) */}
      <EndToEndFlowSection />

      {/* 02: Architecture & Models Table (Direct from PDF Page 1-2 & 10) */}
      <ArchitectureTableSection />

      {/* 03: Multimodal Input Handling Matrix (Direct from PDF Page 2 & 7) */}
      <MultimodalInputSection />

      {/* 04: Detection vs Differentiation (Direct from PDF Page 11) */}
      <DetectionDifferentiationSection />

      {/* 05: Dataset & Anti-Memorisation Splits (Direct from PDF Page 4) */}
      <DatasetSection />

      {/* 06: Empirical Benchmarks & Qualitative Stress-Tests */}
      <BenchmarksSection />

      {/* 07: 7-Layer Engineering Architecture */}
      <ArchitectureSection />

      {/* 08: Features & Studio Launch */}
      <FeaturesSection onEnterApp={onEnterApp} />

      {/* Footer */}
      <footer className="bg-slate-900 text-white py-12 border-t border-slate-800">
        <div className="max-w-[1550px] mx-auto px-6 lg:px-12 flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <div className="flex items-center space-x-2 mb-1.5">
              <div className="w-6 h-6 rounded bg-indigo-500 flex items-center justify-center text-white font-black text-[9px]">Re:</div>
              <span className="font-black text-white text-base">Re:Learn</span>
            </div>
            <p className="text-slate-400 text-xs font-mono">AI Multimodal Misconception Diagnostic Engine</p>
          </div>
          <div className="text-center text-xs font-mono text-slate-400 space-y-1">
            <div>NCERT Secondary Physics · Class 9 &amp; 10</div>
            <div>DeBERTa-v3 · GRU Sequence Analyser · Prof. Maya (Gemini 1.5 Flash)</div>
          </div>
          <div className="flex items-center space-x-4 text-xs text-slate-300">
            <a href="https://github.com/NISHANTTMAURYA/relearn" target="_blank" rel="noopener noreferrer" className="hover:text-white transition-colors">GitHub</a>
            <button onClick={onEnterApp} className="bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2 rounded-xl font-bold transition-colors shadow">Launch Studio →</button>
          </div>
        </div>
      </footer>
    </div>
  );
}
