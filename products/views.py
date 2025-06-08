from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializers
from . import permissions
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema


# the set settings of paginations of all products
class ProductPagination(PageNumberPagination):
    page_size = 2


# the viewset of all products
class ProductAll(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # pagination_class = ProductPagination
    permission_classes = [
        permissions.IsAdminOrReadOnly
    ]


# search in products
@extend_schema(
    responses={200: serializers.ProductSerializer}
)
@api_view(['GET'])
def search_products(request: Request, search: str):
    products_found = models.Product.objects.filter(name__icontains=search)

    paginator = PageNumberPagination()
    paginator.page_size = 2
    paginated_products = paginator.paginate_queryset(products_found, request)

    serialized_products = serializers.ProductSerializer(
        paginated_products, many=True)

    return paginator.get_paginated_response(data=serialized_products.data)
