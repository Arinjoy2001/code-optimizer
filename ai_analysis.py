from transformers import pipeline

# Load the model
code_analysis_model = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

def analyze_code_with_ai(code_snippet):
    """
    Use an AI model to analyze the code for bottlenecks and suggest optimizations.
    """
    prompt = f"Analyze the following Python code for performance issues and suggest optimizations:\n\n{code_snippet}"
    response = code_analysis_model(
        prompt,
        max_new_tokens=200,  # Specify only the number of new tokens to generate
        num_return_sequences=1
    )
    suggestions = response[0]["generated_text"]
    return {"ai_suggestions": suggestions}
