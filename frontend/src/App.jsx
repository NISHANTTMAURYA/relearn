import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import StudentQuizPortal from './components/StudentQuizPortal';
import LearnerRecordView from './components/LearnerRecordView';
import ResearchHubView from './components/ResearchHubView';
import LandingPage from './components/LandingPage';
import { AlertCircle } from 'lucide-react';

const API_BASE = 'http://127.0.0.1:8000';

export default function App() {
  const [showLanding, setShowLanding] = useState(true); // Landing page shown by default
  const [activeTab, setActiveTab] = useState('portal'); // 'portal' | 'record' | 'research'
  const [isAITutorOpen, setIsAITutorOpen] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');

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
        if (tRes.ok) setTopics((await tRes.json()).topics || []);
        if (aRes.ok) setAnalytics(await aRes.json());
        if (taxRes.ok) setTaxonomy(await taxRes.json());
        if (disRes.ok) setDisambiguationCases((await disRes.json()).cases || []);
        setErrorMessage(null);
      } catch (err) {
        console.error('Init error:', err);
        setErrorMessage('FastAPI backend connection note: Make sure uvicorn backend is running on http://127.0.0.1:8000.');
      } finally {
        setIsLoading(false);
      }
    }
    loadData();
  }, []);

  const handleUpdateLearnerRecord = (newRecord) => {
    setLearnerRecords(prev => [
      { ...newRecord, title: newRecord.misconception_id, date: 'Just now' },
      ...prev
    ]);
  };

  const handleEnterApp = () => {
    setShowLanding(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  if (showLanding) {
    return <LandingPage onEnterApp={handleEnterApp} />;
  }

  return (
    <div className="min-h-screen w-full bg-[#FBFBFA] flex flex-col md:flex-row font-sans text-slate-800 antialiased overflow-x-hidden">
      {/* Left Sidebar */}
      <Sidebar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        onBackToLanding={() => setShowLanding(true)}
      />

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 min-h-screen bg-[#FBFBFA]">
        {/* Top Header */}
        <Header
          activeTab={activeTab}
          isAITutorOpen={isAITutorOpen}
          onToggleAITutor={() => setIsAITutorOpen(!isAITutorOpen)}
          searchQuery={searchQuery}
          setSearchQuery={setSearchQuery}
        />

        {/* Body Views */}
        <main className="flex-1 p-4 sm:p-6 overflow-y-auto">
          {errorMessage && (
            <div className="mb-6 p-4 rounded-2xl bg-rose-50 border border-rose-200 text-rose-800 text-xs flex items-center space-x-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0 text-rose-600" />
              <span>{errorMessage}</span>
            </div>
          )}

          {activeTab === 'portal' && (
            <StudentQuizPortal
              topics={topics}
              onUpdateLearnerRecord={handleUpdateLearnerRecord}
              isAITutorOpen={isAITutorOpen}
              searchQuery={searchQuery}
            />
          )}
          {activeTab === 'record' && (
            <LearnerRecordView
              recordHistory={learnerRecords}
              onStartNewSession={() => setActiveTab('portal')}
            />
          )}
          {activeTab === 'research' && (
            <ResearchHubView
              analytics={analytics}
              taxonomy={taxonomy}
              disambiguationCases={disambiguationCases}
            />
          )}
        </main>
      </div>
    </div>
  );
}


