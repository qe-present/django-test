from django.db import models
from rest_framework.serializers import ModelSerializer
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author']

