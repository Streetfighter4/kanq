from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from api.models import Post
from api.serializers import PostSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer

        return PostSerializer

    def create(self, request, *args, **kwargs):  # Upload image to server if needed and create post
        print(request.data['topic'])
        pass

    @list_route()
    def top(self, request):  # Filter topic by query param
        pass

    @list_route()
    def trending(self, request):  # Filter topic by query param
        pass

    @list_route()
    def new(self, request):
        return Response()

    @list_route()
    def feed(self):  # Get feed for a given user
        pass

    @detail_route(methods=['put'])
    def rate(self, request, pk=None):  # Update user's rating of a post
        pass
