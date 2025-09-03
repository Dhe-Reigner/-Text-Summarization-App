import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=api_key
)

def main():
    st.set_page_config(page_title="Text Summarization", page_icon="")
    st.title("Text Summarization")

    user_input =st.text_input("Enter the text you want to summarize here:")

    if st.button("Click to sumarize text"):
        if user_input is not None:
            with st.spinner("Generating summary...."):
                response = client.summarization(
                    user_input,
                    model="facebook/bart-large-cnn"
                )
                st.write(response.summary_text)





if __name__=="__main__":
    main()