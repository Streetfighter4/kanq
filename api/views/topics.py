from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from api.models import Topic
from api.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    @list_route()
    def active(self, request):  # Get all active topics
        active_topics = Topic.objects.all()
        serializer = TopicSerializer(instance=active_topics, many=True)
        return Response(serializer.data)

    @list_route()
    def inactive(self, request):  # Get all inactive topics
        pass

