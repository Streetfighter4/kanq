from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route

from api.models import Post
from api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @list_route()
    def top(self, request): #Filter topic by query param
        pass

    @list_route()
    def trending(self, request): #Filter topic by query param
        pass

    @list_route()
    def new(self, request): #Filter topic by query param
        pass

    @detail_route(methods=['post'])
    def rate(self, request, pk=None):
        pass

