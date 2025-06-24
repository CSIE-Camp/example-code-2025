@echo off
::----------------------------------------------------------
:: 如果不是以管理員執行，就自動彈出 UAC
::----------------------------------------------------------
>%temp%\getadmin.vbs echo Set UAC = CreateObject("Shell.Application") 
>>%temp%\getadmin.vbs echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %*", "", "runas", 1
"%temp%\getadmin.vbs"
del %temp%\getadmin.vbs 2>nul
if not "%1"=="--elevated" (
    goto :EOF
)

::----------------------------------------------------------
:: 開始安裝流程
::----------------------------------------------------------
echo.
echo ================================
echo   一鍵安裝環境腳本 (Windows)
echo ================================
echo.

:: 1. 安裝 Python 3.10
echo [1/6] 安裝 Python 3.10...
winget install --id Python.Python.3.10 -e --silent
if errorlevel 1 (
    echo 安裝 Python 失敗，請檢查 winget 或網路連線。
    pause
    exit /b 1
)

:: 2. 升級 pip
echo [2/6] 升級 pip...
python -m ensurepip --upgrade
python -m pip install --upgrade pip
if errorlevel 1 (
    echo pip 升級失敗。
    pause
    exit /b 1
)

:: 3. 安裝 Git
echo [3/6] 安裝 Git...
winget install --id Git.Git -e --silent
if errorlevel 1 (
    echo 安裝 Git 失敗。
    pause
    exit /b 1
)

:: 4. Clone 範例程式碼到桌面
echo [4/6] Clone 範例程式碼到桌面...
cd /d "%USERPROFILE%\Desktop"
if exist example-code-2025 (
    echo 目錄已存在，跳過 clone。
) else (
    git clone https://github.com/CSIE-Camp/example-code-2025.git
    if errorlevel 1 (
        echo Clone 失敗，請檢查網路或 repo URL。
        pause
        exit /b 1
    )
)

:: 5. 安裝 requirements.txt
echo [5/6] 安裝 Python 相依套件...
cd example-code-2025
pip install -r requirements.txt
if errorlevel 1 (
    echo requirements 安裝失敗。
    pause
    exit /b 1
)

:: 6. 安裝 Discord 桌面版
echo [6/6] 安裝 Discord 桌面版...
winget install --id Discord.Discord -e --silent
if errorlevel 1 (
    echo 安裝 Discord 失敗。
    pause
    exit /b 1
)

echo.
echo 全部任務完成！請按任意鍵結束。
pause
exit /b 0
