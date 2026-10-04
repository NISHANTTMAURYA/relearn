import React, { useState } from 'react';
import {
  BookOpen,
  Search,
  Filter,
  CheckCircle,
  AlertTriangle,
  HelpCircle,
  ChevronDown,
  ChevronUp,
  Layers
} from 'lucide-react';

export default function TaxonomyBrowser({ taxonomy, disambiguationCases }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedChapter, setSelectedChapter] = useState('All');
  const [expandedId, setExpandedId] = useState(null);

  const misconceptions = taxonomy?.misconceptions_index || [];
  const cases = disambiguationCases?.cases || [];

  const chapters = ['All', ...new Set(misconceptions.map((m) => m.chapter))];

  const filtered = misconceptions.filter((m) => {
    const matchesChapter = selectedChapter === 'All' || m.chapter === selectedChapter;
    const matchesSearch =
      m.short_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      m.id.toLowerCase().includes(searchTerm.toLowerCase()) ||
      m.topic.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesChapter && matchesSearch;
  });

  return (
    <div className="space-y-6">
      {/* Intro Header */}
      <div className="editorial-card p-6 bg-white border border-border">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center space-x-2">
              <BookOpen className="w-5 h-5 text-brand" />
              <h2 className="text-lg font-semibold text-charcoal">
                NCERT Class 10 Physics Misconception Taxonomy
              </h2>
            </div>
            <p className="text-xs text-charcoal-muted mt-1 max-w-3xl leading-relaxed">
              Codified catalog of 21 authentic cognitive barriers, naive mental models, and empirical ground truths grounded in NCERT Science Class 10 and CBSE Secondary board standards.
            </p>
          </div>

          <div className="flex items-center space-x-2 text-xs font-mono text-charcoal-muted">
            <span className="px-2.5 py-1 rounded bg-canvas-subtle border border-border">
              21 Core Taxa
            </span>
            <span className="px-2.5 py-1 rounded bg-canvas-subtle border border-border">
              4 Disambiguation Probes
            </span>
          </div>
        </div>

        {/* Search & Filter Toolbar */}
        <div className="mt-4 pt-4 border-t border-border flex flex-col sm:flex-row items-center justify-between gap-3">
          <div className="relative w-full sm:w-72">
            <Search className="w-4 h-4 text-charcoal-subtle absolute left-2.5 top-2.5" />
            <input
              type="text"
              placeholder="Search taxonomy by ID or name..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full text-xs pl-8 pr-3 py-1.5 rounded-md border border-border bg-canvas-subtle text-charcoal focus:bg-white focus:outline-none focus:ring-1 focus:ring-brand focus:border-brand font-mono"
            />
          </div>

          <div className="flex items-center space-x-1.5 overflow-x-auto w-full sm:w-auto pb-1 sm:pb-0">
            <Filter className="w-3.5 h-3.5 text-charcoal-subtle mr-1 hidden sm:inline" />
            {chapters.map((ch) => (
              <button
                key={ch}
                onClick={() => setSelectedChapter(ch)}
                className={`text-xs px-2.5 py-1 rounded-md border whitespace-nowrap font-mono transition-colors ${
                  selectedChapter === ch
                    ? 'bg-charcoal text-white border-charcoal'
                    : 'bg-white text-charcoal-muted border-border hover:bg-slate-50'
                }`}
              >
                {ch.replace('Chapter ', '').split(':')[0]}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Misconceptions Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {filtered.map((item) => {
          const isExpanded = expandedId === item.id;
          const isHigh = item.severity?.toLowerCase().includes('high') || item.severity?.toLowerCase().includes('critical');

          return (
            <div
              key={item.id}
              className="editorial-card p-4 bg-white border border-border transition-shadow hover:shadow-sm"
            >
              <div className="flex items-start justify-between gap-2">
                <div>
                  <div className="flex items-center space-x-2">
                    <span className="text-xs font-mono font-bold text-brand">
                      {item.id}
                    </span>
                    <span
                      className={`text-[10px] font-mono px-1.5 py-0.2 rounded border font-semibold ${
                        isHigh
                          ? 'bg-rose-50 text-rose-700 border-rose-200'
                          : 'bg-slate-100 text-charcoal-muted border-border'
                      }`}
                    >
                      {item.severity?.split(' ')[0]}
                    </span>
                  </div>
                  <h4 className="text-sm font-semibold text-charcoal mt-1 leading-snug">
                    {item.short_name}
                  </h4>
                  <p className="text-xs text-charcoal-muted font-mono mt-0.5">
                    {item.chapter} • {item.topic}
                  </p>
                </div>

                <button
                  onClick={() => setExpandedId(isExpanded ? null : item.id)}
                  className="p-1 text-charcoal-muted hover:text-charcoal rounded"
                >
                  {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                </button>
              </div>

              {/* Collapsible Details */}
              {isExpanded && (
                <div className="mt-3 pt-3 border-t border-border space-y-2 text-xs">
                  <div>
                    <span className="font-mono uppercase text-[10px] font-bold text-rose-700 block">
                      Naive Mental Model:
                    </span>
                    <p className="text-charcoal-muted mt-0.5 leading-relaxed">
                      Learner relies on perceptual surface features (e.g. geometric occlusion, consumable fuel, or static electrostatic analogy) instead of systemic conservation principles.
                    </p>
                  </div>

                  <div>
                    <span className="font-mono uppercase text-[10px] font-bold text-emerald-700 block">
                      Authoritative Scientific Ground Truth:
                    </span>
                    <p className="text-charcoal mt-0.5 leading-relaxed font-medium">
                      Physical behavior is determined by conservation laws and field equations (e.g., ray convergence from every aperture point, closed-loop steady current continuity).
                    </p>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Disambiguation Discrimination Section */}
      <div className="editorial-card p-6 bg-white border border-border space-y-4">
        <div className="flex items-center space-x-2 pb-3 border-b border-border">
          <Layers className="w-5 h-5 text-brand" />
          <div>
            <h3 className="text-base font-semibold text-charcoal">
              Competing Misconception Disambiguation Protocols
            </h3>
            <p className="text-xs text-charcoal-muted">
              Diagnostic probes designed to separate ambiguous student wrong answers that could stem from two competing conceptual errors.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {cases.map((cs) => (
            <div key={cs.case_id} className="p-4 rounded-lg bg-canvas-subtle border border-border space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono font-bold text-charcoal">
                  {cs.case_id} ({cs.domain})
                </span>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-brand-light text-brand border border-brand-border">
                  Disambiguation Probe
                </span>
              </div>

              <div className="text-xs">
                <span className="font-mono text-charcoal-subtle uppercase text-[10px] block">
                  Ambiguous Student Response:
                </span>
                <p className="text-charcoal font-medium mt-0.5">
                  "{cs.ambiguous_student_response}"
                </p>
              </div>

              {/* Competing Hypotheses */}
              <div className="space-y-1.5 pt-2 border-t border-border">
                <span className="font-mono text-charcoal-subtle uppercase text-[10px] block">
                  Competing Hypotheses:
                </span>
                {cs.competing_explanations?.map((exp, i) => (
                  <div key={i} className="text-xs p-2 rounded bg-white border border-border">
                    <span className="font-mono font-semibold text-rose-700">
                      {exp.misconception_id}: {exp.name}
                    </span>
                    <p className="text-charcoal-muted text-[11px] mt-0.5">{exp.hypothesis}</p>
                  </div>
                ))}
              </div>

              {/* Probe Item */}
              {cs.disambiguation_probe_item && (
                <div className="pt-2 border-t border-border text-xs">
                  <span className="font-mono text-charcoal-subtle uppercase text-[10px] block">
                    Diagnostic Disambiguator Item:
                  </span>
                  <p className="text-charcoal text-xs mt-0.5 leading-snug">
                    {cs.disambiguation_probe_item.stem}
                  </p>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
