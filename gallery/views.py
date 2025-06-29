from django.shortcuts import render
from .models import Image
from .serializers import GallerySerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadonly


class Gallery(ModelViewSet):
    serializer_class = GallerySerializer
    queryset = Image.objects.all()
    permission_classes = [IsAdminOrReadonly]
