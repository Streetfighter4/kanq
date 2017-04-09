from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from api import settings
from api.helpers import user_service

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
        objects = self.filter_by_topic(request).order_by('-created_at')
        serializer = PostSerializer(objects, many=True)
        return Response(serializer.data)

    @list_route()
    def feed(self, request):  # Get feed for a given user
        user_id = request.GET.get('user_id', '')
        if user_id:
            # TODO: paginate
            posts = user_service.get_user_feed(user_id, 0, 10)
            serialized = PostSerializer(posts, many=True)
            return Response(serialized.data, status=200)
        else:
            return Response(status=404)

    @detail_route(methods=['put'])
    def rate(self, request, pk=None):  # Update user's rating of a post
        pass

    @staticmethod
    def filter_by_topic(request):
        topic_id = request.GET.get('topic_id', '')
        objects = Post.objects
        if topic_id:
            try:
                objects = objects.filter(topic__id=int(topic_id))
            except ValueError:
                print('Wrong topic id: ' + topic_id)

        return objects

