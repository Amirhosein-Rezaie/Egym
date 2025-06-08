from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializeres
from .permissions import IsAdmin
from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# set the settings of the all blogs
class BlogPagination(PageNumberPagination):
    page_size = 2


# the viewset of all the blogs
class BlogAll(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializeres.BlogSerializer
    pagination_class = BlogPagination
    permission_classes = [
        IsAdmin
    ]


# search in the blogs
@api_view(['GET'])
def search_blogs(request: Request, search: str):
    blogs_found = models.Blog.objects.filter(title__icontains=search)

    serializer = serializeres.BlogSerializer(blogs_found, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
