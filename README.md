# 🎓 LectureMind AI

LectureMind AI is an AI-powered learning assistant that transforms lecture audio into meaningful study resources. It uses **OpenAI Whisper** for speech-to-text transcription and **Google Gemini AI** for generating structured study notes, quizzes, flashcards, and answering questions from lecture content.

---

## 🚀 Features

### 🎤 Audio-to-Text Transcription

* Upload lecture recordings in MP3, WAV, or M4A format.
* Convert spoken lectures into accurate text transcripts using Whisper AI.

### 📚 AI-Generated Study Notes

* Automatically generate structured and concise study notes from lecture transcripts.
* Helps students quickly revise key concepts.

### 📝 Quiz Generation

* Create AI-generated multiple-choice questions (MCQs) from lecture content.
* Useful for self-assessment and exam preparation.

### 🎴 Flashcard Generation

* Generate interactive flashcards for quick revision.
* Improves concept retention and active recall.

### 💬 Lecture Q&A Assistant

* Ask questions related to the uploaded lecture.
* Receive AI-generated answers based on lecture content.

### 🎨 Interactive User Interface

* Built using Streamlit.
* Clean, responsive, and student-friendly interface.

---

## 🛠️ Tech Stack

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| Python            | Backend Development          |
| Streamlit         | User Interface               |
| OpenAI Whisper    | Speech-to-Text Transcription |
| Google Gemini API | Generative AI Features       |
| FFmpeg            | Audio Processing             |

---

## 📂 Project Structure

```text
LectureMind-AI/
│
├── app.py
│
├── utils/
│   ├── transcribe.py
│   └── gemini_utils.py
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/lecturemind-ai.git

cd lecturemind-ai
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://aistudio.google.com/app/apikey

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

```text
Lecture Audio
      │
      ▼
OpenAI Whisper
(Speech-to-Text)
      │
      ▼
Transcript
      │
      ▼
Google Gemini AI
      │
 ┌────┼────┬─────┐
 ▼    ▼    ▼     ▼
Notes Quiz Flashcards Q&A
```

---

## 🎯 Use Cases

* Students preparing for exams
* Online learning platforms
* Educational institutions
* Lecture revision and note-taking
* Self-learning and knowledge retention

---

## 📸 Application Workflow

1. Upload lecture audio.
2. Generate transcript.
3. Generate study notes.
4. Create quizzes.
5. Generate flashcards.
6. Ask questions related to lecture content.

---

## 🔮 Future Enhancements

* PDF Export
* Download Notes Feature
* Multi-Lecture Support
* Retrieval-Augmented Generation (RAG)
* Vector Database Integration (FAISS)
* Chat History
* Learning Analytics Dashboard

---

## 👩‍💻 Author

**Shivali Gupta**
M.Sc. Data Science Student, IIIT Lucknow

---

## ⭐ Acknowledgements

* OpenAI Whisper
* Google Gemini API
* Streamlit Community

---

### 🌟 Transform Lectures into Smart Learning Resources with LectureMind AI! 🚀
