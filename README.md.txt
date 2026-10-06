# RAG Pipeline with LangChain, ChromaDB and Groq

## 📚 Project Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline using LangChain, ChromaDB, Hugging Face embeddings, and a Groq-hosted large language model.

The system allows users to ask questions about a document corpus. Relevant document chunks are retrieved from ChromaDB and passed to the Groq language model as context. The generated answer is displayed together with source information.

## 🎯 Objectives

The main objectives of this project are:

* Build an end-to-end RAG pipeline.
* Load a document corpus.
* Split documents into meaningful chunks.
* Generate vector embeddings.
* Store embeddings in ChromaDB.
* Retrieve relevant document chunks.
* Generate answers using a Groq LLM.
* Provide source citations for retrieved information.
* Create an interactive Q&A chatbot.
* Test retrieval and generation quality.
* Handle questions that cannot be answered from the knowledge base.

## 🏗️ System Architecture

```text
                 ┌─────────────────────┐
                 │    Documents        │
                 │  PDF / TXT Corpus   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Document Loader    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Text Splitter      │
                 │  Chunking           │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ HuggingFace         │
                 │ Embeddings          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     ChromaDB        │
                 │   Vector Store      │
                 └──────────┬──────────┘
                            │
                            │ Retrieval
                            ▼
                  ┌────────────────────┐
                  │ Relevant Chunks    │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │    Groq LLM        │
                  │    Generation      │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Answer + Sources   │
                  └────────────────────┘
```

## 🛠️ Technologies

* Python
* LangChain
* ChromaDB
* Groq
* Hugging Face Sentence Transformers
* Streamlit
* PyPDF
* python-dotenv

## 📁 Project Structure

```text
rag-pipeline-langchain-chromadb/
│
├── data/
│   └── sample_document.txt
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   ├── rag_pipeline.py
│   └── utils.py
│
├── app.py
├── ingest.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd rag-pipeline-langchain-chromadb
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a file named:

```text
.env
```

Copy the contents of `.env.example` and add your own Groq API key.

Example:

```env
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

Do not commit the `.env` file to GitHub.

## 📄 Adding Documents

Place your documents inside:

```text
data/
```

Supported document formats:

* `.txt`
* `.pdf`

Example:

```text
data/
├── sample_document.txt
├── document1.pdf
└── document2.pdf
```

## 🧠 Building the Vector Database

Run:

```bash
python ingest.py
```

The ingestion pipeline performs:

1. Document loading.
2. Text splitting.
3. Embedding generation.
4. ChromaDB indexing.
5. Persistent vector storage.

A local `chroma_db/` directory will be created.

The database is intentionally excluded from GitHub through `.gitignore`.

## 💬 Running the Chatbot

After indexing the documents, run:

```bash
streamlit run app.py
```

The application opens a web interface where users can ask questions.

Example questions:

```text
What is RAG?

What are the stages of the RAG pipeline?

Why is ChromaDB used?

What is the purpose of document chunking?

How are source citations generated?
```

## 🔎 Retrieval Process

For every user question:

```text
User Question
      ↓
Question Embedding
      ↓
ChromaDB Similarity Search
      ↓
Top-K Relevant Chunks
      ↓
Context Construction
      ↓
Groq LLM
      ↓
Final Answer
      ↓
Source Citations
```

## 📌 Source Citations

The application records metadata from retrieved documents.

For PDF documents, page numbers are displayed when available.

Example:

```text
Sources

- data/sample_document.txt
- data/document1.pdf - Page 3
```

This helps users understand where the generated answer originated.

## 🛡️ Hallucination Control

The RAG prompt instructs the model to answer using only the retrieved context.

If the information is not available in the provided documents, the system responds that the answer could not be found.

This reduces unsupported answers.

## 🧪 Testing

The system should be tested with:

### 1. Direct questions

Questions whose answers are clearly present in the documents.

### 2. Paraphrased questions

Questions that use different wording from the documents.

### 3. Multi-part questions

Questions requiring information from multiple retrieved chunks.

### 4. Out-of-scope questions

Questions whose answers are not present in the document corpus.

### 5. Source verification

Check whether the displayed sources actually contain information related to the answer.

## 📊 Evaluation Metrics

The project can be evaluated using:

### Retrieval Accuracy

Measures whether relevant chunks are retrieved.

### Answer Correctness

Measures whether the generated answer correctly answers the question.

### Context Relevance

Measures whether retrieved context is relevant to the question.

### Faithfulness

Measures whether the generated answer is supported by the retrieved context.

### Source Attribution

Measures whether the system correctly identifies the documents used for the response.

### Response Latency

Measures the time required to retrieve documents and generate an answer.

## ⚠️ Limitations

The current implementation has several limitations:

* Retrieval uses similarity search.
* The quality of answers depends on the document corpus.
* Very large documents may require improved chunking strategies.
* Source citation is based on document metadata.
* The system does not perform external web search.
* The system depends on the availability of the Groq API.
* Embeddings are generated locally.

## 🚀 Future Improvements

Potential future improvements include:

* Hybrid keyword + semantic retrieval.
* Reranking retrieved documents.
* Retrieval evaluation using Recall@K.
* Answer evaluation using faithfulness and relevance metrics.
* Conversational memory.
* Multiple document collections.
* Better PDF parsing.
* Metadata filtering.
* Query rewriting.
* Streaming responses.
* User feedback collection.
* Human-in-the-loop answer verification.
* Automated evaluation datasets.
* Improved citation formatting.
* Deployment using Docker.

## 📅 Week-by-Week Development Plan

### Week 1–2: Setup and Research

* Understand RAG architecture.
* Research LangChain.
* Research vector databases.
* Research ChromaDB.
* Research Groq.
* Set up Python environment.
* Create GitHub repository.

### Week 3–4: Core Feature Implementation

* Implement document loading.
* Implement text splitting.
* Implement embeddings.
* Create ChromaDB vector store.
* Implement similarity retrieval.
* Integrate Groq LLM.
* Implement initial RAG pipeline.

### Week 5–6: Integration and Testing

* Integrate all components.
* Create chatbot interface.
* Add source citations.
* Test different questions.
* Test retrieval quality.
* Test hallucination handling.
* Collect feedback.
* Improve chunking and retrieval parameters.

### Week 7: Advanced Features

* Improve source attribution.
* Add edge-case handling.
* Improve prompt design.
* Test out-of-scope questions.
* Investigate retrieval improvements.
* Add evaluation metrics.

### Week 8: Documentation and Final Submission

* Complete README.
* Clean the repository.
* Add architecture diagram.
* Record demonstration video.
* Document test results.
* Document limitations.
* Document future improvements.
* Prepare final presentation.
* Submit final GitHub repository.

## 👨‍💻 Running the Complete Project

```bash
pip install -r requirements.txt
```

Configure:

```text
.env
```

Then index the documents:

```bash
python ingest.py
```

Finally start the application:

```bash
streamlit run app.py
```

## 🔐 Security

API keys must never be committed to GitHub.

Use:

```text
.env
```

for local secrets and:

```text
.env.example
```

as the configuration template.

## 📜 License

This project is provided for educational and academic purposes.
