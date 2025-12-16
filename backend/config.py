class Settings:
    # LLMs
    USE_GROQ = True
    GROQ_API_KEY = "your own api"  # directly here
    GROQ_MODEL = "llama-3.1-8b-instant"
    OLLAMA_MODEL = "llama3.1"

    # Embedding model (MiniLM)
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    # Paths for data and uploads
    DATA_PATH = "backend/data/faiss_index"
    UPLOAD_PATH = "backend/uploads"

settings = Settings()
