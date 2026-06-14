import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_notes(text):

    prompt = f"""
    Convert the following lecture transcript
    into structured study notes.

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)

    print(response.text)

    return response.text
def generate_quiz(text):

    prompt = f"""
    Create 5 MCQ questions from this lecture.

    Transcript:
    {text}

    Format:

    Q1.
    A)
    B)
    C)
    D)

    Correct Answer:
    """

    response = model.generate_content(prompt)

    return response.text
def generate_flashcards(text):

    prompt = f"""
    Create 10 flashcards from this lecture.

    Format:

    Q: Question
    A: Answer

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text
def ask_question(transcript, question):

    prompt = f"""
    Answer ONLY from the lecture transcript.

    Transcript:
    {transcript}

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text