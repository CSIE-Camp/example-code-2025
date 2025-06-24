if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python 未安裝，開始安裝..."
    winget install --id Python.Python.3 -e --silent
} else {
    Write-Host "已偵測到 Python：" (python --version)
}

cd ~/Desktop && git clone https://github.com/CSIE-Camp/example-code-2025.git
cd ~/Desktop/example-code-2025 && pip3 install -r requirements.txt