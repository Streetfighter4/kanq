from rest_framework import serializers
from .models.image import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'uri', 'createdAt')
