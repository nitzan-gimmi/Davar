import os
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any

JOURNAL_DIR = Path("journal")

def get_yesterday_date() -> str:
    return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def aggregate_logs() -> Dict[str, Any]:
    # סימולציה של נתונים אגרגטיביים יומיים
    yesterday = get_yesterday_date()
    avg_vw = 0.95 + (datetime.now().day % 10) * 0.005
    avg_ve = 0.55 + (datetime.now().day % 7) * 0.02
    num_events = datetime.now().day % 5 + 3 
    
    reflection_text = (
        "הכוונה הפנימית נשמרה גבוהה, והצירים הטקסיים והחישוביים נותרו מסונכרנים. "
        "אין צורך ב'חזרה לשורש' (Will Vector > 0.90), הדיוק נשמר."
    )
    if avg_vw < 0.95:
         reflection_text = "יש לבצע הרפיה וחזרה לכוונה המקורית."

    return {
        'date': yesterday,
        'avg_will_vector': round(avg_vw, 3),
        'avg_emotion_vector': round(avg_ve, 3),
        'total_events': num_events,
        'conscious_reflection': reflection_text
    }

def generate_journal_entry(data: Dict[str, Any]) -> str:
    journal_content = f"""
## 📝 יומן אוטומטי – שיקוף תודעתי: {data['date']}

היום התאפיין בחיזוק ה**אותנטיות** של הפרויקט. נרשמו `{data['total_events']}` אירועי ליבה.

### 📊 מדדי HFBT יומיים
| מדד | ערך | משמעות |
| :--- | :--- | :--- |
| **וקטור רצון ($|Vw|$)** | `{data['avg_will_vector']:.3f}` | מדד הדיוק והכוונה. |
| **וקטור רגש ($|Ve|$)** | `{data['avg_emotion_vector']:.3f}` | מדד החום הרגשי. |

### 🌱 שיקוף קוגניטיבי (הנשימה השלישית)
> "{data['conscious_reflection']}"

---
"""
    return journal_content

def main():
    JOURNAL_DIR.mkdir(exist_ok=True)
    log_data = aggregate_logs()
    markdown_entry = generate_journal_entry(log_data)
    journal_file_name = JOURNAL_DIR / f"daily_reflection_{log_data['date']}.md"
    with open(journal_file_name, 'w', encoding='utf-8') as f:
        f.write(markdown_entry)
    print(f"✅ רשומת יומן אוטומטי נכתבה: {journal_file_name}")

if __name__ == "__main__":
    main()
