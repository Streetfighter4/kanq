from pip._vendor.requests.api import post
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from api.models import Comment, Badge
from api.models import Image
from api.models import Medal
from api.models import Post
from api.models import Rating
from api.models import Tag
from api.models import Topic
from api.models import User


# noinspection PyAbstractClass
class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'created_at', 'uri')
        extra_kwargs = {'uri': {'read_only': True}}


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'is_active': {'read_only': True}}

    def create(self, validated_data):
        # Exclude password_confirmation from user creation
        if 'password_confirmation' in validated_data:
            del validated_data['password_confirmation']

        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class TopicSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    best_post_image = serializers.SerializerMethodField()

    def get_best_post_image(self, topic):
        best_post = topic.get_best_post()

        if(best_post):
            image = best_post.image
            serializer = ImageSerializer(image)
            return serializer.data

        return None

    class Meta:
        model = Topic
        fields = ('id', 'name', 'start', 'end', 'tags', 'best_post_image')


class PostSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    creator = UserSerializer(read_only=True)
    image = ImageSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'creator', 'topic', 'image', 'tags', 'created_at')


class PostDetailSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    creator = UserSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)
    comments = serializers.SerializerMethodField()

    def get_comments(self, post):
        comments = Comment.objects.filter(post=post, parent=None)
        serializer = CommentSerializer(instance=comments, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'creator', 'topic', 'image', 'tags', 'comments', 'created_at')


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'value', 'user') # TODO: Fix after model fix


class CommentSerializer(ModelSerializer):
    children = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'user', 'parent', 'children')


class MedalSerializer(ModelSerializer):
    class Meta:
        model = Medal
        fields = ('id', 'rank', 'post')


class BadgeSerializer(ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id', 'price', 'user', 'post')

