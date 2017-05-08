from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from api.models import Topic
from api.serializers import TopicSerializer, TopicDetailSerializer

import logging

logger = logging.getLogger(__name__)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    @list_route()
    def active(self, request):  # Get all active topics
        active_topics = [t for t in Topic.objects.all() if t.is_active()]
        page = self.paginate_queryset(active_topics)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(active_topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @list_route()
    def inactive(self, request):  # Get all inactive topics
        inactive_topics = [t for t in Topic.objects.all() if not t.is_active()]
        page = self.paginate_queryset(inactive_topics)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(inactive_topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        topic = Topic.objects.get(pk=kwargs.get('pk'))
        serializer = TopicDetailSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)

