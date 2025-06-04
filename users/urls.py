from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.RegisterUser),
    path('all/', views.AllUsers),
    path('login/', TokenObtainPairView.as_view()),
    path('refreshlogin/', TokenRefreshView.as_view()),
]
