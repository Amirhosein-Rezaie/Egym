from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Gallery

router = DefaultRouter()
router.register('', Gallery, basename='Gallery')

urlpatterns = [
    path('', include(router.urls)),
]
