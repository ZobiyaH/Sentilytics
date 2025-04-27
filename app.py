import whisper
import openai
import streamlit as st
import asyncio
import aiohttp
import pandas as pd  # For dataframe and CSV

# Setup Streamlit page title
st.set_page_config(page_title="Audio Sentiment Analysis", page_icon="🎧")

# Title for the app
st.title("Audio Sentiment Analysis App 🎧")

# File uploader for audio files
audio_file = st.file_uploader("Upload your audio file", type=["mp3", "m4a"])

# If an audio file is uploaded, process it
if audio_file is not None:
    # Save uploaded file temporarily
    with open("audio.m4a", "wb") as f:
        f.write(audio_file.getbuffer())

    # Loading spinner for transcription
    with st.spinner("Transcribing audio using Whisper..."):
        model = whisper.load_model("base")
        result = model.transcribe("audio.m4a")

    st.success("✅ Audio transcription completed!")

    # Get the transcript
    transcript = result["text"]
    st.subheader("Transcript:")
    st.write(transcript)

    # Split transcript into lines/sentences
    lines = [line.strip() for line in transcript.split('.') if line.strip()]

    # Group sentences into batches
    BATCH_SIZE = 5
    batches = [lines[i:i + BATCH_SIZE] for i in range(0, len(lines), BATCH_SIZE)]

    # Async function to call Groq API for sentiment analysis
    async def get_batch_sentiment_async(session, batch_lines, batch_idx):
        prompt_text = "\n".join([f"{i+1}. {line}" for i, line in enumerate(batch_lines)])
        
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": "You are a precise sentiment detector. For each numbered line, reply with only 'Positive', 'Negative', or 'Neutral', corresponding to the line numbers, and nothing else."},
                {"role": "user", "content": prompt_text}
            ]
        }
        
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        }
        
        async with session.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            
            if 'choices' in response and response['choices']:
                sentiments_text = response['choices'][0]['message']['content'].strip()
                sentiments = sentiments_text.splitlines()
                return batch_idx, batch_lines, sentiments
            else:
                st.error(f"API Error or Unexpected response: {response}")
                return batch_idx, batch_lines, ["Error"] * len(batch_lines)

    # Async function to process all batches and return results
    async def process_sentiment():
        async with aiohttp.ClientSession() as session:
            tasks = []
            for idx, batch in enumerate(batches):
                tasks.append(get_batch_sentiment_async(session, batch, idx))
            
            all_results = await asyncio.gather(*tasks)

        # Sort results based on batch index (to maintain original order)
        all_results.sort(key=lambda x: x[0])

        final_results = []
        for _, lines_batch, sentiments_batch in all_results:
            for line, sentiment in zip(lines_batch, sentiments_batch):
                final_results.append((line, sentiment))

        return final_results

    # Loading spinner for sentiment analysis
    with st.spinner("Analyzing sentiments using Groq..."):
        sentiment_results = asyncio.run(process_sentiment())

    st.success("✅ Sentiment analysis completed!")

    # Display sentiment analysis results in a table
    st.subheader("Sentiment Analysis Results:")
    sentiment_df = pd.DataFrame(sentiment_results, columns=["Sentence", "Sentiment"])
    st.write(sentiment_df)

    # Save to CSV
    csv_file = "sentiment_results.csv"
    sentiment_df.to_csv(csv_file, index=False)

    # Offer download button
    with open(csv_file, "rb") as f:
        st.download_button(
            label="Download Sentiment Results as CSV",
            data=f,
            file_name="sentiment_results.csv",
            mime="text/csv"
        )
