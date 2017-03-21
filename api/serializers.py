from rest_framework.serializers import ModelSerializer

from api.models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'uri', 'createdAt')
