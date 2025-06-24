@echo off
REM ----------------------------------------------------------
REM Auto-elevate to Administrator (avoid infinite loop)
REM ----------------------------------------------------------
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Administrator privileges required. Relaunching as administrator...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb RunAs -ArgumentList '--elevated'"
    exit /b
)
REM Remove --elevated if present
if "%1"=="--elevated" shift

echo.
echo ==========================================
echo   One-Click Environment Setup Script (Windows)
echo ==========================================
echo.

REM 1. Download & install Python 3.10.11 x64
echo [1/6] Downloading and installing Python 3.10.11 (x64)...
set "PYTHON_URL=https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe"
set "PYTHON_EXE=%TEMP%\python-3.10.11-amd64.exe"
powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_EXE%'"
"%PYTHON_EXE%" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
if errorlevel 1 (
    echo ERROR: Failed to install Python.
    pause & exit /b 1
)
del "%PYTHON_EXE%"

REM 2. Ensure pip is available
echo [2/6] Ensuring pip is available...
python -m ensurepip --default-pip 2>nul
if errorlevel 1 (
    echo ensurepip failed. Bootstrapping get-pip.py...
    set "GETPIP=%TEMP%\get-pip.py"
    powershell -Command "Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile '%GETPIP%'"
    python "%GETPIP%"
    del "%GETPIP%"
)
python -m pip install --upgrade pip
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip.
    pause & exit /b 1
)

REM 3. Download & install Git for Windows 2.50.0 x64
echo [3/6] Downloading and installing Git for Windows...
set "GIT_URL=https://sourceforge.net/projects/git-for-windows.mirror/files/v2.50.0.windows.1/Git-2.50.0-64-bit.exe/download"
set "GIT_EXE=%TEMP%\Git-2.50.0-64-bit.exe"
powershell -Command "Invoke-WebRequest -Uri '%GIT_URL%' -OutFile '%GIT_EXE%'"
"%GIT_EXE%" /VERYSILENT /NORESTART
if errorlevel 1 (
    echo ERROR: Failed to install Git.
    pause & exit /b 1
)
del "%GIT_EXE%"

REM 4. Clone sample code to Desktop
echo [4/6] Cloning sample code to Desktop...
cd /d "%USERPROFILE%\Desktop"
if not exist example-code-2025 (
    git clone https://github.com/CSIE-Camp/example-code-2025.git
    if errorlevel 1 (
        echo ERROR: Clone failed.
        pause & exit /b 1
    )
) else (
    echo Directory already exists, skipping clone.
)

REM 5. Install Python dependencies
echo [5/6] Installing Python dependencies...
cd example-code-2025
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    pause & exit /b 1
)

REM 6. Download & install Discord Desktop (x64, stable)
echo [6/6] Downloading and installing Discord Desktop...
set "DISCORD_URL=https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64"
set "DISCORD_EXE=%TEMP%\DiscordSetup.exe"
powershell -Command "Invoke-WebRequest -Uri '%DISCORD_URL%' -OutFile '%DISCORD_EXE%'"
"%DISCORD_EXE%" /s
if errorlevel 1 (
    echo ERROR: Failed to install Discord.
    pause & exit /b 1
)
del "%DISCORD_EXE%"

echo.
echo All tasks completed successfully! Press any key to exit.
pause
exit /b 0
