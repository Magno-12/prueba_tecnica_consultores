from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permiso personalizado para verificar si el usuario es propietario del predio.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the predio.
        return request.user.owner in obj.propietarios.all()
    