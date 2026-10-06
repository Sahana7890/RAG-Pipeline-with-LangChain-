from typing import List

from langchain_core.documents import Document


def format_documents(
    documents: List[Document],
) -> str:
    """
    Convert retrieved documents into a context string.
    """

    formatted_documents = []

    for index, document in enumerate(documents, start=1):

        source = document.metadata.get(
            "source",
            "Unknown source"
        )

        page = document.metadata.get(
            "page"
        )

        if page is not None:
            source_info = (
                f"{source}, page {page + 1}"
            )
        else:
            source_info = source

        formatted_documents.append(
            f"[Source {index}: {source_info}]\n"
            f"{document.page_content}"
        )

    return "\n\n".join(formatted_documents)


def get_sources(
    documents: List[Document],
) -> List[str]:
    """
    Extract source names from retrieved documents.
    """

    sources = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown source"
        )

        page = document.metadata.get("page")

        if page is not None:
            source = (
                f"{source} - Page {page + 1}"
            )

        if source not in sources:
            sources.append(source)

    return sources