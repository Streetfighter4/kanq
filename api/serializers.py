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
    password_confirmation = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'password', 'password_confirmation')
        extra_kwargs = {'password': {'write_only': True}, 'is_active': {'read_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs.pop('password_confirmation'):
            raise serializers.ValidationError('Password doesn\'t match password confirmation')
        return attrs


# TODO: I think this need to be here, so that topic serializer finds it, but maybe it should
# be with the other post serializers somehow
class PostGlanceSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    image = ImageSerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, post):
        return post.get_rating()

    class Meta:
        model = Post
        fields = ('id', 'title', 'creator_id', 'image', 'tags', 'created_at', 'rating')


class TopicSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    best_post_image = serializers.SerializerMethodField()
    active = serializers.SerializerMethodField()

    def get_best_post_image(self, topic):
        best_post = topic.get_best_post()

        if(best_post):
            image = best_post.image
            serializer = ImageSerializer(image)
            return serializer.data

        return None

    def get_active(self, topic):
        return topic.is_active()

    class Meta:
        model = Topic
        fields = ('id', 'name', 'start', 'end', 'tags', 'best_post_image', 'active')


class TopicDetailSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    active = serializers.SerializerMethodField()
    posts = PostGlanceSerializer(many=True)

    def get_active(self, topic):
        return topic.is_active()

    class Meta:
        model = Topic
        fields = ('id', 'name', 'start', 'end', 'tags', 'active', 'posts')


class TopicDetailSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    active = serializers.SerializerMethodField()
    posts = PostGlanceSerializer(many=True)

    def get_active(self, topic):
        return topic.is_active()

    class Meta:
        model = Topic
        fields = ('id', 'name', 'start', 'end', 'tags', 'active', 'posts')


class PostSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    creator = UserSerializer(read_only=True)
    image = ImageSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, post):
        return post.get_rating()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'creator', 'topic', 'image', 'tags', 'created_at', 'rating')

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'value', 'user')


class PostDetailSerializer(ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    creator = UserSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    def get_comments(self, post):
        comments = Comment.objects.filter(post=post, parent=None)
        serializer = CommentSerializer(instance=comments, many=True)
        return serializer.data

    def get_rating(self, post):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        rating = post.get_current_user_vote(user=user)
        serializer = RatingSerializer(instance=rating)
        return serializer.data

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'creator', 'topic', 'image', 'tags', 'comments', 'created_at', 'rating')


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CommentSerializer(ModelSerializer):
    children = RecursiveField(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, comment):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        rating = comment.get_current_user_vote(user=user)
        serializer = RatingSerializer(instance=rating)
        return serializer.data

    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'user', 'rating', 'parent', 'children')


class MedalSerializer(ModelSerializer):
    class Meta:
        model = Medal
        fields = ('id', 'rank', 'post')


class BadgeSerializer(ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id', 'price', 'user', 'post')

