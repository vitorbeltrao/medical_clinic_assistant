import os
from openai import OpenAI
from dotenv import load_dotenv

def chat_iteration(messages, model):
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=model, 
        messages=messages
    )

    return response.choices[0].message.content
