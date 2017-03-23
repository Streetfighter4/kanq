from rest_framework import viewsets
from rest_framework.decorators import detail_route

from api.models import User
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['put'])
    def follow(self, request, pk=None): # follows a given user
        pass

    @detail_route(methods=['put'])
    def unfollow(self, request, pk=None): # unfollows a given user
        pass
