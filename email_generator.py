import ollama

def load_knowledge():
    with open("knowledge/company_policy.txt", "r") as file:
        return file.read()

def detect_email_type(purpose):
    prompt = f"""
    Classify this email into ONE category only:

    - Leave Request
    - Job Application
    - Complaint
    - Meeting Request
    - Thank You
    - General

    Purpose:
    {purpose}

    Return only the category name.
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()


def generate_email(subject, purpose, tone):
    knowledge = load_knowledge()

    email_type = detect_email_type(purpose)

    prompt = f"""
You are an intelligent AI Email Assistant.

Company Guidelines:
{knowledge}

Detected Email Type:
{email_type}

Subject:
{subject}

Purpose:
{purpose}

Tone:
{tone}

Write a professional email.
Return only the email body.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return email_type,response["message"]["content"]