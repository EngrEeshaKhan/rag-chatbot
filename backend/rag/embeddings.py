import os

# ✅ FIX WINDOWS SSL ISSUE
os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"

from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.config import settings

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL
    )
