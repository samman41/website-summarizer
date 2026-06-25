import requests
from bs4 import BeautifulSoup
from google import genai

"""Website Summarizer

This script fetches the text content from a given website URL,
parses it using BeautifulSoup to remove scripts and styles,
and then uses the Google GenAI SDK to generate a concise summary of the company or website.

Usage:
1. Run the script: python summarizer.py
2. Enter the website URL when prompted.

Dependencies:
• requests
• beautifulsoup4
• google-genai"""

def summarize_website(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except Exception as e:
        return f"Error fetching the website: {e}"

    soup = BeautifulSoup(response.text, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text(separator=" ")
    cleaned_text = " ".join(text.split())[:10000]

    prompt = (
        "Read the following website text and write a brief, impressive 2-3 sentence "
        "summary of what this company or website is all about:\n\n"
        f"{cleaned_text}"
    )

    client = genai.Client()
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
    except Exception as e:
        return f"Error generating summary: {e}"

    if hasattr(response, "text"):
        return response.text
    if hasattr(response, "output") and response.output:
        first_output = response.output[0]
        if hasattr(first_output, "content") and first_output.content:
            first_content = first_output.content[0]
            if hasattr(first_content, "text"):
                return first_content.text

    return str(response)


def main():
    target_url = input("Enter a website URL e.g., https://example.com: ")
    summary = summarize_website(target_url)
    print("\nSummary --")
    print(summary)


if __name__ == "__main__":
    main()