import logging

import redis

from api import settings
from api.models import Post

logger = logging.getLogger(__name__)


def get_user_feed(user_id, page, per_page):
    redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

    try:
        redis_instance.ping()
    except redis.ConnectionError:
        logger.warning("Could not establish redis connection on %s:%s" % (settings.REDIS_HOST, settings.REDIS_PORT))
        return

    redis_response = redis_instance.lrange(user_id, page * per_page, per_page - 1)
    post_ids = [int(post_id) for post_id in redis_response]

    return Post.objects.filter(pk__in=post_ids)
