from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class UserAdd(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.RegisterUserSerializer
