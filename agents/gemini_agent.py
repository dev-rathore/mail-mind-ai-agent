import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def is_email_important(subject: str, body: str) -> bool:
    prompt = f"""
You are an AI assistant. Analyze the following email and say if it's important or not.

Subject: {subject}
Body: {body}

Reply only with 'Yes' if important, otherwise 'No'.
"""
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip().lower().startswith("yes")
