from backend.config import settings

# Returns LLM instance
def get_llm():
    if settings.USE_GROQ:
        from langchain_groq import ChatGroq
        # Initialize Groq client
        llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=settings.GROQ_MODEL
        )
        return llm
    else:
        from langchain_ollama import ChatOllama
        llm = ChatOllama(
            model=settings.OLLAMA_MODEL
        )
        return llm
