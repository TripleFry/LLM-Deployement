import os

import requests

BASE_URL = os.environ.get("LLM_API_URL", "http://127.0.0.1:8000")

PROMPTS = [
    "What is artificial intelligence?",
    "Explain machine learning in simple words.",
    "What is a neural network?",
    "Explain the Transformer model.",
    "What is natural language processing?",
]


def main() -> None:
    for index, prompt in enumerate(PROMPTS, start=1):
        response = requests.post(
            f"{BASE_URL}/generate",
            json={"prompt": prompt},
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        print(f"{index}. Prompt: {prompt}")
        print(f"   Response: {data['response']}")
        print()


if __name__ == "__main__":
    main()
