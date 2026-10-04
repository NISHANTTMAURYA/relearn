import subprocess
import sys
import time
import os

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(root, "backend")
    frontend_dir = os.path.join(root, "frontend")
    ai_char_dir = os.path.join(root, "ai_character")

    print("=" * 65)
    print("LAUNCHING RE:LEARN AI DIAGNOSTIC PHYSICS FULL-STACK PLATFORM")
    print("=" * 65)
    
    print("1. Starting Backend FastAPI server on http://127.0.0.1:8000...")
    backend_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=backend_dir
    )

    print("2. Starting 3D AI Character (Prof. Maya) server on http://127.0.0.1:5050...")
    ai_char_proc = subprocess.Popen(
        [sys.executable, "app.py"],
        cwd=ai_char_dir,
        env={**os.environ, "PORT": "5050", "HOST": "127.0.0.1"}
    )

    time.sleep(2)

    print("3. Starting Frontend Vite Dev Server on http://localhost:5173...")
    frontend_proc = subprocess.Popen(
        ["npm.cmd" if os.name == "nt" else "npm", "run", "dev"],
        cwd=frontend_dir
    )

    print("\n[Active URLs]")
    print("  * Frontend UI: http://localhost:5173")
    print("  * Backend API: http://127.0.0.1:8000")
    print("  * 3D AI Character: http://127.0.0.1:5050")
    print("  * Swagger API Docs: http://127.0.0.1:8000/docs")
    print("\nPress Ctrl+C in this terminal to stop all servers.")

    try:
        backend_proc.wait()
        ai_char_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        print("\nStopping Re:Learn services...")
        backend_proc.terminate()
        ai_char_proc.terminate()
        frontend_proc.terminate()

if __name__ == "__main__":
    main()

