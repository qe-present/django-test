from django.db import models
from rest_framework.serializers import ModelSerializer
from .user import User
from .article import Article
class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
