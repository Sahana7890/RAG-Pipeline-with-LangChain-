from .config import TOP_K
from .vector_store import load_vector_store


def get_retriever():
    """
    Create a similarity-based retriever.
    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": TOP_K
        },
    )

    return retriever


def retrieve_documents(question: str):
    """
    Retrieve the most relevant document chunks.
    """

    retriever = get_retriever()

    documents = retriever.invoke(question)

    return documents