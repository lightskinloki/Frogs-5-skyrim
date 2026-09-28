@echo off
title FROGS 5 Live Combat Advisor
cd /d "%~dp0"
echo Starting FROGS live advisor...
echo It reads the existing transcript bridge on port 3111.
echo It serves Jev + Gemini suggestions to the runsheet on port 3112.
py live_advisor.py
pause
