from django.core.management import BaseCommand

from api.models import Topic, Medal

WINNERS_COUNT = 3


class Command(BaseCommand):
    help = 'Updates topics at the end of a period'

    def handle(self, *args, **options):
        topics = Topic.get_topics_to_close()
        for topic in topics:
            topic.closed = True
            self.reward_topic_winners(topic)
            topic.save()
        pass

    @staticmethod
    def reward_topic_winners(topic):
        winner_posts = topic.get_best_posts(WINNERS_COUNT)
        rank = 1
        for post in winner_posts:
            medal = Medal(rank=rank, user=post.creator, post=post)
            medal.save()
            rank = rank + 1

