import ollama

def review_email(email):
    prompt = f"""
You are a professional email reviewer.

Review the email below and improve it by:
- Correcting grammar
- Improving clarity
- Making it more professional
- Keeping the original meaning

Return only the improved email.

Email:
{email}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]