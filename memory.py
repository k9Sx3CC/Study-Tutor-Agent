import streamlit as st


def initialize_memory():
    """Initialize the student's conversation memory."""

    if "messages" not in st.session_state:
        st.session_state.messages = []


def add_message(role, content):
    """Store a message in the current study session."""

    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )


def get_messages():
    """Return all messages from the current study session."""

    return st.session_state.messages


def get_history():
    """Convert conversation messages into text for the tutor."""

    history = []

    for message in st.session_state.messages:
        history.append(
            f'{message["role"]}: {message["content"]}'
        )

    return "\n".join(history)


def clear_memory():
    """Clear the current study session."""

    st.session_state.messages = []
