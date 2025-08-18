from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from ..models import Article,ArticleSerializer


class ArticlesListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
