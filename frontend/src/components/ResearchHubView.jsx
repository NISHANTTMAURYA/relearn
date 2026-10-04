import React, { useState } from 'react';
import AnalyticsDashboard from './AnalyticsDashboard';
import TaxonomyBrowser from './TaxonomyBrowser';
import DisambiguationLabView from './DisambiguationLabView';
import { Cpu, ShieldAlert, BookOpen } from 'lucide-react';

export default function ResearchHubView({ analytics, taxonomy, disambiguationCases }) {
  const [subTab, setSubTab] = useState('benchmarks'); // 'benchmarks' | 'disambiguation' | 'taxonomy'

  return (
    <div className="space-y-6">
      {/* Sub-navigation selector */}
      <div className="bg-white p-2 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between flex-wrap gap-2">
        <div className="flex items-center space-x-2">
          <button
            onClick={() => setSubTab('benchmarks')}
            className={`flex items-center space-x-2 px-4 py-2 text-xs font-bold rounded-lg transition-all ${
              subTab === 'benchmarks'
                ? 'bg-indigo-600 text-white shadow'
                : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
            }`}
          >
            <Cpu className="w-4 h-4" />
            <span>Model Benchmarks & Metrics</span>
          </button>

          <button
            onClick={() => setSubTab('disambiguation')}
            className={`flex items-center space-x-2 px-4 py-2 text-xs font-bold rounded-lg transition-all ${
              subTab === 'disambiguation'
                ? 'bg-indigo-600 text-white shadow'
                : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
            }`}
          >
            <ShieldAlert className="w-4 h-4" />
            <span>Misconception Disambiguation Lab</span>
          </button>

          <button
            onClick={() => setSubTab('taxonomy')}
            className={`flex items-center space-x-2 px-4 py-2 text-xs font-bold rounded-lg transition-all ${
              subTab === 'taxonomy'
                ? 'bg-indigo-600 text-white shadow'
                : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
            }`}
          >
            <BookOpen className="w-4 h-4" />
            <span>NCERT Misconception Taxonomy</span>
          </button>
        </div>

        <div className="text-[11px] font-mono text-slate-500 px-3 py-1 bg-slate-50 rounded border border-slate-200">
          Re:Learn Research Environment • DeBERTa-v3 + Rule Sequence Engine
        </div>
      </div>

      {/* Content Rendering */}
      {subTab === 'benchmarks' && (
        <AnalyticsDashboard analytics={analytics} />
      )}

      {subTab === 'disambiguation' && (
        <DisambiguationLabView disambiguationCases={disambiguationCases} />
      )}

      {subTab === 'taxonomy' && (
        <TaxonomyBrowser taxonomy={taxonomy} />
      )}
    </div>
  );
}
