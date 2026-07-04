import whisper

# Load Whisper model
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Convert speech to text using OpenAI Whisper.
    """
    result = model.transcribe(audio_path)
    return result["text"]