from rest_framework import viewsets

from api.models import Badge
from api.serializers import BadgeSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
