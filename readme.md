This project is a backend service for performing web searches and generating answers using the Google Custom Search API and OpenAI's language models.

## Table of Contents

- [Project Description](#project-description)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)

## Project Description

The Mini Perplexity Backend provides an API for performing web searches using the Google Custom Search API and generating answers using OpenAI's language models. The service integrates with Google Custom Search to fetch search results and uses OpenAI's language models to generate answers based on the search results.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/mini-perplexity-backend.git
    cd mini-perplexity-backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory of the project and add the following environment variables:

    ```plaintext
    SEARCH_API_KEY=your_google_custom_search_api_key
    GOOGLE_CX=your_google_custom_search_engine_id
    LANGUAGE_MODEL_API_KEY=your_openai_api_key
    ```

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Perform Web Search

**Endpoint:** `/api/query/`

**Method:** `POST`

**Description:** Perform a web search using the Google Custom Search API and generate an answer using OpenAI's language model.

**Request Body:**

```json
{
    "query": "your_search_query"
}
```

**Response:**

```json
{
    "answer": "generated_answer_text",
    "sources": [
        {
            "url": "source_url",
            "title": "source_title"
        }
    ]
}
```

### Example Requests:

**Request:**

```bash
curl -X POST http://localhost:8000/api/query/ -H "Content-Type: application/json" -d '{"query": "What is the capital of France?"}'
```

**Output:**

```json
{
    "answer": "The capital of France is Paris.",
    "sources": [
        {
            "url": "https://en.wikipedia.org/wiki/Paris",
            "title": "Paris - Wikipedia"
        },
        {
            "url": "https://www.britannica.com/place/Paris",
            "title": "Paris | Definition, Map, Population, Facts, & History | Britannica"
        }
    ]
}
```