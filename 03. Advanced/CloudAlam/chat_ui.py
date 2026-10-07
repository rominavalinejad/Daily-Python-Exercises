import streamlit as st
import requests
import re
import difflib


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="CloudeAlam Assistant",
    page_icon="☁️",
    layout="centered"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>
.stApp {
    background: #f8fafc;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 7rem;
}

/* Header */
.header {
    text-align: center;
    padding: 25px 20px 10px;
}

.logo {
    width: 56px;
    height: 56px;
    margin: 0 auto 14px;
    border-radius: 16px;
    background: #111827;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 700;
}

.title {
    font-size: 30px;
    font-weight: 700;
    color: #111827;
}

.subtitle {
    margin-top: 6px;
    font-size: 15px;
    color: #6b7280;
}

/* Welcome */
.welcome {
    text-align: center;
    margin-top: 55px;
    margin-bottom: 30px;
}

.welcome-title {
    font-size: 25px;
    font-weight: 600;
    color: #111827;
    margin-bottom: 10px;
}

.welcome-text {
    font-size: 15px;
    color: #6b7280;
    line-height: 1.6;
}

/* Buttons */
.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    background: white;
    color: #374151;
    font-size: 14px;
}

.stButton > button:hover {
    border-color: #9ca3af;
    background: #f9fafb;
}

/* Chat */
[data-testid="stChatMessage"] {
    border-radius: 14px;
}

/* Sources */
.source-box {
    margin-top: 12px;
    padding: 8px 12px;
    border-left: 3px solid #d1d5db;
    color: #6b7280;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# Load Embedding Model
# IMPORTANT:
# Heavy imports and model loading happen only when RAG is used.
# =========================================================

@st.cache_resource(show_spinner=False)
def load_embedding_model():
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )


# =========================================================
# Load Chroma
# IMPORTANT:
# Chroma is imported and initialized only when RAG is used.
# =========================================================

@st.cache_resource(show_spinner=False)
def load_collection():
    import chromadb

    client = chromadb.PersistentClient(
        path="./chroma_db_fast"
    )

    return client.get_collection(
        name="cloudealam_knowledge"
    )


# =========================================================
# Ollama Request
# =========================================================

def ask_llama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
            "keep_alive": "10m",
            "options": {
                "temperature": 0.3,
                "num_predict": 256
            }
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()["response"].strip()


# =========================================================
# Normalize User Text
# =========================================================

def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


# =========================================================
# Greeting Detection
# =========================================================

def is_greeting(text):
    text = normalize_text(text)

    greetings = [
        "hi",
        "hello",
        "hey",
        "hi there",
        "hello there",
        "hey there",
        "good morning",
        "good afternoon",
        "good evening",
        "how are you",
        "how are you doing"
    ]

    if text in greetings:
        return True

    # Handles things such as:
    # heloooo
    # hellooo
    # hiiii
    # heyyy
    compact = re.sub(r"(.)\1+", r"\1", text)

    fuzzy_greetings = [
        "hi",
        "hello",
        "hey"
    ]

    for greeting in fuzzy_greetings:
        similarity = difflib.SequenceMatcher(
            None,
            compact,
            greeting
        ).ratio()

        if similarity >= 0.65:
            return True

    return False


# =========================================================
# CloudeAlam Knowledge Detection
# =========================================================

def is_cloudealam_question(text):
    text = text.lower()

    keywords = [
        "cloudealam",
        "vps",
        "server",
        "database",
        "postgresql",
        "mysql",
        "redis",
        "object storage",
        "storage",
        "kubernetes",
        "backup",
        "backups",
        "pricing",
        "price",
        "cost",
        "support",
        "sla",
        "refund",
        "availability",
        "zone",
        "frankfurt"
    ]

    return any(
        keyword in text
        for keyword in keywords
    )


# =========================================================
# General Conversation
# =========================================================

def general_question(question):
    prompt = f"""
You are CloudeAlam's AI assistant.

The user asked a general conversational question.

Answer naturally, briefly, and helpfully.
If the user is greeting you, respond appropriately.
Do not pretend that general knowledge comes from the CloudeAlam knowledge base.

User:
{question}

Answer:
"""

    return ask_llama(prompt)


# =========================================================
# RAG
# =========================================================

def rag_question(question):
    # These resources are intentionally loaded here, not at startup.
    embedding_model = load_embedding_model()
    collection = load_collection()

    # -------------------------------------
    # Embed question
    # -------------------------------------
    question_embedding = embedding_model.encode(
        [question],
        normalize_embeddings=True
    )

    # -------------------------------------
    # Retrieve
    # -------------------------------------
    results = collection.query(
        query_embeddings=question_embedding.tolist(),
        n_results=3
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    # -------------------------------------
    # Check relevance
    # -------------------------------------
    best_distance = distances[0]

    if best_distance > 0.75:
        return (
            "I don't have enough information in the "
            "CloudeAlam knowledge base to answer that.",
            []
        )

    # -------------------------------------
    # Context
    # -------------------------------------
    context = "\n\n".join(documents)

    # -------------------------------------
    # Prompt
    # -------------------------------------
    prompt = f"""
You are CloudeAlam's customer support assistant.

Answer the user's question using ONLY the information
provided in the context.

Do not invent company-specific information.
Give a concise and direct answer.

Context:
{context}

User question:
{question}

Answer:
"""

    # -------------------------------------
    # Llama
    # -------------------------------------
    answer = ask_llama(prompt)

    # -------------------------------------
    # Sources
    # -------------------------------------
    sources = []

    for metadata in metadatas:
        source = metadata["source"]

        if source not in sources:
            sources.append(source)

    return answer, sources


# =========================================================
# Main Question Router
# =========================================================

def process_question(question):
    # -------------------------------------
    # Greeting
    # -------------------------------------
    if is_greeting(question):
        answer = general_question(question)
        return answer, []

    # -------------------------------------
    # CloudeAlam / Knowledge Base Question
    # -------------------------------------
    if is_cloudealam_question(question):
        return rag_question(question)

    # -------------------------------------
    # General Question
    # -------------------------------------
    answer = general_question(question)
    return answer, []


# =========================================================
# Session State
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# Header
# =========================================================

st.markdown(
    '<div class="header">'
    '<div class="logo">C</div>'
    '<div class="title">CloudeAlam Assistant</div>'
    '<div class="subtitle">'
    'AI-powered assistant for CloudeAlam services'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# Welcome Screen
# =========================================================

if not st.session_state.messages:
    st.markdown(
        '<div class="welcome">'
        '<div class="welcome-title">How can I help?</div>'
        '<div class="welcome-text">'
        'Ask about CloudeAlam services, pricing, '
        'backups, support, or policies.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "VPS pricing",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "How much does a VPS Basic plan cost?"
            )
            st.rerun()

    with col2:
        if st.button(
            "Backup policy",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "How often are VPS backups performed?"
            )
            st.rerun()

    with col3:
        if st.button(
            "Supported databases",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "What database services does CloudeAlam provide?"
            )
            st.rerun()


# =========================================================
# Existing Messages
# =========================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and message.get("sources")
        ):
            st.markdown(
                '<div class="source-box">'
                'Source: '
                + ", ".join(message["sources"])
                + '</div>',
                unsafe_allow_html=True
            )


# =========================================================
# User Input
# =========================================================

question = st.chat_input(
    "Ask about CloudeAlam..."
)


# =========================================================
# Suggested Question
# =========================================================

if "pending_question" in st.session_state:
    question = st.session_state.pending_question
    del st.session_state.pending_question


# =========================================================
# Process
# =========================================================

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer, sources = process_question(question)
                st.markdown(answer)

                if sources:
                    st.markdown(
                        '<div class="source-box">'
                        'Source: '
                        + ", ".join(sources)
                        + '</div>',
                        unsafe_allow_html=True
                    )

            except Exception as error:
                answer = (
                    "I couldn't process your request. "
                    "Please make sure Ollama is running."
                )
                sources = []
                st.error(answer)
                print(error)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources
    })
