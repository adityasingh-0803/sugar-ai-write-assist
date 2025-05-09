from transformers import pipeline

suggestion_pipe = pipeline("text-generation", model="distilgpt2")

def suggest_next_sentence(prompt):
    result = suggestion_pipe(prompt, max_length=50, num_return_sequences=1)
    suggestion = result[0]['generated_text'][len(prompt):].strip()
    return suggestion.split(".")[0] + "."
