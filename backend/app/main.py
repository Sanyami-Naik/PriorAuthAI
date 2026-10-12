
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="PriorAuthAI",
    description="Agentic Healthcare Prior Authorization Platform",
    version="1.0.0"
)


class AuthorizationRequest(BaseModel):
    patient_id: str
    patient_name: str
    procedure: str
    diagnosis: str
    insurance_active: bool
    documents: list[str] = Field(default_factory=list)


@app.get("/")
def home():
    return {
        "message": "Welcome to PriorAuthAI",
        "status": "running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "PriorAuthAI Backend"
    }


@app.post("/api/authorization")
def create_authorization(request: AuthorizationRequest):
    return {
        "patient": request.patient_name,
        "procedure": request.procedure,
        "status": "RECEIVED",
        "message": "Request received for evaluation"
    }
