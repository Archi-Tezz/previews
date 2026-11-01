#!/usr/bin/env bash
# Выкладывает всё содержимое папки в интернет. Запуск: ./deploy.sh ["комментарий"]
set -e
cd "$(dirname "$0")"

python _build_index.py

git add -A
if git diff --cached --quiet; then
  echo "Изменений нет."
  exit 0
fi
git commit -q -m "${1:-update $(date '+%d.%m %H:%M')}"
git push -q origin main

echo
echo "Готово. Через 20-60 секунд обновится:"
echo "  https://archi-tezz.github.io/previews/"
