# backend/views.py

from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from .services.web_search import perform_web_search

from .services.open_ai_service import get_openai_response
from .models import Query, Answer
import requests  # For making HTTP requests (e.g., to search API)

class QueryView(APIView):
    def post(self, request):
        user_query = request.data.get('query')
        print("User query:", user_query)
        # Check if the saved data status is 200
        saved_answer = Answer.objects.filter(query__user_query=user_query).first()
        print("Saved answer:", saved_answer)
        if saved_answer.status == 200:
            # Return the response with answer and sources
            return Response({
            'query': query.user_query,
            'answer': saved_answer.answer_text,
            'sources': saved_answer.sources
            })
        
        query = Query.objects.create(user_query=user_query)
        search_results = perform_web_search(user_query)
        if 'error' in search_results:
            return Response({'error': search_results['error']}, status=500)
        print("Search results:", search_results)
        open_ai_result, sources = self.generate_answer(search_results)
        print("OpenAI result:", open_ai_result["content"])
        # Save the answer to the database
        answer = Answer.objects.create(query=query, answer_text=open_ai_result["content"], status=open_ai_result["status_code"], sources=sources)

        # Return the response with answer and sources
        return Response({
            'query': query.user_query,
            'answer': answer.answer_text,
            'sources': answer.sources
        })

    def generate_answer(self, search_results):
        # Placeholder for answer generation (Replace with actual language model call)
        answer_text = get_openai_response(search_results)
        print("Answer from OpenAI:", answer_text)
        sources = []
        for item in search_results.get('items', []):
            sources.append({
                'url': item.get('link'),
                'title': item.get('title')
            })
        return answer_text, sources



