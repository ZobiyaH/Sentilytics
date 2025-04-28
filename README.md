
# 🚀 Sentilytics
News Sentiment Analysis Dashboard
Real-Time News Sentiment Dashboard with Fluvio & Gro

> Empowering Real-Time Insights, One Headline at a Time: Transforming News into Actionable Sentiment.

---

## 📌 Problem Statement

Select the problem statement number and title from the official list given in Participant Manual.

  
**Problem Statement 3 – Real Time Data Experiences with Fluvio**

---

## 🎯 Objective

**Real-Time Sentiment Analysis:**
With this tool, users can quickly analyze the sentiment behind any news headline, helping them understand public perception and reactions in real-time. This is useful for:

Journalists looking for quick sentiment insights on breaking news.
Business Analysts who want to gauge market sentiments based on financial news.
Marketing Teams monitoring public opinion on brand or product-related news.
Tracking News Trends:
By providing sentiment analysis for various categories of news, users can track how the mood shifts over time, identifying emerging trends and patterns. This can help users to:

Researchers studying societal reactions or political climates.
Investors keeping an eye on market sentiment and the potential impact of news on stock prices.
Improved Decision-Making:
With the ability to understand public sentiment, individuals and organizations can make more informed decisions. Whether it’s about a potential business venture or an investment decision, sentiment analysis helps in:

Investors understanding market movements based on news.
Leaders in political or organizational environments gauging public opinion.
Content Creation:
Content creators and marketers can use sentiment analysis to guide the creation of engaging content. By understanding the mood around specific topics, they can tailor their content to resonate better with the audience.

How It Makes Existing Tasks Easier:
Instant Access to Sentiment Insights:
Traditional sentiment analysis might require complex tools or hours of work. With this tool, users get instant sentiment scores for news headlines, which saves time and allows for faster decision-making.

Automated News Monitoring:
Instead of manually tracking news articles and analyzing their tone, this system automates the entire process. 
 ---

## 🧠 Team & Approach

### Team Name:  
The DigiCrusaders

### Team Members:  
- Zobiya Hussain ([GitHub](https://github.com/ZobiyaH))  
- Mohammad Shees ([GitHub](https://github.com/mshees01))
- Nawaz Hussain Khan
- Tanupriya Dutta  


### Your Approach:  
- Why you chose this problem
In today’s information-driven world, the speed and sentiment of news greatly influence public opinion, markets, and decision-making. However, real-time sentiment analysis across both text and audio streams is still rare, especially with the growing volume of breaking news.
We chose this problem because it combines multimodal AI and real-time streaming — two frontiers where Groq and Fluvio technologies can create massive impact.
Our goal was to build a dashboard that empowers users with instant emotional context behind news, not just headlines.

- Key challenges you addressed
Multimodal Processing: Combining text and audio sentiment into a unified score for a better understanding of news emotions.
Real-Time Streaming: Ensuring low-latency ingestion, processing, and dashboard updates using Fluvio for seamless streaming.
Efficient Model Inference: Optimizing models to run efficiently and in real-time using Groq’s hardware acceleration capabilities.
Data Noise: Handling noisy or incomplete news streams while still extracting meaningful sentiment.
Frontend Scalability: Designing a dashboard UI that could handle rapid updates without lag or clutter.

- Any pivots, brainstorms, or breakthroughs during hacking
Pivot to Audio: Initially, we focused only on text, but mid-hackathon brainstorming made us realize that breaking news often comes via audio/video too (like press releases or interviews), so we expanded to multimodal sentiment.
Lightweight Models: A major breakthrough was realizing that smaller, Groq-optimized models could outperform bulkier standard models for real-time processing without losing much accuracy.
Dynamic UI: Early tests showed that traditional dashboards got overwhelmed with rapid updates. We pivoted to a card-based UI with smooth animations to maintain user clarity even during high news volumes

---

## 🛠️ Tech Stack

### Core Technologies Used:
- Frontend: HTML, CSS, JAVASCRIPT, Dynamic dashboard updates using fetch API
- Backend: Flask (Python web framework), Custom API endpoints for serving enriched news data, Integrated with **Fluvio client ** to consume real-time news streams, **Groq ** inference integration for multimodal (text + audio) sentiment analysis
- Database: PHP, Real-time data fetched directly from Fluvio streams and processed in-memory
- APIs: /sentiment — Fetches live sentiment-analyzed news data for frontend consumption
- Hosting:Locally via Flask development server (localhost) during hackatho

### Sponsor Technologies Used (if any):
- [✅] **Groq:** Groq accelerated the real-time text and audio sentiment analysis pipeline, enabling fast, accurate insights for news events.  
- [ ] **Monad:** _Your blockchain implementation_  
- [✅] **Fluvio:** Fluvio handled the real-time streaming of news data, ensuring instant delivery to the sentiment analysis pipeline and live dashboard updates.  
- [ ] **Base:** _AgentKit / OnchainKit / Smart Wallet usage_  
- [ ] **Screenpipe:** _Screen-based analytics or workflows_  
- [ ] **Stellar:** _Payments, identity, or token usage_
*(Mark with ✅ if completed)*
---

## ✨ Key Features

Highlight the most important features of your project:

- ✅ Real-Time News Streaming: Instantly fetch and process live news data using Fluvio.
- ✅ High-Speed Inference with Groq: Achieve ultra-fast model inference for real-time sentiment updates.
- ✅ Sentiment Analysis: Analyze both text and audio from news sources for deeper insights with Groq. 
- ✅ Multimodal Sentiment Analysis: Analyze both text and audio from news sources for deeper insights with Groq. 


![logo](https://github.com/user-attachments/assets/4800dc07-ade3-416f-8bf4-8ba3ec24a1d5)
<img width="959" alt="dashboard img" src="https://github.com/user-attachments/assets/e12fcf3c-df0e-47f4-894a-f4243c2ac75c" />
<img width="954" alt="index img" src="https://github.com/user-attachments/assets/8691d3fb-f075-485c-ba99-08fed2e64e25" />
![login img](https://github.com/user-attachments/assets/b962e493-441a-48b6-be75-8afc4359d0f6)



---

## 📽️ Demo & Deliverables

- **Demo Video Link:** [https://www.loom.com/share/69db1119aec44f8e8108f0e287462b7e?sid=9098742e-0e0a-4752-bae1-f073959cbada]  
- **Pitch Deck / PPT Link:** [(https://drive.google.com/file/d/1noCovw6PqaiSwDNlSW2Zccc_BIpg99Vz/view?usp=sharing)]  

---

## ✅ Tasks & Bonus Checklist

- [✅ ] **All members of the team completed the mandatory task - Followed at least 2 of our social channels and filled the form** (Details in Participant Manual)  
- [ ✅] **All members of the team completed Bonus Task 1 - Sharing of Badges and filled the form (2 points)**  (Details in Participant Manual)
- [✅ ] **All members of the team completed Bonus Task 2 - Signing up for Sprint.dev and filled the form (3 points)**  (Details in Participant Manual)

*(Mark with ✅ if completed)*

---

## 🧪 How to Run the Project

### Requirements:
- Python / Flask / etc.
- API Keys (if any)
- .env file setup (if needed)

### Local Setup:
Backend/Frontend Split:

Backend:
Built with Flask.

Responsible for:
Fetching news articles (either from static JSON or streaming via Fluvio).
Analyzing news sentiment using Groq's multimodal AI (Text + Audio).
Serving processed/enriched news to the frontend through a REST API (/sentiment endpoint).

Frontend:
Built with HTML, CSS, and JavaScript.

Responsible for:
Displaying real-time news cards with sentiment tags (Positive/Negative/Neutral).
Showing a loading spinner while fetching news.
Auto-refreshing news every few seconds.

Environment Setup Notes:
Python Version: 3.8 or above recommended


File: App.py is a python file for transcribing audio file to text using openai whisper and then analyzing it using Groq api.

Install Python dependencies using pip install -r requirements.txt.

Fluvio:
Install and run Fluvio locally.
Connect your backend Flask app with Fluvio topics to consume live news data.

Groq:
Requires an API key if using cloud-based models.

**NEWS_API_KEY = 'b7f262aaa2aa474381e86133f4879a44'
GROQ_API_KEY = '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'
FLUVIO_TOPIC=news-stream**

---

## 🧬 Future Scope

List improvements, extensions, or follow-up features:

- 📈 More integrations
Integrate additional data sources like RSS feeds, Twitter, and financial news APIs.
Support video news streams with real-time transcription and sentiment analysis.
Expand Groq multimodal capabilities to handle more complex sentiment cues (e.g., sarcasm, emotion detection).

- 🛡️ Security enhancements
Implement authentication and authorization for backend APIs.
Add input validation and sanitization to handle streaming data securely.
Protect API keys and sensitive configurations using secure vaults.

- 🌐 Localization / broader accessibility
Support multilingual news articles and sentiment analysis.
Build accessibility-first UI (ARIA roles, screen reader support).
Add region-specific news filtering and sentiment dashboards.

Advanced Sentiment and Trend Analysis
Aggregate sentiment trends over time to predict public opinion shifts.
Introduce a "heat map" of positive/negative news by location or category.

Deployment at Scale
Migrate from local Fluvio to cloud-based Fluvio clusters for production use.
Host the dashboard using scalable infrastructure like AWS, GCP, or Vercel.



---

## 📎 Resources / Credits

**APIs or Datasets Used:**
Custom breaking news JSON API (via Fluvio streaming pipeline).
Groq multimodal inference API for sentiment analysis (text + audio).

**Open Source Libraries / Tools Referenced:**
Fluvio - Real-time data streaming platform.
Groq - High-speed multimodal AI inferencing.
Flask - Lightweight Python web framework.
TailwindCSS - Utility-first CSS framework.
JavaScript Fetch API - For real-time data fetching.

**Acknowledgements:**
Thanks to the InfinyOn/Fluvio and Groq teams for providing access to cutting-edge technology and excellent documentation.
Special thanks to hackathon organizers, mentors, and fellow participants for their guidance and encouragement!

**🏁 Final Words**
Building Sentilytics- the Real-Time News Sentiment Dashboard was an exhilarating experience! 🚀
We faced challenges in setting up the Fluvio streaming pipeline initially and integrating Groq’s multimodal model for both text and audio at speed. However, through continuous brainstorming, debugging, and team collaboration, we overcame the hurdles.
This project not only sharpened our technical skills but also taught us the importance of real-time data handling, scalable architecture, and building for accessibility.

It was amazing to see everything come together — from a simple idea to a working dashboard analyzing breaking news in real-time! 🔥
Big shout-out to all teammates, mentors, and community members who supported this journey!
---
