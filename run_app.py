import subprocess
import sys
import time
import os

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(root, "backend")
    frontend_dir = os.path.join(root, "frontend")

    print("=" * 65)
    print("LAUNCHING RE:LEARN AI DIAGNOSTIC PHYSICS FULL-STACK PLATFORM")
    print("=" * 65)
    print("1. Starting Backend FastAPI server on http://127.0.0.1:8000...")
    backend_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=backend_dir
    )

    time.sleep(2)

    print("2. Starting Frontend Vite Dev Server on http://localhost:5173...")
    frontend_proc = subprocess.Popen(
        ["npm.cmd" if os.name == "nt" else "npm", "run", "dev"],
        cwd=frontend_dir
    )

    print("\n[Active URLs]")
    print("  * Frontend UI: http://localhost:5173")
    print("  * Backend API: http://127.0.0.1:8000")
    print("  * Swagger API Docs: http://127.0.0.1:8000/docs")
    print("\nPress Ctrl+C in this terminal to stop both servers.")

    try:
        backend_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        print("\nStopping Re:Learn services...")
        backend_proc.terminate()
        frontend_proc.terminate()

if __name__ == "__main__":
    main()
