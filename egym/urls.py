from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from users import views


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('blogs/', include('blogs.urls')),
    path('login/', views.CustomLoginView.as_view()),
    path('register/', views.RegisterUser),
    # swagger and documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(), name='swagger_ui')
]
