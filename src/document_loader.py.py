from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
)


def load_text_file(file_path: str) -> List[Document]:
    """
    Load a TXT document.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    loader = TextLoader(
        str(path),
        encoding="utf-8"
    )

    documents = loader.load()

    return documents


def load_pdf_file(file_path: str) -> List[Document]:
    """
    Load a PDF document.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    loader = PyPDFLoader(str(path))

    documents = loader.load()

    return documents


def load_document(file_path: str) -> List[Document]:
    """
    Automatically select the appropriate loader.
    """

    extension = Path(file_path).suffix.lower()

    if extension == ".txt":
        return load_text_file(file_path)

    if extension == ".pdf":
        return load_pdf_file(file_path)

    raise ValueError(
        f"Unsupported file type: {extension}. "
        "Supported types: .txt and .pdf"
    )


def load_corpus(data_directory: str) -> List[Document]:
    """
    Load all supported documents from a directory.
    """

    data_path = Path(data_directory)

    if not data_path.exists():
        raise FileNotFoundError(
            f"Data directory not found: {data_directory}"
        )

    documents = []

    for file_path in data_path.iterdir():

        if file_path.suffix.lower() in [".txt", ".pdf"]:

            try:
                loaded_documents = load_document(
                    str(file_path)
                )

                documents.extend(loaded_documents)

            except Exception as error:
                print(
                    f"Could not load {file_path.name}: {error}"
                )

    if not documents:
        raise ValueError(
            "No supported documents were found in the data directory."
        )

    return documents