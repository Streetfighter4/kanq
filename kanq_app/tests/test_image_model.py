from django.test import TestCase
from django.utils import timezone

from kanq_app.models.image import Image


class ImageModelTest(TestCase):

    def setUp(self):
        self.image = Image(uri='/image/path/to/image.png')

    def test_image_adds_correctly(self):
        before = Image.objects.count()
        self.image.save()
        after = Image.objects.count()
        self.assertEqual(before + 1, after)


    def test_image_adds_with_current_time(self):
        now = timezone.now()
        self.image.save()
        self.assertTrue((self.image.createdAt - now).seconds < 30)
