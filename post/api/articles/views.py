from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.permissions import BasePermission, SAFE_METHODS
from ..models import Article,ArticleSerializer

# 作者自己可以修改和删除自己的文章
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # 只读权限允许任何请求
        if request.method in SAFE_METHODS:
            return True
        # 修改和删除只允许作者
        return obj.author == request.user.username

class ArticlesListView(ListCreateAPIView):
    """
    用户文章的 列表、创建
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthorOrReadOnly]
        return super().get_permissions()

    # 设置文章的作者是当前登录用户
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username)




class ArticleOneView(RetrieveUpdateDestroyAPIView):
    """
    用户单个文章的 查询、更新、删除
    """
    lookup_url_kwarg = 'article_id'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT','PATCH',  'DELETE']:
            self.permission_classes = [IsAuthorOrReadOnly]
        return super().get_permissions()



class LinkView(RetrieveUpdateDestroyAPIView):
    """
    点赞,有添加点赞和取消点赞两种操作
    """
