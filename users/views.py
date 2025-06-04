from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample


@extend_schema(
    request=serializers.RegisterUserSerializer,
    examples=[
        OpenApiExample(
            'Register Example',
            value={
                "username": "testuser",
                "password": "StrongPassword123",
                "role": "USER|ADMIN"
            },
            request_only=True
        )
    ],
    responses={201: serializers.RegisterUserSerializer},
    description="Register or add a new user."
)
@api_view(['POST'])
def RegisterUser(request: Request):
    user = request.data
    serializer = serializers.RegisterUserSerializer(data=user)

    if (serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(
        {
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_201_CREATED)


@extend_schema(
    description='get all of the users',
    responses={200: serializers.UserSerializer}
)
@api_view(['GET'])
def AllUsers(request):
    users = models.CustomUser.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
