from langchain_core.prompts import ChatPromptTemplate

from .llm import get_llm
from .retriever import retrieve_documents
from .utils import (
    format_documents,
    get_sources,
)


RAG_PROMPT = """
You are a helpful question-answering assistant.

Answer the user's question using ONLY the provided context.

Rules:
1. Do not invent information.
2. If the answer is not available in the context, say:
   "I could not find the answer in the provided documents."
3. Give a clear and concise answer.
4. Use the source information provided in the context.
5. Do not use outside knowledge.

Context:
{context}

Question:
{question}

Answer:
"""


def create_prompt():
    """
    Create the RAG prompt.
    """

    return ChatPromptTemplate.from_template(
        RAG_PROMPT
    )


def answer_question(question: str):
    """
    Complete RAG pipeline:

    Question
        ↓
    Retrieval
        ↓
    Context
        ↓
    Groq LLM
        ↓
    Answer + Sources
    """

    documents = retrieve_documents(question)

    if not documents:
        return {
            "answer": (
                "I could not find relevant information "
                "in the provided documents."
            ),
            "sources": [],
        }

    context = format_documents(documents)

    prompt = create_prompt()

    llm = get_llm()

    messages = prompt.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    response = llm.invoke(messages)

    answer = response.content

    sources = get_sources(documents)

    return {
        "answer": answer,
        "sources": sources,
        "documents": documents,
    }