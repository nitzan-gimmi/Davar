from dataclasses import dataclass
import random

@dataclass
class VectorOfWill:
    htqi: float  # Hebrew Text Quality Index
    ipi: float   # Intent Penetration Index
    eas: float   # Emotional Alignment Score

class IntentCore:
    """
    מנוע ההכרעה מבוסס וקטור הרצון (VoW).
    """
    def __init__(self, htqi_threshold=0.96, ipi_threshold=0.92):
        self.htqi_threshold = htqi_threshold
        self.ipi_threshold = ipi_threshold

    def calculate_vector(self, text: str, context: str) -> VectorOfWill:
        # סימולציה של חישוב הוקטורים בזמן אמת
        # במערכת המלאה זה מתבצע מול גרף הידע
        return VectorOfWill(
            htqi=0.98,  # ברירת מחדל גבוהה
            ipi=random.uniform(0.85, 0.99),
            eas=random.uniform(0.80, 0.95)
        )

    def validate_action(self, vector: VectorOfWill) -> bool:
        """האם הפעולה עוברת את סף האיכות?"""
        return vector.htqi >= self.htqi_threshold
