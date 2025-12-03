from .hfbt_core import HFBTTokenizer
from .hic_core_logic import IntentCore
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GHC_PFC")

class PFCPipeline:
    """
    Pre-Frontal Cortex Pipeline
    מתזמר בין הטוקניזציה, ניתוח הכוונה והפלט.
    """
    def __init__(self):
        self.tokenizer = HFBTTokenizer()
        self.intent_core = IntentCore()

    def process_request(self, user_input: str) -> dict:
        logger.info(f"Processing input: {user_input}")
        
        # 1. טוקניזציה
        tokens = self.tokenizer.tokenize(user_input)
        
        # 2. חישוב וקטור רצון
        vector = self.intent_core.calculate_vector(user_input, "general")
        
        # 3. הכרעה
        approved = self.intent_core.validate_action(vector)
        
        return {
            "input": user_input,
            "tokens_count": len(tokens),
            "vector": {
                "HTQI": vector.htqi,
                "IPI": vector.ipi,
                "EAS": vector.eas
            },
            "status": "APPROVED" if approved else "REJECTED_BY_PROTOCOL"
        }
