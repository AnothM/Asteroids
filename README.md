Asteroids (Pygame)
The repository contains all source code, assets, and configuration needed to run the game locally.

Requirements
Python 3.10+
Pygame
uv (recommended) or pip

Installation
1. Clone the repository
  git clone https://github.com/AnothM/Asteroids.git
  cd Asteroids

2. Create a virtual environment
Linux / macOS / WSL:
  python3 -m venv .venv
Windows:
  python -m venv .venv

3. Activate the virtual environment
Linux / macOS / WSL:
  source .venv/bin/activate
Windows PowerShell:
  .venv\Scripts\Activate.ps1
Windows CMD:
  .venv\Scripts\activate.bat

5. Install dependencies
Using uv (recommended):
  uv sync

If you dont have uv:
pip install uv

OR for manual installation (fallback):
pip install pygame

Running the Game
Linux / macOS / WSL:
python3 main.py

Windows:
python main.py
