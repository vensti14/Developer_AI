from fastapi import APIRouter, UploadFile, Form
from app.services.rag import ingest_repo
import shutil, os

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/")
async def ingest(repo_url: str = Form(None), file: UploadFile = None):
    base = "data/uploads"
    os.makedirs(base, exist_ok=True)
    repo_path = ""

    if repo_url:
        repo_path = ingest_repo(repo_url=repo_url)
    elif file:
        filepath = os.path.join(base, file.filename)
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        repo_path = ingest_repo(zip_path=filepath)
    else:
        return {"error": "Provide repo_url or file"}

    return {"message": "Repo indexed", "path": repo_path}
