from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.BlogAll, basename='allBlogs')

urlpatterns = [
    path('', include(router.urls)),
    path('search/<str:search>', views.search_blogs)
]
