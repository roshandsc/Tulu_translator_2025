from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load tokenizer and model from local directory
tokenizer = AutoTokenizer.from_pretrained("/Users/roshanshetty/Downloads/y_Training/tulu_translator_final")
model = AutoModelForSeq2SeqLM.from_pretrained("/Users/roshanshetty/Downloads/y_Training/tulu_translator_final")

# Create FastAPI instance
app = FastAPI()

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "hi"}

# Request body model
class TranslationRequest(BaseModel):
    tulu_text: str

# POST endpoint for translation
@app.post("/translate")
def translate_text(request: TranslationRequest):
    input_ids = tokenizer(request.tulu_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    translated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"translated_text": translated}

# To run server directly from this script
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)