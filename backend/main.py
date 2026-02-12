from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze(request: PromptRequest):
    return {
        "analysis": f"You sent: {request.text}"
    }

@app.get("/")
def root():
    return {"message": "Backend is running"}
