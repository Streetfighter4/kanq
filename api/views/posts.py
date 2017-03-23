from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route

from api.models import Post
from api.serializers import PostSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer

        return PostSerializer


    @list_route()
    def top(self, request): #Filter topic by query param
        pass

    @list_route()
    def trending(self, request): #Filter topic by query param
        pass

    @list_route()
    def new(self, request): #Filter topic by query param
        pass

    @list_route()
    def feed(self): # get feed for a given user
        pass

    @detail_route(methods=['put'])
    def rate(self, request, pk=None): # update user's rating of a post
        pass

