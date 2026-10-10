# CloudAlam — Retrieval-Augmented Generation (RAG) System

A practical, end-to-end **Retrieval-Augmented Generation (RAG)** project built for **CloudAlam**, a fictional cloud infrastructure provider. The system retrieves relevant information from a curated company knowledge base and uses a locally hosted language model to generate context-grounded answers.

The project goes beyond a basic chatbot: it implements a document ingestion workflow, semantic retrieval with vector embeddings, persistent vector storage, local LLM generation, an interactive chat interface, and automated evaluation scripts for retrieval quality and answer completeness.

---

## Project Overview

CloudAlam's knowledge base contains service and policy documentation for products such as VPS hosting, managed databases, object storage, Kubernetes, backups, support, and service-level targets.

The RAG workflow is designed to answer questions using these documents rather than relying only on the language model's parametric knowledge.

### Key Capabilities

- **Document ingestion:** loads company knowledge-base documents written in Markdown.
- **Text preparation and chunking:** splits source documents into smaller passages suitable for retrieval.
- **Semantic embeddings:** represents document chunks and user questions as vectors using `sentence-transformers/all-MiniLM-L6-v2`.
- **Persistent vector database:** stores and retrieves document chunks with ChromaDB.
- **Semantic search:** retrieves the most relevant passages for a user's question.
- **Context-aware generation:** sends the retrieved context to a locally hosted `llama3.2` model through Ollama.
- **Interactive chat UI:** provides a user-facing interface for asking questions about CloudAlam's services.
- **Retrieval evaluation:** measures whether expected source documents appear among the top retrieved results.
- **Answer evaluation:** checks whether generated answers include required facts from a predefined evaluation set.
- **Evaluation-driven development:** uses measurable test results to identify weaknesses and improve the pipeline.

---

## Architecture

```text
                 CloudAlam Markdown Knowledge Base
                              |
                              v
                     Document Ingestion
                              |
                              v
                      Text Chunking
                              |
                              v
                  Sentence Transformer Model
                              |
                              v
                     ChromaDB Collection
                              |
                  User Question (Chat UI)
                              |
                              v
                  Question Embedding/Search
                              |
                              v
                    Top-K Relevant Chunks
                              |
                              v
                 Context + Question Prompt
                              |
                              v
                    Ollama: llama3.2
                              |
                              v
                       Generated Answer
```

The ingestion pipeline prepares and indexes the knowledge base. At question time, the application retrieves relevant chunks and passes them to the local language model as context for answer generation.

---

## Technology Stack

| Technology | Role in the project |
| --- | --- |
| **Python** | Main implementation language and pipeline orchestration |
| **ChromaDB** | Persistent vector storage and similarity search |
| **Sentence Transformers** | Converts document chunks and queries into embeddings |
| **`all-MiniLM-L6-v2`** | Embedding model used for semantic retrieval |
| **Ollama** | Runs the language model locally and exposes its generation API |
| **`llama3.2`** | Generates answers using the retrieved context |
| **Markdown** | Human-readable source format for the knowledge base |

---

## Project Structure

```text
CloudAlam/
├── load_documents.py       # Loads source knowledge-base documents
├── chunk_documents.py     # Splits documents into retrieval-sized chunks
├── embed_documents.py     # Creates embeddings for document chunks
├── chroma_db.py           # Sets up or manages the ChromaDB index
├── search_chroma.py       # Tests semantic retrieval against the vector store
├── rag.py                 # RAG pipeline: retrieve context and generate an answer
├── chat_ui.py              # Interactive chat interface
├── evaluate_rag.py         # Evaluates retrieval quality
├── evaluate_answers.py    # Evaluates required facts in generated answers
├── chroma_db_fast/         # Persisted ChromaDB data (generated locally)
└── README.md
```

The knowledge-base Markdown files are the source of truth for the fictional company's service information. The ChromaDB directory is generated data and may need to be recreated if it is not included in a checkout.

---

## Knowledge Base

The current dataset consists of **10 Markdown documents and 82 indexed chunks**. It covers key CloudAlam service details, including:

| Area | Example information represented in the knowledge base |
| --- | --- |
| VPS hosting | Basic, Pro, and Business plans, resource allocations, and pricing |
| Backups | Optional VPS backups, six-hour intervals when enabled, and seven daily recovery points |
| Managed databases | PostgreSQL, MySQL, and Redis offerings with Starter, Standard, and Pro tiers |
| Object storage | S3-compatible storage and Standard / Infrequent pricing |
| Kubernetes | Frankfurt deployment across Zones 1 and 2 |
| Customer support | 24/7 support and target first-response times by severity |
| Service availability | Standard VPS target SLA of 99.9% |

These details are fictional project data and are used to demonstrate how a RAG system can retrieve information from structured company documentation.

---

## How the RAG Pipeline Works

### 1. Ingest source documents

The Markdown knowledge-base documents are loaded into the application so their content can be processed consistently.

### 2. Split documents into chunks

Long documents are divided into smaller text segments. Chunking allows the retriever to return focused passages instead of supplying entire documents for every question.

### 3. Generate embeddings

The project uses `sentence-transformers/all-MiniLM-L6-v2` to encode text chunks as dense vector representations. The same embedding model is used for user questions so they can be compared in the same vector space.

### 4. Store and retrieve with ChromaDB

Embeddings, chunk text, and associated metadata are stored in a persistent ChromaDB collection named `cloudealam_knowledge`. The current persisted database path is `./chroma_db_fast`.

At query time, the system performs semantic similarity search and retrieves the top matching chunks for the question.

### 5. Generate a context-grounded answer

The retrieved passages are combined with the user's question and sent to the local Ollama API, using the `llama3.2` model. This gives the model relevant CloudAlam documentation to use when formulating its answer.

### 6. Interact through the chat UI

`chat_ui.py` provides an interface for asking questions against the RAG pipeline. The interface uses lazy loading to reduce the delay before the application becomes usable.

---

## Evaluation

A key focus of this project is evaluating the system rather than relying only on a few successful demo questions. Two evaluation scripts have been implemented for different parts of the pipeline.

### Retrieval Evaluation — `evaluate_rag.py`

The retrieval test set contains **15 questions** with expected source-document relevance. Evaluation uses the top three retrieved chunks/documents.

Latest recorded results:

| Metric | Result | Interpretation |
| --- | ---: | --- |
| **Hit Rate@3** | **100% (15/15)** | The expected relevant source was present in the top three results for every test question. |
| **Mean Reciprocal Rank (MRR)** | **0.967** | Relevant results generally appeared at or very near the top of the ranking. |

One query about the Standard Object Storage price ranked its expected source second rather than first. These results indicate strong retrieval performance on the current, small, curated test set; they should not be interpreted as a guarantee of performance on unseen questions or larger datasets.

### Answer Evaluation — `evaluate_answers.py`

The answer evaluation script checks whether generated responses contain required facts for a set of **15 questions**.

Latest recorded result:

- **14 of 15 checks passed (93.33%).**
- One failure was caused by exact substring matching: the expected text was `24/7`, while the model expressed the same fact as “24 hours a day, 7 days a week.”
- The answer was semantically equivalent, so this case exposed a limitation in the evaluator rather than a factual error in the response.

This is an important distinction: exact string matching can produce false negatives when a correct answer uses different wording. A stronger evaluator should account for semantic equivalence and should be validated against manually reviewed examples.

### Next Evaluation Goal: Faithfulness and Hallucination Detection

The next planned evaluation step is to assess whether each generated answer is supported by the passages retrieved for that question. This differs from checking whether an answer contains expected facts: an answer may include the expected fact while also adding unsupported claims.

A proposed faithfulness evaluation will identify claims that cannot be supported by the retrieved context. LLM-as-a-judge scoring can help with this task, but its decisions should be treated as estimates and reviewed against the source passages, especially for ambiguous cases.

---

## Running the Project

### Prerequisites

- Python 3
- Ollama installed and running locally
- The `llama3.2` model available in Ollama
- The Python packages used by the project scripts, including ChromaDB and Sentence Transformers

### 1. Start Ollama and make sure the model is available

```bash
ollama pull llama3.2
ollama run llama3.2
```

Keep Ollama running while using the RAG application. The project calls the local generation API at:

```text
http://localhost:11434/api/generate
```

### 2. Install Python dependencies

Install the dependencies used by the scripts in your environment. If the project has a `requirements.txt`, use it:

```bash
pip install -r requirements.txt
```

If no dependency file is present, install the packages required by the scripts, including `chromadb`, `sentence-transformers`, and the UI framework used by `chat_ui.py`.

### 3. Build or refresh the vector index

Run the ingestion and indexing scripts in the order appropriate to their current interfaces:

```bash
python load_documents.py
python chunk_documents.py
python embed_documents.py
python chroma_db.py
```

These scripts represent the project's document-loading, chunking, embedding, and vector-store stages. If the persisted database is already available and matches the current documents and embedding model, rebuilding it may not be necessary. Check each script's implementation for its exact inputs and outputs before rerunning the pipeline.

### 4. Test semantic retrieval

```bash
python search_chroma.py
```

### 5. Run the RAG application

```bash
python chat_ui.py
```

### 6. Run the evaluation scripts

```bash
python evaluate_rag.py
python evaluate_answers.py
```

The evaluation results depend on the current knowledge base, vector index, model version, prompt, and test set. Re-run the evaluations after making changes to these components.

---

## Engineering Highlights

- **End-to-end RAG implementation:** connects document preparation, vector search, and LLM-based response generation in one workflow.
- **Local model inference:** uses Ollama with `llama3.2`, allowing generation to run through a local API rather than requiring a hosted LLM API for this setup.
- **Persistent semantic index:** uses ChromaDB so indexed chunks can be reused between application runs.
- **Dedicated retrieval testing:** evaluates ranking behavior with Hit Rate@3 and MRR instead of relying only on manual inspection.
- **Answer-level checks:** validates generated responses against required facts and documents a real limitation in exact-match evaluation.
- **Explicit evaluation boundaries:** distinguishes retrieval success, required-fact coverage, and faithfulness as separate quality dimensions.
- **Responsive UI startup:** applies lazy loading in the chat interface to reduce initial loading friction.

---

## Current Scope and Limitations

- The knowledge base is a small, curated fictional dataset; evaluation scores may not generalize to other domains or larger corpora.
- Retrieval metrics measure whether relevant sources are retrieved, not whether the generated answer is correct.
- Required-fact evaluation can miss semantic equivalents when it relies on exact string matching.
- Faithfulness / unsupported-claim evaluation is the next planned stage and should not be considered complete until implemented and reviewed.
- The project currently documents a local development workflow; production deployment, authentication, monitoring, and access control are outside the scope described here.

---

## Potential Future Improvements

- Implement faithfulness evaluation and unsupported-claim reporting.
- Improve answer evaluation with semantic matching and manually reviewed test cases.
- Expand the question set with paraphrases, edge cases, and questions whose answers are absent from the knowledge base.
- Evaluate retrieval with additional metrics and compare chunk sizes, overlap settings, and embedding models.
- Add explicit source citations to generated answers so users can verify claims against retrieved passages.
- Add automated regression tests for the ingestion, retrieval, and generation stages.
- Track evaluation results across changes to prompts, models, and knowledge-base content.
- Add configuration management for model names, API URLs, database paths, and retrieval parameters.
- Add a dependency lockfile or `requirements.txt` for reproducible setup.

---

## Learning Objectives

This project provides hands-on experience with:

- Building a Retrieval-Augmented Generation pipeline
- Preparing documents for semantic search
- Generating and reusing text embeddings
- Storing and querying vectors with ChromaDB
- Connecting a local language model through an HTTP API
- Designing context-aware prompts
- Building an interactive question-answering interface
- Measuring retrieval quality with ranking metrics
- Evaluating answer coverage and understanding exact-match limitations
- Planning faithfulness and hallucination evaluation

---

## Summary

CloudAlam is an end-to-end RAG learning project that combines a curated Markdown knowledge base, Sentence Transformers embeddings, persistent ChromaDB retrieval, and local LLM generation through Ollama. It also includes separate evaluation scripts for retrieval and answer-level checks, with recorded results of **100% Hit Rate@3** and **93.33% required-fact pass rate** on the current 15-question test set. The project emphasizes not only building the pipeline, but also measuring its behavior and identifying the next steps toward more reliable, context-grounded answers.
