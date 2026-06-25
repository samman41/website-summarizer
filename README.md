Website Summarizer

This application is built with Streamlit and fetches the text content from a given website URL, parses it using BeautifulSoup to remove scripts and styles, and then uses the Google GenAI SDK to generate a concise summary of the company or website. Users can also select their preferred summary format (e.g., Paragraph, Bullet Points) via the user interface.

Installation

To install the necessary dependencies, you must run the following command:
bash
pip install streamlit requests beautifulsoup4 google-genai

Configuration

Configure your API key by creating a .env file and adding your Gemini API key.

Usage

1. Run the application using Streamlit: bash
streamlit run app.py

2. Enter the website URL in the input field and select your desired summary format in the app interface.

Dependencies

• streamlit
• requests
• beautifulsoup4
• google-genai
