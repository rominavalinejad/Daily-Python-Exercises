from sentence_transformers import SentenceTransformer
from chunk_documents import chunks


# ==========================================
# 1. Check Chunks
# ==========================================

print(f"Received {len(chunks)} chunks from chunk_documents.py")


# ==========================================
# 2. Load Embedding Model
# ==========================================

print("Loading embedding model...")

model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)

print("Model loaded!")


# ==========================================
# 3. Create Embeddings
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


# ==========================================
# 4. Show Results
# ==========================================

print()
print("Embedding completed!")

print("Number of embeddings:", len(embeddings))

print("Vector size:", len(embeddings[0]))

print()

print("First chunk:")
print(chunks[0]["content"])

print()

print("First vector preview:")
print(embeddings[0][:10])