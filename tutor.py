from google import genai
import os

api_key = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)
while True:
    question=input("ask: ")
    if(question==exit):
        break
    prompt = f"""
    You are an AI C programming tutor.

    The student is a beginner.

    Explain concepts step by step.

    Student question:
    {question}
    """
    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt)
    print(response.text)