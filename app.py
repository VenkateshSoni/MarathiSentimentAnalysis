import streamlit as st
import requests

# Function to query the Hugging Face model
def query_model(text):
    API_URL = "https://api-inference.huggingface.co/models/ScriptEdgeAI/MarathiSentiment-Bloom-560m"
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Function to analyze sentiment and return label
def analyze_sentiment(text):
    output = query_model(text)
    if isinstance(output, list) and len(output) > 0:
        sentiment_label = output[0][0]['label']
        return sentiment_label

# Streamlit UI
def main():
    st.title("Marathi Sentiment Analysis")

    # Input text area for user input
    user_input = st.text_area("Enter a sentence in Marathi")

    # Button to trigger sentiment analysis
    if st.button("Analyze Sentiment"):
        if user_input:
            sentiment = analyze_sentiment(user_input)
            sentiment_type = ""  # Initialize sentiment type
            if sentiment == "positive":
                sentiment_type = "positive"
                sentiment_color = "green"
            elif sentiment == "negative":
                sentiment_type = "negative"
                sentiment_color = "red"
            else:  # neutral
                sentiment_type = "neutral"
                sentiment_color = "darkgrey"

            # Styling the sentiment output
            styled_sentiment = f"<span style='color:{sentiment_color}; font-weight:bold;'>{sentiment}</span>"
            st.write("Sentiment:", styled_sentiment, unsafe_allow_html=True)
        else:
            st.warning("Please enter a sentence.")

    # Sample test sentences
    st.markdown("### Sample Test Sentences:")
    test_sentences = [
        "मी तुला विचारत नाही आहे/नाहीये",
        "त्याला इंग्रजीत बोलता येत नाही.",
        "आजचा दिवस किती चांगला होता",
        "हे एक रमणीय ठिकाण आहे",
        "तुमचे काम झाले आहे का?",
        "तुम्हाला काही मदत हवी आहे का"
    ]
    for sentence in test_sentences:
        st.write("- " + sentence)

if __name__ == "__main__":
    main()
