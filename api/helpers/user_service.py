from api.models import Post, User
from . import redis_connection


def get_user_feed(user_id, page, per_page):
    post_ids = redis_connection.get_user_feed_ids(user_id, page, per_page)

    if post_ids:
        return Post.objects.filter(pk__in=post_ids).order_by('-created_at')

    user = User.objects.get(pk=user_id)
    start = page * per_page
    end = start + per_page
    return (Post.objects.filter(creator__id__in=user.get_following_ids()) |
            Post.objects.filter(creator_id=user_id)).order_by('-created_at')[start:end]
