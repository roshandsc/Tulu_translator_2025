import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the saved tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("/Users/roshanshetty/Downloads/y_Training/tulu_translator_final")
model = AutoModelForSeq2SeqLM.from_pretrained("/Users/roshanshetty/Downloads/y_Training/tulu_translator_final")

def translate_tulu_to_english(tulu_text):
  """Translates Tulu text to English using the fine-tuned model.

  Args:
    tulu_text: The Tulu text to translate.

  Returns:
    The translated English text.
  """
  input_ids = tokenizer(tulu_text, return_tensors="pt").input_ids
  outputs = model.generate(input_ids)
  translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
  return translated_text

gr.Interface(
    fn=translate_tulu_to_english,
    inputs=gr.Textbox(label="Tulu"),
    outputs=gr.Textbox(label="English"),
    examples=[["Namaskara"], ["Yencha Ullar?"]]
).launch()