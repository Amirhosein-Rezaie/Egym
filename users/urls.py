from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.User_GET_All, basename='getAllusers')

urlpatterns = [
    path('register/', views.RegisterUser),
    # path('', views.AllUsers),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
    path('refreshlogin/', TokenRefreshView.as_view()),
]
