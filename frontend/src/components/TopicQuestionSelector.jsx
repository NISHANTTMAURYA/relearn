import React from 'react';
import { BookOpen, Layers, HelpCircle, Eye, CheckCircle2 } from 'lucide-react';

export default function TopicQuestionSelector({
  topics = [],
  selectedTopic,
  setSelectedTopic,
  selectedQuestion,
  setSelectedQuestion,
  onResetSession
}) {
  return (
    <div className="space-y-4">
      {/* Chapter Selection Pills */}
      <div>
        <label className="block text-xs font-mono font-semibold uppercase tracking-wider text-charcoal-muted mb-2">
          Step 1: Choose Curriculum Chapter (NCERT Physics)
        </label>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-2">
          {topics.map((t) => {
            const isSelected = selectedTopic?.id === t.id;
            return (
              <button
                key={t.id}
                onClick={() => {
                  setSelectedTopic(t);
                  if (t.questions && t.questions.length > 0) {
                    setSelectedQuestion(t.questions[0]);
                  }
                  if (onResetSession) onResetSession();
                }}
                className={`text-left p-2.5 rounded-lg border transition-all ${
                  isSelected
                    ? 'border-brand bg-brand-light/40 ring-1 ring-brand'
                    : 'border-border bg-white hover:border-slate-300 hover:bg-slate-50'
                }`}
              >
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-100 text-charcoal-muted font-medium">
                    {t.grade}
                  </span>
                  <span className="text-[10px] font-mono text-charcoal-subtle">
                    {t.total_items} items
                  </span>
                </div>
                <h4 className="font-semibold text-xs text-charcoal mt-1 line-clamp-1">
                  {t.chapter}
                </h4>
              </button>
            );
          })}
        </div>
      </div>

      {/* Question Selector & Details Card */}
      {selectedTopic && (
        <div className="editorial-card p-4 bg-white border border-border">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-border">
            <div className="flex items-center space-x-2">
              <span className="text-xs font-mono font-semibold uppercase tracking-wider text-charcoal-muted">
                Active Diagnostic Item:
              </span>
              <select
                value={selectedQuestion?.question_id || ''}
                onChange={(e) => {
                  const q = selectedTopic.questions.find((item) => item.question_id === e.target.value);
                  if (q) setSelectedQuestion(q);
                  if (onResetSession) onResetSession();
                }}
                className="text-xs font-mono font-medium bg-canvas-subtle border border-border rounded px-2 py-1 text-charcoal focus:ring-1 focus:ring-brand focus:border-brand"
              >
                {selectedTopic.questions.map((q, idx) => (
                  <option key={q.question_id} value={q.question_id}>
                    Question {idx + 1}: {q.question_id} ({q.question_type})
                  </option>
                ))}
              </select>
            </div>

            <div className="flex items-center space-x-2">
              <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-100 text-charcoal font-medium border border-border">
                Cognitive Level: {selectedQuestion?.cognitive_level || 'Comprehension'}
              </span>
              <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-brand-light text-brand font-medium border border-brand-border">
                Type: {selectedQuestion?.question_type || 'Conceptual'}
              </span>
            </div>
          </div>

          {/* Question Stem Text */}
          <div className="mt-3">
            <h3 className="text-sm sm:text-base font-medium text-charcoal leading-relaxed">
              {selectedQuestion?.stem}
            </h3>
          </div>

          {/* Diagram Note if present */}
          {selectedQuestion?.diagram_meta && (
            <div className="mt-3 p-2.5 rounded bg-canvas-subtle border border-border flex items-start space-x-2 text-xs text-charcoal-muted">
              <Eye className="w-4 h-4 text-brand flex-shrink-0 mt-0.5" />
              <div>
                <span className="font-semibold text-charcoal font-mono uppercase text-[10px]">Physical Setup Context: </span>
                <span>{selectedQuestion.diagram_meta.diagram_description}</span>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
