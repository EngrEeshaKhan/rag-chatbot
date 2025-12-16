import os
import json
import faiss
from backend.config import settings


# ================================
# Save FAISS index and metadata
# ================================
def save_faiss(index, metadata):
    # Create data directory if it doesn't exist
    os.makedirs(settings.DATA_PATH, exist_ok=True)

    # Save FAISS vector index to disk
    faiss.write_index(index, f"{settings.DATA_PATH}/index.faiss")

    # Save metadata (text chunks) as JSON
    with open(f"{settings.DATA_PATH}/metadata.json", "w") as f:
        json.dump(metadata, f)


# ================================
# Load FAISS index and metadata
# ================================
def load_faiss():
    index_path = f"{settings.DATA_PATH}/index.faiss"
    meta_path = f"{settings.DATA_PATH}/metadata.json"

    # If index does not exist, no document has been uploaded yet
    if not os.path.exists(index_path):
        return None, None

    # Load FAISS index from disk
    index = faiss.read_index(index_path)

    # Load metadata (text chunks)
    with open(meta_path, "r") as f:
        metadata = json.load(f)

    return index, metadata
