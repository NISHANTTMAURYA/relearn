import React, { useState, useEffect } from 'react';
import { Play, RotateCcw, Sliders, Zap, Eye, Compass, CheckCircle2 } from 'lucide-react';

export default function InteractiveSimWidget({ simType = 'optics' }) {
  // Optics Lab State
  const [lensCoverage, setLensCoverage] = useState(50); // 0 to 100%

  // Circuit Lab State
  const [switchClosed, setSwitchClosed] = useState(true);
  const [electronOffset, setElectronOffset] = useState(0);

  // Mechanics Free Fall State
  const [isFalling, setIsFalling] = useState(false);
  const [fallProgress, setFallProgress] = useState(0);

  // Animate circuit electrons
  useEffect(() => {
    let animId;
    if (switchClosed) {
      const loop = () => {
        setElectronOffset(prev => (prev + 1) % 100);
        animId = requestAnimationFrame(loop);
      };
      animId = requestAnimationFrame(loop);
    }
    return () => cancelAnimationFrame(animId);
  }, [switchClosed]);

  // Animate free fall
  useEffect(() => {
    let timer;
    if (isFalling) {
      const start = Date.now();
      timer = setInterval(() => {
        const elapsed = (Date.now() - start) / 1000;
        const progress = Math.min(1, elapsed / 1.5);
        setFallProgress(progress * progress); // quadratic gravity y = 0.5 * g * t^2
        if (progress >= 1) {
          setIsFalling(false);
        }
      }, 20);
    }
    return () => clearInterval(timer);
  }, [isFalling]);

  return (
    <div className="editorial-card p-4 sm:p-5 bg-white border border-border">
      <div className="flex items-center justify-between border-b border-border pb-3 mb-4">
        <div className="flex items-center space-x-2">
          <Sliders className="w-4 h-4 text-indigo-600" />
          <h3 className="text-sm font-semibold text-charcoal tracking-tight">
            Interactive Physics Concept Laboratory
          </h3>
          <span className="text-[10px] font-mono uppercase px-2 py-0.5 rounded bg-indigo-50 text-indigo-700 border border-indigo-200">
            Hands-on Simulation
          </span>
        </div>

        <span className="text-xs text-slate-500 font-sans">
          Manipulate variables to physically test cognitive conflict
        </span>
      </div>

      {/* --- SIMULATION 1: OPTICS HALF-LENS LAB --- */}
      {simType === 'optics' && (
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 bg-slate-50 p-3 rounded border border-slate-200">
            <div className="flex-1 w-full">
              <div className="flex justify-between items-center text-xs mb-1">
                <span className="font-semibold text-slate-700">Opaque Black Mask Covering Lens:</span>
                <span className="font-mono text-indigo-700 font-bold">{lensCoverage}% Area Covered</span>
              </div>
              <input
                type="range"
                min="0"
                max="95"
                value={lensCoverage}
                onChange={(e) => setLensCoverage(Number(e.target.value))}
                className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-indigo-600"
              />
            </div>

            <div className="flex items-center space-x-2">
              <button
                onClick={() => setLensCoverage(0)}
                className="px-2.5 py-1 text-xs border rounded bg-white text-slate-700 hover:bg-slate-100"
              >
                0% (Clear)
              </button>
              <button
                onClick={() => setLensCoverage(50)}
                className="px-2.5 py-1 text-xs border rounded bg-white text-indigo-700 font-medium hover:bg-indigo-50"
              >
                50% (Half-Masked)
              </button>
              <button
                onClick={() => setLensCoverage(85)}
                className="px-2.5 py-1 text-xs border rounded bg-white text-slate-700 hover:bg-slate-100"
              >
                85% (Slot)
              </button>
            </div>
          </div>

          {/* Interactive SVG Diagram */}
          <div className="relative w-full h-56 sm:h-64 bg-white border border-slate-200 rounded p-2 flex items-center justify-center">
            <svg viewBox="0 0 600 240" className="w-full h-full">
              {/* Optical Axis */}
              <line x1="20" y1="120" x2="580" y2="120" stroke="#CBD5E1" strokeWidth="1.5" strokeDasharray="4 4" />
              <text x="30" y="112" fill="#94A3B8" fontSize="10" fontFamily="sans-serif">Principal Axis</text>

              {/* Object (Lighted Candle) */}
              <g transform="translate(100, 70)">
                <rect x="-6" y="25" width="12" height="25" fill="#F59E0B" rx="2" />
                <path d="M0 25 Q-4 12, 0 0 Q4 12, 0 25 Z" fill="#EF4444" />
                <path d="M0 22 Q-2 15, 0 6 Q2 15, 0 22 Z" fill="#FDE047" />
                <text x="-16" y="60" fill="#475569" fontSize="10" fontWeight="bold">Object (A)</text>
              </g>

              {/* Convex Lens */}
              <g transform="translate(300, 120)">
                <ellipse cx="0" cy="0" rx="14" ry="85" fill="#E0F2FE" stroke="#0284C7" strokeWidth="2" opacity="0.8" />
                <line x1="0" y1="-95" x2="0" y2="95" stroke="#0284C7" strokeWidth="1" strokeDasharray="2 2" />
                <text x="-25" y="105" fill="#0369A1" fontSize="10" fontWeight="bold">Convex Lens</text>

                {/* Black Paper Mask */}
                {lensCoverage > 0 && (
                  <rect
                    x="-16"
                    y={85 - (lensCoverage / 100) * 170}
                    width="32"
                    height={(lensCoverage / 100) * 170}
                    fill="#1E293B"
                    opacity="0.9"
                    rx="3"
                  />
                )}
              </g>

              {/* Rays from Tip of Candle through uncovered aperture */}
              {lensCoverage < 90 && (
                <>
                  <path
                    d="M100 70 L300 70 L480 160"
                    fill="none"
                    stroke="#F59E0B"
                    strokeWidth="1.8"
                    strokeDasharray={lensCoverage > 30 ? "2 2" : "none"}
                    opacity={(100 - lensCoverage) / 100}
                  />
                  <path
                    d="M100 70 L300 120 L480 160"
                    fill="none"
                    stroke="#10B981"
                    strokeWidth="1.8"
                    opacity={(100 - lensCoverage) / 100}
                  />
                  <path
                    d="M100 70 L300 150 L480 160"
                    fill="none"
                    stroke="#6366F1"
                    strokeWidth="1.8"
                    opacity={lensCoverage > 80 ? 0 : 0.8}
                  />
                </>
              )}

              {/* Viewing Screen */}
              <g transform="translate(480, 50)">
                <rect x="0" y="0" width="8" height="140" fill="#E2E8F0" stroke="#64748B" strokeWidth="1.5" rx="1" />
                <text x="-10" y="155" fill="#475569" fontSize="10" fontWeight="bold">Screen</text>

                {/* Real Inverted Candle Image on Screen */}
                <g
                  transform="translate(4, 90) scale(1, -1)"
                  style={{
                    opacity: Math.max(0.08, (100 - lensCoverage) / 100),
                    transition: 'opacity 0.2s ease-out'
                  }}
                >
                  <rect x="-4" y="20" width="8" height="20" fill="#F59E0B" rx="1" />
                  <path d="M0 20 Q-3 10, 0 0 Q3 10, 0 20 Z" fill="#EF4444" />
                  <path d="M0 17 Q-1.5 12, 0 5 Q1.5 12, 0 17 Z" fill="#FDE047" />
                  <text x="12" y="15" fill="#047857" fontSize="9" fontWeight="bold">
                    Full Inverted Image
                  </text>
                </g>
              </g>
            </svg>
          </div>

          {/* Real-time Empirical Findings Card */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div className="p-2.5 rounded bg-slate-50 border border-slate-200">
              <span className="text-[11px] font-mono text-slate-500 uppercase block">Image Shape</span>
              <span className="text-sm font-semibold text-emerald-700 flex items-center space-x-1 mt-0.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                <span>100% Complete (Intact)</span>
              </span>
              <p className="text-[11px] text-slate-600 mt-1">
                Every uncovered point on the lens receives light from all parts of the candle.
              </p>
            </div>

            <div className="p-2.5 rounded bg-slate-50 border border-slate-200">
              <span className="text-[11px] font-mono text-slate-500 uppercase block">Projected Brightness</span>
              <span className="text-sm font-semibold text-indigo-700 mt-0.5 block">
                {100 - lensCoverage}% of Max Lux
              </span>
              <p className="text-[11px] text-slate-600 mt-1">
                Energy transmission is reduced proportionately to the blocked aperture area.
              </p>
            </div>

            <div className="p-2.5 rounded bg-slate-50 border border-slate-200">
              <span className="text-[11px] font-mono text-slate-500 uppercase block">Misconception Verdict</span>
              <span className="text-xs font-semibold text-rose-700 mt-0.5 block">
                Half-Image Claim Disproved
              </span>
              <p className="text-[11px] text-slate-600 mt-1">
                The lens does not act as a picture stencil; covering half does NOT cut the picture.
              </p>
            </div>
          </div>
        </div>
      )}

      {/* --- SIMULATION 2: ELECTRICITY CURRENT CONSERVATION LAB --- */}
      {simType === 'electricity' && (
        <div className="space-y-4">
          <div className="flex items-center justify-between bg-slate-50 p-3 rounded border border-slate-200">
            <div>
              <span className="text-xs font-semibold text-slate-800">Series Circuit Loop:</span>
              <p className="text-xs text-slate-600 mt-0.5">
                Observe the ammeter readings before and after Bulb 1. Is electric current consumed?
              </p>
            </div>

            <button
              onClick={() => setSwitchClosed(!switchClosed)}
              className={`px-3 py-1.5 rounded text-xs font-semibold transition-colors flex items-center space-x-1.5 ${
                switchClosed
                  ? 'bg-emerald-600 hover:bg-emerald-700 text-white'
                  : 'bg-rose-600 hover:bg-rose-700 text-white'
              }`}
            >
              <Zap className="w-3.5 h-3.5" />
              <span>{switchClosed ? 'Switch: CLOSED (Current Flows)' : 'Switch: OPEN (Zero Current)'}</span>
            </button>
          </div>

          <div className="relative w-full h-56 sm:h-64 bg-white border border-slate-200 rounded p-2 flex items-center justify-center">
            <svg viewBox="0 0 600 240" className="w-full h-full">
              {/* Circuit Wires */}
              <rect x="80" y="40" width="440" height="160" fill="none" stroke="#475569" strokeWidth="4" rx="12" />

              {/* Battery */}
              <g transform="translate(80, 120)">
                <line x1="0" y1="-25" x2="0" y2="25" stroke="#0F172A" strokeWidth="6" />
                <line x1="-12" y1="-12" x2="-12" y2="12" stroke="#0F172A" strokeWidth="4" />
                <text x="-35" y="-5" fill="#EF4444" fontSize="12" fontWeight="bold">+</text>
                <text x="-35" y="20" fill="#3B82F6" fontSize="14" fontWeight="bold">-</text>
                <text x="-60" y="8" fill="#0F172A" fontSize="11" fontWeight="bold">6V Battery</text>
              </g>

              {/* Ammeter A1 (Before Bulb 1) */}
              <g transform="translate(200, 40)">
                <circle cx="0" cy="0" r="20" fill="#FFFFFF" stroke="#4F46E5" strokeWidth="2.5" />
                <text x="-8" y="5" fill="#4F46E5" fontSize="12" fontWeight="bold">A₁</text>
                <text x="-20" y="-28" fill="#1E293B" fontSize="10" fontWeight="bold">
                  {switchClosed ? '0.90 A' : '0.00 A'}
                </text>
              </g>

              {/* Bulb 1 */}
              <g transform="translate(300, 40)">
                <circle cx="0" cy="0" r="16" fill={switchClosed ? "#FEF08A" : "#F1F5F9"} stroke="#D97706" strokeWidth="2" />
                <path d="M-6 4 L0 -6 L6 4" fill="none" stroke="#D97706" strokeWidth="1.5" />
                <text x="-16" y="32" fill="#475569" fontSize="10" fontWeight="bold">Bulb 1</text>
              </g>

              {/* Ammeter A2 (Between Bulbs) */}
              <g transform="translate(400, 40)">
                <circle cx="0" cy="0" r="20" fill="#FFFFFF" stroke="#4F46E5" strokeWidth="2.5" />
                <text x="-8" y="5" fill="#4F46E5" fontSize="12" fontWeight="bold">A₂</text>
                <text x="-20" y="-28" fill="#1E293B" fontSize="10" fontWeight="bold">
                  {switchClosed ? '0.90 A' : '0.00 A'}
                </text>
              </g>

              {/* Bulb 2 */}
              <g transform="translate(520, 120)">
                <circle cx="0" cy="0" r="16" fill={switchClosed ? "#FEF08A" : "#F1F5F9"} stroke="#D97706" strokeWidth="2" />
                <path d="M-6 4 L0 -6 L6 4" fill="none" stroke="#D97706" strokeWidth="1.5" />
                <text x="22" y="5" fill="#475569" fontSize="10" fontWeight="bold">Bulb 2</text>
              </g>

              {/* Ammeter A3 (Returning to Battery) */}
              <g transform="translate(300, 200)">
                <circle cx="0" cy="0" r="20" fill="#FFFFFF" stroke="#4F46E5" strokeWidth="2.5" />
                <text x="-8" y="5" fill="#4F46E5" fontSize="12" fontWeight="bold">A₃</text>
                <text x="-20" y="32" fill="#1E293B" fontSize="10" fontWeight="bold">
                  {switchClosed ? '0.90 A' : '0.00 A'}
                </text>
              </g>
            </svg>
          </div>

          <div className="p-3 bg-emerald-50 border border-emerald-200 rounded text-xs text-emerald-900 leading-relaxed">
            <span className="font-semibold block mb-0.5">Physical Law Verified: Charge Conservation in Closed Loops</span>
            Both ammeters read exactly identical values ($A_1 = A_2 = A_3 = 0.90\text{ A}$). Electric charge is never "used up" or consumed by bulbs; energy is converted, but the rate of charge flow remains strictly conserved at every point in a single loop.
          </div>
        </div>
      )}

      {/* --- SIMULATION 3: MECHANICS FREE FALL LAB --- */}
      {simType === 'mechanics' && (
        <div className="space-y-4">
          <div className="flex items-center justify-between bg-slate-50 p-3 rounded border border-slate-200">
            <div>
              <span className="text-xs font-semibold text-slate-800">Galileo Free Fall Vacuum Tower:</span>
              <p className="text-xs text-slate-600 mt-0.5">
                Drop a 10 kg iron sphere and a 1 kg wood sphere simultaneously.
              </p>
            </div>

            <button
              onClick={() => {
                setFallProgress(0);
                setIsFalling(true);
              }}
              disabled={isFalling}
              className="px-3 py-1.5 rounded text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 text-white disabled:opacity-50 flex items-center space-x-1"
            >
              <Play className="w-3.5 h-3.5" />
              <span>{isFalling ? 'Dropping...' : 'Release Spheres'}</span>
            </button>
          </div>

          <div className="relative w-full h-56 bg-white border border-slate-200 rounded p-4 flex items-center justify-center">
            <svg viewBox="0 0 500 220" className="w-full h-full">
              {/* Tower Height */}
              <line x1="80" y1="30" x2="80" y2="190" stroke="#94A3B8" strokeWidth="3" />
              <line x1="75" y1="190" x2="420" y2="190" stroke="#475569" strokeWidth="4" />
              <text x="20" y="115" fill="#64748B" fontSize="10">Height 20m</text>
              <text x="220" y="208" fill="#475569" fontSize="10" fontWeight="bold">Ground Surface</text>

              {/* Sphere 1: 10 kg Heavy */}
              <g transform={`translate(180, ${30 + fallProgress * 150})`}>
                <circle cx="0" cy="0" r="16" fill="#334155" stroke="#0F172A" strokeWidth="2" />
                <text x="-12" y="4" fill="#FFFFFF" fontSize="10" fontWeight="bold">10kg</text>
              </g>

              {/* Sphere 2: 1 kg Light */}
              <g transform={`translate(320, ${30 + fallProgress * 150})`}>
                <circle cx="0" cy="0" r="10" fill="#F59E0B" stroke="#D97706" strokeWidth="1.5" />
                <text x="-7" y="3" fill="#FFFFFF" fontSize="9" fontWeight="bold">1kg</text>
              </g>
            </svg>
          </div>

          <div className="p-3 bg-emerald-50 border border-emerald-200 rounded text-xs text-emerald-900 leading-relaxed">
            <span className="font-semibold block mb-0.5">Physical Law Verified: Mass Independence of Gravitational Acceleration</span>
            g = GM/R² ≈ 9.8 m/s² depends exclusively on Earth's mass, not the object's mass. Both spheres hit the ground at the exact same instant (t = √(2h/g)).
          </div>
        </div>
      )}
    </div>
  );
}
