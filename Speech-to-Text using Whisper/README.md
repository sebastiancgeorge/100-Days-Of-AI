# 🎙️ Day 4 – Speech Recognition with Whisper (Offline Speech-to-Text)

Welcome to **Day 4** of my **#100DaysOfAI** challenge!  
Today I explored **Whisper**, a powerful speech recognition model developed by OpenAI that works **offline**, and converts spoken audio into text.

---

## 🎯 Goal

Transcribe a `.wav` audio file into readable text using Whisper locally.

---

## 🧰 Tech Stack

| Tool       | Purpose                                |
|------------|----------------------------------------|
| Python     | Core programming language              |
| Whisper    | AI model for speech recognition        |
| PyTorch    | Backend for Whisper model              |
| ffmpeg     | For audio compatibility & conversion   |
| VS Code    | Editor                                 |

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install git+https://github.com/openai/whisper.git
pip install torch
