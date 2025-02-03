from fastapi import FastAPI
from models import ResumeRequest
from services import generate_resume_with_retry

app = FastAPI()

@app.post("/generate-resume/")
async def generate_resume(request: ResumeRequest):
    response = generate_resume_with_retry(request.dict())
    return {"resume": response}


