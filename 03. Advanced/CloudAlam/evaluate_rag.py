import chromadb
from sentence_transformers import SentenceTransformer

CHROMA_PATH = "./chroma_db_fast"
COLLECTION_NAME = "cloudealam_knowledge"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3


TEST_CASES = [
    ("Q01", "How much does the VPS Basic plan cost?", ["products/vps.md"]),
    ("Q02", "What are the specifications of VPS Basic?", ["products/vps.md"]),
    ("Q03", "How much does VPS Pro cost?", ["products/vps.md"]),
    ("Q04", "How often are VPS automated backups performed?", ["policies/backup.md"]),
    ("Q05", "How many daily backup points are kept for VPS?", ["policies/backup.md"]),
    ("Q06", "What database services does CloudeAlam provide?", ["products/database.md"]),
    ("Q07", "How much does the Managed Database Starter plan cost?", ["products/database.md"]),
    ("Q08", "Which databases are supported?", ["products/database.md"]),
    ("Q09", "Is CloudeAlam Object Storage S3 compatible?", ["products/object-storage.md"]),
    ("Q10", "How much does Standard Object Storage cost per GB per month?", ["products/object-storage.md"]),
    ("Q11", "Which zones are available for Kubernetes?", ["products/kubernetes.md"]),
    ("Q12", "Does CloudeAlam provide 24/7 support?", ["support/support.md"]),
    ("Q13", "What is the target response time for critical support issues?", ["support/support.md"]),
    ("Q14", "What is the SLA target for standard VPS?", ["policies/sla.md"]),
    ("Q15", "What is CloudeAlam?", ["company/about.md"]),
]


def normalize_source(source):
    """Normalize Windows/Linux path separators before comparison."""
    return str(source).replace("\\", "/").strip().lower()


print("Loading embedding model...")
model = SentenceTransformer(MODEL_NAME)

print("Connecting to Chroma...")
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(name=COLLECTION_NAME)

print(f"Collection: {COLLECTION_NAME}")
print(f"Records: {collection.count()}")
print(f"Test cases: {len(TEST_CASES)}")
print("=" * 70)

results = []

for case_id, question, expected_sources in TEST_CASES:
    expected_sources = {
        normalize_source(source)
        for source in expected_sources
    }

    embedding = model.encode([question], normalize_embeddings=True)

    retrieved = collection.query(
        query_embeddings=embedding.tolist(),
        n_results=TOP_K,
    )

    metadatas = retrieved["metadatas"][0]
    distances = retrieved["distances"][0]

    sources = [
        normalize_source(metadata["source"])
        for metadata in metadatas
    ]

    rank = None

    for i, source in enumerate(sources, start=1):
        if source in expected_sources:
            rank = i
            break

    hit = rank is not None
    rr = 1 / rank if rank else 0

    results.append((hit, rr))

    status = "PASS" if hit else "FAIL"
    rank_text = str(rank) if rank else "-"

    print(
        f"{case_id} | {status:<4} | rank={rank_text:<2} | "
        f"distance={distances[0]:.3f} | {question}"
    )

    if not hit:
        print("     Retrieved:")
        for i, source in enumerate(sources, start=1):
            print(f"       {i}. {source}")

hit_rate = sum(hit for hit, _ in results) / len(results)
mrr = sum(rr for _, rr in results) / len(results)

print()
print("=" * 70)
print("EVALUATION RESULTS")
print("=" * 70)
print(f"Hit Rate@{TOP_K}: {hit_rate:.2%}")
print(f"MRR:             {mrr:.3f}")
print()
print("Hit Rate@3 = percentage of questions with a correct source in top 3.")
print("MRR = rewards correct sources appearing near the top.")
print()
print("Evaluation complete.")
