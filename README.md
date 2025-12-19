# RAG Chatbot

A **Retrieval-Augmented Generation (RAG) Chatbot** that allows users to upload PDF documents and ask questions. The chatbot provides **context-aware answers** by combining a **LangChain RAG pipeline**, **FAISS vector database**, and a **local LLM as (Llama 3.1 via Ollama)**.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Architecture](#architecture)  
- [Project Structure](#project-structure)  
- [Features](#features)  
- [Installation](#installation)  
  - [Python Environment](#python-environment)  
  - [Docker Setup](#docker-setup)  
- [Usage](#usage)  
- [License](#license)  

---

## Project Overview

RAG Chatbot allows users to:

1. Upload PDF files through a web interface.  
2. Ask questions about the content of the uploaded PDFs.  
3. Receive accurate answers generated using a **local LLM** powered by a **LangChain RAG pipeline**.

The system integrates PDF processing, text chunking, vector embeddings, similarity search, and LLM-based answer generation.

---

## Architecture

<img width="250" height="400" alt="image" src="https://github.com/user-attachments/assets/9d66d08c-4ecc-4846-9b1c-ec97cb77eaf6" />



---

## Project Structure

```

rag-chatbot/
│ .gitignore
│ Dockerfile
│ LICENSE
│ README.md
│
├───backend
│ │ config.py
│ │ main.py
│ │ requirements.txt
│ │
│ ├───data
│ │ └───faiss_index
│ │ index.faiss
│ │ metadata.json
│ │
│ ├───rag
│ │ embeddings.py
│ │ llm.py
│ │ loader.py
│ │ pipeline.py
│ │ retriever.py
│ │ splitter.py
│ │ vectordb.py
│ │ init.py
│ │
│ └───uploads
│
└───frontend
index.html
script.js
style.css

```

## Features

- 🔗 **LangChain** — Implements the RAG pipeline  
- ⚡ **FastAPI** — Backend server for handling API requests  
- 🎨 **HTML / CSS / JavaScript** — Frontend for file upload and Q&A  
- 🧠 **MiniLM Embeddings** — Embedding model for vector representation  
- 📊 **FAISS** — Vector database for similarity search  
- 🤖 **Llama 3.1 (Ollama)** — Local LLM for generating answers  

### API Endpoints
- 📤 `/upload` — Upload PDF files  
- ❓ `/ask` — Ask questions about uploaded PDFs  

- 🐳 **Docker Support** — Containerized deployment


## Installation

### Python Environment

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
 pip install -r backend/requirements.txt
```

### Docker Setup

1. Build Docker image:
```bash
docker build -t rag-chatbot .
```

2.Run Docker container:
```bash
docker run -it -p 8000:8000 rag-chatbot
```

Backend available at http://localhost:8000.

Open frontend/index.html to upload PDFs and ask questions.


## Usage

Upload your PDF via the frontend.

Ask your question.

Backend searches FAISS for relevant chunks and generates an answer using Llama 3.1.

Receive context-aware answers.

## License

This project is licensed under the **MIT** License — free to use, modify, and distribute.









