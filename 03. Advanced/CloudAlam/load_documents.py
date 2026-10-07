from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_BASE = BASE_DIR / "Docs" / "knowledge_base"

documents = []

for file_path in KNOWLEDGE_BASE.rglob("*.md"):
    content = file_path.read_text(encoding="utf-8")

    documents.append({
        "content": content,
        "source": str(file_path)
    })

print(f"Loaded {len(documents)} documents")

for document in documents:
    print("=" * 50)
    print("SOURCE:", document["source"])
    print(document["content"][:300])