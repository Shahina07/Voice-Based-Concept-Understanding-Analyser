from modules.speech_to_text import transcribe_audio
import streamlit as st
import json

# Page Configuration
st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

# Title
st.title("🎤 Voice-Based Concept Understanding Analyser")

st.write("Welcome to the SmartBridge Skill Wallet Project!")

# Load Reference Concepts
with open("reference_concepts/concepts.json", "r") as file:
    concepts = json.load(file)

# Select Concept
selected_concept = st.selectbox(
    "📚 Select a Reference Concept",
    list(concepts.keys())
)

# Show Reference Concept
st.subheader("📖 Reference Concept")
st.info(concepts[selected_concept])

st.markdown("---")

# Upload Audio
uploaded_file = st.file_uploader(
    "🎤 Upload a WAV Audio File",
    type=["wav"]
)

# Play Audio
if uploaded_file is not None:
    st.audio(uploaded_file)

st.markdown("---")

# Analyze Button
if st.button("🚀 Analyze"):

    if uploaded_file is None:
        st.warning("Please upload an audio file.")

    else:
        # Save uploaded audio
        audio_path = f"uploads/{uploaded_file.name}"

        with open(audio_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Convert Speech to Text
        transcript = transcribe_audio(audio_path)

        # Display Transcript
        st.subheader("📝 Transcript")
        st.write(transcript)

st.markdown("---")

st.subheader("📊 Results")