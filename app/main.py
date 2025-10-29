from fastapi import FastAPI
from app.routers import chat, ingest

app = FastAPI(title="CodeCompanion API")
app.include_router(chat.router)
app.include_router(ingest.router)

@app.get("/health")
def health():
    return {"status": "ok"}
