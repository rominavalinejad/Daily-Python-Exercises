import chromadb
import requests

from sentence_transformers import SentenceTransformer


# ==========================================
# 1. Load Embedding Model
# ==========================================

print("Loading embedding model...")

embedding_model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)

print("Embedding model loaded!")


# ==========================================
# 2. Connect to Chroma
# ==========================================

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="cloudealam_knowledge"
)

print("Chroma connected!")
print("Number of records:", collection.count())


# ==========================================
# 3. RAG Function
# ==========================================

def ask_rag(question):

    # --------------------------------------
    # Embed Question
    # --------------------------------------

    question_embedding = embedding_model.encode(
        [question],
        normalize_embeddings=True
    )

    # --------------------------------------
    # Retrieve Relevant Chunks
    # --------------------------------------

    results = collection.query(
        query_embeddings=question_embedding.tolist(),
        n_results=3
    )

    documents = results["documents"][0]

    # --------------------------------------
    # Create Context
    # --------------------------------------

    context = "\n\n".join(documents)

    # --------------------------------------
    # Create Prompt
    # --------------------------------------

    prompt = f"""
You are CloudeAlam's customer support assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context, say:
"I don't have enough information to answer that."

Context:

{context}

User question:

{question}

Answer:
"""

    # --------------------------------------
    # Send Prompt to Llama
    # --------------------------------------

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]


# ==========================================
# 4. Interactive Chat
# ==========================================

print()
print("=" * 70)
print("CloudeAlam RAG Assistant")
print("Type 'exit' to quit.")
print("=" * 70)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = ask_rag(question)

    print("\nCloudeAlam:", answer)