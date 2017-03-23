from rest_framework import viewsets
from rest_framework import mixins

from api.models import Rating
from api.serializers import RatingSerializer


class RatingViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

