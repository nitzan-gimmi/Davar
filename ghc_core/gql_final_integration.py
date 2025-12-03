from fastapi import FastAPI
from .pfc_pipeline import PFCPipeline
import uvicorn

app = FastAPI(title="GHC Sovereign Node", version="1.0.1")
pipeline = PFCPipeline()

@app.get("/")
def read_root():
    return {"system": "GHC Core", "status": "ONLINE", "msg": "רוג'ום הדוכיפת מבצעי"}

@app.post("/process")
def process_text(text: str):
    result = pipeline.process_request(text)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
