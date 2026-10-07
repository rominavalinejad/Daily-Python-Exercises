import chromadb

from sentence_transformers import SentenceTransformer


# ==========================================
# 1. Load Embedding Model
# ==========================================

print("Loading embedding model...")

model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)

print("Model loaded!")


# ==========================================
# 2. Connect to Chroma
# ==========================================

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="cloudealam_knowledge"
)


print("Chroma collection loaded!")
print("Number of records:", collection.count())


# ==========================================
# 3. User Question
# ==========================================

question = "How often are VPS backups performed?"


# ==========================================
# 4. Convert Question to Vector
# ==========================================

question_embedding = model.encode(
    [question],
    normalize_embeddings=True
)


# ==========================================
# 5. Search Chroma
# ==========================================

results = collection.query(
    query_embeddings=question_embedding.tolist(),
    n_results=3
)


# ==========================================
# 6. Show Results
# ==========================================

print()
print("Question:")
print(question)

print()

for i in range(len(results["documents"][0])):

    print("=" * 70)

    print("RESULT:", i + 1)

    print()

    print("SOURCE:")
    print(results["metadatas"][0][i]["source"])

    print()

    print("TEXT:")
    print(results["documents"][0][i])

    print()

    print("DISTANCE:")
    print(results["distances"][0][i])