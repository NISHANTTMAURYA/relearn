import React from 'react';
import { Compass, Award, Cpu, Sparkles, ArrowLeft } from 'lucide-react';

export default function Navbar({ activeTab, setActiveTab, onToggleAITutor, isAITutorOpen, onBackToLanding }) {
  const navItems = [
    { id: 'portal', label: 'Diagnostic Exam Studio', icon: Compass },
    { id: 'record', label: 'Learner Record & BKT', icon: Award },
    { id: 'research', label: 'Research & Benchmarks', icon: Cpu }
  ];

  return (
    <header className="bg-white border-b border-slate-200/80 sticky top-0 z-40 backdrop-blur-sm bg-white/95">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Platform Title */}
          <div className="flex items-center space-x-2">
            {onBackToLanding && (
              <button
                onClick={onBackToLanding}
                className="flex items-center justify-center w-7 h-7 rounded-md hover:bg-slate-100 text-slate-400 hover:text-slate-700 transition-colors mr-1"
                title="Back to home"
              >
                <ArrowLeft className="w-4 h-4" />
              </button>
            )}
            <div
              className="flex items-center space-x-3 cursor-pointer group"
              onClick={() => setActiveTab('portal')}
            >
              <div className="w-8 h-8 rounded bg-slate-900 flex items-center justify-center text-white font-bold tracking-tight text-sm group-hover:bg-indigo-600 transition-colors shadow-sm">
                Re:
              </div>
              <div>
                <div className="flex items-center space-x-2">
                  <span className="font-bold text-base text-slate-900 tracking-tight group-hover:text-indigo-600 transition-colors">
                    Re:Learn
                  </span>
                  <span className="text-[10px] font-mono uppercase px-1.5 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-200 font-medium">
                    NCERT Physics
                  </span>
                </div>
                <p className="text-[11px] text-slate-500 hidden sm:block">
                  Multimodal Diagnostic Engine & 3D AI Mentor
                </p>
              </div>
            </div>
          </div>

          {/* Navigation Items */}
          <nav className="flex items-center space-x-1 sm:space-x-2">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setActiveTab(item.id)}
                  className={`flex items-center space-x-1.5 px-3.5 py-1.5 text-xs font-semibold rounded-md transition-all ${
                    isActive
                      ? 'bg-slate-900 text-white shadow-sm'
                      : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                  }`}
                >
                  <Icon className="w-3.5 h-3.5" />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </nav>

          {/* 3D AI Mentor Toggle Button */}
          <div className="flex items-center space-x-2">
            <button
              onClick={onToggleAITutor}
              className={`flex items-center space-x-1.5 px-3 py-1.5 text-xs font-semibold rounded-md transition-all shadow-sm ${
                isAITutorOpen
                  ? 'bg-indigo-600 text-white ring-2 ring-indigo-300'
                  : 'bg-indigo-50 text-indigo-700 hover:bg-indigo-100 border border-indigo-200'
              }`}
            >
              <Sparkles className="w-3.5 h-3.5 text-indigo-500 animate-pulse" />
              <span>3D AI Mentor</span>
            </button>

            <div className="hidden lg:flex items-center space-x-2 text-[11px] font-mono text-slate-600 bg-slate-50 px-2.5 py-1 rounded border border-slate-200">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              <span>Model A+B Online</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

