#!/usr/bin/env bash

echo "🚀 מתחיל התקנת סביבת GHC Sovereign ב-Termux..."

pkg update && pkg upgrade -y
pkg install -y python rust clang make openssl libcrypt libffi git

if [ ! -d "venv" ]; then
  echo "🐍 יוצר סביבה וירטואלית (venv)..."
  python -m venv venv
fi

source venv/bin/activate

echo "📦 מתקין ספריות Python מ-requirements.txt..."

pip install --upgrade pip
pip install -r requirements.txt

echo "✅ ההתקנה הושלמה! הפעל את המערכת עם: uvicorn ghc_core.gql_final_integration:app --reload"
