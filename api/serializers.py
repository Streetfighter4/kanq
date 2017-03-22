from rest_framework.serializers import ModelSerializer

from api.models import Image
from api.models import Post


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'uri', 'createdAt')


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        # fields = ('id', 'uri', 'createdAt')
