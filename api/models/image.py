from django.db import models


class Image(models.Model):
    TEST_IMAGES = [
        'http://localhost:8000/static/images/plant.jpg',
        'http://localhost:8000/static/images/insect.jpg',
        'http://localhost:8000/static/images/sunset.jpg'
    ]

    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    uri = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.uri
