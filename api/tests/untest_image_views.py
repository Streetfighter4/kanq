from django.test import TestCase
from django.urls import resolve
from api.models import Image
from api.serializers import ImageSerializer
from rest_framework import status
from rest_framework.test import APIRequestFactory

from api.views.images import ImageViewSet


class ImageListViewTest(TestCase):
    def setUp(self):
        self.view = ImageViewSet.as_view()
        self.factory = APIRequestFactory()
        self.correct_data = {'uri': '/some/path/to/image.png'}
        self.error_data = {'random': 'random^2'}
        image = Image(uri='/some/path/to/Image1.png')
        image.save()
        image = Image(uri='/some/path/to/Image2.png')
        image.save()
        image = Image(uri='/some/path/to/Image3.png')
        image.save()

    def test_view_returns_all_images_on_get(self):
        request = self.factory.get('/api/images/', format='json')
        response = self.view(request)
        serializer = ImageSerializer(Image.objects.all(), many=True)
        self.assertEqual(serializer.data, response.data)

    def test_view_creates_image_correctly(self):
        request = self.factory.post('/api/images/', self.correct_data, format='json')
        response = self.view(request)
        self.assertEqual(response.data['uri'], self.correct_data['uri'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.latest('createdAt').uri, self.correct_data['uri'])

    def test_view_returns_error_with_incorrect_data(self):
        request = self.factory.post('/api/images/', self.error_data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data['uri'])


class ImageViewsRouteTest(TestCase):

    def setUp(self):
        self.view = ImageList.as_view()

    def test_images_main_route(self):
        view = resolve('/api/images/')
        self.assertEqual(view.func.__name__, self.view.__name__)
