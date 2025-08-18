from django.urls import path
from .User.views import RegisterView,LoginView
from .articles.views import ArticlesListView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('articles/',ArticlesListView.as_view()),
]