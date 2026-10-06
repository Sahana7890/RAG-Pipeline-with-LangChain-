import streamlit as st

from src.config import validate_config
from src.rag_pipeline import answer_question


st.set_page_config(
    page_title="RAG Q&A Chatbot",
    page_icon="📚",
    layout="centered",
)


st.title("📚 RAG Q&A Chatbot")

st.write(
    "Ask questions about the documents in the knowledge base."
)


# Validate configuration
try:
    validate_config()

except ValueError as error:

    st.error(str(error))
    st.stop()


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )


# User question
question = st.chat_input(
    "Ask a question about the documents..."
)


if question:

    # Display user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)


    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner(
            "Searching documents..."
        ):

            try:

                result = answer_question(
                    question
                )

                answer = result["answer"]
                sources = result["sources"]

                st.markdown(answer)

                # Display sources
                if sources:

                    st.markdown(
                        "### 📌 Sources"
                    )

                    for source in sources:
                        st.write(
                            f"- {source}"
                        )

                else:

                    st.info(
                        "No sources were found."
                    )

                # Store assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

            except Exception as error:

                st.error(
                    f"An error occurred: {error}"
                )