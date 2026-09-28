@echo off
title FROGS 5 Parakeet Live Ear
cd /d "%~dp0"
echo Starting Parakeet live listener...
echo Make sure the existing Antigravity bridge is running on port 3111.
"C:\Users\fbrown\Projects\table-ear\.venv\Scripts\python.exe" live_parakeet_bridge.py
pause
