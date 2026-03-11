"""
HFBT v5.0 - Nitzan Axis Protocol
Hebrew Factor-Based Tokenization with Geometric Semantic Navigation

Core Components:
- HFBTGeometricEngine: Morphological decomposition + Identity resolution
- HBE27 Encoder: Deterministic encoding using Hebrew base-27
- GOKS: Epigenetic memory system
- CoherenceVector: Intent tracking and semantic drift detection
"""

import math
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field

# ============================================================================
# HEBREW BASE-27 ENCODING (HBE)
# ============================================================================
ALPHABET_HBE27 = "אבגדהוזחטיכלמנסעפצקרשתךםןףץ"
HBE_MAP = {char: i for i, char in enumerate(ALPHABET_HBE27)}

@dataclass
class TokenMetadata:
    """Metadata for each token in the system"""
    identity: str
    hbe_id: str
    residual_no: float
    circle: str
    status: str
    vector: Optional[List[float]] = None


class HBE27Encoder:
    """Hebrew Base-27 Deterministic Encoding"""
    
    @staticmethod
    def encode(word: str) -> str:
        """Convert Hebrew word to HBE-27 ID"""
        total = sum(HBE_MAP.get(c, 0) * (27**i) for i, c in enumerate(word[:3]))
        return f"HBE-{total}"
    
    @staticmethod
    def decode(hbe_id: str) -> Optional[str]:
        """Reverse lookup (informational only)"""
        try:
            num = int(hbe_id.replace("HBE-", ""))
            result = ""
            for i in range(3):
                result += ALPHABET_HBE27[num % 27]
                num //= 27
            return result
        except:
            return None


# ============================================================================
# COHERENCE VECTOR (The Intent Tracking System)
# ============================================================================
@dataclass
class CoherenceVector:
    """
    Tracks narrative coherence and prevents semantic drift.
    Components:
    - clarity: Precision of intent (0.0-1.0)
    - emotional_stability (EAS): Emotional alignment (0.0-1.0)
    - narrative_continuity: Prevents context collapse (0.0-1.0)
    - intent_precision (IPI): Phonetic/semantic alignment (0.0-1.0)
    """
    clarity: float = 1.0
    emotional_stability: float = 1.0
    narrative_continuity: float = 1.0
    intent_precision: float = 1.0
    timestamp: int = 0
    
    def magnitude(self) -> float:
        """Calculate overall coherence (0=broken, 1=perfect)"""
        return (self.clarity + self.emotional_stability + 
                self.narrative_continuity + self.intent_precision) / 4.0
    
    def is_resonant(self, threshold: float = 0.80) -> bool:
        """Check if coherence exceeds threshold (EAS >= threshold)"""
        return self.emotional_stability >= threshold
    
    def decay(self, factor: float = 0.02) -> None:
        """Natural decay over time (entropy increase)"""
        self.clarity = max(0.0, self.clarity - factor)
        self.narrative_continuity = max(0.0, self.narrative_continuity - factor)


# ============================================================================
# IDENTITY RESOLUTION (Branching Logic for Name Disambiguation)
# ============================================================================
class IdentityRegistry:
    """Handles ambiguous names and their contextual meanings"""
    
    def __init__(self):
        # Example: "מורן" (Moran) can mean different things at different social distances
        self.registry: Dict[str, Dict[int, Dict]] = {
            "מורן": {
                0: {
                    "full_name": "מורן",
                    "context": "Core/Singular",
                    "meaning": "The One",
                    "circle": "א-Core (Echad)"
                },
                150: {
                    "full_name": "מורן (טייסת)",
                    "context": "Branch/Squadron",
                    "meaning": "The Many",
                    "circle": "וה-Dunbar Limit"
                }
            }
        }
    
    def resolve(self, word: str, vow_distance: int) -> Optional[Dict]:
        """Resolve identity based on Vector of Will (VoW) distance"""
        if word not in self.registry:
            return None
        
        branches = self.registry[word]
        # Find closest branch to the VoW distance
        closest_vr = min(branches.keys(), key=lambda k: abs(k - vow_distance))
        return branches[closest_vr]


# ============================================================================
# DUNBAR CIRCLES (Social/Cognitive Distance Model)
# ============================================================================
class DunbarCircles:
    """Models cognitive proximity based on Dunbar's number theory"""
    
    CIRCLES = [
        (0, 0, "א-Core (Echad)"),           # The singular core
        (1, 10, "ו-Intimate"),               # Intimate circle
        (11, 40, "ע-Close"),                 # Close friends
        (41, 120, "בא-Social"),              # Social circle
        (121, 250, "וה-Dunbar Limit"),      # Dunbar limit
        (251, 1500, "יח-Distant")            # Distant awareness
    ]
    
    @staticmethod
    def get_label(distance: int) -> str:
        """Get circle label based on distance"""
        for low, high, label in DunbarCircles.CIRCLES:
            if low <= distance <= high:
                return label
        return "Outside"


# ============================================================================
# VECTOR OF WILL (VoW) GATE
# ============================================================================
class VoWGate:
    """
    Gate keeper for semantic integrity.
    Blocks tokens that don't meet the threshold of intentional coherence.
    
    Formula: VoW = 0.4*HTQI + 0.3*EAS + 0.3*IPI
    """
    THRESHOLD = 0.92
    
    @staticmethod
    def evaluate(htqi: float, eas: float, ipi: float) -> float:
        """
        Calculate Vector of Will
        - HTQI: Hebrew Text Quality Index (morphological accuracy)
        - EAS: Emotional Alignment Stability
        - IPI: Intent Precision Index
        """
        vow = (0.4 * htqi) + (0.3 * eas) + (0.3 * ipi)
        return vow
    
    @staticmethod
    def passes_gate(vow: float) -> bool:
        """Check if VoW meets minimum threshold"""
        return vow >= VoWGate.THRESHOLD


# ============================================================================
# RESIDUAL CALCULATION
# ============================================================================
class ResidualCalculator:
    """
    Measures the gap between human intention and system output.
    
    Formula: No = |VoW - Vr| / 2
    - VoW: Vector of Will (human intention)
    - Vr: System response vector
    - No: Residual (noise/error margin)
    """
    
    @staticmethod
    def calculate(vow: float, vr: float) -> float:
        """Calculate structural residual"""
        return abs(vow - vr) / 2.0


# ============================================================================
# GOKS - GENERATIVE ORGANIZATIONAL KNOWLEDGE SYSTEM
# ============================================================================
class GOKS:
    """
    Epigenetic memory system using acetylation/methylation principles.
    Stores interactions as "Rujum" (stone markers) in a spiral memory structure.
    """
    
    def __init__(self):
        self.memory_graph: Dict[str, Dict] = {}
        self.rujum_count = 0
    
    def commit_rujum(self, identity: str, distance: int, residual: float, 
                     coherence: CoherenceVector) -> str:
        """
        Commit an interaction as a permanent "stone marker" (Rujum).
        Uses event sourcing for immutability.
        """
        rujum_id = f"RUJUM-{self.rujum_count:06d}"
        self.memory_graph[rujum_id] = {
            "identity": identity,
            "distance": distance,
            "residual": residual,
            "coherence_magnitude": coherence.magnitude(),
            "emotional_alignment": coherence.emotional_stability,
            "status": "Resonant" if coherence.is_resonant() else "Noisy"
        }
        self.rujum_count += 1
        return rujum_id
    
    def apply_methylation(self, rujum_id: str) -> None:
        """Silence (methylate) a Rujum if its coherence is too low"""
        if rujum_id in self.memory_graph:
            if self.memory_graph[rujum_id]["emotional_alignment"] < 0.8:
                self.memory_graph[rujum_id]["methylated"] = True
    
    def apply_acetylation(self, rujum_id: str) -> None:
        """Activate (acetylate) a Rujum for high-coherence memories"""
        if rujum_id in self.memory_graph:
            if self.memory_graph[rujum_id]["emotional_alignment"] >= 0.8:
                self.memory_graph[rujum_id]["acetylated"] = True


# ============================================================================
# HFBT GEOMETRIC ENGINE (The Main Tokenizer)
# ============================================================================
class HFBTGeometricEngine:
    """
    Core Hebrew tokenization engine using geometric semantic navigation.
    
    The "Nitzan Axis" (fourth axis) represents human intention and agency.
    """
    
    def __init__(self):
        self.encoder = HBE27Encoder()
        self.identity_registry = IdentityRegistry()
        self.goks = GOKS()
        self.current_coherence = CoherenceVector()
    
    def tokenize(self, word: str, vow_distance: int = 0, 
                 htqi: float = 0.96, eas: float = 0.85, 
                 ipi: float = 0.90) -> TokenMetadata:
        """
        Main tokenization method with full semantic tracking.
        
        Args:
            word: Hebrew word to tokenize
            vow_distance: Distance in Dunbar circles (0-1500+)
            htqi: Hebrew Text Quality Index
            eas: Emotional Alignment Stability
            ipi: Intent Precision Index
        
        Returns:
            TokenMetadata with full resolution and coherence info
        """
        clean = word.strip()
        
        # 1. Calculate Vector of Will
        vow = VoWGate.evaluate(htqi, eas, ipi)
        gate_passes = VoWGate.passes_gate(vow)
        
        # 2. Attempt identity resolution (handles ambiguous names)
        identity_data = self.identity_registry.resolve(clean, vow_distance)
        
        if identity_data:
            # High-confidence identity found
            full_name = identity_data["full_name"]
            hbe_id = self.encoder.encode(full_name)
            residual = ResidualCalculator.calculate(vow, vow_distance / 1500.0)
            circle = identity_data["circle"]
            status = "Resonant (Identity Resolved)"
        else:
            # Generic tokenization
            hbe_id = self.encoder.encode(clean)
            residual = 0.0
            circle = DunbarCircles.get_label(vow_distance)
            status = "Noisy Input" if not gate_passes else "Valid Token"
            full_name = clean
        
        # 3. Update coherence vector
        self.current_coherence = CoherenceVector(
            clarity=htqi,
            emotional_stability=eas,
            narrative_continuity=1.0 - residual,
            intent_precision=ipi
        )
        
        # 4. Commit to GOKS memory
        if gate_passes:
            rujum_id = self.goks.commit_rujum(full_name, vow_distance, residual, 
                                               self.current_coherence)
            if self.current_coherence.emotional_stability < 0.8:
                self.goks.apply_methylation(rujum_id)
        
        return TokenMetadata(
            identity=full_name,
            hbe_id=hbe_id,
            residual_no=residual,
            circle=circle,
            status=status,
            vector=[vow, htqi, eas, ipi]
        )
    
    def get_coherence_report(self) -> Dict:
        """Return current coherence state"""
        return {
            "magnitude": self.current_coherence.magnitude(),
            "clarity": self.current_coherence.clarity,
            "emotional_stability": self.current_coherence.emotional_stability,
            "narrative_continuity": self.current_coherence.narrative_continuity,
            "intent_precision": self.current_coherence.intent_precision,
            "is_resonant": self.current_coherence.is_resonant()
        }
    
    def get_memory_stats(self) -> Dict:
        """Return GOKS memory statistics"""
        total_rujum = len(self.goks.memory_graph)
        resonant = sum(1 for r in self.goks.memory_graph.values() 
                      if r.get("status") == "Resonant")
        methylated = sum(1 for r in self.goks.memory_graph.values() 
                        if r.get("methylated", False))
        
        return {
            "total_rujum": total_rujum,
            "resonant": resonant,
            "methylated": methylated,
            "utilization": (resonant / max(total_rujum, 1)) * 100
        }


# ============================================================================
# MAIN USAGE EXAMPLE
# ============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("HFBT v5.0 - Nitzan Axis Protocol")
    print("Hebrew Factor-Based Tokenization System")
    print("=" * 70)
    
    engine = HFBTGeometricEngine()
    
    # Test 1: Singular core (מורן as the one)
    print("\n[TEST 1] Singular Core - מורן (VoW distance = 0)")
    result1 = engine.tokenize("מורן", vow_distance=0, htqi=0.98, eas=0.92, ipi=0.95)
    print(f"  Identity: {result1.identity}")
    print(f"  HBE ID: {result1.hbe_id}")
    print(f"  Circle: {result1.circle}")
    print(f"  Residual: {result1.residual_no:.4f}")
    print(f"  Status: {result1.status}")
    print(f"  Vector: {result1.vector}")
    print(f"  Coherence: {engine.get_coherence_report()}")
    
    # Test 2: Social branch (מורן טייסת at Dunbar limit)
    print("\n[TEST 2] Social Branch - מורן (VoW distance = 150)")
    result2 = engine.tokenize("מורן", vow_distance=150, htqi=0.88, eas=0.85, ipi=0.90)
    print(f"  Identity: {result2.identity}")
    print(f"  HBE ID: {result2.hbe_id}")
    print(f"  Circle: {result2.circle}")
    print(f"  Residual: {result2.residual_no:.4f}")
    print(f"  Status: {result2.status}")
    print(f"  Vector: {result2.vector}")
    
    # Test 3: Generic word
    print("\n[TEST 3] Generic Word - דברים")
    result3 = engine.tokenize("דברים", vow_distance=45, htqi=0.94, eas=0.88, ipi=0.92)
    print(f"  Identity: {result3.identity}")
    print(f"  HBE ID: {result3.hbe_id}")
    print(f"  Circle: {result3.circle}")
    print(f"  Residual: {result3.residual_no:.4f}")
    print(f"  Status: {result3.status}")
    
    # Memory report
    print("\n[MEMORY REPORT]")
    memory = engine.get_memory_stats()
    print(f"  Total Rujum: {memory['total_rujum']}")
    print(f"  Resonant: {memory['resonant']}")
    print(f"  Methylated: {memory['methylated']}")
    print(f"  Utilization: {memory['utilization']:.1f}%")
    
    print("\n" + "=" * 70)
