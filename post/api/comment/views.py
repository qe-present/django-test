from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from ..models import Comment, CommentSerializer, Article


class CommentListView(ListCreateAPIView):
    """
    用户评论的 列表、创建
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    # 设置评论的用户是当前登录用户
    def perform_create(self, serializer):
        article_id=self.kwargs.get('article_id')
        article=Article.objects.get(pk=article_id)
        serializer.save(user_id=self.request.user,article_id=article)

    # 只返回当前文章的评论
    def get_queryset(self):
        article_id = self.kwargs.get('article_id')
        return Comment.objects.filter(article_id=article_id).order_by('-created_at')

