import streamlit as st

from agent import StudyTutor
from memory import (
    initialize_memory,
    get_conversation_history,
    add_message,
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

    /* ---------- Main background ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 20% 10%,
                rgba(0, 140, 255, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 85% 20%,
                rgba(0, 229, 255, 0.08),
                transparent 25%
            ),
            #070B14;
        color: #F5F7FA;
    }


    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"] {
        background: #0B1120;
        border-right: 1px solid rgba(0, 183, 255, 0.18);
    }


    /* ---------- Main content ---------- */

    .main-title {
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin-bottom: 5px;

        background: linear-gradient(
            90deg,
            #FFFFFF,
            #53C8FF,
            #00E5FF
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    .subtitle {
        color: #94A3B8;
        font-size: 17px;
        margin-bottom: 30px;
    }


    /* ---------- Hero card ---------- */

    .hero-card {
        padding: 25px;
        border-radius: 18px;

        background:
            linear-gradient(
                135deg,
                rgba(0, 183, 255, 0.10),
                rgba(0, 229, 255, 0.03)
            );

        border: 1px solid rgba(0, 183, 255, 0.22);

        box-shadow:
            0 0 30px rgba(0, 183, 255, 0.06);
    }


    /* ---------- Feature cards ---------- */

    .feature-card {
        padding: 20px;
        border-radius: 16px;

        background: rgba(15, 23, 42, 0.72);

        border: 1px solid rgba(148, 163, 184, 0.10);

        min-height: 130px;
    }


    .feature-title {
        color: #53C8FF;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 7px;
    }


    .feature-text {
        color: #94A3B8;
        font-size: 14px;
    }


    /* ---------- Chat messages ---------- */

    [data-testid="stChatMessage"] {
        border-radius: 16px;
        margin-bottom: 12px;
    }


    /* ---------- Input ---------- */

    [data-testid="stChatInput"] {
        border-color: rgba(0, 183, 255, 0.35);
    }


    /* ---------- Buttons ---------- */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid rgba(0, 183, 255, 0.30);
        background: #0F172A;
        color: #E2E8F0;
    }


    .stButton > button:hover {
        border-color: #00B7FF;
        color: #53C8FF;
    }


    /* ---------- Small status badge ---------- */

    .status-badge {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 20px;

        background: rgba(0, 229, 255, 0.08);

        border: 1px solid rgba(0, 229, 255, 0.20);

        color: #53C8FF;

        font-size: 12px;
        font-weight: 600;
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
# CREATE TUTOR
# =========================================================

if "tutor" not in st.session_state:
    st.session_state.tutor = StudyTutor()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ✦ Study Tutor")

    st.markdown(
        '<span class="status-badge">● AI TUTOR ONLINE</span>',
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### Learning Settings")

    subject = st.selectbox(
        "Subject",
        [
            "General",
            "Mathematics",
            "Science",
            "Computer Science",
            "Electrical Engineering",
            "English",
        ],
    )

    level = st.selectbox(
        "Learning level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )

    st.divider()

    st.markdown("### Tutor capabilities")

    st.markdown(
        """
        **✦ Explain concepts**

        Break difficult topics into simple steps.

        **✦ Practice**

        Generate questions to test understanding.

        **✦ Calculate**

        Use a calculator when mathematics requires it.

        **✦ Study planning**

        Create simple topic-based study plans.

        **✦ Memory**

        Remember the current study conversation.
        """
    )

    st.divider()

    if st.button(
        "Clear Study Session",
        use_container_width=True,
    ):

        clear_memory()

        st.session_state.tutor = StudyTutor()

        st.rerun()


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">Study Tutor AI</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "A personal AI tutor that helps you understand, practice, "
    "and learn step by step."
    "</div>",
    unsafe_allow_html=True,
)


# =========================================================
# HERO
# =========================================================

if len(st.session_state.messages) == 0:

    st.markdown(
        """
        <div class="hero-card">

        <h3>What do you want to learn today?</h3>

        <p style="color:#94A3B8;">
        Ask a question, explore a concept, solve a problem,
        or ask the tutor to create a study plan.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")


    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
            <div class="feature-title">Explain</div>
            <div class="feature-text">
            Learn difficult concepts using simple,
            step-by-step explanations.
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
            <div class="feature-title">Practice</div>
            <div class="feature-text">
            Ask for examples, exercises,
            quizzes, and practice questions.
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
            <div class="feature-title">Understand</div>
            <div class="feature-text">
            Ask follow-up questions until
            the concept becomes clear.
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar="✦" if message["role"] == "assistant" else "👤",
    ):

        st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

prompt = st.chat_input(
    "Ask your Study Tutor anything..."
)


if prompt:

    # -------------------------
    # Display user message
    # -------------------------

    with st.chat_message(
        "user",
        avatar="👤",
    ):

        st.markdown(prompt)


    # -------------------------
    # Save user message
    # -------------------------

    add_message(
        "user",
        prompt,
    )


    # -------------------------
    # Get previous conversation
    # -------------------------

    history = get_conversation_history()


    # -------------------------
    # Run agent
    # -------------------------

    with st.chat_message(
        "assistant",
        avatar="✦",
    ):

        with st.spinner(
            "Your tutor is thinking..."
        ):

            try:

                response = st.session_state.tutor.ask(
                    question=prompt,
                    subject=subject,
                    level=level,
                    history=history,
                )

                answer = str(response)

                st.markdown(answer)

                add_message(
                    "assistant",
                    answer,
                )

            except Exception as error:

                st.error(
                    "The tutor could not complete the request."
                )

                st.caption(
                    f"Error: {error}"
                )
