from backend.rag.retriever import retrieve
from backend.rag.llm import get_llm

def answer_question(query):
    # 1. Retrieve context
    context_chunks = retrieve(query)
    context = "\n\n".join(context_chunks)

    # 2. Prompt
    prompt = f"""
Use ONLY the context below to answer the question.
If the answer is not in the text, say you don't know.

Context:
{context}

Question: {query}
Answer:
"""

    llm = get_llm()

    # ✅ CORRECT LangChain Chat call
    response = llm.invoke(prompt)

    # ✅ response is an AIMessage
    # ✅ AIMessage.content is the text
    return response.content
