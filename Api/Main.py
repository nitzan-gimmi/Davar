# api/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Davar API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "ברוך הבא ל־Davar API"}

@app.post("/tokenize")
def tokenize(input: TextInput):
    tokens = input.text.split()  # מימוש זמני
    return {"tokens": tokens}

@app.post("/decay")
def decay(input: TextInput):
    decay_score = len(input.text) / 10.0  # דוגמה בלבד
    return {"score": decay_score}
