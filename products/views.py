from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializers
from . import permissions


# the set settings of paginations of all products
class ProductPagination(PageNumberPagination):
    page_size = 2


# the viewset of all products
class ProductAll(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = ProductPagination
    permission_classes = [
        permissions.IsAdminOrReadOnly
    ]
