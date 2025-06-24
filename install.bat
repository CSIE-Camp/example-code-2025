@echo off
rem 強制用 bypass 執行 powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install_env.ps1"
