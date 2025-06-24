@echo off
REM ----------------------------------------------------------
REM Auto-elevate to administrator (avoid infinite loop)
REM ----------------------------------------------------------
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Administrator privileges required. Relaunching as administrator...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb RunAs -ArgumentList '--elevated'"
    exit /b
)

REM Remove --elevated parameter if present
if "%1"=="--elevated" shift

echo.
echo ==========================================
echo   One-Click Environment Setup Script (Windows)
echo ==========================================
echo.

REM 1. Install Python 3.10
echo [1/6] Installing Python 3.10...
winget install --id Python.Python.3.10 -e --silent
if errorlevel 1 (
    echo ERROR: Failed to install Python. Please check winget or network connectivity.
    pause
    exit /b 1
)

REM 2. Ensure pip is available
echo [2/6] Ensuring pip is available...

REM Try built-in ensurepip
python -m ensurepip --default-pip 2>nul

REM If ensurepip failed, download get-pip.py and run it
if errorlevel 1 (
    echo ensurepip failed. Downloading get-pip.py...
    powershell -Command "Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py"
    python get-pip.py
    del get-pip.py
)

REM Finally, upgrade pip itself
python -m pip install --upgrade pip
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip.
    pause
    exit /b 1
)

REM 3. Install Git
echo [3/6] Installing Git...
winget install --id Git.Git -e --silent
if errorlevel 1 (
    echo ERROR: Failed to install Git.
    pause
    exit /b 1
)

REM 4. Clone sample code to Desktop
echo [4/6] Cloning sample code to Desktop...
cd /d "%USERPROFILE%\Desktop"
if exist example-code-2025 (
    echo Directory already exists, skipping clone.
) else (
    git clone https://github.com/CSIE-Camp/example-code-2025.git
    if errorlevel 1 (
        echo ERROR: Clone failed. Please check network or repo URL.
        pause
        exit /b 1
    )
)

REM 5. Install Python dependencies
echo [5/6] Installing Python dependencies...
cd example-code-2025
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    pause
    exit /b 1
)

REM 6. Install Discord Desktop
echo [6/6] Installing Discord Desktop...
winget install --id Discord.Discord -e --silent
if errorlevel 1 (
    echo ERROR: Failed to install Discord.
    pause
    exit /b 1
)

echo.
echo All tasks completed! Press any key to exit.
pause
exit /b 0
