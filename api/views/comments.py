from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.models import Comment, Rating
from api.serializers import CommentSerializer, RatingSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @detail_route(methods=['put'])
    def rate(self, request, pk=None):  # Update user's rating of a post
        vote = request.data['vote']
        if vote is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        vote = int(vote)
        if not (vote == Rating.LIKE_VALUE) and not(vote == Rating.DISLIKE_VALUE):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        comment = get_object_or_404(Comment, id=pk)
        rating = comment.get_current_user_vote(request.user)

        if rating is None:
            rating = Rating.objects.create(content_object=comment, value=vote, user = request.user)
        else:
            rating.value = request.data['vote']
            rating.save()
        serializer_rating = RatingSerializer(rating)
        return Response(serializer_rating.data, status=status.HTTP_200_OK)
