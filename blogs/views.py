from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializeres


class BlogPagination(PageNumberPagination):
    page_size = 2


class BlogAll(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializeres.BlogSerializer
    pagination_class = BlogPagination
