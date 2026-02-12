from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI, RateLimitError
import os

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
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": request.text}],
        )

        return {
            "analysis": response.choices[0].message.content,
            "source": "openai"
        }

    except RateLimitError:
        # 👇 MOCK automático
        return {
            "analysis": f"(Mocked response) You asked: {request.text}",
            "source": "mock"
        }

    except Exception as e:
        return {
            "analysis": f"Unexpected error: {str(e)}",
            "source": "error"
        }

@app.get("/")
def root():
    return {"message": "Backend is running"}

