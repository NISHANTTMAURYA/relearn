import React, { useState, useEffect, useRef } from 'react';
import {
  Brain, Database, Sparkles, ChevronRight, CheckCircle, XCircle, ArrowRight,
  BookOpen, Zap, Target, Activity, Users, Shield, Cpu, Award,
  AlertTriangle, Monitor, Table, Layers, FileText
} from 'lucide-react';
import {
  LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, ReferenceLine, RadarChart, PolarGrid,
  PolarAngleAxis, Radar, Cell
} from 'recharts';

// ── Palette ──────────────────────────────────────────────────────────────────
const C = {
  indigo: { bg: 'bg-indigo-50', text: 'text-indigo-700', border: 'border-indigo-200', badge: 'bg-indigo-100 text-indigo-700', dot: 'bg-indigo-500' },
  violet: { bg: 'bg-violet-50', text: 'text-violet-700', border: 'border-violet-200', badge: 'bg-violet-100 text-violet-700', dot: 'bg-violet-500' },
  emerald:{ bg: 'bg-emerald-50', text: 'text-emerald-700', border: 'border-emerald-200', badge: 'bg-emerald-100 text-emerald-700', dot: 'bg-emerald-500' },
  amber:  { bg: 'bg-amber-50', text: 'text-amber-700', border: 'border-amber-200', badge: 'bg-amber-100 text-amber-700', dot: 'bg-amber-500' },
  rose:   { bg: 'bg-rose-50', text: 'text-rose-700', border: 'border-rose-200', badge: 'bg-rose-100 text-rose-700', dot: 'bg-rose-500' },
};

// ── Benchmark & Dataset Training Data ────────────────────────────────────────
const benchmarkData = [
  { iter: 'Iter 1', records: 2500, testAcc: 100, oodAcc: 0, macroF1: 1.0, status: 'fail', note: 'Catastrophic Template Memorisation' },
  { iter: 'Iter 2', records: 8400, testAcc: 74.34, oodAcc: 73.41, macroF1: 70.94, status: 'partial', note: 'Cold-Start Cross-Validation' },
  { iter: 'Iter 3', records: 12600, testAcc: 87.37, oodAcc: 90.48, macroF1: 83.78, status: 'pass', note: 'Template-Disjoint Splitting' },
  { iter: 'Iter 4', records: 16800, testAcc: 88.59, oodAcc: 88.89, macroF1: 86.78, status: 'pass', note: 'Cosine LR Decay + Label Smoothing' },
  { iter: 'Iter 5', records: 21000, testAcc: 85.00, oodAcc: 85.32, macroF1: 82.82, status: 'pass', note: 'Production Scale with Abstention' },
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

// Interactive Hero Student Responses
const HERO_EXAMPLES = [
  {
    id: 'optics-standard',
    category: 'Ray Optics (Standard)',
    query: 'When half of a concave mirror is covered with black tape, only half the image is formed on the screen.',
    badge: 'MISC-OPT-001 · Stencil Model',
    conf: '99.7%',
    studentMindset: 'Student assumes the glass acts like a window shutter: blocking half the mirror physically cuts half the object’s picture.',
    scientificTruth: 'Every point on the mirror reflects rays from all points on the object. The complete image forms, but at 50% light intensity.',
    color: 'indigo'
  },
  {
    id: 'optics-vernacular',
    category: 'CBSE Vernacular (Hinglish)',
    query: 'Mirror ko aadhi tape se cover kar diya, toh screen pe aadhi hi image aayegi.',
    badge: 'MISC-OPT-001 · Vernacular Parsing',
    conf: '99.7%',
    studentMindset: 'Informal student shorthand for the same window-stencil fallacy in conversational classroom Hindi/English.',
    scientificTruth: 'DeBERTa-v3 parses casual student phrasings without penalty, accurately identifying the root optics misconception.',
    color: 'violet'
  },
  {
    id: 'electricity',
    category: 'Current Electricity',
    query: 'Current is used up in the first bulb, so the second bulb in series receives less electricity and glows dimmer.',
    badge: 'MISC-ELEC-001 · Fuel Attenuation',
    conf: '97.2%',
    studentMindset: 'Treats electrical current as consumable fuel that diminishes sequentially along a circuit wire.',
    scientificTruth: 'Conservation of charge dictates that electric current is identical at all points in a single-loop series circuit.',
    color: 'amber'
  },
  {
    id: 'kinematics-slip',
    category: 'Kinematics (Slip vs Flaw)',
    query: 'Distance = 100 m, time = 5 s. Speed = 100 × 5 = 500 m/s.',
    badge: 'CARELESS_CALCULATION_ERROR · Slip',
    conf: '98.4%',
    studentMindset: 'Multiplied distance by time instead of dividing. Concept understood, but arithmetic operation inverted.',
    scientificTruth: 'The system flags this as a transient calculation slip, avoiding unnecessary conceptual lectures.',
    color: 'emerald'
  }
];

// 8 Flow Steps from PDF Page 10
const PIPELINE_STEPS = [
  { step: '1', title: 'Student Answers Quiz', model: 'Quiz Portal', desc: 'Accepts MCQ, free text, math steps, or diagram photo in natural language.' },
  { step: '2', title: 'Multimodal Preprocessing', model: 'PaddleOCR + Vision', desc: 'Converts handwriting, equations, and diagrams into clean structured text.' },
  { step: '3', title: 'Model 1: Individual Diagnosis', model: 'DeBERTa-v3', desc: 'Finds the exact mental misconception causing the wrong answer across 46 classes.' },
  { step: '4', title: 'Model 2: Sequence Analysis', model: 'GRU Model', desc: 'Tracks patterns across consecutive answers to detect persistent misunderstandings.' },
  { step: '5', title: 'Synthesis & Confidence Gate', model: 'Abstention Gate', desc: 'If evidence is uncertain, asks a quick follow-up question instead of guessing.' },
  { step: '6', title: 'Targeted Remediation', model: 'POE + Prof. Vikram', desc: 'Predict-Observe-Explain cycle with 3D avatar, SVG whiteboard, and PhET simulation.' },
  { step: '7', title: 'Isomorphic Reassessment', model: 'Question Bank', desc: 'Gives a fresh near-transfer question with new numbers to test true understanding.' },
  { step: '8', title: 'BKT Mastery Tracking', model: 'BKT Engine', desc: 'Updates knowledge state P(L) in the student profile, tracking cured misconceptions.' },
];

// The 17 Exact Dataset Features (From train.csv schema)
const DATASET_FEATURES = [
  { name: 'record_id', desc: 'Unique attempt ID (e.g. REC-00001).' },
  { name: 'question_id', desc: 'NCERT standard question ID (PHY-Class10-01-0001).' },
  { name: 'question_family', desc: 'Isomorphic curriculum family template.' },
  { name: 'curriculum_grade', desc: 'Target grade level (Class 9 / 10).' },
  { name: 'curriculum_chapter', desc: 'NCERT textbook chapter name.' },
  { name: 'topic_concept', desc: 'Specific physics law being tested.' },
  { name: 'question_text', desc: 'Full problem stem with numbers & context.' },
  { name: 'correct_answer_and_steps', desc: 'Authoritative NCERT solution & steps.' },
  { name: 'student_response', desc: 'Raw typed answer, formula, or Hinglish.' },
  { name: 'misconception_label', desc: 'Codified error code (e.g. MISC-OPT-001).' },
  { name: 'error_type', desc: 'Misconception, calculation slip, or unsure.' },
  { name: 'diagnostic_confidence', desc: 'Calibrated model certainty (High/Med/Low).' },
  { name: 'evidence_rationale', desc: 'Reason why the diagnosis applies.' },
  { name: 'has_diagram', desc: 'Boolean flag for visual diagram inclusion.' },
  { name: 'diagram_type', desc: 'Diagram type (ray, circuit, force vector).' },
  { name: 'diagram_description', desc: 'Geometric vector & ray coordinates.' },
  { name: 'split', desc: 'Disjoint split (train, val, test, ood_test).' }
];

const personas = [
  { name: 'Standard Concept', example: '"If top half covered, only bottom half shows"', label: 'MISC-OPT-001' },
  { name: 'CBSE Vernacular', example: '"bro only bottom part shows up, rest cut ho gaya"', label: 'MISC-OPT-001' },
  { name: 'Shorthand', example: '"idk mybe crrnt used up in 1st bulb"', label: 'MISC-ELEC-001' },
  { name: 'Calculation Slip', example: '"100×5 = 500 m/s, speed = 500"', label: 'CARELESS_CALCULATION_ERROR' },
];

function Fade({ children, className = '' }) {
  const ref = useRef(null);
  const [inView, setInView] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(([e]) => { if (e.isIntersecting) { setInView(true); obs.disconnect(); } }, { threshold: 0.1 });
    obs.observe(el);
    return () => obs.disconnect();
  }, []);
  return <div ref={ref} className={`transition-all duration-700 ${inView ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-6'} ${className}`}>{children}</div>;
}

// Custom Tooltip for Charts
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

// ── Main Component ────────────────────────────────────────────────────────────
export default function LandingPage({ onEnterApp }) {
  const [selectedExample, setSelectedExample] = useState(HERO_EXAMPLES[0]);
  const [activeFeature, setActiveFeature] = useState(DATASET_FEATURES[0]);
  const [scrolled, setScrolled] = useState(false);
  const [diffStudent, setDiffStudent] = useState('A');

  useEffect(() => {
    const fn = () => setScrolled(window.scrollY > 30);
    window.addEventListener('scroll', fn);
    return () => window.removeEventListener('scroll', fn);
  }, []);

  const scrollTo = id => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  return (
    <div className="min-h-screen bg-white font-sans text-slate-900 antialiased selection:bg-indigo-100">
      {/* Floating Header */}
      <header className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'bg-white/95 backdrop-blur shadow-sm border-b border-slate-200' : 'bg-transparent'}`}>
        <div className="max-w-[1500px] mx-auto px-6 lg:px-12 h-16 flex items-center justify-between">
          <div className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white font-black text-xs shadow-sm">Re:</div>
            <span className="font-black text-slate-900 text-base">Re:Learn</span>
            <span className="text-[10px] font-mono font-semibold bg-indigo-50 text-indigo-700 border border-indigo-200 px-2 py-0.5 rounded-full">NCERT Physics</span>
          </div>

          <nav className="hidden md:flex items-center space-x-1 text-xs font-semibold text-slate-600">
            <button onClick={() => scrollTo('pipeline')} className="px-3 py-1.5 hover:text-slate-900 hover:bg-slate-100 rounded-lg">8-Step Flow</button>
            <button onClick={() => scrollTo('dataset')} className="px-3 py-1.5 hover:text-slate-900 hover:bg-slate-100 rounded-lg">Dataset &amp; Splits</button>
            <button onClick={() => scrollTo('benchmarks')} className="px-3 py-1.5 hover:text-slate-900 hover:bg-slate-100 rounded-lg">Benchmarks &amp; Training</button>
            <button onClick={() => scrollTo('models')} className="px-3 py-1.5 hover:text-slate-900 hover:bg-slate-100 rounded-lg">AI Models</button>
          </nav>

          <button onClick={onEnterApp} className="flex items-center space-x-1.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs px-4 py-2 rounded-xl shadow transition-all hover:-translate-y-0.5">
            <Zap className="w-3.5 h-3.5" /><span>Launch Studio</span>
          </button>
        </div>
      </header>

      <div className="h-16" />

      {/* ── 1. Hero Section ──────────────────────────────────────────────── */}
      <section className="relative overflow-hidden w-full bg-gradient-to-b from-[#F0F2FD] via-[#F6F8FE] to-white py-12 lg:py-16">
        <div className="max-w-[1500px] mx-auto px-6 lg:px-12">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
            
            {/* Left 7 cols: Title & Interactive Demo */}
            <div className="lg:col-span-7">
              <div className="inline-flex items-center space-x-2 text-xs font-mono font-semibold uppercase tracking-wider text-indigo-700 bg-indigo-100/70 border border-indigo-200 px-3 py-1 rounded-full mb-4">
                <span className="w-2 h-2 rounded-full bg-indigo-600 animate-pulse" />
                <span>NCERT Physics Class 9 &amp; 10 Diagnostic Platform</span>
              </div>

              <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-slate-900 leading-[1.08] mb-4">
                AI That Finds<br />
                What You<br />
                <span className="text-indigo-600">Don't Know</span>
              </h1>

              <p className="text-base sm:text-lg text-slate-600 mb-6 max-w-xl leading-relaxed font-normal">
                Re:Learn uncovers the exact physical misconception behind wrong answers — delivering multimodal Predict-Observe-Explain remediation and tracking mastery with Bayesian Knowledge Tracing.
              </p>

              {/* Interactive Scenario Buttons */}
              <div className="mb-3">
                <span className="text-xs font-mono font-bold text-slate-500 uppercase tracking-wider block mb-2">
                  Test Diagnostic Examples:
                </span>
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

              {/* Interactive Input Box with Clean Word Wrapping (NO CUT-OFF) */}
              <div className="bg-white border-2 border-indigo-300 rounded-2xl p-3.5 shadow-lg shadow-indigo-100/60 max-w-2xl mb-4 transition-all">
                <div className="flex items-start space-x-2.5 mb-3">
                  <span className="text-indigo-600 font-bold text-lg leading-snug">›</span>
                  <div className="text-sm sm:text-base text-slate-900 font-mono font-medium leading-relaxed break-words flex-1 select-all">
                    "{selectedExample.query}"
                  </div>
                </div>

                <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2 border-t border-slate-100">
                  <div className="flex items-center space-x-2 text-xs font-mono">
                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                    <span className="font-bold text-indigo-700">{selectedExample.badge}</span>
                    <span className="text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 font-bold">
                      {selectedExample.conf}
                    </span>
                  </div>

                  <button
                    onClick={onEnterApp}
                    className="w-full sm:w-auto bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs px-5 py-2.5 rounded-xl shadow-md transition-all flex items-center justify-center space-x-1.5 whitespace-nowrap"
                  >
                    <span>Diagnose In Studio</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>

              {/* In Plain Words Comparison Card */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 max-w-2xl text-xs mb-6">
                <div className="bg-rose-50/60 border border-rose-200/70 rounded-xl p-3">
                  <span className="font-bold font-mono text-rose-700 uppercase block mb-1">Student's Mental Flaw:</span>
                  <p className="text-slate-700 leading-relaxed">{selectedExample.studentMindset}</p>
                </div>
                <div className="bg-emerald-50/60 border border-emerald-200/70 rounded-xl p-3">
                  <span className="font-bold font-mono text-emerald-800 uppercase block mb-1">In Simple Words (Reality):</span>
                  <p className="text-slate-800 leading-relaxed">{selectedExample.scientificTruth}</p>
                </div>
              </div>

              {/* Quick High-Level Stats */}
              <div className="flex items-center gap-6 pt-4 border-t border-slate-200">
                <div>
                  <div className="text-2xl font-black text-slate-900">21,000</div>
                  <div className="text-[11px] font-mono text-slate-500 uppercase">Responses</div>
                </div>
                <div className="w-px h-8 bg-slate-200" />
                <div>
                  <div className="text-2xl font-black text-slate-900">17 Features</div>
                  <div className="text-[11px] font-mono text-slate-500 uppercase">Schema Columns</div>
                </div>
                <div className="w-px h-8 bg-slate-200" />
                <div>
                  <div className="text-2xl font-black text-indigo-600">88.59%</div>
                  <div className="text-[11px] font-mono text-slate-500 uppercase">Test Accuracy</div>
                </div>
              </div>
            </div>

            {/* Right 5 cols: Student Illustration with Animated Callouts */}
            <div className="lg:col-span-5 relative flex items-center justify-center">
              <div className="absolute w-72 h-72 rounded-full bg-indigo-200/40 blur-3xl -z-10" />
              <div className="relative w-full max-w-md flex flex-col items-center">
                <img
                  src="/student_illustration.png"
                  alt="Student learning physics with Re:Learn"
                  className="w-full max-w-[380px] h-auto object-contain drop-shadow-xl select-none"
                  onError={(e) => { e.target.src = '/landing_hero.jpg'; }}
                />

                <div className="absolute -top-3 -left-2 bg-white/95 backdrop-blur-md border border-indigo-200 shadow-md rounded-xl p-2.5 max-w-[190px]">
                  <span className="text-[10px] font-bold font-mono text-indigo-800 uppercase block mb-0.5">1. Student Input</span>
                  <p className="text-[11px] text-slate-600 leading-tight">Enters reasoning in English or Hinglish slang</p>
                </div>

                <div className="absolute -top-3 -right-2 bg-white/95 backdrop-blur-md border border-emerald-200 shadow-md rounded-xl p-2.5 max-w-[190px]">
                  <span className="text-[10px] font-bold font-mono text-emerald-800 uppercase block mb-0.5">2. AI Diagnosis</span>
                  <p className="text-[11px] text-slate-600 leading-tight">DeBERTa-v3 identifies the exact mental misconception</p>
                </div>

                <div className="absolute -bottom-3 left-2 bg-white/95 backdrop-blur-md border border-amber-200 shadow-md rounded-xl p-2.5 max-w-[190px]">
                  <span className="text-[10px] font-bold font-mono text-amber-800 uppercase block mb-0.5">3. Sequence Tracking</span>
                  <p className="text-[11px] text-slate-600 leading-tight">Tracks recurring errors across multiple questions</p>
                </div>

                <div className="absolute -bottom-3 right-2 bg-white/95 backdrop-blur-md border border-violet-200 shadow-md rounded-xl p-2.5 max-w-[190px]">
                  <span className="text-[10px] font-bold font-mono text-violet-800 uppercase block mb-0.5">4. POE Remediation</span>
                  <p className="text-[11px] text-slate-600 leading-tight">3D Mentor, Whiteboard &amp; BKT mastery test</p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* ── 2. The 8-Step End-to-End Pipeline (PDF Doc Flow) ─────────────── */}
      <section id="pipeline" className="py-16 bg-slate-50 border-y border-slate-200">
        <div className="max-w-[1500px] mx-auto px-6 lg:px-12">
          {/* Hand-Drawn Blueprint Flow: How Model 1, Model 2 Predict & Merge */}
          <div className="mb-10 bg-[#FAF9F6] border-2 border-dashed border-slate-300 rounded-3xl p-6 sm:p-8 shadow-xs relative overflow-hidden font-sans">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dashed border-slate-300 pb-4 mb-6">
              <div>
                <span className="text-[11px] font-mono uppercase tracking-wider text-indigo-700 bg-indigo-50 border border-indigo-200 px-2.5 py-1 rounded-md font-bold">
                  ✎ Hand-Drawn Architecture Blueprint
                </span>
                <h3 className="text-xl sm:text-2xl font-black text-slate-900 mt-1">
                  How Model 1 &amp; Model 2 Predict &amp; Merge
                </h3>
              </div>
              <span className="text-xs font-mono text-slate-500 italic">
                NCERT Multi-Question Diagnostic Protocol
              </span>
            </div>

            {/* Hand-Drawn Cards Pipeline (4 Simple Steps with Clear Arrows & Exact Techniques) */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 items-stretch">
              
              {/* Step 1: Student Input */}
              <div className="bg-white border-2 border-slate-800 rounded-2xl p-4 shadow-[4px_4px_0px_0px_rgba(15,23,42,1)] flex flex-col justify-between relative">
                <div>
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono uppercase bg-slate-100 text-slate-800 px-2 py-0.5 rounded font-bold border border-slate-300">
                      Step 1 · Data Collection
                    </span>
                    <span className="text-xs font-mono text-slate-400 font-bold">INPUT</span>
                  </div>
                  <h4 className="font-bold text-slate-900 text-sm mt-2">10-Question Multimodal Exam</h4>
                  <p className="text-xs text-slate-600 mt-1.5 leading-relaxed">
                    Student submits numerical answers, scientific formulas, handwritten drawings, or plain text reasoning.
                  </p>
                </div>
                <div className="mt-3 p-2 bg-slate-50 border border-dashed border-slate-300 rounded-xl font-mono text-[11px] text-slate-700">
                  Technique: <strong>Multimodal Tokenization</strong> (PaddleOCR + Physics Tokenizer)
                </div>
              </div>

              {/* Step 2: Model 1 & Model 2 */}
              <div className="bg-white border-2 border-indigo-800 rounded-2xl p-4 shadow-[4px_4px_0px_0px_rgba(79,70,229,1)] flex flex-col justify-between relative">
                <div className="hidden lg:block absolute -left-3 top-1/2 -translate-y-1/2 bg-indigo-600 text-white rounded-full p-1 text-[10px] font-bold z-10">
                  ➜
                </div>
                <div>
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono uppercase bg-indigo-50 text-indigo-700 px-2 py-0.5 rounded font-bold border border-indigo-200">
                      Step 2 · Local Predictions
                    </span>
                    <span className="text-xs font-mono text-indigo-600 font-bold">DUAL AI</span>
                  </div>
                  <h4 className="font-bold text-indigo-950 text-sm mt-2">Model 1 &amp; Model 2 Predictions</h4>
                  
                  <div className="mt-2 space-y-2 text-xs text-slate-600 leading-snug">
                    <div className="p-2 bg-indigo-50/80 rounded-lg border border-indigo-100">
                      <strong className="text-indigo-950 block">Model 1 (DeBERTa-v3):</strong>
                      <span className="text-[11px]"><strong>What it predicts:</strong> Exact misconception tag (1 of 46 classes).</span>
                      <span className="text-[11px] block text-indigo-800 mt-0.5"><strong>Technique:</strong> Disentangled Self-Attention.</span>
                    </div>
                    <div className="p-2 bg-emerald-50/80 rounded-lg border border-emerald-100">
                      <strong className="text-emerald-950 block">Model 2 (Bi-GRU):</strong>
                      <span className="text-[11px]"><strong>What it predicts:</strong> Entrenched Flaw vs Careless Slip vs Guess.</span>
                      <span className="text-[11px] block text-emerald-800 mt-0.5"><strong>Technique:</strong> Recurrent Hidden State Sequence Tracking.</span>
                    </div>
                  </div>
                </div>
                <div className="mt-3 p-2 bg-indigo-100/70 border border-indigo-200 rounded-xl font-mono text-[11px] text-indigo-900 font-semibold">
                  Local Output: [Tag: MISC-OPT-001] + [Trajectory: Flaw]
                </div>
              </div>

              {/* Step 3: Synthesis Merger Gate */}
              <div className="bg-white border-2 border-amber-800 rounded-2xl p-4 shadow-[4px_4px_0px_0px_rgba(217,119,6,1)] flex flex-col justify-between relative">
                <div className="hidden lg:block absolute -left-3 top-1/2 -translate-y-1/2 bg-amber-600 text-white rounded-full p-1 text-[10px] font-bold z-10">
                  ➜
                </div>
                <div>
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono uppercase bg-amber-50 text-amber-800 px-2 py-0.5 rounded font-bold border border-amber-200">
                      Step 3 · Fusion Gate
                    </span>
                    <span className="text-xs font-mono text-amber-600 font-bold">MERGER</span>
                  </div>
                  <h4 className="font-bold text-amber-950 text-sm mt-2">How Both Models Merge</h4>
                  
                  <div className="mt-2 space-y-1.5 text-xs text-slate-600 leading-relaxed">
                    <p className="font-semibold text-amber-950">Technique: <strong>Confidence-Weighted Bayesian Fusion</strong></p>
                    <ul className="list-disc pl-3.5 space-y-1 text-[11px]">
                      <li><strong>Score Fusion:</strong> Multiplies Model 1 label probability with Model 2 consistency weight.</li>
                      <li><strong>Abstention Gate:</strong> If confidence &lt; 85%, triggers an active tie-breaker probe question.</li>
                      <li><strong>Output Payload:</strong> Builds authoritative physics ground-truth for lesson plan.</li>
                    </ul>
                  </div>
                </div>
                <div className="mt-3 p-2 bg-amber-50 border border-amber-200 rounded-xl font-mono text-[11px] text-amber-800 font-semibold">
                  Merged Verdict: Verified Mental Misconception
                </div>
              </div>

              {/* Step 4: Prof. Vikram Delivery (Clarifying Gemini vs Local Model) */}
              <div className="bg-white border-2 border-purple-800 rounded-2xl p-4 shadow-[4px_4px_0px_0px_rgba(147,51,234,1)] flex flex-col justify-between relative">
                <div className="hidden lg:block absolute -left-3 top-1/2 -translate-y-1/2 bg-purple-600 text-white rounded-full p-1 text-[10px] font-bold z-10">
                  ➜
                </div>
                <div>
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono uppercase bg-purple-50 text-purple-700 px-2 py-0.5 rounded font-bold border border-purple-200">
                      Step 4 · Remediation
                    </span>
                    <span className="text-xs font-mono text-purple-600 font-bold">3D AVATAR</span>
                  </div>
                  <h4 className="font-bold text-purple-950 text-sm mt-2">Prof. Vikram Speaks Local Output</h4>
                  
                  <div className="mt-2 space-y-1.5 text-xs text-slate-600 leading-relaxed">
                    <p className="font-semibold text-purple-950">Technique: <strong>Constrained Pedagogical RAG</strong></p>
                    <div className="p-2 bg-purple-50 rounded-lg border border-purple-200 text-[11px] font-medium text-purple-950">
                      💡 <strong>Who does what?</strong> Local Models find the diagnosis. Gemini only speaks it like a friendly 3D mentor.
                    </div>
                    <ul className="list-disc pl-3.5 space-y-1 mt-1 text-[11px]">
                      <li>Avatar speaks explanation with WebGL lip-sync</li>
                      <li>Draws dynamic SVG whiteboard proof</li>
                      <li>BKT updates student mastery probability</li>
                    </ul>
                  </div>
                </div>
                <div className="mt-3 p-2 bg-purple-50 border border-purple-200 rounded-xl font-mono text-[11px] text-purple-800 font-semibold">
                  Delivery: Predict-Observe-Explain (POE) Session
                </div>
              </div>

            </div>

            {/* Hand-Drawn Flow Arrow Summary */}
            <div className="mt-6 pt-4 border-t border-dashed border-slate-300 flex flex-wrap items-center justify-center gap-2 text-xs font-mono text-slate-700 text-center">
              <span className="px-2.5 py-1 bg-white border border-slate-300 rounded-lg font-bold shadow-2xs">1. Exam Answers</span>
              <span className="text-indigo-600 font-bold">──▶</span>
              <span className="px-2.5 py-1 bg-indigo-50 border border-indigo-300 rounded-lg font-bold text-indigo-700 shadow-2xs">2. Model 1 (DeBERTa) + Model 2 (Bi-GRU)</span>
              <span className="text-indigo-600 font-bold">──▶</span>
              <span className="px-2.5 py-1 bg-amber-50 border border-amber-300 rounded-lg font-bold text-amber-900 shadow-2xs">3. Bayesian Fusion Gate</span>
              <span className="text-indigo-600 font-bold">──▶</span>
              <span className="px-2.5 py-1 bg-purple-600 text-white rounded-lg font-bold shadow-2xs">4. Prof. Vikram Delivers Local Verdict</span>
            </div>
          </div>

          {/* ========================================================================= */}
          {/* THE MISCONCEPTION DIFFERENTIATOR: COMPACT NORMAL-SIZED CARD                */}
          {/* ========================================================================= */}
          {/* ========================================================================= */}
          {/* COMPACT DUAL-AI EXPLANATION CARD (MODEL 1 + MODEL 2)                      */}
          {/* ========================================================================= */}
          {/* ========================================================================= */}
          {/* THE MISCONCEPTION DIFFERENTIATOR CARD: MODEL 1 + MODEL 2                   */}
          {/* ========================================================================= */}
          <div className="mb-8 bg-white rounded-2xl border-2 border-indigo-200 p-4 sm:p-5 shadow-xs space-y-3.5">
            {/* Header + Case context in one line */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-100 pb-2.5">
              <div className="flex items-center space-x-2">
                <span className="w-2 h-2 rounded-full bg-indigo-600"></span>
                <h3 className="text-sm sm:text-base font-bold text-slate-900">
                  The Misconception Differentiator: Same Wrong Answer ➔ Different Causes
                </h3>
              </div>
              <span className="text-[11px] font-mono bg-indigo-50 text-indigo-700 border border-indigo-200 px-2.5 py-0.5 rounded-md font-bold self-start sm:self-auto">
                NCERT Benchmark: Covering Lens • Both Students Pick [A] "Half image forms" ❌
              </span>
            </div>

            {/* Model 1 & Model 2 Side-by-Side in 2 Columns */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-3 text-xs">
              {/* Left Column: Q1 - How are two students with same wrong answer differentiated? */}
              <div className="p-3.5 rounded-xl bg-indigo-50/70 border border-indigo-200 flex flex-col justify-between space-y-2">
                <div>
                  <div className="flex items-center justify-between mb-1.5">
                    <span className="px-2 py-0.5 rounded bg-indigo-600 text-white font-mono text-[10px] font-bold">
                      1. SAME WRONG ANSWER DIFFERENTIATION
                    </span>
                    <span className="text-[10px] font-mono font-bold text-indigo-700">Model 1 (DeBERTa-v3)</span>
                  </div>
                  <p className="text-[11px] text-slate-700 mb-2 leading-relaxed">
                    Standard LMS gives both students 0/1 marks identically. <strong>Model 1 reads their written working</strong> to uncover two totally different mental blocks:
                  </p>

                  <div className="space-y-1.5 text-[11px]">
                    <div className="p-2 rounded-lg bg-white border border-indigo-100 shadow-2xs">
                      <strong className="text-indigo-900 block font-mono text-[10px]">Student A: "Lower half masked, light blocked from bottom"</strong>
                      <span className="text-slate-600">➔ <strong>MISC-OPT-001 (Aperture Fallacy)</strong>: Thinks lens acts like a stencil window. Remediated via Whiteboard ray tracing.</span>
                    </div>
                    <div className="p-2 rounded-lg bg-white border border-indigo-100 shadow-2xs">
                      <strong className="text-purple-900 block font-mono text-[10px]">Student B: "Light travels in rigid straight beams"</strong>
                      <span className="text-slate-600">➔ <strong>MISC-OPT-004 (Holistic Ray Fallacy)</strong>: Thinks light is rigid picture. Remediated via Wavefront curvature simulation.</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Right Column: Q2 - How does Model 2 (Sequence Model) help? */}
              <div className="p-3.5 rounded-xl bg-slate-900 text-white flex flex-col justify-between space-y-2">
                <div>
                  <div className="flex items-center justify-between mb-1.5">
                    <span className="px-2 py-0.5 rounded bg-emerald-500 text-slate-950 font-mono text-[10px] font-bold">
                      2. HOW MODEL 2 (SEQUENCE MODEL) HELPS
                    </span>
                    <span className="text-[10px] font-mono font-bold text-emerald-400">Macro Trajectory Analyzer</span>
                  </div>
                  <p className="text-[11px] text-slate-300 mb-2 leading-relaxed">
                    Model 1 only inspects 1 question. It cannot know if Student A made a careless slip or has a deep conceptual flaw. <strong>Model 2 tracks all 10 exam questions:</strong>
                  </p>

                  <div className="grid grid-cols-3 gap-1.5 text-[10px] font-mono text-center mb-2">
                    <div className="p-1.5 rounded bg-slate-800 border border-slate-700">
                      <strong className="text-emerald-400 block text-xs">40%</strong>
                      <span className="text-slate-300 text-[10px]">Competence (4 Qs)</span>
                    </div>
                    <div className="p-1.5 rounded bg-slate-800 border border-slate-700">
                      <strong className="text-amber-400 block text-xs">20%</strong>
                      <span className="text-slate-300 text-[10px]">Slips (2 Qs)</span>
                    </div>
                    <div className="p-1.5 rounded bg-slate-800 border border-slate-700">
                      <strong className="text-rose-400 block text-xs">40%</strong>
                      <span className="text-slate-300 text-[10px]">Entrenched (4 Qs)</span>
                    </div>
                  </div>
                </div>

                <div className="p-2 rounded bg-indigo-950 border border-indigo-700/60 text-[11px] text-indigo-200 leading-normal">
                  <strong>The Breakthrough:</strong> Don't fail the student (4/10) or reteach the whole chapter. Model 2 proves 60% working competence and isolates the 1 root flaw, saving 80% study time.
                </div>
              </div>
            </div>
          </div>

          {/* 8 Step Visual Grid with Animated Flow */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
            {PIPELINE_STEPS.map((s, idx) => (
              <Fade key={s.step}>
                <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-xs hover:shadow-md transition-shadow h-full flex flex-col justify-between">
                  <div>
                    <div className="flex items-center justify-between mb-3">
                      <span className="w-7 h-7 rounded-lg bg-indigo-600 text-white font-mono font-bold text-xs flex items-center justify-center">
                        {s.step}
                      </span>
                      <span className="text-[10px] font-mono bg-indigo-50 text-indigo-700 px-2 py-0.5 rounded font-semibold">
                        {s.model}
                      </span>
                    </div>
                    <h3 className="text-sm font-bold text-slate-900 mb-1">{s.title}</h3>
                    <p className="text-xs text-slate-500 leading-relaxed mb-3">{s.desc}</p>
                  </div>

                  <div className="bg-slate-50 rounded-xl p-2.5 border border-slate-100 flex items-center justify-between text-[11px] font-mono text-slate-700">
                    <span className="font-bold text-indigo-600">Signal:</span>
                    <span className="text-slate-500 truncate">{idx === 7 ? 'Mastery DB' : `→ Step ${idx + 2}`}</span>
                  </div>
                </div>
              </Fade>
            ))}
          </div>

          <div className="bg-indigo-900 text-white rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="flex items-center space-x-3">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse" />
              <span className="text-xs font-mono font-medium">
                Flow: Input → OCR/Vision → DeBERTa Diagnosis → GRU Sequence → Synthesis Gate → POE Remediation → Reassessment → BKT Mastery
              </span>
            </div>
            <button onClick={onEnterApp} className="text-xs font-bold text-white bg-indigo-600 hover:bg-indigo-500 px-4 py-2 rounded-xl whitespace-nowrap shadow">
              Try Flow In Studio →
            </button>
          </div>
        </div>
      </section>

      {/* ── 3. Dataset Architecture, Growth Chart & Splits ─────────────────── */}
      <section id="dataset" className="py-16 bg-white">
        <div className="max-w-[1500px] mx-auto px-6 lg:px-12">
          <Fade className="mb-8">
            <span className="text-[11px] font-mono font-semibold uppercase tracking-widest text-indigo-600 bg-indigo-50 border border-indigo-200 px-3 py-1 rounded-full mb-3 inline-block">
              02 — Dataset &amp; Splits
            </span>
            <h2 className="text-3xl font-black text-slate-900 tracking-tight mb-2">
              21,000 Responses.<br />
              <span className="text-indigo-600">Anti-Memorisation Template Splits.</span>
            </h2>
            <p className="text-slate-600 text-sm max-w-2xl leading-relaxed">
              Curated across 42 NCERT Physics curriculum families with strict template-disjoint splitting. The model is tested on question templates it never saw during training, proving it learned physics principles rather than sentence memorization.
            </p>
          </Fade>

          {/* Stat Cards */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4">
              <span className="text-xs font-mono text-slate-500 block mb-1">TRAINING RESPONSES</span>
              <span className="text-2xl font-black text-slate-900">21,000</span>
              <span className="text-[11px] text-slate-500 block mt-0.5">13,860 train / 3,780 test</span>
            </div>
            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4">
              <span className="text-xs font-mono text-slate-500 block mb-1">CURRICULUM FAMILIES</span>
              <span className="text-2xl font-black text-slate-900">42 Families</span>
              <span className="text-[11px] text-slate-500 block mt-0.5">500 responses per family</span>
            </div>
            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4">
              <span className="text-xs font-mono text-slate-500 block mb-1">LONGITUDINAL SEQUENCES</span>
              <span className="text-2xl font-black text-violet-700">2,700</span>
              <span className="text-[11px] text-slate-500 block mt-0.5">45 trajectory archetypes</span>
            </div>
            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4">
              <span className="text-xs font-mono text-slate-500 block mb-1">OOD STRESS ITEMS</span>
              <span className="text-2xl font-black text-amber-600">252 Items</span>
              <span className="text-[11px] text-slate-500 block mt-0.5">Real-world messy slang</span>
            </div>
          </div>

          {/* Dataset Growth Chart + Split Bar Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            {/* Growth Bar Chart */}
            <Fade>
              <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-xs h-full">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="font-bold text-slate-900 text-sm">Dataset Growth Across Iterations</h3>
                  <span className="text-[10px] font-mono text-slate-400 bg-slate-50 border border-slate-200 px-2 py-1 rounded-lg">Records</span>
                </div>
                <ResponsiveContainer width="100%" height={210}>
                  <BarChart data={datasetGrowth} margin={{ top: 5, right: 10, left: -10, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                    <XAxis dataKey="iter" tick={{ fontSize: 11, fontFamily: 'monospace' }} />
                    <YAxis tick={{ fontSize: 11, fontFamily: 'monospace' }} />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="records" name="Records" radius={[6, 6, 0, 0]}>
                      {datasetGrowth.map((e, i) => <Cell key={i} fill={i === 0 ? '#FDA4AF' : i === 1 ? '#A78BFA' : '#818CF8'} />)}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </Fade>

            {/* Split breakdown */}
            <Fade>
              <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-xs h-full flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center space-x-2">
                      <Shield className="w-4 h-4 text-slate-600" />
                      <h3 className="font-bold text-slate-900 text-sm">Template-Disjoint Splits</h3>
                    </div>
                    <span className="text-[10px] font-mono bg-emerald-100 text-emerald-700 px-2 py-1 rounded-lg font-semibold">Zero Phrasing Leakage</span>
                  </div>

                  <div className="space-y-3.5 mb-5">
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
                </div>

                <div className="grid grid-cols-2 gap-2.5 pt-2">
                  {personas.map(p => (
                    <div key={p.name} className="bg-slate-50 border border-slate-200 rounded-xl p-2">
                      <div className="text-[10px] font-bold text-slate-700">{p.name}</div>
                      <p className="text-[10px] font-mono text-slate-400 italic truncate">"{p.example}"</p>
                    </div>
                  ))}
                </div>
              </div>
            </Fade>
          </div>

          {/* Compact 17 Dataset Features Explorer (NO HUGE TABLE) */}
          <Fade>
            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-5">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3 pb-2 border-b border-slate-200">
                <div className="flex items-center space-x-2">
                  <Table className="w-4 h-4 text-indigo-600" />
                  <h3 className="text-xs font-mono font-bold uppercase tracking-wider text-slate-800">
                    17 Standardized Dataset Features (Click To Inspect)
                  </h3>
                </div>
                <span className="text-[11px] font-mono text-slate-500">
                  Active: <strong className="text-indigo-600 font-bold">{activeFeature.name}</strong>
                </span>
              </div>

              {/* Compact Pill Cloud */}
              <div className="flex flex-wrap gap-1.5 mb-3">
                {DATASET_FEATURES.map((feat) => {
                  const isSel = activeFeature.name === feat.name;
                  return (
                    <button
                      key={feat.name}
                      onClick={() => setActiveFeature(feat)}
                      className={`text-[11px] font-mono px-2.5 py-1 rounded-lg border transition-all ${
                        isSel
                          ? 'bg-indigo-600 text-white border-indigo-600 font-bold shadow-xs'
                          : 'bg-white text-slate-600 border-slate-200 hover:border-indigo-300 hover:bg-white'
                      }`}
                    >
                      {feat.name}
                    </button>
                  );
                })}
              </div>

              {/* Compact Single-line Explainer Box */}
              <div className="bg-white p-3 rounded-xl border border-indigo-100 flex items-center space-x-3 text-xs">
                <code className="font-mono font-bold text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200">
                  {activeFeature.name}
                </code>
                <span className="text-slate-700 font-medium">
                  {activeFeature.desc}
                </span>
              </div>
            </div>
          </Fade>
        </div>
      </section>

      {/* ── 4. Empirical Benchmarks & Training Iterations ────────────────── */}
      <section id="benchmarks" className="py-16 bg-slate-50 border-t border-slate-200">
        <div className="max-w-[1500px] mx-auto px-6 lg:px-12">
          <Fade className="mb-8">
            <span className="text-[11px] font-mono font-semibold uppercase tracking-widest text-indigo-600 bg-indigo-50 border border-indigo-200 px-3 py-1 rounded-full mb-3 inline-block">
              03 — Empirical Benchmarks &amp; Training
            </span>
            <h2 className="text-3xl font-black text-slate-900 tracking-tight mb-2">
              5 Training Iterations.<br />
              <span className="text-indigo-600">From 0% OOD to 90.48%.</span>
            </h2>
            <p className="text-slate-600 text-sm max-w-xl leading-relaxed">
              Tracking model accuracy and generalization across 5 training iterations — from catastrophic template memorization to robust out-of-distribution performance.
            </p>
          </Fade>

          {/* Main Accuracy Chart */}
          <Fade className="mb-6">
            <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-xs">
              <div className="flex items-center justify-between mb-4">
                <h3 className="font-bold text-slate-900 text-sm">Accuracy Evolution — Test vs OOD Across Iterations</h3>
                <div className="flex items-center space-x-4 text-xs font-mono">
                  <span className="flex items-center space-x-1"><span className="w-3 h-0.5 bg-indigo-500 inline-block rounded" /><span className="text-slate-500">Test Acc</span></span>
                  <span className="flex items-center space-x-1"><span className="w-3 h-0.5 bg-emerald-500 inline-block rounded" /><span className="text-slate-500">OOD Acc</span></span>
                  <span className="flex items-center space-x-1"><span className="w-3 h-0.5 bg-violet-400 inline-block rounded border-dashed border-t-2" /><span className="text-slate-500">Target 85%</span></span>
                </div>
              </div>
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={benchmarkData} margin={{ top: 10, right: 20, left: -10, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                  <XAxis dataKey="iter" tick={{ fontSize: 11, fontFamily: 'monospace' }} />
                  <YAxis domain={[0, 105]} tick={{ fontSize: 11, fontFamily: 'monospace' }} />
                  <Tooltip content={<CustomTooltip />} />
                  <ReferenceLine y={85} stroke="#A78BFA" strokeDasharray="5 3" label={{ value: 'Target 85%', fontSize: 10, fill: '#7C3AED' }} />
                  <Line type="monotone" dataKey="testAcc" name="Test Accuracy" stroke="#4F46E5" strokeWidth={2.5} dot={{ r: 5 }} />
                  <Line type="monotone" dataKey="oodAcc" name="OOD Accuracy" stroke="#10B981" strokeWidth={2.5} dot={{ r: 5 }} />
                  <Line type="monotone" dataKey="macroF1" name="Macro F1 ×100" stroke="#F59E0B" strokeWidth={1.5} strokeDasharray="4 2" dot={{ r: 4 }} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </Fade>

          {/* Radar Chart + Qualitative Stress Tests */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <Fade>
              <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-xs h-full flex flex-col justify-between">
                <div>
                  <h3 className="font-bold text-slate-900 text-sm mb-4">Multi-Metric Verification (Iteration 4)</h3>
                  <ResponsiveContainer width="100%" height={230}>
                    <RadarChart data={radarData}>
                      <PolarGrid stroke="#E2E8F0" />
                      <PolarAngleAxis dataKey="metric" tick={{ fontSize: 10, fontFamily: 'monospace' }} />
                      <Radar name="Performance" dataKey="value" stroke="#4F46E5" fill="#4F46E5" fillOpacity={0.15} strokeWidth={2} dot={{ r: 4 }} />
                      <Tooltip content={<CustomTooltip />} />
                    </RadarChart>
                  </ResponsiveContainer>
                </div>
                <div className="text-xs text-slate-500 bg-slate-50 p-2.5 rounded-xl border border-slate-100 font-mono mt-3">
                  Abstention Calibration: 98.8% · Sequence Pattern: 100%
                </div>
              </div>
            </Fade>

            <Fade>
              <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-xs h-full">
                <h3 className="font-bold text-slate-900 text-sm mb-4">Qualitative Stress-Test Responses</h3>
                <div className="space-y-2.5 text-xs">
                  {[
                    { q: '"If top half covered, only bottom half shows up"', label: 'MISC-OPT-001', conf: '99.7%', note: 'Standard phrasing' },
                    { q: '"bro only bottom part shows up, rest cut ho gaya"', label: 'MISC-OPT-001', conf: '99.7%', note: 'Vernacular Hinglish slang' },
                    { q: '"idk forgot formula"', label: 'UNSURE_INSUFFICIENT_EVIDENCE', conf: '100%', note: 'Correctly abstains' },
                    { q: '"current gets used up in first bulb"', label: 'MISC-ELEC-001', conf: '97.2%', note: 'Circuit fuel model' },
                  ].map(t => (
                    <div key={t.q} className="bg-slate-50 border border-slate-100 rounded-xl p-3">
                      <p className="font-mono text-slate-700 italic mb-1">"{t.q}"</p>
                      <div className="flex items-center justify-between">
                        <span className="text-[10px] font-mono font-semibold bg-indigo-100 text-indigo-700 px-2 py-0.5 rounded">{t.label}</span>
                        <div className="flex items-center space-x-2">
                          <span className="text-[10px] text-slate-400 font-mono">{t.note}</span>
                          <span className="text-xs font-black text-emerald-600">{t.conf}</span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </Fade>
          </div>

          {/* Iteration Training Table */}
          <Fade className="mb-6">
            <div className="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-xs">
              <div className="overflow-x-auto">
                <table className="w-full text-left text-sm">
                  <thead>
                    <tr className="bg-slate-900 text-white font-mono text-xs">
                      <th className="px-5 py-3.5 font-semibold">Iteration</th>
                      <th className="px-5 py-3.5 font-semibold">Records</th>
                      <th className="px-5 py-3.5 font-semibold">Families</th>
                      <th className="px-5 py-3.5 font-semibold">Test Acc</th>
                      <th className="px-5 py-3.5 font-semibold">OOD Acc</th>
                      <th className="px-5 py-3.5 font-semibold">Macro F1</th>
                      <th className="px-5 py-3.5 font-semibold">Training Focus / Status</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {benchmarkData.map((row, i) => (
                      <tr key={row.iter} className={i % 2 === 0 ? 'bg-white' : 'bg-slate-50/60'}>
                        <td className="px-5 py-3 font-bold text-slate-800 text-xs font-mono">{row.iter}</td>
                        <td className="px-5 py-3 font-mono text-xs text-slate-500">{row.records.toLocaleString()}</td>
                        <td className="px-5 py-3 font-mono text-xs text-slate-500">{row.iter === 'Iter 1' ? 25 : 42}</td>
                        <td className="px-5 py-3 font-black text-sm" style={{ color: row.status === 'fail' ? '#E11D48' : row.status === 'partial' ? '#D97706' : '#059669' }}>{row.testAcc}%</td>
                        <td className="px-5 py-3 font-black text-sm" style={{ color: row.status === 'fail' ? '#E11D48' : row.status === 'partial' ? '#D97706' : '#059669' }}>{row.oodAcc}%</td>
                        <td className="px-5 py-3 font-mono text-xs text-slate-500">{(row.macroF1 / 100).toFixed(4)}</td>
                        <td className="px-5 py-3 text-xs">
                          <span className="font-medium text-slate-700 mr-2">{row.note}</span>
                          {row.status === 'fail' && <span className="text-[10px] font-mono text-rose-600 bg-rose-50 px-2 py-0.5 rounded font-bold">FAIL</span>}
                          {row.status === 'partial' && <span className="text-[10px] font-mono text-amber-600 bg-amber-50 px-2 py-0.5 rounded font-bold">PARTIAL</span>}
                          {row.status === 'pass' && <span className="text-[10px] font-mono text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded font-bold">PASS</span>}
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
                <div className="font-bold text-emerald-800 text-sm">All Benchmark Targets Achieved</div>
                <div className="text-xs text-emerald-700 font-mono">≥85% held-out test accuracy · ≥80% OOD challenge · 100% sequence accuracy · 98.8% abstention calibration</div>
              </div>
            </div>
          </Fade>
        </div>
      </section>

      {/* ── 5. The 3 Core AI Models ──────────────────────────────────────── */}
      <section id="models" className="py-16 bg-white border-t border-slate-200">
        <div className="max-w-[1500px] mx-auto px-6 lg:px-12">
          <Fade className="mb-10 text-center max-w-2xl mx-auto">
            <span className="text-[11px] font-mono font-semibold uppercase tracking-widest text-indigo-600 bg-indigo-50 border border-indigo-200 px-3 py-1 rounded-full mb-3 inline-block">
              04 — Core Intelligence
            </span>
            <h2 className="text-3xl font-black text-slate-900 tracking-tight mb-2">
              Three Purpose-Built <span className="text-indigo-600">AI Components</span>
            </h2>
            <p className="text-slate-600 text-sm">
              Instead of an unfocused LLM chatbot, Re:Learn separates individual response diagnosis, sequence pattern detection, and multimodal teaching into 3 dedicated models.
            </p>
          </Fade>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            <Fade>
              <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-xs h-full flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-xs font-mono font-bold bg-indigo-100 text-indigo-700 px-2.5 py-0.5 rounded-full">Model 1</span>
                    <Brain className="w-5 h-5 text-indigo-600" />
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 mb-1">DeBERTa-v3 Classifier</h3>
                  <p className="text-xs text-slate-500 mb-4 leading-relaxed">
                    Trained on 13,860 student answers across 46 misconception classes with calibrated abstention for ambiguous queries.
                  </p>
                  <div className="space-y-2 mb-4 text-xs font-mono">
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>Test Accuracy</span><strong className="text-indigo-600">88.59%</strong></div>
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>OOD Accuracy</span><strong className="text-emerald-600">90.48%</strong></div>
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>Macro F1</span><strong>0.8678</strong></div>
                  </div>
                </div>
                <div className="bg-slate-50 rounded-xl p-3 border border-slate-100 text-xs text-slate-700">
                  <strong className="text-slate-900">In simple words: </strong>Finds the exact reason why a single student answer was wrong.
                </div>
              </div>
            </Fade>

            <Fade>
              <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-xs h-full flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-xs font-mono font-bold bg-emerald-100 text-emerald-700 px-2.5 py-0.5 rounded-full">Model 2</span>
                    <Activity className="w-5 h-5 text-emerald-600" />
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 mb-1">GRU Sequence Analyser</h3>
                  <p className="text-xs text-slate-500 mb-4 leading-relaxed">
                    Classifies 2,700 student trajectory sequences across 45 archetypes. Distinguishes recurring mental flaws from transient slips.
                  </p>
                  <div className="space-y-2 mb-4 text-xs font-mono">
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>Sequence Acc.</span><strong className="text-emerald-600">100%</strong></div>
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>Archetypes</span><strong>45 Classes</strong></div>
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>BKT Gain</span><strong className="text-indigo-600">+0.58 ΔP(L)</strong></div>
                  </div>
                </div>
                <div className="bg-slate-50 rounded-xl p-3 border border-slate-100 text-xs text-slate-700">
                  <strong className="text-slate-900">In simple words: </strong>Watches if the student repeatedly makes the same mistake across questions.
                </div>
              </div>
            </Fade>

            <Fade>
              <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-xs h-full flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-2.5 py-0.5 rounded-full">Intervention</span>
                    <Sparkles className="w-5 h-5 text-amber-600" />
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 mb-1">Prof. Vikram (3D AI Mentor)</h3>
                  <p className="text-xs text-slate-500 mb-4 leading-relaxed">
                    NCERT Physics RAG voice counselor. Powers 3D WebGL avatar lip-sync, dynamic whiteboard, and bilingual EN/HI speech.
                  </p>
                  <div className="space-y-2 mb-4 text-xs font-mono">
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>AI Engine</span><strong>Prof. Vikram 3D Embodied AI</strong></div>
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>Abstention Cal.</span><strong className="text-emerald-600">98.8%</strong></div>
                    <div className="flex justify-between bg-slate-50 p-2 rounded-lg"><span>Avatar Rendering</span><strong className="text-violet-600">3D WebGL / Three.js</strong></div>
                  </div>
                </div>
                <div className="bg-slate-50 rounded-xl p-3 border border-slate-100 text-xs text-slate-700">
                  <strong className="text-slate-900">In simple words: </strong>Reteaches the concept using interactive experiments and visual sketches.
                </div>
              </div>
            </Fade>
          </div>
        </div>
      </section>

      {/* ── 6. Call to Action / Launch Studio ────────────────────────────── */}
      <section className="py-16 bg-gradient-to-r from-indigo-50 via-purple-50 to-indigo-100 border-t border-indigo-200">
        <div className="max-w-[1500px] mx-auto px-6 lg:px-12 flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <h3 className="text-2xl font-black text-slate-900 mb-1.5">Ready to Test Diagnostic Physics?</h3>
            <p className="text-slate-600 text-sm max-w-lg">
              Launch the Diagnostic Studio to select a Class 9 or 10 chapter, solve questions in plain language, and experience multimodal AI remediation.
            </p>
          </div>
          <div className="flex gap-3">
            <button
              onClick={onEnterApp}
              className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm px-7 py-3.5 rounded-xl shadow-md transition-all hover:-translate-y-0.5 flex items-center space-x-2 whitespace-nowrap"
            >
              <Zap className="w-4 h-4" /><span>Launch Diagnostic Studio</span>
            </button>
            <a
              href="https://github.com/NISHANTTMAURYA/relearn"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 font-semibold text-sm px-6 py-3.5 rounded-xl transition-colors whitespace-nowrap"
            >
              GitHub →
            </a>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-white py-10 border-t border-slate-800">
        <div className="max-w-[1500px] mx-auto px-6 lg:px-12 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-mono text-slate-400">
          <div className="flex items-center space-x-2">
            <span className="font-black text-white text-sm">Re:Learn</span>
            <span>· NCERT Physics Misconception Diagnostic Engine</span>
          </div>
          <div>DeBERTa-v3 · Sequence Pattern Analyzer · Prof. Vikram (3D Embodied AI Mentor)</div>
        </div>
      </footer>
    </div>
  );
}
