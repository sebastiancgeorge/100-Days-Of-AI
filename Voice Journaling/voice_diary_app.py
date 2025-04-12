import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

model = whisper.load_model("base")

# Audio settings
SAMPLE_RATE = 44100
DURATION = 10  # seconds

def record_audio():
    status_label.config(text="Recording...")
    app.update()
    recording = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write("temp.wav", SAMPLE_RATE, recording)
    status_label.config(text="Recording complete ✅")

def transcribe_audio():
    status_label.config(text="Transcribing...")
    app.update()
    result = model.transcribe("temp.wav")
    transcription = result["text"]
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, transcription)
    save_transcript(transcription)
    status_label.config(text="Transcription done & saved 📝")

def save_transcript(text):
    os.makedirs("diary", exist_ok=True)
    filename = datetime.now().strftime("diary/%Y-%m-%d.txt")
    with open(filename, "w") as f:
        f.write(text)

# GUI setup
app = tk.Tk()
app.title("Voice Diary – Whisper AI")
app.geometry("500x400")

record_btn = tk.Button(app, text="🎙️ Record Voice", command=record_audio, font=("Helvetica", 14))
record_btn.pack(pady=10)

transcribe_btn = tk.Button(app, text="📝 Transcribe & Save", command=transcribe_audio, font=("Helvetica", 14))
transcribe_btn.pack(pady=10)

text_box = tk.Text(app, height=10, width=60, wrap="word")
text_box.pack(pady=10)

status_label = tk.Label(app, text="", font=("Helvetica", 10), fg="green")
status_label.pack()

app.mainloop()
