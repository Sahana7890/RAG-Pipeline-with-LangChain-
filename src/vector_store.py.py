from typing import List

from langchain_core.documents import Document
from langchain_chroma import Chroma

from .config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_PERSIST_DIRECTORY,
)

from .embeddings import get_embeddings


def create_vector_store(
    documents: List[Document],
):
    """
    Create a persistent ChromaDB vector store
    from document chunks.
    """

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=CHROMA_COLLECTION_NAME,
        persist_directory=CHROMA_PERSIST_DIRECTORY,
    )

    return vector_store


def load_vector_store():
    """
    Load an existing ChromaDB vector store.
    """

    embeddings = get_embeddings()

    vector_store = Chroma(
        collection_name=CHROMA_COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_PERSIST_DIRECTORY,
    )

    return vector_store