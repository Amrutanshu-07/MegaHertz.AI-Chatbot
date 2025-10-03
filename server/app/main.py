from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.ai import get_gemini_response

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    response_text = await get_gemini_response(request.message)
    return ChatResponse(response=response_text)
