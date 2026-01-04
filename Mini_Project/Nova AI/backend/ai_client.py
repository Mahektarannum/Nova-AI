import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Create Groq client
client = Groq(api_key=API_KEY)


def get_ai_response(user_message: str) -> str:
    if not user_message.strip():
        return "Say something 🙂"

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Nova AI, a smart, concise, and helpful assistant. "
                        "Answer clearly and practically. Avoid unnecessary verbosity."
                    )
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.6,
            max_tokens=512
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error talking to AI: {str(e)}"
