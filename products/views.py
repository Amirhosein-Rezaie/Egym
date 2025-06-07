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


# paginations for funstion base views
paginator = PageNumberPagination()


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


# search in products
@api_view(['GET'])
def serach_products(request: Request, search: str):
    products_found = models.Product.objects.filter(name=search)

    # pagination datas
    paginator.page_size = 2
    paginated_products = paginator.paginate_queryset(products_found)

    # serialize the datas
    serialized_products = serializers.ProductSerializer(
        data=paginated_products, many=True)

    if (serialized_products.is_valid()):
        return Response(data=serialized_products.data, status=status.HTTP_302_FOUND)

    return Response(data={
        'success': False,
        'error': serialized_products.errors
    }, status=status.HTTP_404_NOT_FOUND)
