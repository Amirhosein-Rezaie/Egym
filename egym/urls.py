from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from users import views as UsersViews
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

ExerciseRouter = DefaultRouter()
ExerciseRouter.register('', UsersViews.GetAllExercisesViewset)


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('blogs/', include('blogs.urls')),
    # swagger and documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(), name='swagger_ui'),
    # exercises url
    path('exercises/', include(ExerciseRouter.urls)),
    # login django users
    path('login', include('rest_framework.urls')),
    # token login
    path('token-login/', UsersViews.TokenCustomLogin.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
