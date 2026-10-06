from langchain_groq import ChatGroq

from .config import GROQ_API_KEY, GROQ_MODEL


def get_llm():
    """
    Initialize the Groq chat model.
    """

    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Add it to your .env file."
        )

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        temperature=0,
    )

    return llm