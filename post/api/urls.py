from django.urls import path
from .User.views import RegisterView,LoginView
from .articles import ArticlesListView,ArticleOneView
from .category import CategoryListView
from .comment import CommentListView
urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('articles/',ArticlesListView.as_view()),
    path('articles/<int:article_id>/',ArticleOneView.as_view()),
    path('articles/<int:article_id>/comments/', CommentListView.as_view()),
    path('category/',CategoryListView.as_view()),

]