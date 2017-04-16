from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.models import User
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes_by_action = {'create': []}

    @detail_route(methods=['put'])
    def follow(self, request, pk=None): # follows a given user
        pass

    @detail_route(methods=['put'])
    def unfollow(self, request, pk=None): # unfollows a given user
        pass

    @detail_route(methods=['get'])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    # Override create to return token
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        response = serializer.data
        response['access_token'] = Token.objects.get(user=user).key
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    # Token isn't required when creating user (signup)
    def get_permissions(self):
        if self.action in self.permission_classes_by_action.keys():
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        else:
            return [permission() for permission in self.permission_classes]
