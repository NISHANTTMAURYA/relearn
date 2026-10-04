import React from 'react';
import {
  Compass, BarChart2, BookOpen, Activity, Brain,
  Sparkles, ChevronLeft, ChevronRight, Home
} from 'lucide-react';

const navItems = [
  { id: 'home', label: 'Home', icon: Home },
  { id: 'portal', label: 'Diagnostic Studio', icon: Compass },
  { id: 'record', label: 'Learner Record', icon: Activity },
  { id: 'research', label: 'Research & Benchmarks', icon: BarChart2 },
  { id: 'taxonomy', label: 'Misconception Guide', icon: BookOpen },
];

export default function Sidebar({ activeTab, setActiveTab, collapsed: externalCollapsed, setCollapsed: externalSetCollapsed, onGoHome, onBackToLanding, isAITutorOpen, onToggleAITutor }) {
  const [internalCollapsed, setInternalCollapsed] = React.useState(false);
  const collapsed = externalCollapsed !== undefined ? externalCollapsed : internalCollapsed;
  const setCollapsed = externalSetCollapsed || setInternalCollapsed;
  const handleHomeClick = onGoHome || onBackToLanding;

  return (
    <aside
      className={`flex flex-col h-screen sticky top-0 bg-white border-r border-slate-200/80 transition-all duration-300 ease-in-out flex-shrink-0 z-30 ${
        collapsed ? 'w-[72px]' : 'w-56'
      }`}
    >
      {/* Logo */}
      <div className="flex items-center justify-between px-4 h-16 border-b border-slate-100 flex-shrink-0">
        {!collapsed && (
          <button onClick={handleHomeClick} className="flex items-center space-x-2 group text-left">
            <div className="w-7 h-7 rounded-lg bg-indigo-600 flex items-center justify-center text-white font-black text-[10px] group-hover:bg-indigo-700 transition-colors">
              Re:
            </div>
            <div>
              <div className="font-black text-slate-900 text-sm tracking-tight leading-none group-hover:text-indigo-600 transition-colors">Re:Learn</div>
              <div className="text-[9px] font-mono text-slate-400">NCERT Physics AI</div>
            </div>
          </button>
        )}
        {collapsed && (
          <button onClick={handleHomeClick} className="mx-auto w-7 h-7 rounded-lg bg-indigo-600 flex items-center justify-center text-white font-black text-[10px] hover:bg-indigo-700 transition-colors">
            Re:
          </button>
        )}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className={`flex-shrink-0 w-6 h-6 rounded-md hover:bg-slate-100 text-slate-400 hover:text-slate-600 flex items-center justify-center transition-colors ${collapsed ? 'mx-auto mt-1' : ''}`}
        >
          {collapsed ? <ChevronRight className="w-3.5 h-3.5" /> : <ChevronLeft className="w-3.5 h-3.5" />}
        </button>
      </div>

      {/* Nav Items */}
      <nav className="flex-1 py-4 space-y-0.5 px-2 overflow-y-auto overflow-x-hidden">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => {
                if (item.id === 'home' && handleHomeClick) {
                  handleHomeClick();
                } else {
                  setActiveTab(item.id);
                }
              }}
              className={`w-full flex items-center rounded-xl transition-all duration-150 group ${
                collapsed ? 'justify-center p-2.5' : 'space-x-3 px-3 py-2.5'
              } ${
                isActive
                  ? 'bg-indigo-50 text-indigo-700'
                  : 'text-slate-500 hover:bg-slate-50 hover:text-slate-800'
              }`}
              title={collapsed ? item.label : undefined}
            >
              <Icon className={`flex-shrink-0 transition-colors ${collapsed ? 'w-5 h-5' : 'w-4 h-4'} ${isActive ? 'text-indigo-600' : 'text-slate-400 group-hover:text-slate-600'}`} />
              {!collapsed && (
                <span className={`text-xs font-semibold truncate ${isActive ? 'text-indigo-700' : ''}`}>
                  {item.label}
                </span>
              )}
              {!collapsed && isActive && (
                <div className="ml-auto w-1.5 h-1.5 rounded-full bg-indigo-500 flex-shrink-0" />
              )}
            </button>
          );
        })}
      </nav>

      {/* AI Mentor Toggle */}
      <div className="px-2 pb-3">
        <button
          onClick={onToggleAITutor}
          className={`w-full rounded-xl transition-all duration-150 ${
            collapsed ? 'p-2.5 flex justify-center' : 'px-3 py-2.5 flex items-center space-x-3'
          } ${isAITutorOpen ? 'bg-indigo-600 text-white' : 'bg-indigo-50 text-indigo-700 hover:bg-indigo-100'}`}
          title={collapsed ? '3D AI Mentor' : undefined}
        >
          <Sparkles className={`flex-shrink-0 ${collapsed ? 'w-5 h-5' : 'w-4 h-4'} ${isAITutorOpen ? 'text-white animate-pulse' : 'text-indigo-500'}`} />
          {!collapsed && <span className="text-xs font-bold">3D AI Mentor</span>}
        </button>
      </div>

      {/* Status dot */}
      {!collapsed && (
        <div className="px-3 pb-4">
          <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex items-center space-x-2">
            <div className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
            <span className="text-[10px] font-mono text-slate-500">Model A+B Online</span>
          </div>
        </div>
      )}
      {collapsed && (
        <div className="px-2 pb-4 flex justify-center">
          <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" title="Models Online" />
        </div>
      )}
    </aside>
  );
}
