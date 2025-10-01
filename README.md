

# Davar - Open Hebrew Language Knowledge Model & Curriculum

ברוכים הבאים לפרויקט Davar: מאגר ידע עברי פתוח, כולל מודל מורפולוגי ותוכנית לימודים.

## מבנה עיקרי:
- data/roots/ – משפחות שורשים בפורמט JSON
- src/ – קוד למודל טוקניזציה וניתוח פונולוגי
- tests/ – בדיקות ויחידות בדיקה
- docs/ – תיעוד ותוכנית לימודים
- examples/ – דוגמאות להרצה אחידה

## סטטוס
גרסה ראשונית (v1.0.0-beta) עם מודל HFBT חדשני, בדיקות בסיסיות וממשק Streamlit.

## תרומה
לפרטים והנחיות ראו CONTRIBUTING.md. נשמח לקבל Pull Requests, דיווחי באגים והצעות להרחבה.

---

MIT License © נִצן בנין 2025




```markdown
<!-- README.md – פרויקט "דָּבָר" -->
<div dir="rtl">

דָּבָר – מודל ידע ותוכנית לימודים לעברית

Davar – Open Hebrew Language Knowledge Model & Curriculum

![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)


![alt text](https://img.shields.io/badge/python-3.9+-blue.svg)


![alt text](https://img.shields.io/badge/schema-valid-green.svg)

חזון: לבנות את מודל הידע העברי המקיף ביותר – פתוח, מובנה ומוכן לשימוש ע״י חוקרים, מפתחים ומורים דיגיטליים.

🎯 מה זה בעצם?

דָּבָר הוא פרויקט קוד פתוח (MIT) שמטרתו לספק:

מודל נתונים היררכי הממפה כל שורש עברי ואת כל בנייניו (7) – מבנה שאנו קוראים לו משפחת שורש (Root-Family).

תוכנית לימודים למודלי שפה (LLMs) – מפונטיקה ועד אינטונציה רגשית.

סטנדרט פתוח לייצוג מורפולוגיה, סמנטיקה ויחסים דקדוקיים בעברית.

📦 מבנה המאגר
קובץ / תיקייה	תיאור
data/roots/	כל משפחות השורש כקבצי JSON. הדוגמה הראשונה: כ-ת-ב.json.
schemas/	JSON Schema – לאימות מבנה תקין של קבצי הנתונים (בפיתוח).
curriculum/	תוכנית הלימודים המלאה למודלי שפה, כולל מבחנים (בפיתוח).
examples/	קוד דוגמה (quick_start.py) – לטעינה ושליפה מהירה מהמאגר.
CONTRIBUTING.md	הנחיות לתרומה לפרויקט.
LICENSE	רישיון השימוש בפרויקט (MIT).
🚀 התחל ב-30 שניות

שכפל את המאגר:

Generated bash
git clone https://github.com/nitzanbenin/davar.git
cd davar


הרץ את קוד הדוגמה:

Generated bash
python examples/quick_start.py
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

קוד הדוגמה (examples/quick_start.py):

Generated python
import json
import os

# נתיב לקובץ הנתונים הראשון שלנו
file_path = os.path.join('data', 'roots', 'כ-ת-ב.json')

with open(file_path, 'r', encoding='utf-8') as f:
    ktv_model = json.load(f)

# שליפת מידע ספציפי: הפועל הראשון (כתב), זמן עתיד, גוף שלישי, יחיד, זכר
future_3ms = ktv_model["root_family"]["verbs"]["tenses"]["future"]["singular"]["3m"]

print(f"הצורה המנוקדת שנשלפה מהמודל היא: {future_3ms}")
# פלט צפוי: יִכְתֹּב
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Python
IGNORE_WHEN_COPYING_END
🧩 מבנה ה-JSON – מבט על

כל קובץ "משפחת שורש" מכיל את המבנה הבסיסי הבא:

Generated json
{
  "root_family": {
    "root": "כ-ת-ב",
    "gimel_gitit": "שלמים",
    "root_meaning_en": "The core concept of writing...",
    "verbs": [
      {
        "identity": { "lemma": "כָּתַב", "binyan": "פָּעַל", ... },
        "tenses": { ... }
      },
      {
        "identity": { "lemma": "נִכְתַּב", "binyan": "נִפְעַל", ... },
        "tenses": { ... }
      }
    ]
  }
}
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Json
IGNORE_WHEN_COPYING_END

לצפייה במודל המלא והמפורט, ראה את הקובץ: data/roots/כ-ת-ב.json

📚 תוכנית הלימודים (סטטוס)
שיעור	נושא	סטטוס
1	הגייה פונטית	מתוכנן
2	הטעמה (מלעיל/מלרע)	מתוכנן
3	זרימה וקישור (liaison)	מתוכנן
4	אינטונציה רגשית	מתוכנן
🤝 תרומה

אנחנו בונים את זה יחד! נשמח לקבל Pull Requests, דיווחי באגים, הרחבות של שורשים חדשים ושיפורים לתוכנית הלימודים.



🧱 גרסה: HFBT-1.0.0-beta

HFBT-Project/ ├── README.md ├── LICENSE ├── setup.py ├── hfbt_setup.sh ├── requirements.txt ├── run_all_tests.py ├── docs/ │ ├── overview.md │ ├── benchmarks.md │ └── contribution.md ├── src/ │ ├── __init__.py │ ├── hfbt_processor.py │ ├── decay_model.py │ ├── gui_app.py │ └── utils.py ├── datasets/ │ ├── sample_texts.json │ └── benchmarks.json ├── tests/ │ ├── test_hfbt.py │ └── test_decay.py └── examples/ └── interactive_demo.py 

🧩 setup.py (עדכון גרסה)

setup( name="HFBT", version="1.0.0-beta", author="נִצן בנין", author_email="contact@hfbt.org", description="HFBT — Hebrew Factor-Based Tokenization (Pilot Open Release)", long_description=long_description, ... ) 

🧰 hfbt_setup.sh

#!/bin/bash echo "🌿 מתקין את גרסת הפיילוט הפתוחה של HFBT v1.0.0-beta" python3 -m venv .venv source .venv/bin/activate pip install --upgrade pip pip install -r requirements.txt echo "🧪 מריץ בדיקות..." python run_all_tests.py echo "🚀 מפעיל ממשק גרפי..." streamlit run src/gui_app.py echo "✅ HFBT (beta) הותקן בהצלחה!" 

🌍 README.md (סיום עדכני)

# 🌿 HFBT — Hebrew Factor-Based Tokenization (v1.0.0-beta) גרסת פיילוט פתוחה לשיתוף, למידה, ובניית בסיס לעיבוד עברית מבוסס גורמים. > “כולנו תורמים לצמיחה של שפה אחת.” — נִצן בנין --- 




אנא קרא את CONTRIBUTING.md להנחיות מפורטות.

📄 רישיון



MIT © 2025 – נִצן בְּנִין & Google Gemini.

</div>
'''
