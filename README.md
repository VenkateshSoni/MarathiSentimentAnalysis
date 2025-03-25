# Marathi Sentiment Analysis Streamlit App
# Marathi Sentiment Analysis App

This Streamlit application provides an interface for performing sentiment analysis on Marathi sentences using a pre-trained model hosted on Hugging Face.
The pretrained model namely `ScriptEdgeAI/MarathiSentiment-Bloom-560m` was **finetuned for Marathi language** improving the **3 class sentiment analysis accuracy**
by more than **2 times** and **2 class sentiment analysis accuracy** by more than **2.5 times**.
**Link to the model and more details - `https://huggingface.co/ScriptEdgeAI/MarathiSentiment-Bloom-560m`**

## Features

- **User Input**: Allows users to input Marathi text for sentiment analysis.
- **Sentiment Analysis**: Utilizes the `ScriptEdgeAI/MarathiSentiment-Bloom-560m` model to analyze the sentiment of the input text.
- **Sample Test Sentences**: Provides a list of sample Marathi sentences for users to test the functionality.

## Setup and Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/VenkateshSoni/marathi-sentiment-analysis.git
    cd marathi-sentiment-analysis
    ```

2. **Install Dependencies**

    Ensure you have Python 3.7+ installed. Install the required packages using:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Hugging Face API Key**

    Create a `.env` file in the root directory and add your Hugging Face API key:

    ```plaintext
    HF_API_KEY=your_huggingface_api_key
    ```

## Running the Application

To start the Streamlit app, use the following command:

```bash
streamlit run app.py
```

This will open the application in your default web browser.

## Usage

1. **Enter Text**: Input a Marathi sentence in the text area provided.
2. **Analyze Sentiment**: Click the "Analyze Sentiment" button to get the sentiment label.
3. **View Results**: The sentiment label (e.g., Positive, Negative, Neutral) will be displayed below the input field.
4. **Sample Sentences**: Test the application with provided sample sentences by copying and pasting them into the input field.
