from rest_framework.permissions import BasePermission, SAFE_METHODS

class RolePermission(BasePermission):
    """
    Allows access based on user role.
    """

    def has_permission(self, request,view):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.role == "superadmin":
            return True

        if user.role == "admin":
            return request.method in ["GET", "PUT"]

        if user.role == "user":
            return request.method in SAFE_METHODS  

        return False
