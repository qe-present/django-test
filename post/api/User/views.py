from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from ..models import User, UserSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
