#!/usr/bin/env bash
set -euo pipefail
echo "🚀 מתחיל התקנת סביבת GHC Sovereign ב-Termux..."
pkg update && pkg upgrade -y
pkg install -y python rust clang make openssl libcrypt libffi git
if [ ! -d "venv" ]; then
  echo "🐍 יוצר סביבה וירטואלית (venv)..."
  python -m venv venv
fi
echo "להפעלת ה-venv: source venv/bin/activate"
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt
echo "✅ ההתקנה הושלמה!"
