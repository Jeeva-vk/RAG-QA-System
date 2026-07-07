import google.generativeai as genai

import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_answer(
    question,
    context
):

    prompt = f"""
You are an organization assistant.

Answer ONLY from the context.

If information is not present,
reply:

Information not available in dataset.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text