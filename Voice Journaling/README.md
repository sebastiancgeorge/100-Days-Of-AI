# 🗒️ Day 5 – AI-Powered Voice Diary (Whisper + Tkinter)

Welcome to **Day 5** of my **#100DaysOfAI** challenge!  
Today, I built a simple **Voice Diary App** that lets you record voice notes, transcribe them offline using **Whisper**, and save them as text files — all in a clean desktop GUI.

---

## 🎯 Goal

Turn your daily voice thoughts into text using Whisper’s offline speech recognition, and save them as diary entries.

---

## 🧰 Technologies Used

| Tool             | Purpose                                |
|------------------|----------------------------------------|
| Python           | Main programming language              |
| OpenAI Whisper   | Offline speech-to-text model           |
| Tkinter          | GUI framework for desktop apps         |
| sounddevice      | Record audio via microphone            |
| scipy.io.wavfile | Save raw audio as `.wav`               |
| datetime         | Timestamp for diary file naming        |

---

## 🚀 Setup Instructions

### 1. Install Python Packages

```bash
pip install git+https://github.com/openai/whisper.git
pip install torch sounddevice scipy
