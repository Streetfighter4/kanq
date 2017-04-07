import logging
import redis

from api import settings

logger = logging.getLogger(__name__)


def get_user_feed_ids(user_id, page, per_page):
    if (page * per_page + per_page) > settings.REDIS_FEED_MAX_LENGTH:
        return []

    redis_instance = get_instance()
    if redis_instance:
        start = page * per_page
        end = start + per_page - 1
        redis_response = redis_instance.lrange(user_id, start, end)
        return [int(post_id) for post_id in redis_response]
    else:
        return []


def push_new_post(post):
    followers_ids = post.creator.get_followers_ids()

    redis_instance = get_instance()
    if redis_instance:
        redis_pipe = redis_instance.pipeline(transaction=False)
        redis_pipe.lpush(post.creator_id, post.id)

        for follower_id in followers_ids:
            redis_pipe.lpush(follower_id, post.id).ltrim(follower_id, 0, settings.REDIS_FEED_MAX_LENGTH - 1)

        redis_pipe.execute()


def get_instance():
    redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

    try:
        redis_instance.ping()
    except redis.ConnectionError:
        # logger.warning("Could not establish redis connection on %s:%s" % (settings.REDIS_HOST, settings.REDIS_PORT))
        # TODO: Enable log when it's redirected to a file
        return None

    return redis_instance
