import streamlit as st
import requests

# Function to query the Hugging Face model
def query_model(text):
    API_URL = "https://api-inference.huggingface.co/models/ScriptEdgeAI/MarathiSentiment-Bloom-560m"
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Response content is not valid JSON:", response.text)
            return {"error": "Invalid JSON response"}
    else:
        print(f"Request failed with status {response.status_code}")
        print("Response text:", response.text)
        return {"error": f"Request failed: {response.status_code}"}

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
            st.write("- ", "Sentiment:", sentiment, """
            \n
            """)
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
