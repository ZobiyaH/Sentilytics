# Sentilytics
News Sentiment Analysis Dashboard
# Real-Time News Sentiment Dashboard with Fluvio & Groq

## Overview
This project implements a real-time news sentiment dashboard that leverages **Groq** for multimodal sentiment analysis (text + audio) and **Fluvio** for streaming breaking news data. The system fetches live news articles, analyzes their sentiment (positive, negative, or neutral), and provides real-time updates as the sentiment evolves. It is designed to process both text and audio data, making it a powerful tool for analyzing news content from multiple perspectives.

## Features
- **Real-time News Streaming**: Uses Fluvio to stream live breaking news articles.
- **Multimodal Sentiment Analysis**: Analyzes both text and audio content of news using Groq.
- **Responsive User Interface**: The dashboard dynamically updates the news and sentiment analysis with a clean and modern user interface.
- **Visual Sentiment Indicators**: Displays sentiment as color-coded labels (green for positive, red for negative, and yellow for neutral).
- **Multimedia Integration**: Processes news articles with both textual and audio components to deliver a more comprehensive sentiment analysis.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, TailwindCSS
- **Backend**: Flask (Python)
- **Sentiment Analysis**: Groq (for multimodal analysis of text and audio)
- **News Streaming**: Fluvio (for real-time news data streaming)
- **Real-time Updates**: JavaScript and Fetch API for periodic updates

## Project Architecture
The project is divided into three main parts:
1. **Frontend**: Displays the sentiment dashboard and updates the content dynamically based on real-time data.
2. **Backend**: Flask server fetches news data, performs sentiment analysis using Groq, and serves the results via a RESTful API.
3. **Streaming & Analysis**: Fluvio is used for real-time news streaming, while Groq processes both text and audio components for sentiment analysis.

## Setup & Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask (Backend)
- Fluvio (for news streaming)
- Groq (for sentiment analysis)

### Clone the Repository
Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <project-directory>

Install Fluvio and Groq
Follow the official documentation to install Fluvio and Groq

Ensure both are set up and running correctly.

Running the Project
Start the Flask Backend: Run the Flask app to start the backend server:


Run the Frontend:

Open the index.html file in your browser to view the dashboard.

If you are running a local server, you can use a tool like Python's HTTP server or a code editor extension (e.g., VS Code's Live Server) to view the page.

Streaming and Sentiment Analysis:

The backend will interact with Fluvio to stream real-time news and use Groq for sentiment analysis.

The frontend will update the news sentiment dynamically every few seconds.

API Endpoints
The Flask backend provides an API endpoint to fetch the sentiment data:


GET http://127.0.0.1:7800/sentiment
This endpoint returns a JSON array of news articles with sentiment analysis:


[
  {
    "headline": "Breaking News: Market Crash",
    "category": "Finance",
    "sentiment": "Negative",
    "description": "The stock market has crashed due to unforeseen economic events.",
    "source": "Financial News"
  },
  {
    "headline": "Tech Industry Soars Amidst Pandemic",
    "category": "Technology",
    "sentiment": "Positive",
    "description": "The tech sector is thriving even as other industries struggle.",
    "source": "Tech Insider"
  }
]

License
This project is open-source and available under the MIT License.

Contributing
Feel free to contribute to this project by forking the repository and submitting pull requests. Please follow these steps:

Fork the repository.

Create a new branch for your feature or fix.

Make your changes and test them.

Submit a pull request with a clear description of your changes.

Contact
For inquiries or more information about the project, please reach out:

Email: hussainzobiya27@gmail.com

GitHub: @ZobiyaH

