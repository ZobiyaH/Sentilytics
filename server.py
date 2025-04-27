from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Groq API Key (replace with your actual API key)
GROQ_API_KEY = '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'

# Function to analyze sentiment using Groq
def analyze_sentiment(text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Analyze this news headline and give sentiment: Positive, Neutral, or Negative."},
            {"role": "user", "content": text}
        ]
    }
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        if response.status_code == 200:
            sentiment = response.json()['choices'][0]['message']['content'].strip()
            return sentiment
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return "Unknown"

# Endpoint to receive news from producer and analyze sentiment
@app.route('/news', methods=['POST'])
def receive_news():
    news = request.json  # Expecting a JSON payload
    enriched_news = []

    for article in news:
        headline = article['headline']
        if headline:
            sentiment = analyze_sentiment(headline)
            enriched_news.append({
                "headline": headline,
                "category": article['category'],
                "sentiment": sentiment
            })

    return jsonify(enriched_news)

# Serve the enriched news to the frontend
@app.route('/sentiment')
def get_sentiment_news():
    
    example_news = [
        {"headline": "Tech industry sees massive growth", "category": "technology", "sentiment": "Positive"},
        {"headline": "Stock market drops due to economic slowdown", "category": "finance", "sentiment": "Negative"}
    ]
    return jsonify(example_news)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7800)  # Running on port 7300 for the sentiment analysis server

