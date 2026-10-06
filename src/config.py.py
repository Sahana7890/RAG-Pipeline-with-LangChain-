import os
from pathlib import Path

from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Data directory
DATA_DIR = BASE_DIR / "data"


# ChromaDB directory
CHROMA_PERSIST_DIRECTORY = os.getenv(
    "CHROMA_PERSIST_DIRECTORY",
    str(BASE_DIR / "chroma_db")
)


# Chroma collection
CHROMA_COLLECTION_NAME = os.getenv(
    "CHROMA_COLLECTION_NAME",
    "rag_documents"
)


# Groq configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.1-8b-instant"
)


# Embedding configuration
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)


# Text chunking
CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", "800")
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", "150")
)


# Retrieval
TOP_K = int(
    os.getenv("TOP_K", "4")
)


def validate_config():
    """Validate required configuration."""

    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Create a .env file and add your Groq API key."
        )