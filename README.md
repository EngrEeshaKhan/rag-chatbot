# RAG Chatbot

A **Retrieval-Augmented Generation (RAG) Chatbot** that allows users to upload PDF documents and ask questions. The chatbot provides **context-aware answers** by combining a **LangChain RAG pipeline**, **FAISS vector database**, and a **local LLM (Llama 3.1 via Ollama)**.

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

## Tech Stack

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="40" />
</p>








