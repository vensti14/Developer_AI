# app/services/llm.py
import os
from groq import Groq
from app.services.rag import retrieve

# Load environment variables (optional if using .env)
from dotenv import load_dotenv
load_dotenv()

# Get API key and model from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

# Safety check
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY environment variable. Please set it before running the app.")

client = Groq(api_key=GROQ_API_KEY)

def chat_with_rag(query: str, mode: str = "explain") -> str:
    docs = retrieve(query)
    context = "\n\n".join(
        [f"From {d.metadata.get('source','unknown')}:\n{d.page_content[:600]}" for d in docs]
    )

    prompt = (
        f"You are CodeCompanion, a helpful developer assistant.\n"
        f"Task: {mode.upper()}\n\n"
        f"User Query: {query}\n\n"
        f"Relevant Code Context:\n{context}\n\n"
        f"Answer concisely, precisely, and cite file paths if helpful."
    )

    try:
        chat_completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a professional coding assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=600,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Groq API error: {repr(e)}"
