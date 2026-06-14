import os

os.environ["PATH"] += os.pathsep + r"D:\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

import whisper

print("Loading model...")
model = whisper.load_model("base")
print("Model loaded")

def transcribe_audio(audio_path):

    result = model.transcribe(
    audio_path,
    language="en"
)

    print(result)

    return result["text"]