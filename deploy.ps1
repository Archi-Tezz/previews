# Выкладывает содержимое папки в интернет.
# Запуск: .\deploy.ps1   или   .\deploy.ps1 "комментарий"
param([string]$Message = "")

Set-Location $PSScriptRoot

python _build_index.py
if ($LASTEXITCODE -ne 0) { Write-Host "Ошибка сборки списка." -ForegroundColor Red; exit 1 }

git add -A
git diff --cached --quiet
if ($LASTEXITCODE -eq 0) { Write-Host "Изменений нет." -ForegroundColor Yellow; exit 0 }

if ($Message -eq "") { $Message = "update " + (Get-Date -Format "dd.MM HH:mm") }
git commit -q -m $Message
git push -q origin main
if ($LASTEXITCODE -ne 0) { Write-Host "Push не прошёл." -ForegroundColor Red; exit 1 }

Write-Host ""
Write-Host "Готово. Через 20-60 секунд обновится:" -ForegroundColor Green
Write-Host "  https://archi-tezz.github.io/previews/"
