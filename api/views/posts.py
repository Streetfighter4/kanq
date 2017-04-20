import base64
from django.utils import timezone
import os

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from api.models import Post, Image
from api.serializers import PostSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer

        return PostSerializer

    def create(self, request, *args, **kwargs):  # Upload image to server if needed and create post
        images_dir = './images/'
        image_name = '{}_{}'.format(request.data['creator'], timezone.now().strftime("%Y_%m_%d_%H_%M_%S"))
        image_extension = request.data['extension']
        full_path = '{}{}{}'.format(images_dir, image_name, image_extension)
        print(full_path)
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        data = request.data.copy()
        decoded = str(base64.urlsafe_b64decode(data['image']))
        file = open(full_path, 'w+')
        file.write(decoded)
        file.close()

        image = Image.objects.create(uri=full_path)
        data['image'] = image.id

        post = Post.objects.create(description = data['description'], title=data['title'],
                                   creator_id = data['creator'], topic_id = data['topic'], image_id=data['image'])
        serializer = PostSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
    def feed(self):  # Get feed for a given user
        pass

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

