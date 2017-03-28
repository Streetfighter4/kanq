from rest_framework import viewsets

from api.models import Image
from api.serializers import ImageSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
