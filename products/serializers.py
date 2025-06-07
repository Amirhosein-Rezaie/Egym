from rest_framework.serializers import ModelSerializer
from . import models


class ImageSerilizer(ModelSerializer):
    class Meta:
        model = models.Image
        fields = ['id', 'file']


class ProductSerializer(ModelSerializer):
    images_product = ImageSerilizer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'