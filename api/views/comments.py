from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.models import Comment, Rating
from api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @detail_route(methods=['put'])
    def rate(self, request, pk=None):  # Update user's rating of a post
        post = get_object_or_404(Comment, id=pk)
        Rating.objects.create(content_object=post, value=request.data['vote'], user = request.user)
        return Response(status=status.HTTP_200_OK)
