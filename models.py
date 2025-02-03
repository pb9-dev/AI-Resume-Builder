from pydantic import BaseModel

class ResumeRequest(BaseModel):
    name: str
    title: str
    email: str
    summary: str