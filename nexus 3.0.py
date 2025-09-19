import requests
from transformers import pipeline

API_KEY = "AIzaSyDPJXOCWlCNvIumpWDvviugfE_bM9xObA0"
SEARCH_ENGINE_ID = "a26af794463f142a9"

summarizer = pipeline("summarization")

def google_search(query, api_key='AIzaSyDPJXOCWlCNvIumpWDvviugfE_bM9xObA0', cse_id='a26af794463f142a9'):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'num': 1,
    }
    response = requests.get(url, params=params)
    results = response.json()

    if "items" not in results:
        return None

    combined_text = " ".join(item['snippet'] for item in results['items'])
    return combined_text

def chatbot():
    print("Welcome to the Nexus! Ask me anything or type 'exit' to quit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() == "exit":
            print("Bot: Goodbye!")
            break

        search_results = google_search(question)
        if not search_results:
            print("Bot: Sorry, I couldn't find any useful information.")
            continue

        summary = summarizer(search_results, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

        print(f"Bot: {summary}\n")

if __name__ == "__main__":
    chatbot()

