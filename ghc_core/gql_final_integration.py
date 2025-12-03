import os
from typing import List, Optional, Dict, Any
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from neo4j import GraphDatabase, Driver
from datetime import datetime

# --- 1. הגדרות חיבור ל-Neo4j (מותאם ל-Termux/Edge) ---
# ברירת מחדל: עבודה מול localhost. אם אין שרת, ה-DAO יטפל בזה.
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://127.0.0.1:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
NEO4J_DB = os.getenv("NEO4J_DB", "ghc_kg")

# --- 2. שכבת ה-DAO (Data Access Object) ---
class Neo4jDAO:
    def __init__(self, uri: str, user: str, password: str, database: str):
        try:
            self.driver: Driver = GraphDatabase.driver(uri, auth=(user, password))
            self.database = database
            print(f"✅ Connection established to Neo4j at {uri}")
        except Exception as e:
            # במצב Offline או שגיאה, המערכת לא תקרוס אלא תודיע
            print(f"⚠️ Warning: Could not connect to Neo4j: {e}")
            self.driver = None
    
    def close(self):
        if self.driver:
            self.driver.close()

    def roll_up_trust_for_root(self, root_text: str) -> Dict[str, Any]:
        """ MUTATION: Roll-Up Trust Calculation - עדכון אמון מלמטה למעלה (ציר י-ע-ל) """
        if not self.driver: 
            return {"root": root_text, "avg_score": 0.0, "max_score": 0.0, "updated_at": "Offline Mode"}
        
        q = """
        MATCH (r:Root {text: $root_text})<-[:DERIVES_FROM]-(l:Lexeme)
        OPTIONAL MATCH (l)-[:INTEGRITY_AT]->(snap:IntegritySnapshot)
        WITH r, avg(coalesce(snap.score, 0.0)) AS avg_score, max(coalesce(snap.score, 0.0)) AS max_score
        SET r.trust_rollup_avg = avg_score, r.trust_rollup_max = max_score, r.trust_updated_at = datetime()
        RETURN r.text AS root, r.trust_rollup_avg AS avg_score, r.trust_rollup_max AS max_score, r.trust_updated_at AS updated_at
        """
        try:
            with self.driver.session(database=self.database) as session:
                res = session.execute_write(lambda tx: tx.run(q, root_text=root_text).data())
            return res[0] if res else {"root": root_text, "avg_score": 0.0, "max_score": 0.0, "updated_at": datetime.now().isoformat()}
        except Exception as e:
            print(f"Error in rollup: {e}")
            return {"root": root_text, "avg_score": 0.0, "max_score": 0.0, "updated_at": "Error"}

    def check_axiomatic_violation(self) -> List[Dict[str, Any]]:
        """ QUERY: AEM Check - בדיקת הפרות מבניות (ציר ד-י-ק) """
        if not self.driver: return []
        
        q = """
        MATCH (u:User {user_id: 'GHC_TARGET_USER'})
        MATCH (l_bad:Lexeme)-[:INTEGRITY_AT]->(snap:IntegritySnapshot)
        WHERE snap.state = 'QUARANTINE' AND snap.rationale CONTAINS 'Gender'
        RETURN l_bad.text AS violating_lexeme, snap.state AS violation_status, 
               u.gender AS canonical_gender, u.preferred_pronoun AS canonical_pronoun
        LIMIT 10
        """
        try:
            with self.driver.session(database=self.database) as session:
                res = session.execute_read(lambda tx: tx.run(q).data())
            return res
        except Exception as e:
            print(f"Error in AEM check: {e}")
            return []

# --- אתחול ה-DAO ---
DAO = Neo4jDAO(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DB)

# --- 3. הגדרות GraphQL ---
@strawberry.type
class TrustRollup:
    root: str
    avg_score: float
    max_score: float
    updated_at: str

@strawberry.type
class AxiomViolation:
    violating_lexeme: Optional[str]
    violation_status: Optional[str]
    canonical_gender: str
    canonical_pronoun: str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def rollup_root_trust(self, root_text: str) -> Optional[TrustRollup]:
        return DAO.roll_up_trust_for_root(root_text)

@strawberry.type
class Query:
    @strawberry.field
    def check_axiomatic_violation(self) -> List[AxiomViolation]:
        return [AxiomViolation(**r) for r in DAO.check_axiomatic_violation()]

schema = strawberry.Schema(query=Query, mutation=Mutation)

# --- 4. הגדרת FastAPI ---
app = FastAPI(title="GHC KGBR API - Rujum Edition")
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.on_event("shutdown")
def shutdown_event():
    DAO.close()