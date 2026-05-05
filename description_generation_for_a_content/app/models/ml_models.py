import whisper
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# ---------- Whisper Model ----------
whisper_model = whisper.load_model("base")


# ---------- FLAN-T5 Model ----------
model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

summarizer = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)