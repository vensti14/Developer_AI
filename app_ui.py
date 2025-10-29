import streamlit as st
import requests

st.set_page_config(page_title="CodeCompanion 💡", page_icon="🤖", layout="wide")
st.title("💬 CodeCompanion – AI Code Assistant")

API_URL = "http://127.0.0.1:8000/chat/"  # 👈 change to your deployed FastAPI URL later

query = st.text_area("🧠 Ask about any code (file, function, etc.):", height=150)
mode = st.selectbox("Select mode:", ["explain", "optimize", "debug"])

if st.button("⚡ Run"):
    with st.spinner("Thinking..."):
        try:
            payload = {"query": query, "mode": mode}
            res = requests.post(API_URL, json=payload)
            answer = res.json().get("answer", "⚠️ No response.")
            st.markdown(f"### 🧩 Answer:\n{answer}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
