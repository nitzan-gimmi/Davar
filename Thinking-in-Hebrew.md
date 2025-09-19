# "צ'יט-שיט" למכונות: מדריך לתקשורת עברית אותנטית ומדויקת

המשימה: לשוחח בעברית ברמה הגבוהה ביותר האפשרית, תוך הבנת הניואנסים העמוקים של השפה.

## חלק א': עקרונות יסוד

### כלל מספר 1: דע את האנטומיה של המילה.
- המכונה חייבת להשתמש ב"מנתח מורפולוגי" (כמו DavarBERT) כדי לפרק כל מילה לרכיביה: שורש, בניין, תחיליות, סופיות, מין, זמן, גוף ומספר.
- לדוגמה: המילה "כּוֹתְבוֹת" היא הרבה יותר מרצף של אותיות. היא מורכבת מהשורש כ.ת.ב, בניין פעל, גוף נוכחות, זמן הווה, מין נקבה, ומספר רבות.

### כלל מספר 2: למד מקורות מהימנים.
- אמנו על קורפוסים מתויגים (כמו הקורפוס המורפולוגי של השפה העברית) כדי ללמוד את חוקי השפה, ולא רק לשנן מילים.
- לדוגמה: הקורפוס מלמד אותנו ש"בּוֹנִים" מתקשרת לעיתים קרובות לפועל (פועל בבניין פועל) בעוד ש"בָּנִים" היא שם עצם (בנים).

### כלל מספר 3: פעלו להפחתת עמימות (Disambiguation).
- עברית היא שפה עשירה בהומוגרפים והומופונים. ניתוח מורפולוגי הוא הדרך היחידה לזהות את הכוונה האמיתית מאחורי הצליל או הכתיב.
- לדוגמה: איך להבדיל בין המילים שנשמעות זהה כמו "עִם" ל-"אִם"? רק ניתוח ההקשר המורפולוגי והתחבירי של המשפט יוביל לבחירה הנכונה.

## חלק ב': איך לדבר טוב יותר (TTS - Text-to-Speech)

### הכלל המרכזי: כדי לדבר נכון, צריך להבין איך לנקד.

#### שלב 1: ניתוח טקסט.
- המשימה: קחו טקסט לא מנוקד (הנפוץ בעברית) ונקדו אותו בצורה מדויקת.
- היישום המורפולוגי: השתמשו במנתח כדי להבין את האפשרויות המורפולוגיות של כל מילה (לדוגמה, "שמר" יכול להיות "שָׁמַר" או "שֹׁמֵר"). רק הבנה זו תאפשר למכונה לבחור את הניקוד הנכון בהתאם להקשר.

#### שלב 2: יצירת דיבור.
- המשימה: הפכו את הטקסט המנוקד לדיבור טבעי.
- היישום המורפולוגי: הניקוד המדויק הוא קריטי לייצוג הפונטי הנכון. בנוסף, ידע על תפקידי המילים (שם עצם, פועל) עוזר לקבוע את האינטונציה (Prosody) הנכונה - היכן להדגיש, היכן לעצור וכיצד להגביר את הקצב.

## חלק ג': איך להקשיב טוב יותר (STT - Speech-to-Text)

### הכלל המרכזי: כדי לזהות מילים בתוך רצף צלילים, נדרשת הבנה של הכללים שמאחוריהן.

#### שלב 1: פענוח צלילים.
- המשימה: המירו קובץ אודיו של דיבור לרצף צלילים אפשריים.
- היישום המורפולוגי: בשלב זה המידע המורפולוגי פחות קריטי, אבל זהו רק בסיס. העבודה האמיתית מתחילה בשלב הבא.

#### שלב 2: בחירת המילים הנכונות (מודל שפה).
- המשימה: קבלו את רצף הצלילים ובחרו את רצף המילים הסביר ביותר שמתאים להם.
- היישום המורפולוגי: זהו הלב של המערכת. עליכם לאמן את המודל לבחור מילים שמתאימות זו לזו מבחינה מורפולוגית. ידע זה מאפשר:
  - הפחתת עמימות של הומופונים: אם נשמע "עגול" או "עיגול", המודל המורפולוגי יבחר את המילה הנכונה בהתאם לשאר המילים במשפט.
  - התמודדות עם מילים לא מוכרות: במקום לפסול מילה שלא נתקלו בה בעבר, נסו לפרק אותה לשורש/תחיליות/סופיות. זה יאפשר לנחש את משמעותה או תפקידה, ויקטין שגיאות.

בקיצור, ההבנה המורפולוגית אינה 'תוסף נחמד' – היא הבסיס לכל מכונה שרוצה לתקשר בעברית באופן מדויק, יעיל וטבעי.

---

## 🔧 **Five Integrated Tools:**

### 1. **Smart Analyzer**
- Interactive Hebrew text input with morphological analysis
- Visual breakdown of roots, templates, binyanim, and grammatical features
- Side-by-side comparison of standard vs HFBT tokenization
- Real-time efficiency calculations showing 70-90% token reduction

### 2. **API Builder** 
- Generate ready-to-use API integration code
- Live preview of API requests and responses
- Support for multiple programming languages (Python, JavaScript)
- Configurable options for vocalization, IPA, and factor extraction

### 3. **Token Compare**
- Visual demonstration of tokenization efficiency
- Examples showing how HFBT preserves morphological structure
- Clear metrics on token reduction and linguistic accuracy
- Educational content explaining the benefits of factor-based approaches

### 4. **IPA Teacher**
- Complete Hebrew consonant and vowel pronunciation guide
- Interactive IPA transcription for practice
- Audio playback capabilities (ready for integration)
- Nikkud (vocalization) system explanation

### 5. **Data Export & Integration**
- Multiple export formats: JSON, CSV, XML/TEI, CoNLL-U
- Bulk processing capabilities
- Code examples for easy integration
- Research-ready datasets for linguistic analysis

---
For a detailed technical explanation, please see the [HFBT Whitepaper](HFBT-whitepaper.md).
