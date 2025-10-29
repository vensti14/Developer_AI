from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm import chat_with_rag

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    query: str
    mode: str = "explain"

@router.post("/")
async def chat_endpoint(req: ChatRequest):
    response = chat_with_rag(req.query, req.mode)
    return {"answer": response}
