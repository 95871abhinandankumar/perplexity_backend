
from django.db import models

class Query(models.Model):
    user_query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query(id={self.id}, query='{self.user_query[:50]}')"


class Answer(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    status = models.IntegerField(default=500)
    sources = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer(id={self.id}, answer='{self.answer_text[:50]}')"
