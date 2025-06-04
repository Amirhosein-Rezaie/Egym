from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializers


class ProductPagination(PageNumberPagination):
    page_size = 2


class ProductAll(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = ProductPagination
