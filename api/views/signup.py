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
        return Response(new_user, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)