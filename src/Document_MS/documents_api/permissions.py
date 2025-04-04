from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Allows admin users to perform any action.
    Allows read-only access to non-admin users.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True  # Allow read-only access
        return request.user and request.user.is_staff  # Allow write access to admins only