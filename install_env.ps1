# install_env.ps1
# ──────────────────────────────────────────────
# Allow this script to bypass execution policy for this session
Set-ExecutionPolicy Bypass -Scope Process -Force

# 1. Install Python if it's not already installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python not found. Installing now..." -ForegroundColor Yellow
    winget install --id Python.Python.3 -e --silent

    # Wait until Python shows up in PATH
    Write-Host "Waiting for Python installation to complete" -NoNewline
    while (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Start-Sleep -Seconds 5
        Write-Host "." -NoNewline
    }
    Write-Host "`nInstallation complete. Detected version:" (python --version) -ForegroundColor Green
}
else {
    Write-Host "Python already installed. Version:" (python --version) -ForegroundColor Green
}

# 2. Clone the example repository to the Desktop
$target = Join-Path $HOME Desktop\example-code-2025
if (-not (Test-Path $target)) {
    Write-Host "Cloning example-code-2025 repository..." -ForegroundColor Yellow
    git clone https://github.com/CSIE-Camp/example-code-2025.git $target
}
else {
    Write-Host "Directory already exists. Skipping clone." -ForegroundColor Cyan
}

# 3. Install Python dependencies
Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Yellow
Set-Location $target

# Choose pip3 if available, otherwise pip
$pip = (Get-Command pip3 -ErrorAction SilentlyContinue) ? "pip3" : "pip"
& $pip install -r requirements.txt

Write-Host "Environment setup is complete!" -ForegroundColor Green
Pause
