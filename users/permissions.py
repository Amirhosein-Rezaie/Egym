from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser


# a permission class for only users
class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff == False


# a permission class for only anonymous user
class IsAnonymous(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user == AnonymousUser
        )


# only admins can edit ,delete ,add something
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return getattr(request.user, 'is_staff', None) == True


# return a user if user is the user has logged in
class OwerUserORadmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.id == obj.id or
            request.user.is_staff == True
        )
