from rest_framework.serializers import ModelSerializer
from .models import Image


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
