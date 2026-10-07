import chromadb

from sentence_transformers import SentenceTransformer
from chunk_documents import chunks


# ==========================================
# 1. Load Embedding Model
# ==========================================

print("Loading embedding model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded!")


# ==========================================
# 2. Prepare Texts
# ==========================================

texts = [
    chunk["content"]
    for chunk in chunks
]

print("Creating embeddings...")

embeddings = model.encode(
    texts,
    normalize_embeddings=True
)

print(f"Created {len(embeddings)} embeddings")


# ==========================================
# 3. Create Chroma Database
# ==========================================

print("Creating Chroma database...")

client = chromadb.PersistentClient(
    path="./chroma_db_fast"
)

collection = client.get_or_create_collection(
    name="cloudealam_knowledge"
)


# ==========================================
# 4. Prepare IDs and Metadata
# ==========================================

ids = [
    f"{chunk['source']}-{chunk['chunk_id']}"
    for chunk in chunks
]

metadatas = [
    {
        "source": chunk["source"],
        "chunk_id": chunk["chunk_id"]
    }
    for chunk in chunks
]


# ==========================================
# 5. Store Data
# ==========================================

collection.upsert(
    ids=ids,
    documents=texts,
    embeddings=embeddings.tolist(),
    metadatas=metadatas
)


print()
print("Data stored in Chroma!")
print("Number of records:", collection.count())