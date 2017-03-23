from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from api.models import Comment
from api.models import Image
from api.models import Medal
from api.models import Post
from api.models import Rating
from api.models import Tag
from api.models import Topic
from api.models import User


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'uri', 'createdAt')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'is_active': {'read_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class PostSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'creator', 'topic', 'image', 'tags')


class TopicSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'start', 'end', 'tags')


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'value', 'user') # TODO: Fix after model fix


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'user', 'parent', 'children')


class MedalSerializer(ModelSerializer):
    class Meta:
        model = Medal
        fields = ('id', 'rank', 'post')
