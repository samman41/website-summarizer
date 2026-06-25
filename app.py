import os
import streamlit as st
from dotenv import load_dotenv
from summarizer import summarize_website

load_dotenv()


st.title("Website Summarizer")
format_option =st.selectbox("Choose summary format:", ["Paragraph", "Bullet Points"])
url = st.text_input("Enter the URL of the website you want to summarize:")

if st.button("Summarize"):
    if url:
        summary = summarize_website(url, summary_format=format_option)
        st.write("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter a valid URL.")