from pathlib import Path
import re


# ==========================================
# 1. Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_BASE = BASE_DIR / "Docs" / "knowledge_base"


# ==========================================
# 2. Load Documents
# ==========================================

documents = []

for file_path in KNOWLEDGE_BASE.rglob("*.md"):
    content = file_path.read_text(encoding="utf-8")

    source = file_path.relative_to(KNOWLEDGE_BASE)

    documents.append({
        "content": content,
        "source": str(source)
    })


print(f"Loaded {len(documents)} documents")


# ==========================================
# 3. Split Markdown into Sections
# ==========================================

def split_into_sections(text):
    """
    Split Markdown document based on headings.

    Example:

    ## VPS Plans
    ...
    ## Backups
    ...

    becomes separate sections.
    """

    lines = text.splitlines()

    sections = []
    current_section = []

    for line in lines:

        # Markdown heading
        if re.match(r"^#{1,6}\s+", line):

            # Save previous section
            if current_section:
                sections.append("\n".join(current_section).strip())

            current_section = [line]

        else:
            current_section.append(line)

    # Save last section
    if current_section:
        sections.append("\n".join(current_section).strip())

    return [section for section in sections if section]


# ==========================================
# 4. Split Large Sections
# ==========================================

def split_large_section(section, chunk_size=700, overlap=100):
    """
    Split a large section while trying to preserve
    paragraphs and sentences.
    """

    if len(section) <= chunk_size:
        return [section]

    paragraphs = re.split(r"\n\s*\n", section)

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if not paragraph:
            continue

        # If adding this paragraph keeps us below the limit
        if len(current_chunk) + len(paragraph) + 2 <= chunk_size:

            if current_chunk:
                current_chunk += "\n\n"

            current_chunk += paragraph

        else:

            if current_chunk:
                chunks.append(current_chunk)

            # Very large paragraph
            if len(paragraph) > chunk_size:

                sentences = re.split(
                    r"(?<=[.!?])\s+",
                    paragraph
                )

                current_chunk = ""

                for sentence in sentences:

                    if len(current_chunk) + len(sentence) + 1 <= chunk_size:

                        if current_chunk:
                            current_chunk += " "

                        current_chunk += sentence

                    else:

                        if current_chunk:
                            chunks.append(current_chunk)

                        current_chunk = sentence

            else:
                current_chunk = paragraph

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


# ==========================================
# 5. Add Overlap
# ==========================================

def add_overlap(chunks, overlap=100):
    """
    Add a small amount of context from the previous chunk.
    """

    if len(chunks) <= 1:
        return chunks

    result = []

    for i, chunk in enumerate(chunks):

        if i == 0:
            result.append(chunk)
            continue

        previous_chunk = chunks[i - 1]

        overlap_text = previous_chunk[-overlap:]

        # Try to start overlap at a clean word boundary
        first_space = overlap_text.find(" ")

        if first_space != -1:
            overlap_text = overlap_text[first_space + 1:]

        result.append(
            overlap_text + "\n\n" + chunk
        )

    return result


# ==========================================
# 6. Create Chunks
# ==========================================

chunks = []

for document in documents:

    sections = split_into_sections(
        document["content"]
    )

    document_chunks = []

    for section in sections:

        section_chunks = split_large_section(
            section,
            chunk_size=700,
            overlap=100
        )

        document_chunks.extend(section_chunks)

    document_chunks = add_overlap(
        document_chunks,
        overlap=100
    )

    for index, chunk in enumerate(document_chunks):

        chunks.append({
            "content": chunk,
            "source": document["source"],
            "chunk_id": index
        })


# ==========================================
# 7. Results
# ==========================================

print(f"Created {len(chunks)} chunks")


# ==========================================
# 8. Show Chunks
# ==========================================

for chunk in chunks[:10]:

    print("=" * 70)

    print("SOURCE:", chunk["source"])
    print("CHUNK ID:", chunk["chunk_id"])
    print("SIZE:", len(chunk["content"]))

    print()

    print(chunk["content"])