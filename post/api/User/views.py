from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.contrib.auth.hashers import make_password

from ..models import User, UserSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        password = make_password(serializer.validated_data['password'])
        serializer.save(password=password)



class LoginView(ObtainAuthToken):
    pass
