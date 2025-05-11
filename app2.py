from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import uvicorn

# Load the saved tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("/Users/roshanshetty/Downloads/y_Training/tulu_translator_final")
model = AutoModelForSeq2SeqLM.from_pretrained("/Users/roshanshetty/Downloads/y_Training/tulu_translator_final")

# Initialize FastAPI app
app = FastAPI()

# Define request body schema
class TranslationRequest(BaseModel):
    tulu_text: str

@app.post("/translate")
def translate(request: TranslationRequest):
    """API endpoint to translate Tulu text to English"""
    input_ids = tokenizer(request.tulu_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"translated_text": translated_text}

# Entry point to run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)