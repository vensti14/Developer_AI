### CodeCompanion – AI Developer Assistant

CodeCompanion is a full-stack AI tool that helps developers **explain**, **debug**, and **optimize** code.  
It combines a FastAPI backend with a Streamlit frontend and uses large language models (LLMs) through **Groq** or **Hugging Face APIs**.  
The app also supports basic RAG (retrieval-augmented generation) to provide context-aware answers from source files.

---

###  Tech Stack
- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **AI Models:** Groq API / Hugging Face Inference  
- **Embeddings:** BAAI/bge-base-en-v1.5  
- **Other Tools:** LangChain, FAISS, Docker  
- **Deployment:** Render (API) + Hugging Face Spaces (UI)

---

###  Features
- Explain complex functions or files in plain English  
- Detect and suggest fixes for code issues  
- Recommend optimizations for speed or clarity  
- Retrieve relevant snippets using FAISS for contextual responses  
- Simple and clean UI with multiple analysis modes

---

###  Quick Start

```bash
git clone https://github.com/vensti14/CodeCompanion.git
cd CodeCompanion
pip install -r requirements.txt
