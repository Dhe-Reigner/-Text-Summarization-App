📝 Text Summarization App

Harnessing the power of Hugging Face models and a simple Streamlit GUI, this project provides an easy-to-use web interface for summarizing long text into concise summaries.

🚀 Features

Uses the facebook/bart-large-cnn model from Hugging Face 🤗

Interactive Streamlit interface for entering and summarizing text

Clean, user-friendly design with one-click summarization

Environment variable support via dotenv for secure API key handling

📷 Demo

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/text-summarization-app.git
cd text-summarization-app


Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt

🔑 Setup

Create a .env file in the project root.

Add your Hugging Face API token:

HF_TOKEN=your_huggingface_token_here

▶️ Usage

Run the app:

streamlit run app.py


Then, open the app in your browser:

http://localhost:8501

📦 Requirements

Python 3.9+

Streamlit

huggingface_hub

python-dotenv

Install dependencies with:

pip install -r requirements.txt

🧠 Model Used

facebook/bart-large-cnn

A transformer-based model fine-tuned for summarization tasks.

💡 Future Improvements

Add support for multiple summarization models

Include text file / PDF input support

Deploy on Hugging Face Spaces / Streamlit Cloud

✨ Built with Python, Hugging Face, and Streamlit.
