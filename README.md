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

