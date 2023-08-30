from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Permiso personalizado para verificar si el usuario es propietario del predio.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.owner in obj.propietarios.all()
