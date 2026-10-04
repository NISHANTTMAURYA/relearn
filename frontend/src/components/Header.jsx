import React from 'react';
import { Search, Bell, Settings, Sparkles, User } from 'lucide-react';

export default function Header({ 
  activeTab, 
  isAITutorOpen, 
  onToggleAITutor,
  searchQuery,
  setSearchQuery
}) {
  const titles = {
    portal: { main: 'Diagnostic Studio', sub: 'Interactive NCERT Physics Misconception Diagnostic & Remediation Flow' },
    record: { main: 'Learner Cognitive Record', sub: 'BKT Mastery Probabilities & Multi-Turn Attempt Trajectories' },
    research: { main: 'Research & Model Benchmarks', sub: 'Model A DeBERTa Metrics, Disambiguation Lab & Taxonomy Browser' }
  };

  const currentTitle = titles[activeTab] || titles.portal;

  return (
    <header className="bg-white border-b border-slate-100 py-4 px-6 flex items-center justify-between gap-4 sticky top-0 z-30">
      {/* Page Title & Greeting */}
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">{currentTitle.main}</h2>
        <p className="text-xs text-slate-400 font-medium">{currentTitle.sub}</p>
      </div>

      {/* Center Search Input (Matching Coursify Search Bar) */}
      <div className="hidden md:flex items-center flex-1 max-w-md mx-4 relative">
        <Search className="w-4 h-4 text-slate-400 absolute left-3.5" />
        <input
          type="text"
          placeholder="Search NCERT concepts, misconceptions (e.g. Half-Lens, Current)..."
          value={searchQuery || ''}
          onChange={(e) => setSearchQuery && setSearchQuery(e.target.value)}
          className="w-full bg-slate-50 border border-slate-200/80 rounded-2xl pl-10 pr-4 py-2 text-xs text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:bg-white transition-all"
        />
      </div>

      {/* Right Controls: 3D Tutor Toggle + Profile Badge */}
      <div className="flex items-center space-x-3 flex-shrink-0">
        <button
          onClick={onToggleAITutor}
          className={`flex items-center space-x-2 px-3.5 py-2 text-xs font-bold rounded-2xl transition-all ${
            isAITutorOpen
              ? 'bg-indigo-600 text-white shadow-sm ring-2 ring-indigo-300'
              : 'bg-indigo-50 text-indigo-700 hover:bg-indigo-100 border border-indigo-200'
          }`}
        >
          <Sparkles className="w-3.5 h-3.5 animate-pulse text-indigo-400" />
          <span>3D AI Mentor</span>
        </button>

        {/* User Profile Avatar Pill (Matching top right of Coursify image) */}
        <div className="flex items-center space-x-2 bg-slate-50 border border-slate-200/80 p-1.5 pr-3 rounded-2xl">
          <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-600 to-indigo-500 flex items-center justify-center text-white font-bold text-xs shadow-xs">
            PV
          </div>
          <div className="hidden sm:block text-left leading-tight">
            <span className="block text-xs font-bold text-slate-800">Prof. Vikram</span>
            <span className="block text-[10px] text-slate-400 font-medium">Diagnostic Studio</span>
          </div>
        </div>
      </div>
    </header>
  );
}
