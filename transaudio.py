from websocket_server import send_to_all_clients
import whisper
import openai
import csv

# Load Whisper model
model = whisper.load_model("base")  # or "small", "medium", "large"
result = model.transcribe("newsaudio.m4a")

# Get full transcript
transcript = result["text"]
print("Transcript:\n", transcript)

# Setup Groq (OpenAI-compatible) API client
client = openai.OpenAI(
    api_key="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",  # ← your Groq API key
    base_url="https://api.groq.com/openai/v1"
)

# Split transcript into lines/sentences
lines = [line.strip() for line in transcript.split('.') if line.strip()]

# Group sentences into batches to save API cost
BATCH_SIZE = 10 # adjust if needed
batches = [lines[i:i+BATCH_SIZE] for i in range(0, len(lines), BATCH_SIZE)]

# Define function to get sentiments from Groq for a batch
def get_batch_sentiment_groq(batch_lines):
    prompt_text = "\n".join(batch_lines)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # using latest working model
        messages=[
            {"role": "system", "content": "You are a precise sentiment detector. For each line of the text, reply with only 'Positive', 'Negative', or 'Neutral' corresponding to each line, and nothing else."},
            {"role": "user", "content": prompt_text}
        ]
    )
    sentiments_text = response.choices[0].message.content.strip()
    # If Groq returns numbering like "1. Negative", clean it
    sentiments = [line.split('. ', 1)[-1].strip() for line in sentiments_text.splitlines()]
    return sentiments

# Analyze sentiment batch by batch
results = []  # to store for CSV

for batch in batches:
    sentiments = get_batch_sentiment_groq(batch)
    for line, sentiment in zip(batch, sentiments):
        print(f"{line} → {sentiment}")
        results.append((line, sentiment))  # Save for CSV

# Write final output into a CSV file
with open('sentiment_output.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Sentence', 'Sentiment'])  # Header
    writer.writerows(results)

print("\n✅ Sentiment analysis complete! Output saved to 'sentiment_output.csv'")
