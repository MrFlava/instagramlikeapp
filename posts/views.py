from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (CreateAPIView, ListAPIView)

from posts.serializers import PostSerializer, LikeSerializer, CommentSerializer
from posts.models import Post, Like, Comment


# Create your views here.

class PostCreateView(CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class PostsListView(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostLikeView(CreateAPIView):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class PostCommentView(CreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
