import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import StudentQuizPortal from './components/StudentQuizPortal';
import LearnerRecordView from './components/LearnerRecordView';
import DisambiguationLabView from './components/DisambiguationLabView';
import TaxonomyBrowser from './components/TaxonomyBrowser';
import AnalyticsDashboard from './components/AnalyticsDashboard';
import AICharacterTeacher from './components/AICharacterTeacher';
import ErrorBoundary from './components/ErrorBoundary';
import { AlertCircle } from 'lucide-react';

const API_BASE = 'http://127.0.0.1:8000';

export default function App() {
  const [activeTab, setActiveTab] = useState('portal'); // 'portal' | 'record' | 'disambig' | 'taxonomy' | 'analytics'
  const [isAITutorOpen, setIsAITutorOpen] = useState(false);

  // Global Loaded Data
  const [topics, setTopics] = useState([]);
  const [analytics, setAnalytics] = useState(null);
  const [taxonomy, setTaxonomy] = useState(null);
  const [disambiguationCases, setDisambiguationCases] = useState([]);
  const [learnerRecords, setLearnerRecords] = useState([]);
  const [errorMessage, setErrorMessage] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Initialize data from FastAPI backend
  useEffect(() => {
    async function loadData() {
      try {
        setIsLoading(true);
        const [tRes, aRes, taxRes, disRes] = await Promise.all([
          fetch(`${API_BASE}/api/topics`),
          fetch(`${API_BASE}/api/analytics`),
          fetch(`${API_BASE}/api/taxonomy`),
          fetch(`${API_BASE}/api/disambiguation-cases`)
        ]);

        if (tRes.ok) {
          const tData = await tRes.json();
          setTopics(tData.topics || []);
        }
        if (aRes.ok) {
          const aData = await aRes.json();
          setAnalytics(aData);
        }
        if (taxRes.ok) {
          const taxData = await taxRes.json();
          setTaxonomy(taxData);
        }
        if (disRes.ok) {
          const disData = await disRes.json();
          setDisambiguationCases(disData.cases || []);
        }
        setErrorMessage(null);
      } catch (err) {
        console.error('Init error:', err);
        setErrorMessage('FastAPI backend connection error. Please ensure backend is running at http://127.0.0.1:8000.');
      } finally {
        setIsLoading(false);
      }
    }
    loadData();
  }, []);

  // Update learner record when student completes an intervention reassessment
  const handleUpdateLearnerRecord = (newRecord) => {
    setLearnerRecords(prev => [
      {
        ...newRecord,
        title: newRecord.misconception_id,
        date: 'Just now'
      },
      ...prev
    ]);
  };

  return (
    <div className="min-h-screen bg-[#FBFBFA] flex flex-col font-sans text-charcoal relative">
      {/* Sticky Top Navbar */}
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        isAITutorOpen={isAITutorOpen}
        onToggleAITutor={() => setIsAITutorOpen(!isAITutorOpen)}
      />

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {errorMessage && (
          <div className="mb-6 p-4 rounded-lg bg-rose-50 border border-rose-200 text-rose-800 text-xs flex items-center space-x-2">
            <AlertCircle className="w-4 h-4 flex-shrink-0 text-rose-600" />
            <span>{errorMessage}</span>
          </div>
        )}

        {/* Tab 1: Student Diagnostic Learning Studio */}
        {activeTab === 'portal' && (
          <StudentQuizPortal
            topics={topics}
            onUpdateLearnerRecord={handleUpdateLearnerRecord}
          />
        )}

        {/* Tab 2: Learner Cognitive Record & BKT Progress */}
        {activeTab === 'record' && (
          <LearnerRecordView
            recordHistory={learnerRecords}
            onStartNewSession={() => setActiveTab('portal')}
          />
        )}

        {/* Tab 3: Misconception Disambiguation Lab */}
        {activeTab === 'disambig' && (
          <DisambiguationLabView
            disambiguationCases={disambiguationCases}
          />
        )}

        {/* Tab 4: NCERT Misconception Taxonomy Browser */}
        {activeTab === 'taxonomy' && (
          <TaxonomyBrowser taxonomy={taxonomy} />
        )}

        {/* Tab 5: Research & Model Benchmark Dashboard */}
        {activeTab === 'analytics' && (
          <AnalyticsDashboard analytics={analytics} />
        )}
      </main>

      {/* Floating AI Tutor Modal Widget */}
      {isAITutorOpen && (
        <div className="fixed bottom-4 right-4 z-50 animate-in fade-in slide-in-from-bottom-5 duration-200">
          <ErrorBoundary message="AI Mentor floating widget safely paused.">
            <AICharacterTeacher
              compact={true}
              onClose={() => setIsAITutorOpen(false)}
              textToSpeak="Hello! I am your AI Physics Mentor. Ask me any physics question or select a misconception to begin!"
            />
          </ErrorBoundary>
        </div>
      )}


      {/* Minimal Academic Footer */}
      <footer className="bg-white border-t border-border py-4 mt-auto">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 font-mono gap-2">
          <span>Re:Learn • Adaptive Physics Misconception Diagnostic Environment</span>
          <span>NCERT Science Class 10 & 9 Standards • Apache 2.0</span>
        </div>
      </footer>
    </div>
  );
}
