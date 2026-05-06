from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

summarizer = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

def generate_description(text):
    prompt = f"summarize: {text}"
    
    result = summarizer(
        prompt,
        max_length=120,
        do_sample=False
    )

    return result[0]["generated_text"]