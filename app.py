import os
import whisper
import asyncio
import aiohttp
import streamlit as st
import pandas as pd

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="Audio News🎧", page_icon="🎧", layout="wide")

# -----------------------
# Custom CSS for styling
# -----------------------
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg,#f9fafb 0%, #ffffff 100%); }
h1, h2, h3 { font-family: 'Inter', sans-serif; }
.card {
    background: #ffffff;
    padding: 16px;
    margin-bottom: 12px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}
.sentiment-pill {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.85rem;
}
.pos { background:#dcfce7; color:#166534; }
.neg { background:#fee2e2; color:#991b1b; }
.neu { background:#f3f4f6; color:#374151; }
</style>
""", unsafe_allow_html=True)

# -----------------------
# Sidebar
# -----------------------
with st.sidebar:
    st.title("⚙️ Settings")
    whisper_model = st.selectbox("Whisper Model", ["tiny", "base", "small", "medium"], index=1)
    batch_size = st.slider("Batch size (sentences/request)", 1, 10, 5)
    st.markdown("---")
    st.caption("🔑 GROQ API KEY")

# -----------------------
# Header
# -----------------------
st.markdown("<h1>🎧Audio News Sentiment Analysis</h1>", unsafe_allow_html=True)
st.markdown("Upload an **audio file** → Transcribe → Detect Sentiment with Groq")

# -----------------------
# File Upload
# -----------------------
audio_file = st.file_uploader("Upload your audio file", type=["mp3", "m4a", "wav"])

if audio_file is not None:
    # Save uploaded file
    with open("audio.m4a", "wb") as f:
        f.write(audio_file.getbuffer())

    # Transcription step
    with st.spinner("📝 Transcribing audio with Whisper..."):
        model = whisper.load_model(whisper_model)
        result = model.transcribe("audio.m4a")

    st.success("✅ Transcription completed!")

    transcript = result["text"]

    with st.expander("📜 Full Transcript", expanded=False):
        st.write(transcript)

    # Split into sentences
    lines = [line.strip() for line in transcript.split('.') if line.strip()]
    batches = [lines[i:i + batch_size] for i in range(0, len(lines), batch_size)]

    # Async call to Groq
    async def get_batch_sentiment_async(session, batch_lines, batch_idx):
        prompt_text = "\n".join([f"{i+1}. {line}" for i, line in enumerate(batch_lines)])
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": "You are a precise sentiment detector. For each numbered line, reply with only 'Positive', 'Negative', or 'Neutral'."},
                {"role": "user", "content": prompt_text}
            ]
        }
        headers = {
            "Authorization": "Bearer groq_api_key(removed due to security reasons)",
            "Content-Type": "application/json"
        }
        async with session.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            if 'choices' in response and response['choices']:
                sentiments_text = response['choices'][0]['message']['content'].strip()
                sentiments = [s.strip() for s in sentiments_text.splitlines() if s.strip()]
                return batch_idx, batch_lines, sentiments
            else:
                return batch_idx, batch_lines, ["Error"] * len(batch_lines)

    async def process_sentiment():
        async with aiohttp.ClientSession() as session:
            tasks = [get_batch_sentiment_async(session, batch, idx) for idx, batch in enumerate(batches)]
            all_results = await asyncio.gather(*tasks)
        all_results.sort(key=lambda x: x[0])
        final_results = []
        for _, lines_batch, sentiments_batch in all_results:
            for line, sentiment in zip(lines_batch, sentiments_batch):
                final_results.append((line, sentiment))
        return final_results

    # Run sentiment analysis
    with st.spinner("🔎 Analyzing sentiments with Groq..."):
        sentiment_results = asyncio.run(process_sentiment())
    st.success("✅ Sentiment analysis completed!")

    # Display results
    st.subheader("📊 Sentiment Results")
    df = pd.DataFrame(sentiment_results, columns=["Sentence", "Sentiment"])

    for sentence, sentiment in sentiment_results:
        css_class = "neu"
        if "Positive" in sentiment:
            css_class = "pos"
        elif "Negative" in sentiment:
            css_class = "neg"
        st.markdown(
            f"<div class='card'><p><b>{sentence}</b></p>"
            f"<span class='sentiment-pill {css_class}'>{sentiment}</span></div>",
            unsafe_allow_html=True
        )

    # Quick stats
    st.subheader("📈 Summary")
    pos = df["Sentiment"].str.contains("Positive").sum()
    neg = df["Sentiment"].str.contains("Negative").sum()
    neu = df["Sentiment"].str.contains("Neutral").sum()
    col1, col2, col3 = st.columns(3)
    col1.metric("Positive", pos)
    col2.metric("Negative", neg)
    col3.metric("Neutral", neu)

    # Download button
    csv_file = "sentiment_results.csv"
    df.to_csv(csv_file, index=False)
    with open(csv_file, "rb") as f:
        st.download_button("⬇️ Download Results as CSV", f, file_name="sentiment_results.csv", mime="text/csv")
