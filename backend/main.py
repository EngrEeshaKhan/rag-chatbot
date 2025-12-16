import os
import numpy as np
import faiss
import logging

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from backend.config import settings
from backend.rag.loader import load_pdf
from backend.rag.splitter import split_text
from backend.rag.embeddings import get_embeddings
from backend.rag.vectordb import save_faiss
from backend.rag.pipeline import answer_question

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PDF Upload
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs(settings.UPLOAD_PATH, exist_ok=True)
    save_path = f"{settings.UPLOAD_PATH}/{file.filename}"
    with open(save_path, "wb") as f:
        f.write(await file.read())

    text = load_pdf(save_path)
    chunks = split_text(text)

    embeddings = get_embeddings()
    vectors = embeddings.embed_documents(chunks)
    vectors_np = np.array(vectors).astype("float32")

    index = faiss.IndexFlatL2(vectors_np.shape[1])
    index.add(vectors_np)

    metadata = {i: chunk for i, chunk in enumerate(chunks)}
    save_faiss(index, metadata)

    return {"message": "File uploaded and processed successfully"}

# Ask endpoint
@app.post("/ask")
async def ask(question: str = Form(...)):
    try:
        answer = answer_question(question)
    except Exception as e:
        logger.error(f"Failed to answer question: {e}")
        answer = f"Could not generate answer. Please check server logs. Error: {e}"
    return {"answer": answer}
