@echo off
REM ----------------------------------------------------------
REM Automatically relaunch with administrator privileges (avoid infinite loop)
REM ----------------------------------------------------------
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Administrator privileges required, restarting as administrator...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb RunAs -ArgumentList '--elevated'"
    exit /b
)

REM If already elevated, remove the --elevated argument
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
    echo Failed to install Python. Please check winget or your network connection.
    pause
    exit /b 1
)

REM 2. Upgrade pip
echo [2/6] Upgrading pip...
python -m ensurepip --upgrade
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to upgrade pip.
    pause
    exit /b 1
)

REM 3. Install Git
echo [3/6] Installing Git...
winget install --id Git.Git -e --silent
if errorlevel 1 (
    echo Failed to install Git.
    pause
    exit /b 1
)

REM 4. Clone the sample repository to Desktop
echo [4/6] Cloning sample code to Desktop...
cd /d "%USERPROFILE%\Desktop"
if exist example-code-2025 (
    echo Directory already exists, skipping clone.
) else (
    git clone https://github.com/CSIE-Camp/example-code-2025.git
    if errorlevel 1 (
        echo Clone failed. Please check your network or the repo URL.
        pause
        exit /b 1
    )
)

REM 5. Install Python dependencies
echo [5/6] Installing Python dependencies...
cd example-code-2025
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install requirements.
    pause
    exit /b 1
)

REM 6. Install Discord Desktop
echo [6/6] Installing Discord Desktop...
winget install --id Discord.Discord -e --silent
if errorlevel 1 (
    echo Failed to install Discord.
    pause
    exit /b 1
)

echo.
echo All tasks completed! Press any key to exit.
pause
exit /b 0
