import requests
from flask import Flask, jsonify
import time

# Your News API Key
API_KEY = 'b7f262aaa2aa474381e86133f4879a44'
NEWSAPI_URL = "https://newsapi.org/v2/top-headlines"

categories = ['business', 'technology', 'sports', 'health', 'science', 'entertainment']

app = Flask(__name__)

# Function to fetch real-time news
def fetch_news():
    all_news = []
    for category in categories:
        params = {
            'category': category,
            'language': 'en',
            'pageSize': 5,
            'apiKey': API_KEY
        }
        
        response = requests.get(NEWSAPI_URL, params=params)
        news = response.json()
        
        if news.get('status') == 'ok' and 'articles' in news:
            for article in news['articles']:
                headline = article.get('title')
                description = article.get('description')
                all_news.append({
                    'headline': headline,
                    'category': category
                })
    return all_news

@app.route('/fetch_and_send_news')
def fetch_and_send_news():
    news = fetch_news()

    # Send news to the sentiment analysis server
    sentiment_analysis_url = "http://127.0.0.1:7800/news"  # Replace with your actual server URL
    response = requests.post(sentiment_analysis_url, json=news)
    
    if response.status_code == 200:
        enriched_news = response.json()
        return jsonify(enriched_news)
    else:
        return jsonify({"error": "Failed to analyze sentiment"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7900)  # Running on port 6300 for the producer

