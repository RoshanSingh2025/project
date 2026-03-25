import requests
import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_tavily(query):
    url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": 5
    }

    response = requests.post(url, json=payload)
    data = response.json()

    results = []
    for item in data.get("results", []):
        results.append({
            "title": item.get("title"),
            "content": item.get("content"),
            "url": item.get("url")
        })

    return results