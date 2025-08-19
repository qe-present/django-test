from django.db import models
from rest_framework.serializers import ModelSerializer,DateTimeField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name

class CategorySerializer(ModelSerializer):
    created_at = DateTimeField(format='%Y-%m-%d %H:%M:%S')
    updated_at = DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']