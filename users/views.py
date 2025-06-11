from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.pagination import PageNumberPagination
from . import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser


# set settings for paginations of users
class UserPaginations(PageNumberPagination):
    page_size = 2


# viewset of all the users
class User_GET_All(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    # pagination_class = UserPaginations
    queryset = models.CustomUser.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAnonymous()]
        if self.action in ['list', 'partial_update']:
            return [IsAdminUser()]
        if self.action in ['retrieve', 'destroy']:
            return [permissions.OwerUserORadmin()]
        return super().get_permissions()


# get all exercises
class GetAllExercisesViewset(viewsets.ModelViewSet):
    queryset = models.Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer
    permission_classes = [
        permissions.IsAdminOrReadOnly
    ]


# custome login
class TokenCustomLogin(TokenObtainPairView):
    permission_classes = [permissions.IsAnonymous]