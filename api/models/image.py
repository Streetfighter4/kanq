from django.db import models


class Image(models.Model):
    TEST_IMAGES = [
        '/static/images/plant.jpg',
        '/static/images/insect.jpg',
        '/static/images/sunset.jpg'
    ]

    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    uri = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.uri
