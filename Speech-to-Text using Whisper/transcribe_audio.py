import whisper

# Load the base model (can be replaced with 'small', 'medium', or 'large')
model = whisper.load_model("base")

# Load and transcribe the audio
result = model.transcribe("audio.wav")

# Print result
print("\n🔊 Transcription:\n")
print(result["text"])

# Optionally save to a text file
with open("transcript.txt", "w") as f:
    f.write(result["text"])
