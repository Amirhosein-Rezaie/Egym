from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission
)


class IsAdminOrReadonly(BasePermission):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS):
            return True
        if (request.method not in SAFE_METHODS):
            return bool(request.user.is_staff == True)
        return super().has_permission(request, view)
