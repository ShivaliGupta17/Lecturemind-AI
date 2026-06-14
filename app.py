import streamlit as st

from utils.transcribe import transcribe_audio

from utils.gemini_utils import (
    generate_notes,
    generate_quiz,
    generate_flashcards,
    ask_question
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="LectureMind AI ",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-weight: bold;
}

h1 {
    color: #2563eb;
}

.stTextArea textarea {
    border-radius: 10px;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    """
    <h1 style='text-align:center;'>
        🎓 LectureMind AI
    </h1>

    <p style='text-align:center; font-size:18px; color:gray;'>
        Convert Lecture Audio → Transcript → Notes → Quiz → Flashcards
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("📚 Project Info")

    st.info(
        """
        AI Lecture Assistant

        ✅ Speech To Text

        ✅ Notes Generator

        ✅ Quiz Generator

        ✅ Flashcards Generator

        ✅ Q&A Assistant
        """
    )

# ---------------- FILE UPLOAD ----------------

audio_file = st.file_uploader(
    "🎤 Upload Lecture Audio",
    type=["mp3", "wav", "m4a"]
)

# ---------------- STATUS CARDS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🎤 Audio",
        "Uploaded" if audio_file else "Pending"
    )

with col2:
    st.metric(
        "📝 Transcript",
        "Ready" if "transcript" in st.session_state else "Pending"
    )

with col3:
    st.metric(
        "📚 Notes",
        "Ready" if "notes" in st.session_state else "Pending"
    )

# ---------------- MAIN APP ----------------

if audio_file:

    with open("lecture.wav", "wb") as f:
        f.write(audio_file.read())

    st.success("✅ Audio Uploaded Successfully")

    # Transcript Button

    if st.button("📝 Generate Transcript"):

        with st.spinner("Generating Transcript..."):

            transcript = transcribe_audio(
                "lecture.wav"
            )

            st.session_state["transcript"] = transcript

    # Show Transcript

    if "transcript" in st.session_state:

        st.subheader("📝 Transcript")

        st.text_area(
            "Transcript Output",
            st.session_state["transcript"],
            height=250
        )

        st.divider()

        # TABS

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📚 Notes",
                "📝 Quiz",
                "🎴 Flashcards",
                "💬 Q&A"
            ]
        )

        # ---------------- NOTES ----------------

        with tab1:

            if st.button("📚 Generate Notes"):

                with st.spinner("Generating Notes..."):

                    notes = generate_notes(
                        st.session_state["transcript"]
                    )

                    st.session_state["notes"] = notes

            if "notes" in st.session_state:

                st.subheader("📚 Study Notes")

                st.write(
                    st.session_state["notes"]
                )

        # ---------------- QUIZ ----------------

        with tab2:

            if st.button("📝 Generate Quiz"):

                with st.spinner("Generating Quiz..."):

                    quiz = generate_quiz(
                        st.session_state["transcript"]
                    )

                    st.session_state["quiz"] = quiz

            if "quiz" in st.session_state:

                st.subheader("📝 Quiz")

                st.write(
                    st.session_state["quiz"]
                )

        # ---------------- FLASHCARDS ----------------

        with tab3:

            if st.button("🎴 Generate Flashcards"):

                with st.spinner("Generating Flashcards..."):

                    flashcards = generate_flashcards(
                        st.session_state["transcript"]
                    )

                    st.session_state["flashcards"] = flashcards

            if "flashcards" in st.session_state:

                st.subheader("🎴 Flashcards")

                st.write(
                    st.session_state["flashcards"]
                )

        # ---------------- Q&A ----------------

        with tab4:

            question = st.text_input(
                "Ask anything from the lecture"
            )

            if st.button("🤖 Ask"):

                if question.strip():

                    with st.spinner("Generating Answer..."):

                        answer = ask_question(
                            st.session_state["transcript"],
                            question
                        )

                        st.session_state["answer"] = answer

            if "answer" in st.session_state:

                st.subheader("🤖 Answer")

                st.write(
                    st.session_state["answer"]
                )