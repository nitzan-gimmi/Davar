# GHC Core Package
# Hebrew Factor-Based Tokenization & Goal-Oriented Knowledge System

# Guarded imports to avoid import-time errors when modules are not yet present.
try:
    from .hfbt_core import HFBTTokenizer
    from .hic_core_logic import IntentCore
    from .pfc_pipeline import PFCPipeline
except Exception:
    # Modules not present yet — keep package importable for documentation/tests.
    HFBTTokenizer = None
    IntentCore = None
    PFCPipeline = None

__version__ = "1.0.1"
