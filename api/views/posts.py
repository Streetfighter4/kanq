import base64
import os

from rest_framework import status

from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from kanq.settings import REST_FRAMEWORK
from api.helpers import user_service

from api.models import Post, Image, Rating

from api.serializers import PostSerializer, PostDetailSerializer, PostGlanceSerializer
from api.settings import TRENDING_POST_FALLOUT

import logging

logger = logging.getLogger(__name__)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer

        return PostSerializer

    def create(self, request, *args, **kwargs):  # Upload image to server if needed and create post
        images_dir = './images/'
        image_name = 'image1'
        image_extension = '.png'
        full_path = images_dir + image_name + image_extension
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
        return Response(post, status=status.HTTP_201_CREATED)

        #    return Response(new_post, status=status.HTTP_400_BAD_REQUEST)

    @list_route()
    def top(self, request):  # Filter topic by query param
        print(request.GET.get('offset'))
        print(request.GET.get('limit'))
        posts = self.filter_by_topic(request).all()
        posts = sorted(posts, key=lambda p: p.get_rating(), reverse=True)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @list_route()
    def trending(self, request):  # Filter topic by query param
        posts = Post.objects.all()
        trending_posts = sorted(posts, key=lambda p: -p.get_trend_coefficient(TRENDING_POST_FALLOUT))
        serializer = PostGlanceSerializer(trending_posts, many=True)
        return Response(data=serializer.data, status=200)

    @list_route()
    def new(self, request):
        objects = self.filter_by_topic(request).order_by('-created_at')
        page = self.paginate_queryset(objects)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @list_route()
    def feed(self, request):  # Get feed for a given user
        user_id = request.GET.get('user_id', '')

        if user_id:
            page = request.GET.get('page', '0')
            page_size = REST_FRAMEWORK.PAGE_SIZE
            posts = user_service.get_user_feed(user_id, page, page_size)
            serialized = PostSerializer(posts, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @detail_route(methods=['put'])
    def rate(self, request, pk=None):  # Update user's rating of a post
        #TODO: request.data['vote'] in var
        #TODO: error checking
        post = get_object_or_404(Post, id=pk)
        rating = post.get_current_user_vote(request.user)
        if (rating is None):
            Rating.objects.create(content_object=post, value=request.data['vote'], user = request.user)
        else:
            rating.value = request.data['vote']
            rating.save()
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def filter_by_topic(request):
        topic_id = request.GET.get('topic_id', '')
        objects = Post.objects
        if topic_id:
            try:
                objects = objects.filter(topic__id=int(topic_id))
            except ValueError:
                logger.error('Tried filtering by topic with wrong topic_id')

        return objects

