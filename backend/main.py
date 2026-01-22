from fastapi import FastAPI, HTTPException
from backend.models import ChatRequest, ChatResponse
from backend.llm_client import get_chat_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Chatbot API")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    response_text = get_chat_response(request.message)
    return ChatResponse(response=response_text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
