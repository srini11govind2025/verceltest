from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks data
with open("students.json", "r") as f:
    students = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    marks = [students.get(n, None) for n in name]
    return {"marks": marks}
