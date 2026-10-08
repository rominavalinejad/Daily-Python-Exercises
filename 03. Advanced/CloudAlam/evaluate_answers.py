import re
import requests
import chromadb
from sentence_transformers import SentenceTransformer


DB_PATH = "./chroma_db_fast"
COLLECTION_NAME = "cloudealam_knowledge"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"

TOP_K = 3


TEST_CASES = [
    {
        "id": "Q01",
        "question": "How much does the VPS Basic plan cost?",
        "expected_source": "products/vps.md",
        "required_facts": ["€8", "month"],
    },
    {
        "id": "Q02",
        "question": "What are the specifications of VPS Basic?",
        "expected_source": "products/vps.md",
        "required_facts": ["2 vCPU", "4GB RAM", "80GB NVMe", "2TB"],
    },
    {
        "id": "Q03",
        "question": "How much does VPS Pro cost?",
        "expected_source": "products/vps.md",
        "required_facts": ["€16", "month"],
    },
    {
        "id": "Q04",
        "question": "How often are VPS automated backups performed?",
        "expected_source": "policies/backup.md",
        "required_facts": ["6 hours"],
    },
    {
        "id": "Q05",
        "question": "How many daily backup points are kept for VPS?",
        "expected_source": "policies/backup.md",
        "required_facts": ["7 daily"],
    },
    {
        "id": "Q06",
        "question": "What database services does CloudeAlam provide?",
        "expected_source": "products/database.md",
        "required_facts": ["PostgreSQL", "MySQL", "Redis"],
    },
    {
        "id": "Q07",
        "question": "How much does the Managed Database Starter plan cost?",
        "expected_source": "products/database.md",
        "required_facts": ["€18"],
    },
    {
        "id": "Q08",
        "question": "Which databases are supported?",
        "expected_source": "products/database.md",
        "required_facts": ["PostgreSQL", "MySQL", "Redis"],
    },
    {
        "id": "Q09",
        "question": "Is CloudeAlam Object Storage S3 compatible?",
        "expected_source": "products/object-storage.md",
        "required_facts": ["S3"],
    },
    {
        "id": "Q10",
        "question": "How much does Standard Object Storage cost per GB per month?",
        "expected_source": "products/object-storage.md",
        "required_facts": ["€0.02", "GB", "month"],
    },
    {
        "id": "Q11",
        "question": "Which zones are available for Kubernetes?",
        "expected_source": "products/kubernetes.md",
        "required_facts": ["Frankfurt", "zone 1", "zone 2"],
    },
    {
        "id": "Q12",
        "question": "Does CloudeAlam provide 24/7 support?",
        "expected_source": "support/support.md",
        "required_facts": ["24/7"],
    },
    {
        "id": "Q13",
        "question": "What is the target response time for critical support issues?",
        "expected_source": "support/support.md",
        "required_facts": ["2 hours"],
    },
    {
        "id": "Q14",
        "question": "What is the SLA target for standard VPS?",
        "expected_source": "policies/sla.md",
        "required_facts": ["99.9%"],
    },
    {
        "id": "Q15",
        "question": "What is CloudeAlam?",
        "expected_source": "company/about.md",
        "required_facts": ["cloud", "infrastructure"],
    },
]


def normalize_source(source):
    return str(source).replace("\\", "/").strip().lower()


def normalize_text(text):
    return re.sub(r"\s+", " ", text.lower()).strip()


def fact_present(answer, fact):
    answer = normalize_text(answer)
    fact = normalize_text(fact)

    if fact in answer:
        return True

    # tolerate formatting differences such as:
    # "2 vCPU" vs "2-vCPU"
    compact_answer = re.sub(r"[\s\-_/]+", "", answer)
    compact_fact = re.sub(r"[\s\-_/]+", "", fact)

    return compact_fact in compact_answer


print("Loading embedding model...")

model = SentenceTransformer(EMBEDDING_MODEL)

print("Loading Chroma...")

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection(
    name=COLLECTION_NAME
)


def ask_llama(question, context):

    prompt = f"""
You are the CloudeAlam support assistant.

Answer the user's question using ONLY the provided context.

Do not invent information.

If the context does not contain the answer,
say that the information is not available.

Context:

{context}

Question:

{question}

Answer:
""".strip()

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "10m",
            "options": {
                "temperature": 0.2,
                "num_predict": 256,
            },
        },
        timeout=120,
    )

    response.raise_for_status()

    return response.json()["response"].strip()


def evaluate_case(case):

    question = case["question"]

    query_embedding = model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    expected_source = normalize_source(
        case["expected_source"]
    )

    retrieved_sources = [
        normalize_source(
            metadata.get("source", "")
        )
        for metadata in metadatas
    ]

    retrieval_rank = None

    for index, source in enumerate(
        retrieved_sources,
        start=1
    ):
        if source == expected_source:
            retrieval_rank = index
            break

    context_parts = []

    for document, metadata in zip(
        documents,
        metadatas
    ):
        source = metadata.get(
            "source",
            "unknown"
        )

        context_parts.append(
            f"Source: {source}\n{document}"
        )

    context = "\n\n---\n\n".join(
        context_parts
    )

    answer = ask_llama(
        question,
        context
    )

    passed_facts = [
        fact
        for fact in case["required_facts"]
        if fact_present(answer, fact)
    ]

    missing_facts = [
        fact
        for fact in case["required_facts"]
        if not fact_present(answer, fact)
    ]

    answer_pass = len(missing_facts) == 0

    return {
        "id": case["id"],
        "question": question,
        "retrieval_rank": retrieval_rank,
        "best_distance": distances[0],
        "answer": answer,
        "answer_pass": answer_pass,
        "passed_facts": passed_facts,
        "missing_facts": missing_facts,
    }


print()
print("=" * 70)
print("LLM ANSWER EVALUATION")
print("=" * 70)

results = []

for case in TEST_CASES:

    print()
    print(f"Running {case['id']}...")

    result = evaluate_case(case)

    results.append(result)

    status = (
        "PASS"
        if result["answer_pass"]
        else "FAIL"
    )

    print(
        f"{result['id']} | {status} | "
        f"retrieval_rank={result['retrieval_rank']} | "
        f"distance={result['best_distance']:.3f}"
    )

    print(
        f"Question: {result['question']}"
    )

    print(
        f"Answer: {result['answer']}"
    )

    if result["missing_facts"]:

        print(
            "Missing facts:",
            ", ".join(
                result["missing_facts"]
            )
        )


answer_pass_rate = (
    sum(
        result["answer_pass"]
        for result in results
    )
    / len(results)
    * 100
)

retrieval_success = sum(
    result["retrieval_rank"] is not None
    for result in results
)


print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

print(
    f"Retrieval success: "
    f"{retrieval_success}/{len(results)}"
)

print(
    f"Answer Pass Rate: "
    f"{answer_pass_rate:.2f}%"
)

print()
print("Interpretation:")
print(
    "- Retrieval evaluation = did we find the right document?"
)
print(
    "- Answer evaluation = did the LLM include the required facts?"
)
print(
    "- High retrieval + low answer score usually means "
    "the problem is in generation/prompt/model quality."
)