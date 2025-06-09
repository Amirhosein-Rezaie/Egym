from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


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
    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)


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
            user_id_from_url = view.kwargs.get('id') or view.kwargs.get('pk')

            if user.is_authenticated and user_id_from_url:
                return int(user_id_from_url) == int(user.id)

            return user.is_authenticated and user.is_staff
        return False


# post user for only quests
class QuestsOnly(BasePermission):
    def has_permission(self, request, view):
        return not request.user or not request.user.is_authenticated
