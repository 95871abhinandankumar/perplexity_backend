import requests
from perplexity_backend.settings import SEARCH_API_KEY, GOOGLE_CX


def perform_web_search(query):
    url = f'https://www.googleapis.com/customsearch/v1?key={SEARCH_API_KEY}&cx={GOOGLE_CX}&q={query}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        search_results = response.json()
        return search_results
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}