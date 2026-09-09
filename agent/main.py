import json
import os
from typing import Optional

from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel, Field

from prompt import SYSTEM_PROMPT, build_user_prompt

app = FastAPI(title="Rhapsody Evaluation Agent", version="1.0.0")

class EvaluationRequest(BaseModel):
    matchbook: str = Field(min_length=1)
    transcript: str = Field(min_length=1)
    use_case: str = Field(default="unspecified")
    broker_profile: Optional[str] = None
    competencies: Optional[list[str]] = None

class CompetencyResult(BaseModel):
    competency: str
    score: Optional[float]
    status: str
    confidence: str
    evidence: str
    expected: str
    gap: str
    feedback: str

class EvaluationResult(BaseModel):
    overall_score: Optional[float]
    top_strength: Optional[str]
    top_development_area: Optional[str]
    next_action: Optional[str]
    competencies: list[CompetencyResult]


def get_client() -> OpenAI:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not configured")
    return OpenAI(api_key=key)


@app.get("/health")
def health():
    return {"status": "ok", "service": "rhapsody-evaluator-agent"}


@app.post("/evaluate", response_model=EvaluationResult)
def evaluate(request: EvaluationRequest):
    client = get_client()
    model = os.getenv("OPENAI_MODEL", "gpt-5.6")
    user_prompt = build_user_prompt(
        request.matchbook,
        request.transcript,
        request.use_case,
        request.broker_profile,
        request.competencies,
    )

    try:
        response = client.responses.create(
            model=model,
            instructions=SYSTEM_PROMPT,
            input=user_prompt,
            temperature=0.1,
        )
        raw = response.output_text
        data = json.loads(raw)
        return EvaluationResult.model_validate(data)
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=502, detail=f"Model returned invalid JSON: {exc}")
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Evaluation failed: {exc}")
