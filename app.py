```python
import streamlit as st

from crew import run_tutor
from memory import (
    initialize_memory,
    add_message,
    get_messages,
    get_history,
    clear_memory,
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =========================================
       GLOBAL APP
       ========================================= */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(0, 191, 255, 0.10),
                transparent 28%
            ),
            radial-gradient(
                circle at 85% 80%,
                rgba(0, 100, 255, 0.08),
                transparent 30%
            ),
            #070B14;

        color: #E8F1FF;
    }


    /* =========================================
       MAIN CONTENT
       ========================================= */

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* =========================================
       SIDEBAR
       ========================================= */

    section[data-testid="stSidebar"] {
        background: #090F1C;
        border-right: 1px solid rgba(0, 191, 255, 0.15);
    }


    section[data-testid="stSidebar"] h2 {
        color: #FFFFFF;
    }


    /* =========================================
       HERO SECTION
       ========================================= */

    .hero {
        padding: 28px 30px;
        border-radius: 22px;

        background: rgba(10, 18, 32, 0.82);

        border: 1px solid rgba(0, 191, 255, 0.20);

        box-shadow:
            0 0 35px rgba(0, 191, 255, 0.08),
            inset 0 1px 0 rgba(255, 255, 255, 0.04);

        margin-bottom: 25px;
    }


    .hero-badge {
        display: inline-block;

        padding: 6px 12px;

        border-radius: 999px;

        background: rgba(0, 191, 255, 0.10);

        border: 1px solid rgba(0, 191, 255, 0.25);

        color: #55DFFF;

        font-size: 12px;

        font-weight: 600;

        letter-spacing: 0.08em;

        text-transform: uppercase;

        margin-bottom: 12px;
    }


    .hero-title {
        font-size: 42px;

        font-weight: 750;

        line-height: 1.1;

        color: #FFFFFF;

        margin-bottom: 10px;
    }


    .hero-title span {
        color: #32D6FF;

        text-shadow:
            0 0 18px rgba(50, 214, 255, 0.45);
    }


    .hero-subtitle {
        color: #9FB2C8;

        font-size: 16px;

        line-height: 1.6;

        max-width: 720px;
    }


    /* =========================================
       SECTION LABEL
       ========================================= */

    .section-label {
        color: #55DFFF;

        font-size: 12px;

        font-weight: 700;

        text-transform: uppercase;

        letter-spacing: 0.12em;

        margin-top: 25px;

        margin-bottom: 8px;
    }


    /* =========================================
       CHAT MESSAGES
       ========================================= */

    div[data-testid="stChatMessage"] {
        background: rgba(12, 20, 35, 0.75);

        border: 1px solid rgba(255, 255, 255, 0.06);

        border-radius: 18px;

        padding: 10px;

        margin-bottom: 12px;
    }


    /* =========================================
       CHAT INPUT
       ========================================= */

    div[data-testid="stChatInput"] {
        border: 1px solid rgba(0, 191, 255, 0.25);

        border-radius: 18px;

        background: #0C1423;

        box-shadow:
            0 0 20px rgba(0, 191, 255, 0.06);
    }


    div[data-testid="stChatInput"]:focus-within {
        border-color: #32D6FF;

        box-shadow:
            0 0 25px rgba(50, 214, 255, 0.18);
    }


    /* =========================================
       BUTTONS
       ========================================= */

    .stButton > button {
        width: 100%;

        border-radius: 12px;

        border: 1px solid rgba(50, 214, 255, 0.30);

        background: rgba(0, 191, 255, 0.08);

        color: #DDF8FF;

        font-weight: 600;

        transition: all 0.2s ease;
    }


    .stButton > button:hover {
        border-color: #32D6FF;

        background: rgba(0, 191, 255, 0.16);

        box-shadow:
            0 0 18px rgba(50, 214, 255, 0.15);

        color: #FFFFFF;
    }


    /* =========================================
       SELECT BOX
       ========================================= */

    div[data-baseweb="select"] > div {
        background: #0C1423;

        border: 1px solid rgba(0, 191, 255, 0.15);

        border-radius: 12px;
    }


    /* =========================================
       FEATURE CARDS
       ========================================= */

    .feature-card {
        background: rgba(12, 20, 35, 0.72);

        border: 1px solid rgba(255, 255, 255, 0.06);

        border-radius: 18px;

        padding: 20px;

        height: 100%;
    }


    .feature-icon {
        font-size: 25px;

        margin-bottom: 8px;
    }


    .feature-title {
        color: #FFFFFF;

        font-size: 16px;

        font-weight: 700;

        margin-bottom: 5px;
    }


    .feature-text {
        color: #8FA5BB;

        font-size: 13px;

        line-height: 1.5;
    }


    /* =========================================
       STATUS CARD
       ========================================= */

    .status-card {
        background: rgba(0, 191, 255, 0.05);

        border: 1px solid rgba(0, 191, 255, 0.12);

        border-radius: 12px;

        padding: 12px;

        color: #8FA5BB;

        font-size: 12px;

        margin-top: 15px;
    }


    /* =========================================
       FOOTER
       ========================================= */

    .footer {
        text-align: center;

        color: #61758A;

        font-size: 12px;

        margin-top: 45px;

        padding-top: 20px;

        border-top: 1px solid rgba(255, 255, 255, 0.05);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# INITIALIZE MEMORY
# =========================================================

initialize_memory()


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            ✦ AI Study Assistant
        </div>

        <div class="hero-title">
            Learn smarter with your
            <span>AI Tutor.</span>
        </div>

        <div class="hero-subtitle">
            Ask questions, understand difficult concepts,
            practice what you learn, and get personalized
            guidance from your Study Tutor Agent.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ✦ Study Tutor")

    st.caption(
        "Your AI-powered learning companion"
    )

    st.markdown("---")

    st.markdown(
        '<div class="section-label">Learning Settings</div>',
        unsafe_allow_html=True,
    )


    # -----------------------------------------
    # Subject
    # -----------------------------------------

    subject = st.selectbox(
        "Subject",
        [
            "Mathematics",
            "Science",
            "Computer Science",
            "English",
        ],
    )


    # -----------------------------------------
    # Learning Level
    # -----------------------------------------

    level = st.selectbox(
        "Learning Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )


    st.markdown("---")


    # -----------------------------------------
    # Capabilities
    # -----------------------------------------

    st.markdown(
        '<div class="section-label">Tutor Capabilities</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            color:#8FA5BB;
            line-height:1.9;
            font-size:13px;
        ">

        ✦ Concept explanations<br>
        ✦ Step-by-step examples<br>
        ✦ Practice questions<br>
        ✦ Answer feedback<br>
        ✦ Study planning<br>
        ✦ Mathematical calculations

        </div>
        """,
        unsafe_allow_html=True,
    )


    # -----------------------------------------
    # Memory status
    # -----------------------------------------

    message_count = len(get_messages())

    st.markdown(
        f"""
        <div class="status-card">

        <strong style="color:#55DFFF;">
        ✦ Session Memory
        </strong>

        <br><br>

        {message_count} messages stored in this session.

        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown("---")


    # -----------------------------------------
    # Clear Memory
    # -----------------------------------------

    if st.button("↻ Clear Conversation"):

        clear_memory()

        st.rerun()


# =========================================================
# EMPTY STATE
# =========================================================

if len(get_messages()) == 0:

    st.markdown(
        '<div class="section-label">Start Learning</div>',
        unsafe_allow_html=True,
    )


    col1, col2, col3 = st.columns(3)


    # -----------------------------------------
    # Card 1
    # -----------------------------------------

    with col1:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    ◈
                </div>

                <div class="feature-title">
                    Understand
                </div>

                <div class="feature-text">
                    Ask about a difficult concept
                    and receive an explanation
                    suited to your level.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # -----------------------------------------
    # Card 2
    # -----------------------------------------

    with col2:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    ◇
                </div>

                <div class="feature-title">
                    Practice
                </div>

                <div class="feature-text">
                    Test your understanding with
                    questions and examples generated
                    by your AI tutor.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # -----------------------------------------
    # Card 3
    # -----------------------------------------

    with col3:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    ✦
                </div>

                <div class="feature-title">
                    Improve
                </div>

                <div class="feature-text">
                    Submit your answers and receive
                    constructive feedback to improve
                    your understanding.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in get_messages():

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

question = st.chat_input(
    "Ask your Study Tutor anything..."
)


# =========================================================
# PROCESS USER QUESTION
# =========================================================

if question:

    # -----------------------------------------
    # Show user message
    # -----------------------------------------

    with st.chat_message("user"):

        st.markdown(question)


    # -----------------------------------------
    # Save user message
    # -----------------------------------------

    add_message(
        role="user",
        content=question,
    )


    # -----------------------------------------
    # Get conversation history
    # -----------------------------------------

    history = get_history()


    # -----------------------------------------
    # Run Study Tutor
    # -----------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "✦ Your tutor is thinking..."
        ):

            try:

                response = run_tutor(
                    subject=subject,
                    level=level,
                    question=question,
                    history=history,
                )


                # Convert CrewAI result to text
                answer = str(response)


                # Display answer
                st.markdown(answer)


                # Save tutor response
                add_message(
                    role="assistant",
                    content=answer,
                )


            except Exception as e:

                st.error(
                    "The tutor could not respond."
                )

                st.caption(
                    "Please check your Groq API key "
                    "and deployment settings."
                )

                st.write(str(e))


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Study Tutor AI · Powered by CrewAI + Groq
    </div>
    """,
    unsafe_allow_html=True,
)
```
