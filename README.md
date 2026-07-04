# 🎤 Voice-Based Concept Understanding Analyser (VBCUA)

> An AI-powered Streamlit application that converts spoken explanations into text and assists in evaluating conceptual understanding.

---

# 📌 Project Overview

The **Voice-Based Concept Understanding Analyser (VBCUA)** is an AI-powered educational application developed as part of the **SmartBridge Skill Wallet Program**.

The application enables users to upload a voice recording explaining a concept. It converts the speech into text using **OpenAI Whisper** and displays the transcript through an interactive Streamlit interface. The project also includes modules for scoring, filler word detection, reporting, and database integration, providing a foundation for concept understanding analysis.

---

# 🚀 Features

- 🎤 Upload WAV audio files
- 🗣️ Speech-to-Text transcription using OpenAI Whisper
- 📚 Select reference concepts from a predefined knowledge base
- 📝 Display generated transcript
- 📊 Modular scoring engine
- 💬 Filler word detection module
- 📁 Database support
- 📈 Interactive Streamlit interface

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application Framework |
| OpenAI Whisper | Speech-to-Text |
| FFmpeg | Audio Processing |
| JSON | Reference Concepts |
| SQLite | Database Support |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```
Voice-Based-Concept-Understanding-Analyser/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets/
├── database/
├── modules/
│   ├── audio_utils.py
│   ├── database.py
│   ├── filler_detector.py
│   ├── report_engine.py
│   ├── scoring_engine.py
│   └── speech_to_text.py
│
├── reference_concepts/
│   └── concepts.json
│
├── screenshots/
└── uploads/
```

---

# ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shahina07/Voice-Based-Concept-Understanding-Analyser.git
```

### 2. Navigate to the Project Directory

```bash
cd Voice-Based-Concept-Understanding-Analyser
```

### 3. Create a Virtual Environment (Optional)

```bash
conda create -n vbcu_env python=3.10
conda activate vbcu_env
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

# 🔄 Application Workflow

```
Upload WAV Audio
        │
        ▼
Speech-to-Text using Whisper
        │
        ▼
Generate Transcript
        │
        ▼
Display Transcript
```

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Audio Upload
- Transcript Output

Store them inside the `screenshots` folder.

---

# 🎯 Future Enhancements

- Semantic similarity analysis
- Concept understanding score generation
- PDF report generation
- Support for MP3 and MP4 audio
- Live microphone recording
- AI-generated feedback
- Multilingual speech support

---

# 👨‍💻 Team Members

### Team Lead

- Shahina

### Team Members

- Somudala Niharika
- Hari Kumar Saladhi
- Shaik Karishma

---

# 📜 License

This project was developed for educational purposes as part of the **SmartBridge Skill Wallet Program**.

---

# 👩‍💻 Developed By

**Shahina**

B.Tech (2023–2027)

Raghu Engineering College

GitHub: https://github.com/Shahina07

---

# 🎥 Demo Video

The project demonstration video can be viewed using the link below:

**Demo Video:**  
https://drive.google.com/file/d/1Ug_BGCBkhB4x_rIiVg7mSKCJL8kRoasR/view?usp=drive_link

---