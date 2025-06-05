from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from .permissions import IsAdmin, IsAnonymous, user_required, anonymous_required
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404


# set settings for paginations of users
class UserPaginations(PageNumberPagination):
    page_size = 2


# the func for register a user and set documentation
@extend_schema(
    request=serializers.RegisterUserSerializer,
    examples=[
        OpenApiExample(
            'Register Example',
            value={
                "username": "testuser",
                "password": "StrongPassword123",
                "role": "USER|ADMIN",
                "phone": "string-11"
            },
            request_only=True
        )
    ],
    responses={201: serializers.RegisterUserSerializer},
    description="Register or add a new user. phone with 11 characters"
)
@api_view(['POST'])
@anonymous_required
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


# the function base view of all users and set documentation
@extend_schema(
    description='get all of the users',
    responses={200: serializers.UserSerializer}
)
@api_view(['GET'])
def AllUsers(request):
    users = models.CustomUser.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# viewset of all the users
class User_GET_All(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    pagination_class = UserPaginations
    queryset = models.CustomUser.objects.all()
    permission_classes = [
        IsAdmin
    ]


# custom login view
class CustomLoginView(TokenObtainPairView):
    permission_classes = [IsAnonymous]


# get one user
@api_view(['GET'])
def GetUser(request: Request, user_id: int):
    user = get_object_or_404(models.CustomUser, id=user_id)
    serializer = serializers.UserSerializer(user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
