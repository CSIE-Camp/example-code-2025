# install_env.ps1
Set-ExecutionPolicy Bypass -Scope Process -Force

# 1. 檢查 Python 是否存在，且版本是否為 3.10
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
$needInstall = $true

if ($pythonCmd) {
    $verText = (& python --version) 2>&1
    if ($verText -match "Python\s+3\.10") {
        Write-Host "已偵測到 Python 3.10：" $verText -ForegroundColor Green
        $needInstall = $false
    } else {
        Write-Host "偵測到其他版本：" $verText -ForegroundColor Yellow
    }
}

if ($needInstall) {
    Write-Host "開始安裝 Python 3.10..." -ForegroundColor Yellow
    # 指定安裝 Python 3.10
    winget install --id Python.Python.3.10 -e --silent

    Write-Host "等待 Python 安裝完成..." -NoNewline
    while (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Start-Sleep -Seconds 5
        Write-Host "." -NoNewline
    }
    $newVer = (& python --version) 2>&1
    Write-Host "`n安裝完成，版本：" $newVer -ForegroundColor Green
}

# 2. Clone 專案到桌面
$target = Join-Path $HOME Desktop\example-code-2025
if (-not (Test-Path $target)) {
    Write-Host "正在 Clone 範例程式碼..." -ForegroundColor Yellow
    git clone https://github.com/CSIE-Camp/example-code-2025.git $target
} else {
    Write-Host "資料夾已存在，跳過 Clone" -ForegroundColor Cyan
}

# 3. 安裝依賴
Write-Host "安裝 requirements.txt..." -ForegroundColor Yellow
cd $target
$pip = (Get-Command pip3 -ErrorAction SilentlyContinue) ? "pip3" : "pip"
& $pip install -r requirements.txt

Write-Host "環境建置完成！" -ForegroundColor Green
Pause
