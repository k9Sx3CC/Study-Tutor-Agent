import streamlit as st


# =========================================================
# INITIALIZE MEMORY
# =========================================================

def initialize_memory():

    if "messages" not in st.session_state:

        st.session_state.messages = []


# =========================================================
# ADD MESSAGE
# =========================================================

def add_message(
    role,
    content,
):

    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )


# =========================================================
# GET HISTORY
# =========================================================

def get_conversation_history():

    initialize_memory()


    history = []


    for message in st.session_state.messages:

        role = message["role"]

        content = message["content"]

        history.append(
            f"{role}: {content}"
        )


    return "\n".join(history)


# =========================================================
# CLEAR MEMORY
# =========================================================

def clear_memory():

    st.session_state.messages = []
