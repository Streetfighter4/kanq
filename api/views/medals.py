from rest_framework import viewsets

from api.models import Medal
from api.serializers import MedalSerializer


class MedalViewSet(viewsets.ModelViewSet):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer

