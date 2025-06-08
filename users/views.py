from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.pagination import PageNumberPagination
from . import permissions
from rest_framework_simplejwt.views import TokenObtainPairView


# set settings for paginations of users
class UserPaginations(PageNumberPagination):
    page_size = 2


# viewset of all the users
class User_GET_All(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    # pagination_class = UserPaginations
    queryset = models.CustomUser.objects.all()
    permission_classes = [
        permissions.PostForAnonymousGetPutDeleteForAdmin
    ]


# custom login view
class CustomLoginView(TokenObtainPairView):
    permission_classes = [permissions.IsAnonymous]


# get all exercises
class GetAllExercisesViewset(viewsets.ModelViewSet):
    queryset = models.Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer
    permission_classes = [
        permissions.IsAdminOrReadOnly
    ]
