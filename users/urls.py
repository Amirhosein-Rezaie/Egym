from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.Users, basename='getAllusers')

urlpatterns = [
    # path('', views.AllUsers),
    path('', include(router.urls)),
    path('refreshlogin/', TokenRefreshView.as_view()),
]
