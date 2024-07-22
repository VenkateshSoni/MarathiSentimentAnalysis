import streamlit as st
import requests

# Function to query the Hugging Face model
def query_model(text):
    API_URL = "https://api-inference.huggingface.co/models/ScriptEdgeAI/MarathiSentiment-Bloom-560m"
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Function to analyze sentiment and return label and type
def analyze_sentiment(text):
    output = query_model(text)
    if isinstance(output, list) and len(output) > 0:
        sentiment_label = output[0][0]['label']
        sentiment_type = output[0][0]['sentiment_type']
        return sentiment_label, sentiment_type

# Streamlit UI
def main():
    st.title("Marathi Sentiment Analysis")

    # Input text area for user input
    user_input = st.text_area("Enter a sentence in Marathi")

    # Button to trigger sentiment analysis
    if st.button("Analyze Sentiment"):
        if user_input:
            sentiment_label, sentiment_type = analyze_sentiment(user_input)
            if sentiment_type == "positive":
                st.write("Sentiment:", f"<span style='color:green; font-weight:bold;'>{sentiment_label}</span>", unsafe_allow_html=True)
            elif sentiment_type == "negative":
                st.write("Sentiment:", f"<span style='color:red; font-weight:bold;'>{sentiment_label}</span>", unsafe_allow_html=True)
            else:  # neutral
                st.write("Sentiment:", f"<span style='color:darkgrey; font-weight:bold;'>{sentiment_label}</span>", unsafe_allow_html=True)
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
