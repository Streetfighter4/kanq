from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import UserSerializer
from api.models import User


@api_view(['POST'])
def signup(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        new_user = serialized.save()
        serialized_new_user = UserSerializer(new_user)
        return Response(serialized_new_user.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)