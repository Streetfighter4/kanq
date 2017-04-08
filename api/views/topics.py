from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from api.models import Topic
from api.serializers import TopicSerializer, TopicDetailSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    @list_route()
    def active(self, request):  # Get all active topics
        active_topics = [t for t in Topic.objects.all() if t.is_active()]
        serializer = TopicSerializer(instance=active_topics, many=True)
        return Response(serializer.data)

    @list_route()
    def inactive(self, request):  # Get all inactive topics
        inactive_topics = [t for t in Topic.objects.all() if not t.is_active()]
        serializer = TopicSerializer(instance=inactive_topics, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        topic = Topic.objects.get(pk=pk)
        serializer = TopicDetailSerializer(topic)
        return Response(serializer.data)


