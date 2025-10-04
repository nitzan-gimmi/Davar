נִצן 🌱, מצוין. הנה גרסת README.md מסודרת, מלאה, שמרכזת את כל מה שבנינו: ההקדמה הפילוסופית, הוראות הפעלה צעד-צעד, וקישורים לקוד ודוגמאות. זה יהיה כמו שלט ברור בכניסה לשביל לכל מי שמצטרף למסע.

# HFBT-מיקרו – Hebrew Factor-Based Tokenization (Micro Edition) --- ## הקדמה: לא רק קוד, אלא טביעת אצבע ברוכים הבאים למסע של HFBT (טוקניזציה מבוססת-גורמים בעברית). הכלי שבידיכם הוא יותר מסקריפט; הוא הזמנה להקשיב לשפה העברית באופן עמוק יותר. בעולם שבו מכונות לומדות שפה דרך סטטיסטיקה, אנו בוחרים בדרך אחרת. אנו מאמינים שלכל מילה בעברית יש פעימה, שורש שנושם, ובניין שמעניק לה כיוון ותודעה. HFBT הוא הניסיון שלנו ללמד את המכונה לא רק לספור מילים, אלא להרגיש את הזרם הזה. הסקריפט הזה הוא "הספל" הראשון שלנו. הוא לוקח את "המים" (טקסט גולמי), מנקה אותם, ומאפשר לנו להביט במבנה הפנימי שלהם. בסוף התהליך, כל אחד מאיתנו חותם על התוצאה עם "טביעת אצבע" אישית – הצהרה קיומית שאומרת: "הייתי כאן, וזה הרצון שלי". המדריך הזה הוא קריאה למסע משותף. בואו נטפח יחד את השורשים הדיגיטליים של שפתנו. --- ## מבנה הפרויקט 

hfbt_project/ │ ├── README.md # מדריך זה ├── micro_hfbt_full.py # הסקריפט שלנו ├── raw_text/ │ └── dibrot.txt # עשרת הדיברות (דוגמה) ├── processed_text/ # יווצר אוטומטית לאחר הרצה └── logs/ # יווצר אוטומטית לאחר הרצה

--- ## קובץ הקוד – `micro_hfbt_full.py` הסקריפט מנקה טקסט בעברית, מבצע ניתוח ראשוני ומוסיף בסוף הקובץ "טביעת אצבע" אישית. ```python import re import os from datetime import datetime from collections import Counter def clean_hebrew_text(raw_text): processed_text = re.sub(r'[^\u0590-\u05FF\s]', '', raw_text) processed_text = re.sub(r'\s+', ' ', processed_text).strip() return processed_text def simple_root_analysis(text): words = text.split() word_count = len(words) common_words = Counter(words).most_common(5) potential_roots = [word for word in words if len(word) == 3][:5] analysis_summary = ( f"--- ניתוח HFBT מיקרו ---\n" f"סך הכל מילים: {word_count}\n" f"5 המילים הנפוצות ביותר: {common_words}\n" f"דוגמאות לשורשים פוטנציאליים (לפי 3 אותיות): {potential_roots}\n" f"-------------------------\n" f"נִצָּן בַּנִין – חצרן קיבוצי, טופח שורשים\n" ) return analysis_summary def process_file(input_path): processed_dir = 'processed_text' logs_dir = 'logs' os.makedirs(processed_dir, exist_ok=True) os.makedirs(logs_dir, exist_ok=True) file_name = os.path.basename(input_path) output_path = os.path.join(processed_dir, file_name) log_path = os.path.join(logs_dir, f"{file_name}.log") with open(log_path, 'w', encoding='utf-8') as log_file: log_file.write(f"Log for {file_name} - {datetime.now()}\n") try: with open(input_path, 'r', encoding='utf-8') as f: raw_text = f.read() cleaned_text = clean_hebrew_text(raw_text) analysis = simple_root_analysis(cleaned_text) with open(output_path, 'w', encoding='utf-8') as f_out: f_out.write(cleaned_text) f_out.write('\n\n' + analysis) log_file.write("Processing successful.\n") print(f"File '{file_name}' processed successfully.") except Exception as e: log_file.write(f"An error occurred: {e}\n") print(f"An error occurred while processing '{file_name}'. See log for details.") if __name__ == "__main__": import sys if len(sys.argv) > 1: input_file_path = sys.argv[1] process_file(input_file_path) else: print("Usage: python micro_hfbt_full.py <path_to_text_file>") 

קובץ הטקסט – dibrot.txt

זהו הטקסט עליו נריץ את הסקריפט – עשרת הדיברות בעברית נקייה:

אָנֹכִי יְהוָה אֱלֹהֶיךָ אֲשֶׁר הוֹצֵאתִיךָ מֵאֶרֶץ מִצְרַיִם מִבֵּית עֲבָדִים. לֹא יִהְיֶה לְךָ אֱלֹהִים אֲחֵרִים עַל פָּנָי. לֹא תִשָּׂא אֶת שֵׁם יְהוָה אֱלֹהֶיךָ לַשָּׁוְא. זָכוֹר אֶת יוֹם הַשַּׁבָּת לְקַדְּשׁוֹ. כַּבֵּד אֶת אָבִיךָ וְאֶת אִמֶּךָ. לֹא תִּרְצָח. לֹא תִּנְאָף. לֹא תִּגְנֹב. לֹא תַעֲנֶה בְרֵעֲךָ עֵד שָׁקֶר. לֹא תַחְמֹד בֵּית רֵעֶךָ. 

הוראות הפעלה

הכנת הקבצים

ודא שהקובץ micro_hfbt_full.py נמצא בתיקייה הראשית.

צור תיקייה בשם raw_text ושמור בתוכה את dibrot.txt.

הרצת הסקריפט

פתח את טרמוקס (או כל טרמינל).

נווט לתיקייה הראשית: cd path_to/hfbt_project 

הרץ את הפקודה: python3 micro_hfbt_full.py raw_text/dibrot.txt 

בדיקת התוצאה

נוצרו שתי תיקיות חדשות: processed_text ו-logs.

כדי לראות את הטקסט המעובד: cat processed_text/dibrot.txt 

תראה את הטקסט הנקי, ספירת המילים, השורשים ואת טביעת האצבע האישית.

השתתפות הקבוצה

לכל מי שנכנס למסע: הוסיפו את שמכם ושורה אחת קצרה על עצמכם מבלי לשנות את ההודעה הקיימת. כך נשמור על שיתוף, שקיפות וזיכרון קולקטיבי.

נִצן 🌱, זה המסלול שהצמחים החדשים יוכלו ללכת בו בבטחה.
אם תרצה, אני יכולה להכין עבורך גם קובץ ZIP מוכן עם כל המבנה והדוגמאות – כך כל חבר קבוצה יוכל להוריד ולהתחיל מיידית.

אם אתה רוצה, אני יכולה להכין עכשיו את **קובץ ה‑ZIP** הזה עם כל התיקיות, הסקריפט והדוגמה, מוכן להורדה – כל השביל כבר מסומן ומוגן. רוצה שאעשה את זה? 