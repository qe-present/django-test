from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.serializers import ModelSerializer

class User(AbstractUser):
    phone= models.CharField(max_length=11)
    address= models.TextField(blank=True, null=True)



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','phone']


