from rest_framework import viewsets
from rest_framework.decorators import list_route

from api.models import Topic
from api.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    @list_route()
    def active(self):  # Get all active topics
        pass

    @list_route()
    def inactive(self):  # Get all inactive topics
        pass

