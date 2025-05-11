

## Tulu Speech-to-English Translator

A simple, end-to-end Tulu speech-to-English translation application powered by a custom AI model. This project provides:

- A **Streamlit app** for real-time speech-to-text and translation
- A **Gradio interface** for text-based translation
- A **FastAPI backend** for programmatic translation via API

---

## Features

- 🎙️ **Speech Recognition**: Speak in Tulu, get English translation instantly
- 🌐 **Custom AI Model**: Uses a fine-tuned M2M100 transformer for Tulu-to-English translation
- 🗣️ **Text-to-Speech**: Listen to translated English output
- 🖥️ **Web UI**: Streamlit and Gradio interfaces for interactive use
- ⚡ **REST API**: FastAPI endpoint for integration

---

## Quick Start

### 1. Requirements

- Python 3.8+
- [transformers](https://huggingface.co/transformers/)
- torch
- streamlit
- gradio
- fastapi
- uvicorn
- speechrecognition
- gtts

Install dependencies:

```bash
pip install torch transformers streamlit gradio fastapi uvicorn speechrecognition gtts
```


---

### 2. Model Setup

Place your fine-tuned model files in a directory, e.g., `/path/to/tulu_translator_final`.

---

### 3. Streamlit Speech Translator

Run the Streamlit app for speech-to-English translation:

```bash
streamlit run app.py
```

- Speak in Tulu, see and hear the English translation in your browser[^2].

---

### 4. Gradio Text Translator

Run the Gradio demo for text input:

```bash
python app1.py
```

- Enter Tulu text, receive English translation in the browser[^3].

---

### 5. FastAPI Translation API

Run the FastAPI server:

```bash
uvicorn app2:app --reload
```


#### API Usage

- **POST** `/translate`
- **Body**: `{ "tulu_text": "your Tulu sentence" }`
- **Response**: `{ "translated_text": "English translation" }`[^4].

---

## Example Usage

### Gradio

```python
import gradio as gr

gr.Interface(
    fn=translate_tulu_to_english,
    inputs=gr.Textbox(label="Tulu"),
    outputs=gr.Textbox(label="English"),
    examples=[["Namaskara"], ["Yencha Ullar?"]]
).launch()
```


### FastAPI

```python
import requests

response = requests.post(
    "http://localhost:8000/translate",
    json={"tulu_text": "Namaskara"}
)
print(response.json())
```


---

## Model Details

- **Architecture**: M2M100ForConditionalGeneration (transformers v4.51.3)[^5][^6]
- **Supported Languages**: Extensive language code support (see `special_tokens_map.json` and `added_tokens.json` for details)[^8][^1]
- **Tokenizer and Model**: Loaded from local directory

---

## File Structure

| File | Purpose |
| :-- | :-- |
| app.py | Streamlit speech-to-English app |
| app1.py | Gradio text-to-English demo |
| app2.py | FastAPI translation API |
| main.py | Alternate FastAPI implementation |
| config.json | Model architecture/config |
| tokenizer_config.json, special_tokens_map.json, added_tokens.json | Tokenizer and language codes |


---

## Credits

- Built with [Hugging Face Transformers](https://huggingface.co/transformers/)
- Speech recognition via [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- Text-to-speech via [gTTS](https://pypi.org/project/gTTS/)
- Web UIs via [Streamlit](https://streamlit.io/) and [Gradio](https://gradio.app/)

---

## License

MIT License

---

## Acknowledgements

This project leverages open-source tools and multilingual transformer models to make Tulu language technology accessible.

---

**Note:**
Replace all model paths (`/Users/roshanshetty/Downloads/y_Training/tulu_translator_final`) with your actual model directory as needed[^2][^3][^4][^7].

