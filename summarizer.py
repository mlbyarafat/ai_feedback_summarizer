from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="t5-small")

def summarize_text(text):
    summary = summarizer_pipeline(text, max_length=60, min_length=10, do_sample=False)
    return summary[0]['summary_text']
