from django.urls import path
from .User.views import RegisterView
urlpatterns = [
    path('register/',RegisterView.as_view())
]