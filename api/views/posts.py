import base64
import logging
import os

from django.utils import timezone
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.helpers import user_service
from api.models import Rating
from api.serializers import PostGlanceSerializer, RatingSerializer
from api.settings import TRENDING_POST_FALLOUT
from kanq.settings import REST_FRAMEWORK

logger = logging.getLogger(__name__)
from api.models import Post, Image, Topic
from api.serializers import PostSerializer, PostDetailSerializer

MAX_POSTS_ALLOWED = 500


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        elif self.action == 'top'\
                or self.action == 'new'\
                or self.action == 'trending':
            return PostGlanceSerializer

        return PostSerializer

    def create(self, request, *args, **kwargs):  # Upload image to server if needed and create post
        data = request.data.copy()
        posts_count = Post.objects.filter(topic_id=data['topic_id'], creator=request.user.id).count()
        if posts_count >= MAX_POSTS_ALLOWED:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if data['topic_id'] is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        topic = Topic.objects.get(pk=data['topic_id'])
        if not topic.is_active():
            return Response(status=status.HTTP_403_FORBIDDEN)

        images_dir = 'api/static/images/'
        image_name = '{}_{}'.format(request.user.id, timezone.now().strftime("%Y_%m_%d_%H_%M_%S"))
        image_extension = request.data['extension']
        if '.' not in image_extension:
            image_extension = '.' + image_extension

        full_path = '{}{}{}'.format(images_dir, image_name, image_extension)
        image_url= 'http://localhost:8000/static/images/' + image_name + image_extension

        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        image = data['image']
        print(image)
        decoded = base64.b64decode(image)
        with open(full_path, "wb") as fh:
            fh.write(decoded)
        fh.close()

        image = Image.objects.create(uri=image_url)
        post = Post.objects.create(description=data['description'], title=data['title'],
                                   creator_id=request.user.id, topic_id=data['topic_id'], image_id=image.id)
        serializer = PostSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @list_route()
    def top(self, request):  # Filter topic by query param
        posts = self.filter_by_topic(request).all()
        posts = sorted(posts, key=lambda p: p.get_rating(), reverse=True)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @list_route()
    def trending(self, request):  # Filter topic by query param
        # TODO: This should filter posts by topic_id param
        posts = Post.objects.all()
        trending_posts = sorted(posts, key=lambda p: -p.get_trend_coefficient(TRENDING_POST_FALLOUT))
        page = self.paginate_queryset(trending_posts)
        if page is not None:
            serializer = PostGlanceSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        else:
            serializer = PostGlanceSerializer(trending_posts, many=True, context={'request': request})

        return Response(data=serializer.data, status=200)

    @list_route()
    def new(self, request):
        objects = self.filter_by_topic(request).order_by('-created_at')
        page = self.paginate_queryset(objects)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @list_route()
    def feed(self, request):  # Get feed for a given user
        user = request.user

        if user:
            user_id = str(user.id)
            page = request.GET.get('page', '0')
            page_size = REST_FRAMEWORK['PAGE_SIZE']
            posts = user_service.get_user_feed(user_id, int(page), page_size)
            serialized = PostGlanceSerializer(posts, many=True, context={'request': request})
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @detail_route(methods=['put'])
    def rate(self, request, pk=None):  # Update user's rating of a post
        vote = request.data['vote']
        if vote is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        vote = int(vote)

        if not (vote == Rating.LIKE_VALUE) \
                and not (vote == Rating.DISLIKE_VALUE) \
                and not (vote == Rating.DELETE_RATING_VALUE):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        post = get_object_or_404(Post, id=pk)
        rating = post.get_current_user_vote(request.user)

        if rating is None:
            rating = Rating.objects.create(content_object=post, value=vote, user=request.user)
        else:
            if vote == Rating.DELETE_RATING_VALUE:
                rating.delete()
                return Response(status=status.HTTP_200_OK)

            rating.value = vote
            rating.save()
        serializer_rating = RatingSerializer(rating)
        return Response(serializer_rating.data, status=status.HTTP_200_OK)

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
