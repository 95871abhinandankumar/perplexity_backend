# backend/serializers.py

from rest_framework import serializers
from .models import Query, Answer

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['id', 'user_query', 'created_at']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'query', 'answer_text', 'sources', 'created_at']
