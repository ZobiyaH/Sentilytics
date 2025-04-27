
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
- [✅ ] **Groq:** Groq accelerated the real-time text and audio sentiment analysis pipeline, enabling fast, accurate insights for news events.  
- [ ] **Monad:** _Your blockchain implementation_  
- [ ✅] **Fluvio:** Fluvio handled the real-time streaming of news data, ensuring instant delivery to the sentiment analysis pipeline and live dashboard updates.  
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
```bash
# Clone the repo
git clone https://github.com/your-team/project-name

# Install dependencies
cd project-name
npm install

# Start development server
npm run dev
```

Provide any backend/frontend split or environment setup notes here.

---

## 🧬 Future Scope

List improvements, extensions, or follow-up features:

- 📈 More integrations  
- 🛡️ Security enhancements  
- 🌐 Localization / broader accessibility  

---

## 📎 Resources / Credits

- APIs or datasets used  
- Open source libraries or tools referenced  
- Acknowledgements  

---

## 🏁 Final Words

Share your hackathon journey — challenges, learnings, fun moments, or shout-outs!

---
