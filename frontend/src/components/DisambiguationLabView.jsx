import React, { useState } from 'react';
import { ShieldAlert, Compass, CheckCircle2, ArrowRight, HelpCircle, Sparkles } from 'lucide-react';

export default function DisambiguationLabView({ disambiguationCases = [] }) {
  const [selectedCaseIndex, setSelectedCaseIndex] = useState(0);
  const [activeProbeSelection, setActiveProbeSelection] = useState(null);

  // Fallback demo cases if backend list is empty
  const cases = disambiguationCases.length > 0 ? disambiguationCases : [
    {
      case_id: 'DISAMBIG-01',
      title: 'Current Attenuation vs. Battery Constant Current Source',
      identical_incorrect_answer: 'Student claims Ammeter A2 reads lower than A1 in a series circuit.',
      phenomenon_context: 'Two identical light bulbs connected in series with a 6V DC battery.',
      competing_hypotheses: [
        {
          id: 'MISC-ELEC-001',
          name: 'Current Attenuation / Consumption Model',
          mental_model: 'Believes electric current flows like water and is physically eaten or depleted by the first bulb.'
        },
        {
          id: 'MISC-ELEC-002',
          name: 'Battery as Constant Current Source Fallacy',
          mental_model: 'Believes the battery pushes a constant current and each downstream resistor creates a local barrier.'
        }
      ],
      discriminating_probe: {
        stem: 'If we swap Bulb 1 and Bulb 2, or place Ammeter A1 after Bulb 2, what will happen?',
        options: [
          {
            key: 'A',
            text: 'Ammeter A2 will now be higher because it is closer to the battery.',
            identifies: 'MISC-ELEC-001 (Directional Attenuation Model)'
          },
          {
            key: 'B',
            text: 'Both ammeters still read different values because resistors always block current locally.',
            identifies: 'MISC-ELEC-002 (Local Impedance Fallacy)'
          },
          {
            key: 'C',
            text: 'Both ammeters will read exactly 0.90 A because electric charge is conserved in a closed loop.',
            identifies: 'CORRECT: Scientifically Accurate Understanding'
          }
        ]
      },
      why_it_matters: 'Simply saying "wrong" leaves the teacher unaware whether to teach charge conservation (Kirchhoff) or battery terminal characteristics (Ohm).'
    },
    {
      case_id: 'DISAMBIG-02',
      title: 'Half-Lens Blocking vs. Screen Reification',
      identical_incorrect_answer: 'Student claims no image or only half image is formed.',
      phenomenon_context: 'Convex lens with lower half covered by black paper.',
      competing_hypotheses: [
        {
          id: 'MISC-OPT-001',
          name: 'Half-Lens Stencil Fallacy',
          mental_model: 'Believes covering half the glass cuts the image in half like a window stencil.'
        },
        {
          id: 'MISC-OPT-002',
          name: 'Screen Reification Fallacy',
          mental_model: 'Believes the image is a physical drawing that only exists if a cardboard screen is placed to catch it.'
        }
      ],
      discriminating_probe: {
        stem: 'If the cardboard screen is removed, does the image still exist in the space behind the lens?',
        options: [
          {
            key: 'A',
            text: 'No, without the screen the image cannot exist at all.',
            identifies: 'MISC-OPT-002 (Screen Reification)'
          },
          {
            key: 'B',
            text: 'The image exists in air, but only the top half of the candle rays are converging.',
            identifies: 'MISC-OPT-001 (Half-Lens Blocking)'
          },
          {
            key: 'C',
            text: 'The full aerial image exists at the focal plane; the eye can view it directly by looking into the converging cone of rays.',
            identifies: 'CORRECT: Aerial Real Image Concept'
          }
        ]
      },
      why_it_matters: 'Distinguishes between aperture misconception and fundamental ray convergence in 3D space.'
    }
  ];

  const currentCase = cases[selectedCaseIndex] || cases[0];

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Header Banner */}
      <div className="editorial-card p-6 bg-white border border-border space-y-2">
        <div className="flex items-center space-x-2">
          <span className="text-xs font-mono uppercase tracking-wider text-rose-700 bg-rose-50 px-2 py-0.5 rounded border border-rose-200">
            Mandatory Requirement 3
          </span>
          <span className="text-xs font-mono text-slate-500">
            Problem Statement Feature Mapping
          </span>
        </div>
        <h2 className="text-xl font-bold text-charcoal">
          Misconception Disambiguation Laboratory
        </h2>
        <p className="text-xs text-slate-600 leading-relaxed">
          <strong>The Educational Dilemma:</strong> Two students can write the <em>exact same incorrect answer</em> for completely different cognitive reasons. This laboratory demonstrates how Re:Learn uses diagnostic probing to isolate the true underlying mental model.
        </p>

        {/* Case selector tabs */}
        <div className="flex flex-wrap gap-2 pt-3 border-t border-border">
          {cases.map((c, idx) => (
            <button
              key={c.case_id}
              onClick={() => {
                setSelectedCaseIndex(idx);
                setActiveProbeSelection(null);
              }}
              className={`px-3 py-1.5 rounded text-xs font-mono transition-colors ${
                selectedCaseIndex === idx
                  ? 'bg-charcoal text-white font-semibold'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              {c.case_id}: {c.title.split(' vs')[0]}
            </button>
          ))}
        </div>
      </div>

      {/* Case Details Card */}
      <div className="editorial-card p-6 bg-white border border-border space-y-5">
        <div>
          <span className="text-xs font-mono text-indigo-700 uppercase font-semibold">
            {currentCase.case_id} • Case Study
          </span>
          <h3 className="text-lg font-bold text-charcoal mt-0.5">
            {currentCase.title}
          </h3>
          <p className="text-xs text-slate-500 mt-1">
            <strong>Physical Setup:</strong> {currentCase.phenomenon_context}
          </p>
        </div>

        {/* The Identical Wrong Answer Box */}
        <div className="p-4 rounded-lg bg-rose-50/70 border border-rose-200 text-slate-800 space-y-1">
          <div className="flex items-center space-x-2 text-rose-800 font-bold text-xs uppercase font-mono">
            <ShieldAlert className="w-4 h-4 text-rose-600" />
            <span>Identical Student Incorrect Observation:</span>
          </div>
          <p className="text-sm font-semibold text-rose-950 font-serif italic">
            "{currentCase.identical_incorrect_answer}"
          </p>
          <p className="text-xs text-rose-700 pt-1">
            A traditional LMS marks this as simply ❌ WRONG. Re:Learn uncovers the two distinct competing explanations:
          </p>
        </div>

        {/* Competing Hypotheses Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {currentCase.competing_hypotheses.map((hyp, hIdx) => (
            <div key={hIdx} className="p-4 rounded border border-slate-200 bg-slate-50 space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-white text-indigo-700 border border-slate-200 font-bold">
                  Hypothesis {hIdx === 0 ? 'A' : 'B'}
                </span>
                <span className="text-[10px] font-mono text-slate-500">{hyp.id}</span>
              </div>

              <h4 className="text-xs font-bold text-slate-900">{hyp.name}</h4>
              <p className="text-xs text-slate-600 leading-relaxed">{hyp.mental_model}</p>
            </div>
          ))}
        </div>

        {/* Discriminating Probing Item */}
        <div className="p-5 rounded-lg bg-indigo-50/50 border border-indigo-100 space-y-3">
          <div className="flex items-center space-x-2">
            <Sparkles className="w-4 h-4 text-indigo-600" />
            <h4 className="text-xs font-bold font-mono uppercase text-indigo-900">
              Re:Learn Diagnostic Discrimination Probe:
            </h4>
          </div>

          <p className="text-xs font-medium text-slate-800">
            {currentCase.discriminating_probe?.stem}
          </p>

          {/* Probe Options */}
          <div className="space-y-2 pt-1">
            {currentCase.discriminating_probe?.options.map((opt) => (
              <button
                key={opt.key}
                type="button"
                onClick={() => setActiveProbeSelection(opt.key)}
                className={`w-full text-left p-3 rounded border text-xs transition-all flex items-start space-x-3 ${
                  activeProbeSelection === opt.key
                    ? 'border-indigo-600 bg-white shadow-sm ring-1 ring-indigo-600 text-slate-900'
                    : 'border-slate-200 bg-white/70 hover:bg-white text-slate-700'
                }`}
              >
                <span className="font-mono font-bold w-5 h-5 rounded-full bg-slate-100 flex items-center justify-center text-xs flex-shrink-0 mt-0.5">
                  {opt.key}
                </span>
                <div className="flex-1">
                  <span>{opt.text}</span>
                  {activeProbeSelection === opt.key && (
                    <div className="mt-2 pt-2 border-t border-slate-100 flex items-center space-x-1.5 text-[11px] font-mono font-bold text-indigo-700">
                      <span>→ Diagnostic Discrimination:</span>
                      <span className="underline">{opt.identifies}</span>
                    </div>
                  )}
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* Pedagogical Justification */}
        <div className="text-xs text-slate-500 font-sans border-t border-border pt-3">
          <strong>Why this is essential:</strong> {currentCase.why_it_matters}
        </div>
      </div>
    </div>
  );
}
