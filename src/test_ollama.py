import ollama

response = ollama.chat(
    model="mistral",
    messages=[
        {
            "role": "user",
            "content": "Summarize this in two sentences: Python is widely used in machine learning, web development, and automation."
        }
    ]
)

print(response["message"]["content"])