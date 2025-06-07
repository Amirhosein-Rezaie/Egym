from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.ProductAll, basename='allProducts')

urlpatterns = [
    path('', include(router.urls)),
    path('<str:search>', views.serach_products)
]
