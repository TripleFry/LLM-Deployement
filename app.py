from __future__ import annotations

from threading import Lock
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline

MODEL_NAME = "google/flan-t5-small"
MAX_NEW_TOKENS = 50

app = FastAPI(
    title="LLM Deployment API",
    version="1.0.0",
    description="A simple FastAPI service for text generation using a pre-trained LLM.",
)


class PromptRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Text prompt to send to the model")


class GenerationResponse(BaseModel):
    response: str
    model: str


_generator: Any | None = None
_generator_lock = Lock()


def get_generator() -> Any:
    global _generator
    if _generator is None:
        with _generator_lock:
            if _generator is None:
                _generator = pipeline("text2text-generation", model=MODEL_NAME)
    return _generator


@app.on_event("startup")
def load_model_on_startup() -> None:
    get_generator()


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "LLM API is running", "model": MODEL_NAME}


@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "model": MODEL_NAME, "model_loaded": _generator is not None}


@app.post("/generate", response_model=GenerationResponse)
def generate(request: PromptRequest) -> GenerationResponse:
    try:
        generator = get_generator()
        result = generator(request.prompt, max_new_tokens=MAX_NEW_TOKENS)
        generated_text = result[0]["generated_text"].strip()
        return GenerationResponse(response=generated_text, model=MODEL_NAME)
    except Exception as exc:  # pragma: no cover - surfaced in API response
        raise HTTPException(status_code=500, detail=f"Generation failed: {exc}") from exc


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
