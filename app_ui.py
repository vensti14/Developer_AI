import os
import streamlit as st
import requests

# Streamlit Page Configuration
st.set_page_config(page_title="CodeCompanion 💡", page_icon="🤖", layout="wide")
st.title("💬 CodeCompanion – AI Code Assistant")

# Load API URL from environment/secrets or fallback to Render
API_URL = os.getenv("API_URL", "https://codecompanion.onrender.com/chat/")
st.caption(f"🌐 Connected to: {API_URL}")

# Input Section
query = st.text_area("🧠 Ask about any code (file, function, etc.):", height=150)
mode = st.selectbox("Select mode:", ["explain", "optimize", "debug"])

# Action Button
if st.button("⚡ Run"):
    if not query.strip():
        st.warning("Please enter some code or a question before running.")
    else:
        with st.spinner("🧠 Thinking... please wait"):
            try:
                payload = {"query": query, "mode": mode}
                response = requests.post(API_URL, json=payload, timeout=90)

                if response.status_code == 200:
                    answer = response.json().get("answer", "⚠️ No response received.")
                    st.markdown("### 🧩 **Answer:**")
                    st.write(answer)
                else:
                    st.error(f"❌ API returned error: {response.status_code}")
            except Exception as e:
                st.error(f"🚨 Connection error: {e}")
