import os

os.environ["PATH"] += os.pathsep + r"D:\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

import streamlit as st
import whisper

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

model = load_whisper()

def transcribe_audio(audio_path):

    result = model.transcribe(
    audio_path,
    language="en"
)

    print(result)

    return result["text"]
