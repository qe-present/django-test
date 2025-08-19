from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer,SerializerMethodField,SlugRelatedField

from .category import Category


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    # 点赞
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 分类
    categories = models.ManyToManyField(Category, related_name='articles', blank=True)


    def __str__(self):
        return self.title

class ArticleSerializer(ModelSerializer):
    comments =SerializerMethodField()
    categories = SlugRelatedField(
        many=True,
        queryset=Category.objects.all(),
        slug_field='name'
    )
    def get_comments(self, obj):
        from .comment import CommentSerializer
        return CommentSerializer(obj.comments.all(), many=True).data

    class Meta:
        model = Article
        fields = ['id','title', 'content','categories','comments']
