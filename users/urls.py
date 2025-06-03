from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.UserAdd)

urlpatterns = [
    path('register/', include(router.urls))
]
