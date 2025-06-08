from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from functools import wraps


# a permission class for only admins
class IsAdmin(BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.is_staff == True


# a permission class for only users
class IsUser(BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.is_staff == False


# a permission class for only anonymous user
class IsAnonymous(BasePermission):
    def has_permission(self, request: Request, view):
        return not request.user or request.user.is_anonymous


# a permission decorator for only anonymous user
def anonymous_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user and user.is_authenticated:
            return Response({'detail': 'You are already logged in.'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


# a permission decorator for only users
def user_required(view_func):
    def _wrapped_view(request, *args, **kwargs):

        if getattr(request.user, 'role', None) != 'user':
            return Response({'detail': 'Only users with role=user are allowed.'}, status=status.HTTP_403_FORBIDDEN)

        return view_func(request, *args, **kwargs)
    return _wrapped_view


# only admins can edit ,delete ,add something
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view):
        if request.method in SAFE_METHODS:
            return True
        return getattr(request.user, 'is_staff', None) == True


class PostForAnonymousGetPutDeleteForAdmin(BasePermission):
    def has_permission(self, request: Request, view):
        user = request.user

        if request.method == 'POST':
            return not user.is_authenticated

        elif request.method in ['GET', 'DELETE', 'PUT']:
            return user.is_authenticated and user.is_staff

        return False
