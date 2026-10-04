import React, { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw, ChevronRight, ChevronLeft, PenTool, Code, CheckCircle2 } from 'lucide-react';

export default function WhiteboardCanvas({
  commands = [],
  plan = null,
  miscId = '',
  title = 'Structured AI Physics Whiteboard'
}) {
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [showDslInspector, setShowDslInspector] = useState(false);

  // If a dynamic plan from /api/generate-whiteboard is supplied, use its steps
  const stepsData = plan?.steps || [];
  const totalSteps = stepsData.length > 0 ? stepsData.length : 4;

  useEffect(() => {
    let timer;
    if (isPlaying) {
      timer = setInterval(() => {
        setCurrentStep((prev) => {
          if (prev >= totalSteps - 1) {
            setIsPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, 2400);
    }
    return () => clearInterval(timer);
  }, [isPlaying, totalSteps]);

  // Diagram flags for fallback SVG
  const isOptics = !miscId || miscId.includes('OPT') || miscId.toLowerCase().includes('lens');
  const isElec = miscId.includes('ELEC') || miscId.toLowerCase().includes('current') || miscId.toLowerCase().includes('circuit');
  const isMech = miscId.includes('MECH') || miscId.includes('GRAV') || miscId.includes('MOT');

  // Active step details
  const activeStepObj = stepsData[currentStep];
  const stepTitle = activeStepObj?.title || `Step ${currentStep + 1}`;
  const stepNarration = activeStepObj?.narration;
  const boardInstruction = activeStepObj?.board_instruction || commands[currentStep] || (
    currentStep === 0 ? 'Setup experimental physical apparatus and reference coordinates.' :
    currentStep === 1 ? 'Trace primary physical vectors and rays according to scientific laws.' :
    currentStep === 2 ? 'Apply experimental constraint (masking aperture / measuring series currents).' :
    'Observe counter-intuitive proof reconciling cognitive conflict.'
  );

  // Collect all actions up to currentStep for dynamic rendering
  const accumulatedActions = [];
  if (stepsData.length > 0) {
    for (let i = 0; i <= currentStep; i++) {
      if (stepsData[i]?.actions) {
        accumulatedActions.push(...stepsData[i].actions);
      }
    }
  }

  return (
    <div className="editorial-card overflow-hidden bg-white border border-border shadow-sm">
      {/* Whiteboard Top Toolbar */}
      <div className="bg-slate-100/90 px-4 py-2.5 border-b border-border flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center space-x-2">
          <PenTool className="w-4 h-4 text-indigo-600" />
          <span className="text-xs font-mono font-semibold uppercase tracking-wider text-charcoal">
            {plan?.board_title || title}
          </span>
          <span className="text-xs text-indigo-700 bg-indigo-50 border border-indigo-200 px-2 py-0.5 rounded font-mono font-medium">
            Step {currentStep + 1} of {totalSteps}
          </span>
        </div>

        {/* Playback Controls & DSL Toggle */}
        <div className="flex items-center space-x-2">
          <button
            onClick={() => setShowDslInspector(!showDslInspector)}
            className={`px-2 py-1 text-xs font-mono rounded border flex items-center space-x-1 transition-colors ${
              showDslInspector
                ? 'bg-indigo-600 text-white border-indigo-600'
                : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
            }`}
            title="Inspect Model Drawing DSL JSON"
          >
            <Code className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">DSL Inspector</span>
          </button>

          <div className="h-4 w-px bg-slate-300 mx-1 hidden sm:block"></div>

          <button
            onClick={() => setCurrentStep(Math.max(0, currentStep - 1))}
            disabled={currentStep === 0}
            className="p-1 rounded text-slate-700 hover:bg-slate-200 disabled:opacity-30"
            title="Previous Step"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>

          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="px-2.5 py-1 text-xs font-medium rounded bg-charcoal text-white hover:bg-slate-800 flex items-center space-x-1"
          >
            {isPlaying ? <Pause className="w-3 h-3" /> : <Play className="w-3 h-3" />}
            <span>{isPlaying ? 'Pause' : 'Animate Step-by-Step'}</span>
          </button>

          <button
            onClick={() => setCurrentStep(Math.min(totalSteps - 1, currentStep + 1))}
            disabled={currentStep === totalSteps - 1}
            className="p-1 rounded text-slate-700 hover:bg-slate-200 disabled:opacity-30"
            title="Next Step"
          >
            <ChevronRight className="w-4 h-4" />
          </button>

          <button
            onClick={() => {
              setCurrentStep(0);
              setIsPlaying(false);
            }}
            className="p-1 rounded text-slate-500 hover:bg-slate-200"
            title="Reset"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* DSL Code Inspector Modal / Drawer */}
      {showDslInspector && (
        <div className="p-3 bg-slate-900 text-slate-100 border-b border-slate-800 text-xs font-mono max-h-48 overflow-y-auto">
          <div className="flex items-center justify-between pb-1 border-b border-slate-800 mb-2">
            <span className="text-emerald-400 font-bold">
              // Model Structured Drawing DSL Output (Step {currentStep + 1})
            </span>
            <span className="text-slate-400 text-[10px]">Zero training needed • LLM JSON schema</span>
          </div>
          <pre className="text-[11px] leading-relaxed overflow-x-auto text-slate-300">
            {JSON.stringify(
              stepsData[currentStep] || {
                step_number: currentStep + 1,
                instruction: boardInstruction,
                rendered_mode: 'high_fidelity_vector_svg'
              },
              null,
              2
            )}
          </pre>
        </div>
      )}

      {/* Light Mode Whiteboard Drawing Surface */}
      <div className="relative w-full h-72 sm:h-84 bg-white flex items-center justify-center p-3 border-b border-border">
        {/* Crisp academic millimeter graph background */}
        <div
          className="absolute inset-0 opacity-40 pointer-events-none"
          style={{
            backgroundImage: 'linear-gradient(to right, #E2E8F0 1px, transparent 1px), linear-gradient(to bottom, #E2E8F0 1px, transparent 1px)',
            backgroundSize: '24px 24px'
          }}
        />

        <svg viewBox="0 0 600 300" className="w-full h-full max-h-full">
          {/* If dynamic actions exist, render them */}
          {accumulatedActions.length > 0 ? (
            <g className="transition-all duration-300">
              {accumulatedActions.map((action, i) => {
                if (action.tool === 'line') {
                  return (
                    <line
                      key={i}
                      x1={action.x1}
                      y1={action.y1}
                      x2={action.x2}
                      y2={action.y2}
                      stroke={action.stroke || '#94A3B8'}
                      strokeWidth={action.width || 1.5}
                      strokeDasharray={action.dash}
                    />
                  );
                }
                if (action.tool === 'lens') {
                  return (
                    <ellipse
                      key={i}
                      cx={action.x}
                      cy={action.y}
                      rx={action.rx || 14}
                      ry={action.ry || 95}
                      fill={action.fill || '#F0F9FF'}
                      stroke={action.stroke || '#0284C7'}
                      strokeWidth={2}
                      opacity="0.85"
                    />
                  );
                }
                if (action.tool === 'candle') {
                  return (
                    <g key={i}>
                      <rect x={action.x - 4} y={action.y} width="8" height={action.height || 70} fill="#F59E0B" rx="1" />
                      <circle cx={action.x} cy={action.y - 7} r="6" fill="#F59E0B" />
                      <circle cx={action.x} cy={action.y - 7} r="3" fill="#EF4444" />
                      <text x={action.x - 20} y={action.y + (action.height || 70) + 16} fill="#334155" fontSize="10" fontWeight="bold">
                        {action.label || 'Candle'}
                      </text>
                    </g>
                  );
                }
                if (action.tool === 'screen') {
                  return (
                    <g key={i}>
                      <rect x={action.x - 3} y={action.y} width="6" height={action.height || 210} fill="#E2E8F0" stroke="#64748B" strokeWidth="1.5" />
                      <text x={action.x - 12} y={action.y + (action.height || 210) + 16} fill="#334155" fontSize="10" fontWeight="bold">
                        {action.label || 'Screen'}
                      </text>
                    </g>
                  );
                }
                if (action.tool === 'ray') {
                  return (
                    <g key={i}>
                      <path
                        d={`M ${action.x1} ${action.y1} L ${action.x2} ${action.y2} ${action.x3 !== undefined ? `L ${action.x3} ${action.y3}` : ''}`}
                        fill="none"
                        stroke={action.stroke || '#2563EB'}
                        strokeWidth={action.width || 2}
                        strokeDasharray={action.dash}
                      />
                      {action.label && (
                        <text x={(action.x1 + action.x2) / 2 - 20} y={Math.min(action.y1, action.y2) - 6} fill={action.stroke || '#2563EB'} fontSize="9" fontWeight="bold">
                          {action.label}
                        </text>
                      )}
                    </g>
                  );
                }
                if (action.tool === 'mask') {
                  return (
                    <g key={i}>
                      <rect x={action.x} y={action.y} width={action.width} height={action.height} fill={action.fill || '#1E293B'} rx="2" />
                      {action.label && (
                        <text x={action.x - 30} y={action.y + action.height + 15} fill="#BE123C" fontSize="10" fontWeight="bold">
                          {action.label}
                        </text>
                      )}
                    </g>
                  );
                }
                if (action.tool === 'point') {
                  return <circle key={i} cx={action.cx} cy={action.cy} r={action.r || 4} fill={action.fill || '#DC2626'} />;
                }
                if (action.tool === 'callout') {
                  return (
                    <g key={i}>
                      <rect x={action.x} y={action.y} width={action.width} height={action.height} fill={action.fill || '#FEF3C7'} stroke={action.stroke || '#D97706'} strokeWidth="1.2" rx="4" />
                      <text x={action.x + 10} y={action.y + 24} fontSize="11" fontWeight="bold" fill="#78350F">
                        {action.title}
                      </text>
                    </g>
                  );
                }
                if (action.tool === 'rect') {
                  return (
                    <g key={i}>
                      <rect x={action.x} y={action.y} width={action.width} height={action.height} fill={action.fill || '#F8FAFC'} stroke={action.stroke || '#CBD5E1'} strokeWidth={action.strokeWidth || 1} rx="4" />
                      {action.label && (
                        <text x={action.x + 8} y={action.y + 20} fill="#334155" fontSize="10" fontWeight="bold">
                          {action.label}
                        </text>
                      )}
                    </g>
                  );
                }
                if (action.tool === 'text') {
                  return (
                    <text key={i} x={action.x} y={action.y} fill={action.color || '#334155'} fontWeight={action.weight || 'normal'} fontSize={action.size || 11}>
                      {action.text}
                    </text>
                  );
                }
                return null;
              })}
            </g>
          ) : (
            /* Fallback to Default High-Fidelity SVG Scenes */
            <>
              {/* OPTICS RAY DIAGRAM */}
              {isOptics && (
                <>
                  <g className="transition-opacity duration-500">
                    <line x1="20" y1="150" x2="580" y2="150" stroke="#94A3B8" strokeWidth="1.5" strokeDasharray="4 4" />
                    <ellipse cx="300" cy="150" rx="14" ry="100" fill="#F0F9FF" stroke="#0284C7" strokeWidth="2.5" />
                    <line x1="300" y1="30" x2="300" y2="270" stroke="#0284C7" strokeWidth="1" strokeDasharray="3 3" />
                    
                    {/* Candle Object */}
                    <rect x="75" y="80" width="10" height="70" fill="#F59E0B" rx="1" />
                    <path d="M80 80 Q76 65, 80 50 Q84 65, 80 80 Z" fill="#EF4444" />
                    <text x="65" y="170" fill="#334155" fontSize="11" fontWeight="bold">Object (A)</text>
                    
                    {/* Screen */}
                    <rect x="510" y="50" width="8" height="190" fill="#E2E8F0" stroke="#64748B" strokeWidth="1.5" />
                    <text x="500" y="260" fill="#334155" fontSize="11" fontWeight="bold">Screen</text>
                  </g>

                  {/* Step 1: Draw Rays from Candle through Top Half */}
                  {currentStep >= 1 && (
                    <g className="transition-all duration-500">
                      <path d="M80 50 L300 50 L510 210" fill="none" stroke="#D97706" strokeWidth="2" />
                      <path d="M80 50 L300 150 L510 210" fill="none" stroke="#2563EB" strokeWidth="2" />
                      <text x="180" y="45" fill="#B45309" fontSize="10" fontWeight="bold">Ray 1 (Parallel)</text>
                      <text x="180" y="115" fill="#1D4ED8" fontSize="10" fontWeight="bold">Ray 2 (Optical Center)</text>
                    </g>
                  )}

                  {/* Step 2: Draw the Black Paper Mask on Lower Half */}
                  {currentStep >= 2 && (
                    <g className="transition-all duration-500">
                      <rect x="286" y="150" width="28" height="100" fill="#1E293B" rx="2" />
                      <text x="250" y="275" fill="#E11D48" fontSize="10" fontWeight="bold">
                        Opaque Black Mask (Lower 50%)
                      </text>
                    </g>
                  )}

                  {/* Step 3: Draw Complete Real Inverted Image with 50% Intensity Annotation */}
                  {currentStep >= 3 && (
                    <g className="transition-all duration-500">
                      {/* Full candle on screen, inverted */}
                      <rect x="510" y="150" width="8" height="60" fill="#D97706" opacity="0.5" rx="1" />
                      <path d="M514 210 Q510 220, 514 230 Q518 220, 514 210 Z" fill="#DC2626" opacity="0.6" />
                      
                      {/* Explanatory Callout Banner */}
                      <rect x="170" y="20" width="260" height="34" fill="#FEF3C7" stroke="#D97706" strokeWidth="1.2" rx="4" />
                      <text x="185" y="38" fill="#92400E" fontSize="11" fontWeight="bold">
                        Scientific Fact: 100% of Image Remains!
                      </text>
                      <text x="185" y="49" fill="#B45309" fontSize="9">
                        Aperture controls irradiance, not geometric field of view.
                      </text>
                    </g>
                  )}
                </>
              )}

              {/* ELECTRICITY CIRCUIT */}
              {isElec && (
                <>
                  <rect x="100" y="70" width="400" height="160" fill="none" stroke="#334155" strokeWidth="3" rx="8" />
                  
                  {/* Battery */}
                  <g>
                    <rect x="70" y="130" width="60" height="40" fill="#F8FAFC" stroke="#0284C7" strokeWidth="2" rx="4" />
                    <text x="80" y="154" fill="#0284C7" fontSize="11" fontWeight="bold">12V DC</text>
                  </g>

                  {/* Bulb 1 */}
                  <g>
                    <circle cx="250" cy="70" r="16" fill={currentStep >= 1 ? "#FEF08A" : "#F1F5F9"} stroke="#CA8A04" strokeWidth="2" />
                    <text x="238" y="45" fill="#334155" fontSize="11" fontWeight="bold">Bulb 1</text>
                  </g>

                  {/* Bulb 2 */}
                  <g>
                    <circle cx="410" cy="70" r="16" fill={currentStep >= 1 ? "#FEF08A" : "#F1F5F9"} stroke="#CA8A04" strokeWidth="2" />
                    <text x="398" y="45" fill="#334155" fontSize="11" fontWeight="bold">Bulb 2</text>
                  </g>

                  {/* Ammeters */}
                  {currentStep >= 2 && (
                    <g>
                      <circle cx="180" cy="70" r="12" fill="#ECFDF5" stroke="#059669" strokeWidth="1.5" />
                      <text x="174" y="74" fill="#059669" fontSize="9" fontWeight="bold">2A</text>
                      <circle cx="330" cy="70" r="12" fill="#ECFDF5" stroke="#059669" strokeWidth="1.5" />
                      <text x="324" y="74" fill="#059669" fontSize="9" fontWeight="bold">2A</text>
                      <circle cx="470" cy="70" r="12" fill="#ECFDF5" stroke="#059669" strokeWidth="1.5" />
                      <text x="464" y="74" fill="#059669" fontSize="9" fontWeight="bold">2A</text>
                    </g>
                  )}

                  {currentStep >= 3 && (
                    <g>
                      <rect x="180" y="115" width="240" height="42" fill="#ECFDF5" stroke="#059669" strokeWidth="1.2" rx="4" />
                      <text x="190" y="134" fill="#065F46" fontSize="11" fontWeight="bold">
                        Current Conservation: I₁ = I₂ = 2.0 A
                      </text>
                      <text x="190" y="148" fill="#065F46" fontSize="10">
                        Current is rate of charge flow; not consumed!
                      </text>
                    </g>
                  )}
                </>
              )}

              {/* MECHANICS KINEMATICS */}
              {isMech && (
                <>
                  <line x1="80" y1="240" x2="520" y2="240" stroke="#334155" strokeWidth="2" />
                  <line x1="80" y1="240" x2="80" y2="40" stroke="#334155" strokeWidth="2" />
                  <text x="530" y="245" fill="#334155" fontSize="11" fontWeight="bold">Time (t / s)</text>
                  <text x="30" y="40" fill="#334155" fontSize="11" fontWeight="bold">Distance (d / m)</text>

                  {currentStep >= 1 && (
                    <>
                      <line x1="80" y1="240" x2="400" y2="80" stroke="#2563EB" strokeWidth="3" />
                      <circle cx="400" cy="80" r="5" fill="#1D4ED8" />
                      <text x="410" y="85" fill="#1D4ED8" fontSize="10" fontWeight="bold">(5 s, 100 m)</text>
                    </>
                  )}

                  {currentStep >= 2 && (
                    <g>
                      <rect x="250" y="140" width="180" height="40" fill="#EFF6FF" stroke="#3B82F6" strokeWidth="1.2" rx="3" />
                      <text x="260" y="158" fill="#1D4ED8" fontSize="11" fontWeight="bold">
                        Speed = Slope = Δd / Δt
                      </text>
                      <text x="260" y="172" fill="#1E40AF" fontSize="10">
                        100 m ÷ 5 s = 20 m/s
                      </text>
                    </g>
                  )}

                  {currentStep >= 3 && (
                    <g>
                      <rect x="180" y="40" width="280" height="40" fill="#FFF1F2" stroke="#E11D48" strokeWidth="1.2" rx="3" />
                      <text x="190" y="56" fill="#BE123C" fontSize="10" fontWeight="bold">
                        ⚠️ Multiplication Error: 100 × 5 = 500 m·s
                      </text>
                      <text x="190" y="70" fill="#9F1239" fontSize="9">
                        Units are m·s, which is NOT velocity (m/s).
                      </text>
                    </g>
                  )}
                </>
              )}
            </>
          )}
        </svg>
      </div>

      {/* Narration & Step Explanation Cleanly Formatted (No Overlapping Text) */}
      <div className="p-3.5 bg-slate-50 border-t border-slate-200 space-y-2">
        {stepNarration && (
          <div className="text-xs text-slate-800 bg-white p-2.5 rounded border border-slate-200">
            <span className="font-bold text-indigo-700 mr-1.5 font-mono">Narration:</span>
            <span>"{stepNarration}"</span>
          </div>
        )}

        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
          <div className="text-slate-700 font-sans">
            <strong className="text-charcoal font-semibold">{stepTitle}:</strong>{' '}
            <span className="text-slate-600">{boardInstruction}</span>
          </div>

          <div className="text-[10px] font-mono text-slate-500 bg-slate-100 px-2 py-1 rounded border border-slate-200 self-start sm:self-auto shrink-0">
            DSL: Step {currentStep + 1} of {totalSteps}
          </div>
        </div>
      </div>
    </div>
  );
}
