# app/lead_scoring.py
import requests
from bs4 import BeautifulSoup

KEYWORDS = {
    "AI": 2,
    "machine learning": 2,
    "book a demo": 3,
    "we're hiring": 3,
    "growth": 1,
    "automation": 2,
    "digital": 1,
    "data-driven": 2,
    "careers": 2,
    "solutions": 1
}

def fetch_website_text(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text().lower()
    except:
        return ""

def score_lead_from_url(url):
    content = fetch_website_text(url)
    score = 0
    found_keywords = []
    for keyword, weight in KEYWORDS.items():
        if keyword in content:
            score += weight
            found_keywords.append(keyword)
    return score, found_keywords
