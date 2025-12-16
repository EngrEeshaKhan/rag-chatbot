import numpy as np
from backend.rag.embeddings import get_embeddings
from backend.rag.vectordb import load_faiss


def retrieve(query):
    # Load FAISS index and metadata
    index, metadata = load_faiss()
    if index is None or metadata is None:
        return ["No FAISS index found. Upload a document first."]

    # Convert query to vector
    embeddings = get_embeddings()
    q_vector = embeddings.embed_query(query)
    q_vector = np.array(q_vector).astype("float32").reshape(1, -1)

    # Search top-k similar chunks
    k = 12  # ✅ increase to cover more of the document
    distances, indices = index.search(q_vector, k)

    results = []
    print("\n===== RETRIEVED CHUNKS =====")
    for i in indices[0]:
        key = str(i)
        if key in metadata:
            results.append(metadata[key])
            print(f"CHUNK {i} (first 300 chars):\n{metadata[key][:300]}\n---")
    print("============================\n")

    if not results:
        return ["No relevant context found in the document."]

    return results
