import os
from pathlib import Path

import faiss
import google.generativeai as genai
import numpy as np
import streamlit as st
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# =====================================================
# Load Gemini API Key
# =====================================================

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY not found in .env")
    st.stop()

genai.configure(api_key=API_KEY)

# Use any model available in your account
MODEL_NAME = "models/gemini-2.5-flash"

model = genai.GenerativeModel(MODEL_NAME)

# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="Context Aware RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Context-Aware Chatbot using Gemini + FAISS")

# =====================================================
# Load Documents
# =====================================================

BASE_DIR = Path(__file__).resolve().parent
DOC_PATH = BASE_DIR / "data" / "documents.txt"

if not DOC_PATH.exists():
    st.error(f"documents.txt not found.\nExpected location:\n{DOC_PATH}")
    st.stop()

text = DOC_PATH.read_text(encoding="utf-8")

chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

# =====================================================
# Cache Embedding Model
# =====================================================

@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

embedder = load_embedder()

# =====================================================
# Cache FAISS Index
# =====================================================

@st.cache_resource
def build_index():

    embeddings = embedder.encode(chunks)

    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])

    index.add(embeddings)

    return index

index = build_index()

# =====================================================
# Retrieval
# =====================================================

def retrieve(query, k=3):

    query_embedding = embedder.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, k)

    docs = [chunks[i] for i in indices[0]]

    return docs

# =====================================================
# Chat History
# =====================================================

if "history" not in st.session_state:
    st.session_state.history = []

# =====================================================
# User Input
# =====================================================

question = st.text_input("Ask your question")

col1, col2 = st.columns(2)

send = col1.button("Send")

clear = col2.button("Clear Chat")

if clear:
    st.session_state.history = []
    st.rerun()

# =====================================================
# Generate Answer
# =====================================================

if send:

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    context = "\n".join(retrieve(question))

    history = "\n".join(st.session_state.history[-6:])

    prompt = f"""
You are an intelligent assistant.

Conversation History:
{history}

Knowledge Base:
{context}

Question:
{question}

Instructions:
- Answer from the knowledge base.
- If the answer is unavailable, say:
"I don't know based on the provided documents."
"""

    with st.spinner("Generating response..."):

        try:

            response = model.generate_content(prompt)

            answer = response.text

        except Exception as e:

            st.error(str(e))
            st.stop()

    st.session_state.history.append(f"👤 User: {question}")
    st.session_state.history.append(f"🤖 Assistant: {answer}")

    st.success("Answer")

    st.write(answer)

# =====================================================
# Conversation History
# =====================================================

if st.session_state.history:

    st.markdown("---")

    st.subheader("Conversation")

    for chat in st.session_state.history:
        st.write(chat)