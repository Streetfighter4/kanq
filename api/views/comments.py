from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.models import Comment, Rating
from api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @detail_route(methods=['put'])
    def rate(self, request, pk=None):  # Update user's rating of a post
        comment = get_object_or_404(Comment, id=pk)
        rating = comment.get_current_user_vote(request.user)
        if (rating is None):
            Rating.objects.create(content_object=comment, value=request.data['vote'], user = request.user)
        else:
            rating.value = request.data['vote']
            rating.save()
        return Response(rating, status=status.HTTP_200_OK)
