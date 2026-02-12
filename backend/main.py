import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class PromptRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze(request: PromptRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional AI assistant that analyzes text and provides clear insights."
            },
            {
                "role": "user",
                "content": request.text
            }
        ],
    )

    return {
        "analysis": response.choices[0].message.content
    }

@app.get("/")
def root():
    return {"message": "Backend is running"}
