import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError(
        "HF_TOKEN was not found. "
        "Check your .env file."
    )


client = InferenceClient(
    token=HF_TOKEN
)


def test_huggingface():
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:fastest",
        messages=[
            {
                "role": "user",
                "content": "Say hello in one sentence."
            }
        ],
        max_tokens=50
    )

    return response.choices[0].message.content