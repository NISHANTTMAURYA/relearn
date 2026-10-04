import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { Volume2, VolumeX, Play, Pause, RotateCcw, X, Sparkles, MessageSquare, Send, AlertCircle, RefreshCw } from 'lucide-react';

const API_BASE = 'http://127.0.0.1:8000';

function checkWebGLSupport() {
  try {
    const canvas = document.createElement('canvas');
    return !!(
      window.WebGLRenderingContext &&
      (canvas.getContext('webgl') || canvas.getContext('experimental-webgl'))
    );
  } catch (e) {
    return false;
  }
}

export default function AICharacterTeacher({
  textToSpeak = '',
  misconceptionId = '',
  compact = false,
  onClose = null,
  title = 'Prof. Vikram — 3D AI Physics Mentor'
}) {
  const containerRef = useRef(null);
  const [speechText, setSpeechText] = useState(textToSpeak);
  const [inputPrompt, setInputPrompt] = useState('');
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [isLoadingAudio, setIsLoadingAudio] = useState(false);
  const [currentGesture, setCurrentGesture] = useState('explaining');
  const [modelLoaded, setModelLoaded] = useState(false);
  const [webglUnavailable, setWebglUnavailable] = useState(false);

  // References to keep Three.js state outside React render loop
  const sceneRef = useRef(null);
  const cameraRef = useRef(null);
  const rendererRef = useRef(null);
  const characterRef = useRef(null);
  const controlsRef = useRef(null);
  const mixerRef = useRef(null);
  const activeAudioRef = useRef(null);
  const visemesRef = useRef([]);
  const faceMeshesRef = useRef([]);
  const armBonesRef = useRef({});
  const headBonesRef = useRef({});

  // 1. Initialize Three.js 3D Avatar Scene (with strict WebGL fallback)
  useEffect(() => {
    if (!checkWebGLSupport()) {
      setWebglUnavailable(true);
      setModelLoaded(true);
      return;
    }

    if (!containerRef.current) return;

    let animationFrameId;
    let renderer;
    let scene;
    let camera;

    try {
      const container = containerRef.current;
      const width = container.clientWidth || 400;
      const height = container.clientHeight || (compact ? 320 : 420);

      // Scene
      scene = new THREE.Scene();
      scene.background = new THREE.Color(0xf8fafc);
      sceneRef.current = scene;

      // Camera
      camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
      camera.position.set(0, 1.4, 1.25);
      cameraRef.current = camera;

      // Safe WebGL Renderer construction
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer.setSize(width, height);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.shadowMap.enabled = true;
      rendererRef.current = renderer;

      container.appendChild(renderer.domElement);

      // Controls
      const controls = new OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.05;
      controls.maxPolarAngle = Math.PI / 2 + 0.1;
      controls.minDistance = 0.6;
      controls.maxDistance = 3.0;
      controls.target.set(0, 1.35, 0);
      controlsRef.current = controls;

      // Lighting
      const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
      scene.add(ambientLight);

      const dirLight = new THREE.DirectionalLight(0xffffff, 1.1);
      dirLight.position.set(2, 4, 3);
      dirLight.castShadow = true;
      scene.add(dirLight);

      const fillLight = new THREE.DirectionalLight(0xe0e7ff, 0.5);
      fillLight.position.set(-2, 2, -2);
      scene.add(fillLight);

      // Load Avatar GLTF Model
      const loader = new GLTFLoader();
      const modelUrls = [
        '/models/avatar_indian_teacher_glasses.glb',
        '/models/avatar.glb',
        `${API_BASE}/static/models/avatar_indian_teacher_glasses.glb`,
        `${API_BASE}/static/models/avatar.glb`
      ];

      function tryLoad(index) {
        if (index >= modelUrls.length) {
          createProceduralHead(scene);
          setModelLoaded(true);
          return;
        }

        loader.load(
          modelUrls[index],
          (gltf) => {
            const character = gltf.scene;
            scene.add(character);
            characterRef.current = character;

            if (gltf.animations && gltf.animations.length > 0) {
              const mixer = new THREE.AnimationMixer(character);
              const action = mixer.clipAction(gltf.animations[0]);
              action.play();
              mixerRef.current = mixer;
            }

            const faceMeshes = [];
            const armBones = {};
            const headBones = {};

            character.traverse((node) => {
              if (node.morphTargetDictionary) faceMeshes.push(node);
              if (node.type === 'Bone') {
                const name = node.name.toLowerCase();
                if ((name.includes('head') || name === 'head') && !name.includes('end')) headBones.head = node;
                if (name.includes('neck') || name === 'neck') headBones.neck = node;
                if (name.includes('left') && name.includes('arm') && !name.includes('fore')) armBones.leftArm = node;
                if (name.includes('right') && name.includes('arm') && !name.includes('fore')) armBones.rightArm = node;
                if (name.includes('left') && (name.includes('forearm') || name.includes('fore_arm'))) armBones.leftForeArm = node;
                if (name.includes('right') && (name.includes('forearm') || name.includes('fore_arm'))) armBones.rightForeArm = node;
              }
            });

            faceMeshesRef.current = faceMeshes;
            armBonesRef.current = armBones;
            headBonesRef.current = headBones;

            let headY = 1.45;
            const targetBone = headBones.neck || headBones.head;
            if (targetBone) {
              const worldPos = new THREE.Vector3();
              targetBone.getWorldPosition(worldPos);
              if (worldPos.y > 0) headY = worldPos.y;
            }
            controls.target.set(0, headY - 0.1, 0);
            camera.position.set(0, headY - 0.05, 1.1);
            controls.update();

            setModelLoaded(true);
          },
          undefined,
          () => tryLoad(index + 1)
        );
      }

      function createProceduralHead(sc) {
        const group = new THREE.Group();
        const headGeo = new THREE.SphereGeometry(0.2, 32, 32);
        const headMat = new THREE.MeshStandardMaterial({ color: 0xfed7aa, roughness: 0.5 });
        const headMesh = new THREE.Mesh(headGeo, headMat);
        headMesh.position.set(0, 1.45, 0);
        group.add(headMesh);

        const gGeo = new THREE.TorusGeometry(0.04, 0.008, 16, 32);
        const gMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
        const leftG = new THREE.Mesh(gGeo, gMat);
        leftG.position.set(-0.06, 1.47, 0.18);
        const rightG = new THREE.Mesh(gGeo, gMat);
        rightG.position.set(0.06, 1.47, 0.18);
        group.add(leftG);
        group.add(rightG);

        sc.add(group);
        characterRef.current = group;
      }

      tryLoad(0);

      const clock = new THREE.Clock();

      function animate() {
        animationFrameId = requestAnimationFrame(animate);
        const delta = clock.getDelta();
        const time = clock.getElapsedTime();

        if (mixerRef.current) mixerRef.current.update(delta);

        // Head motion
        const head = headBonesRef.current.head || headBonesRef.current.neck;
        if (head) {
          const nod = isSpeaking ? Math.sin(time * 6) * 0.04 : Math.sin(time * 1.5) * 0.015;
          const sway = Math.sin(time * 0.8) * 0.02;
          head.rotation.x = -0.05 + nod;
          head.rotation.y = sway;
        }

        // Arm gestures
        const { leftArm, rightArm } = armBonesRef.current;
        if (leftArm && rightArm) {
          let tLeft = { x: 1.3, y: 0.1, z: 0.1 };
          let tRight = { x: 1.3, y: -0.1, z: -0.1 };

          if (isSpeaking || currentGesture === 'explaining') {
            tLeft = { x: 1.1 + Math.sin(time * 3) * 0.1, y: 0.3, z: 0.3 };
            tRight = { x: 1.1 - Math.sin(time * 3) * 0.1, y: -0.3, z: -0.3 };
          } else if (currentGesture === 'pointing') {
            tRight = { x: 0.8, y: 0.5, z: -0.5 };
            tLeft = { x: 1.3, y: 0.1, z: 0.1 };
          } else if (currentGesture === 'presenting') {
            tLeft = { x: 0.9, y: 0.4, z: 0.4 };
            tRight = { x: 0.9, y: 0.4, z: -0.4 };
          }

          ['x', 'y', 'z'].forEach(axis => {
            leftArm.rotation[axis] = THREE.MathUtils.lerp(leftArm.rotation[axis], tLeft[axis], 0.1);
            rightArm.rotation[axis] = THREE.MathUtils.lerp(rightArm.rotation[axis], tRight[axis], 0.1);
          });
        }

        // Lip sync
        if (faceMeshesRef.current.length > 0) {
          let mouthOpen = 0.05;
          let smile = 0.2;
          let visemeAa = 0;

          if (isSpeaking) {
            mouthOpen = 0.2 + Math.abs(Math.sin(time * 12)) * 0.5;
            smile = 0.3;
            visemeAa = mouthOpen * 0.8;
          }

          faceMeshesRef.current.forEach(mesh => {
            const dict = mesh.morphTargetDictionary;
            if (!dict) return;
            const setT = (name, val) => {
              if (dict[name] !== undefined) {
                mesh.morphTargetInfluences[dict[name]] = THREE.MathUtils.clamp(val, 0, 1);
              }
            };
            setT('jawOpen', mouthOpen);
            setT('mouthOpen', mouthOpen);
            setT('mouthSmile', smile);
            setT('viseme_aa', visemeAa);
          });
        }

        if (controlsRef.current) controlsRef.current.update();
        if (rendererRef.current && sceneRef.current && cameraRef.current) {
          rendererRef.current.render(sceneRef.current, cameraRef.current);
        }
      }

      animate();

      const handleResize = () => {
        if (!containerRef.current || !rendererRef.current || !cameraRef.current) return;
        const w = containerRef.current.clientWidth;
        const h = containerRef.current.clientHeight || (compact ? 320 : 420);
        cameraRef.current.aspect = w / h;
        cameraRef.current.updateProjectionMatrix();
        rendererRef.current.setSize(w, h);
      };

      window.addEventListener('resize', handleResize);

      return () => {
        window.removeEventListener('resize', handleResize);
        cancelAnimationFrame(animationFrameId);
        if (rendererRef.current && rendererRef.current.domElement) {
          rendererRef.current.domElement.remove();
        }
      };
    } catch (err) {
      console.warn('Three.js WebGL context initialization failed, falling back to 2D avatar:', err);
      setWebglUnavailable(true);
      setModelLoaded(true);
    }
  }, [compact]);

  // Handle Speech API & Audio Playback
  const handleSpeak = async (overrideText = '') => {
    const text = overrideText || speechText || 'Let us investigate this physics concept together!';
    if (!text || (typeof text === 'string' && !text.trim())) return;

    try {
      setIsLoadingAudio(true);
      setIsPaused(false);

      if (activeAudioRef.current) {
        activeAudioRef.current.pause();
        activeAudioRef.current = null;
      }

      const res = await fetch(`${API_BASE}/api/character/speak`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: text,
          misconception_id: misconceptionId
        })
      });

      setIsLoadingAudio(false);

      if (res.ok) {
        const data = await res.json();
        if (data.visemes) visemesRef.current = data.visemes;

        if (data.audio_base64) {
          const mimeType = (data.audio_base64.startsWith('UklGR') || data.audio_base64.startsWith('RIFF')) ? 'audio/wav' : 'audio/mpeg';
          const audio = new Audio(`data:${mimeType};base64,` + data.audio_base64);
          activeAudioRef.current = audio;

          audio.onplay = () => setIsSpeaking(true);
          audio.onpause = () => setIsSpeaking(false);
          audio.onended = () => {
            setIsSpeaking(false);
            activeAudioRef.current = null;
          };

          audio.play().catch(e => console.warn('Audio play error, using Web Speech fallback:', e));
          return;
        }
      }

      // Web Speech API Browser Fallback
      if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const clean = text.replace(/\[.*?\]/g, '').replace(/https?:\/\/\S+/g, '');
        const utt = new SpeechSynthesisUtterance(clean);
        utt.rate = 1.0;
        utt.pitch = 1.05;

        const voices = window.speechSynthesis.getVoices();
        const pref = voices.find(v => v.lang.includes('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Zira')));
        if (pref) utt.voice = pref;

        utt.onstart = () => setIsSpeaking(true);
        utt.onend = () => setIsSpeaking(false);
        utt.onerror = () => setIsSpeaking(false);

        window.speechSynthesis.speak(utt);
      }
    } catch (err) {
      console.error('Character speak error:', err);
      setIsLoadingAudio(false);
      setIsSpeaking(false);
    }
  };

  const handleTogglePause = () => {
    if (activeAudioRef.current) {
      if (activeAudioRef.current.paused) {
        activeAudioRef.current.play();
        setIsSpeaking(true);
        setIsPaused(false);
      } else {
        activeAudioRef.current.pause();
        setIsSpeaking(false);
        setIsPaused(true);
      }
    } else if (typeof window !== 'undefined' && window.speechSynthesis) {
      if (window.speechSynthesis.speaking) {
        if (window.speechSynthesis.paused) {
          window.speechSynthesis.resume();
          setIsSpeaking(true);
          setIsPaused(false);
        } else {
          window.speechSynthesis.pause();
          setIsSpeaking(false);
          setIsPaused(true);
        }
      }
    }
  };

  const handleStop = () => {
    if (activeAudioRef.current) {
      activeAudioRef.current.pause();
      activeAudioRef.current = null;
    }
    if (typeof window !== 'undefined' && window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    setIsSpeaking(false);
    setIsPaused(false);
  };

  useEffect(() => {
    if (textToSpeak) {
      setSpeechText(textToSpeak);
      handleSpeak(textToSpeak);
    }
  }, [textToSpeak, misconceptionId]);

  return (
    <div className={`editorial-card bg-white border border-border overflow-hidden flex flex-col ${compact ? 'max-w-md w-full shadow-2xl rounded-xl' : 'w-full rounded-lg'}`}>
      {/* Widget Header */}
      <div className="bg-slate-900 text-white px-4 py-3 flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <div className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></div>
          <span className="font-semibold text-xs tracking-wide uppercase">{title}</span>
          <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 text-indigo-300 border border-slate-700">
            {webglUnavailable ? '2D Audio Mentor' : '3D WebGL Avatar'}
          </span>
        </div>
        {onClose && (
          <button onClick={onClose} className="text-slate-400 hover:text-white transition-colors p-1">
            <X className="w-4 h-4" />
          </button>
        )}
      </div>

      {/* Viewport: 3D Canvas OR 2D Fallback */}
      <div className="relative bg-gradient-to-b from-slate-100 to-slate-200 border-b border-slate-200 overflow-hidden">
        {!webglUnavailable ? (
          <div
            ref={containerRef}
            className={`w-full ${compact ? 'h-72' : 'h-80 sm:h-96'} cursor-grab active:cursor-grabbing`}
          />
        ) : (
          /* 2D Animated Mentor Canvas when WebGL is disabled */
          <div className={`w-full ${compact ? 'h-72' : 'h-80 sm:h-96'} flex flex-col items-center justify-center p-6 bg-radial from-indigo-50/80 to-slate-100`}>
            {/* Animated SVG Teacher Avatar */}
            <div className="relative mb-3">
              <svg className={`w-32 h-32 sm:w-40 sm:h-40 transition-transform ${isSpeaking ? 'scale-105' : 'scale-100'}`} viewBox="0 0 160 160">
                {/* Outer Glow */}
                <circle cx="80" cy="80" r="74" fill="#EEF2FF" stroke="#C7D2FE" strokeWidth="2" />
                
                {/* Body / Coat */}
                <path d="M 30 155 Q 80 135 130 155 L 130 160 L 30 160 Z" fill="#1E293B" />
                <path d="M 60 140 L 80 160 L 100 140 Z" fill="#4338CA" />

                {/* Head */}
                <ellipse cx="80" cy="75" rx="36" ry="42" fill="#FED7AA" />
                
                {/* Hair */}
                <path d="M 44 65 Q 80 20 116 65 Q 120 40 100 30 Q 80 25 60 30 Q 40 40 44 65 Z" fill="#1E293B" />
                <path d="M 44 65 Q 40 85 45 100 Q 48 85 52 75 Z" fill="#1E293B" />
                <path d="M 116 65 Q 120 85 115 100 Q 112 85 108 75 Z" fill="#1E293B" />

                {/* Glasses */}
                <rect x="52" y="66" width="22" height="15" rx="3" fill="none" stroke="#0F172A" strokeWidth="2.5" />
                <rect x="86" y="66" width="22" height="15" rx="3" fill="none" stroke="#0F172A" strokeWidth="2.5" />
                <line x1="74" y1="73" x2="86" y2="73" stroke="#0F172A" strokeWidth="2.5" />

                {/* Eyes behind glasses */}
                <circle cx="63" cy="73" r="2.5" fill="#1E293B" />
                <circle cx="97" cy="73" r="2.5" fill="#1E293B" />

                {/* Smile / Speaking Mouth */}
                {isSpeaking ? (
                  <ellipse cx="80" cy="98" rx="8" ry="6" fill="#991B1B" className="animate-pulse" />
                ) : (
                  <path d="M 72 96 Q 80 104 88 96" fill="none" stroke="#991B1B" strokeWidth="2.5" strokeLinecap="round" />
                )}
              </svg>

              {/* Status Indicator */}
              <div className="absolute -bottom-1 right-2 bg-emerald-500 w-5 h-5 rounded-full border-2 border-white flex items-center justify-center">
                <span className="w-2 h-2 rounded-full bg-white animate-ping"></span>
              </div>
            </div>

            {/* Speaking Audio Waves */}
            <div className="flex items-center space-x-1.5 h-6">
              {[0.4, 0.8, 1.2, 0.6, 1.4, 0.9, 0.5].map((scale, i) => (
                <div
                  key={i}
                  className={`w-1 bg-indigo-600 rounded-full transition-all duration-150 ${
                    isSpeaking ? 'animate-pulse' : 'h-1.5 opacity-40'
                  }`}
                  style={{
                    height: isSpeaking ? `${Math.max(4, scale * 18)}px` : '4px',
                    animationDelay: `${i * 80}ms`
                  }}
                />
              ))}
            </div>

            <p className="text-[11px] font-mono text-slate-500 mt-2 text-center">
              Audio-Synchronized Pedagogical Mentor
            </p>
          </div>
        )}

        {/* Loading Spinner for 3D */}
        {!webglUnavailable && !modelLoaded && (
          <div className="absolute inset-0 flex items-center justify-center bg-slate-900/10 backdrop-blur-xs text-xs font-mono text-slate-700">
            <div className="flex items-center space-x-2 bg-white px-3 py-1.5 rounded-md shadow border border-slate-200">
              <span className="w-3 h-3 border-2 border-indigo-600 border-t-transparent rounded-full animate-spin"></span>
              <span>Initializing 3D Avatar...</span>
            </div>
          </div>
        )}

        {/* Live Audio Status Overlay */}
        {isSpeaking && !webglUnavailable && (
          <div className="absolute bottom-3 left-3 bg-indigo-600/90 text-white text-[11px] font-mono px-2.5 py-1 rounded-full backdrop-blur-sm flex items-center space-x-1.5 shadow">
            <div className="flex items-center space-x-0.5">
              <span className="w-1 h-2.5 bg-white rounded-full animate-pulse"></span>
              <span className="w-1 h-3.5 bg-white rounded-full animate-pulse delay-75"></span>
              <span className="w-1 h-2 bg-white rounded-full animate-pulse delay-150"></span>
            </div>
            <span>Speaking Explanation</span>
          </div>
        )}

        {/* Quick Gesture Switcher (Only in 3D mode) */}
        {!webglUnavailable && (
          <div className="absolute top-3 right-3 flex flex-col space-y-1">
            {['explaining', 'pointing', 'presenting'].map((g) => (
              <button
                key={g}
                onClick={() => setCurrentGesture(g)}
                className={`px-2 py-0.5 text-[10px] font-mono uppercase rounded transition-colors shadow-xs ${
                  currentGesture === g ? 'bg-indigo-600 text-white font-semibold' : 'bg-white/90 text-slate-700 hover:bg-white border border-slate-200'
                }`}
              >
                {g}
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Controls & Speech Bar */}
      <div className="p-4 space-y-3 bg-white">
        {speechText && (
          <div className="p-3 rounded-lg bg-slate-50 border border-slate-200 text-xs text-slate-800 leading-relaxed font-sans">
            <span className="font-semibold text-indigo-700 font-mono text-[10px] block uppercase mb-1">
              Teacher Voice Narration:
            </span>
            "{speechText}"
          </div>
        )}

        <div className="flex items-center justify-between gap-2">
          <div className="flex items-center space-x-2">
            <button
              onClick={() => handleSpeak()}
              disabled={isLoadingAudio}
              className="px-3.5 py-1.5 rounded-md bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold tracking-wide uppercase transition-colors flex items-center space-x-1.5 shadow-xs disabled:opacity-50"
            >
              {isLoadingAudio ? (
                <span className="w-3.5 h-3.5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
              ) : (
                <Volume2 className="w-3.5 h-3.5" />
              )}
              <span>{isSpeaking ? 'Replay Voice' : 'Speak POE Explanation'}</span>
            </button>

            {(isSpeaking || isPaused) && (
              <button
                onClick={handleTogglePause}
                className="px-3 py-1.5 rounded-md bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-medium transition-colors flex items-center space-x-1 border border-slate-200"
              >
                {isPaused ? <Play className="w-3.5 h-3.5 text-emerald-600" /> : <Pause className="w-3.5 h-3.5 text-amber-600" />}
                <span>{isPaused ? 'Resume' : 'Pause'}</span>
              </button>
            )}

            {(isSpeaking || isPaused) && (
              <button
                onClick={handleStop}
                className="px-2.5 py-1.5 rounded-md bg-rose-50 hover:bg-rose-100 text-rose-700 text-xs font-medium transition-colors border border-rose-200"
              >
                Stop
              </button>
            )}
          </div>
        </div>

        {/* Custom Question Input */}
        <div className="flex items-center space-x-2 pt-1 border-t border-slate-100">
          <input
            type="text"
            placeholder="Ask AI Teacher a physics question..."
            value={inputPrompt}
            onChange={(e) => setInputPrompt(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && inputPrompt.trim()) {
                setSpeechText(inputPrompt);
                handleSpeak(inputPrompt);
                setInputPrompt('');
              }
            }}
            className="flex-1 px-3 py-1.5 text-xs rounded-md border border-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500 font-sans"
          />
          <button
            onClick={() => {
              if (inputPrompt.trim()) {
                setSpeechText(inputPrompt);
                handleSpeak(inputPrompt);
                setInputPrompt('');
              }
            }}
            className="p-1.5 rounded-md bg-slate-900 text-white hover:bg-indigo-600 transition-colors"
            title="Send to Teacher"
          >
            <Send className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
}
