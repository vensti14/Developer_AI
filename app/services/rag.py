import os, glob, faiss
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

from git import Repo
import tempfile, zipfile

def ingest_repo(repo_url=None, zip_path=None):
    if repo_url:
        tmp = tempfile.mkdtemp()
        Repo.clone_from(repo_url, tmp)
        folder = tmp
    else:
        tmp = tempfile.mkdtemp()
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(tmp)
        folder = tmp

    # collect .py files
    files = [f for f in glob.glob(f"{folder}/**/*.py", recursive=True)]
    docs = []
    for fp in files:
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        docs.append(Document(page_content=text, metadata={"source": fp}))

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")  # or your local embedding model
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("data/indexes/current_index")
    return folder

def retrieve(query: str, k: int = 5):
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    vectorstore = FAISS.load_local("data/indexes/current_index", embeddings,allow_dangerous_deserialization=True)
    docs = vectorstore.similarity_search(query, k=k)
    return docs
