import requests

SERPER_KEY = "YOUR_API_KEY"

def search_web(query):

    url = "https://google.serper.dev/search"

    payload = {"q": query}

    headers = {
        "X-API-KEY": SERPER_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
