import speech_recognition as sr
from gtts import gTTS
import streamlit as st
import os
import tempfile
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import unicodedata

# --------------------------
# Load your translation model
# --------------------------
# Ensure the correct path for your model directory (replace with your local or hosted path)
model_path = "/Users/roshanshetty/Downloads/y_Training/tulu_translator_final"  # Change this to your actual model path
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# --------------------------
# Function to translate using your custom model
# --------------------------
def translate_with_custom_model(text):
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        outputs = model.generate(**inputs)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        st.write(f"Error during translation: {str(e)}")
        return None

# --------------------------
# Speak using Google TTS
# --------------------------
def speak(text, language_code='en'):
    try:
        tts = gTTS(text=text, lang=language_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            audio_bytes = open(tmpfile.name, 'rb').read()
            st.audio(audio_bytes, format='audio.mp3')
    except Exception as e:
        st.write(f"Error during speech synthesis: {str(e)}")

# --------------------------
# Speech Recognition
# --------------------------
def recognize_speech():
    try:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            st.write("🎧 Listening for Tulu speech...")
            audio = recognizer.listen(source)
        command = recognizer.recognize_google(audio)
        st.write(f"🗣️ Recognized speech: {command}")
        return command.lower().strip()
    except sr.UnknownValueError:
        st.write("😕 Sorry, I couldn't understand the speech.")
        return None
    except sr.RequestError:
        st.write("⚠️ Sorry, there was an issue with the speech recognition service.")
        return None
    except Exception as e:
        st.write(f"Error during speech recognition: {str(e)}")
        return None

# --------------------------
# Streamlit UI
# --------------------------
st.title("🎙️ Tulu Speech-to-English Translator")
st.write("Speak in Tulu and this app will translate it to English using your custom AI model.")

command = recognize_speech()

if command:
    response = translate_with_custom_model(command)
    if response:
        st.write(f"🌐 Translated (to English): {response}")
        speak(response, language_code='en')
    else:
        st.write("Translation failed.")