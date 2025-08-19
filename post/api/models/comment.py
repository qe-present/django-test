from django.db import models
from rest_framework import serializers
from .user import User
from .article import Article

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CommentSerializer(serializers.ModelSerializer):
    username= serializers.CharField(source='user_id.username', read_only=True)
    class Meta:
        model = Comment
        fields = ['username','content']
