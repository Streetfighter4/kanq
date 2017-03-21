from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Image
from api.serializers import ImageSerializer


class ImageList(APIView):

    def get(self, request, format=None):
        allImages = Image.objects.all()
        serializer = ImageSerializer(allImages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

