from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, permissions, mixins
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Post
from .serializers import (CommentSerializer,
                          PostSerializer)

from .permissions import IsAuthorOrReadOnly


class CreateViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class ChildrenCommentViewSet(CreateViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("comment_id")
        print(post_id)
        print(comment_id)
        post = get_object_or_404(Post, id=post_id)
        comment = get_object_or_404(Comment, id=comment_id, post=post_id)
        serializer.save(author=self.request.user, parent=comment, post=post)
