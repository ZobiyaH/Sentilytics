import requests

GROQ_API_KEY = "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"

# Function to get sentiment
def get_sentiment(text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",  # Change to Llama 3.1 8B
        "messages": [
            {
                "role": "system",
                "content": "You are a sentiment analysis model. Return only one of: 'Positive', 'Negative', or 'Neutral'."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return "Error"
