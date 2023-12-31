from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from apps.property_management.models.predio import Predio
from apps.property_management.serializers.predio_serializer import PredioSerializer
from apps.property_management.permissions import IsOwner


class PredioViewSet(GenericViewSet):

    queryset = Predio.objects.all()
    serializer_class = PredioSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsOwner()]

    def list(self, request):
        """
        Endpoint: Listado de predios
        ---
        Body: N/A
        ---
        Response:
        [
            {
                "id": 1,
                "nombre_direccion": "Calle principal 123",
                "tipo": "Casa",
                "numero_catastral": "1234567890",
                "numero_matricula": "ABC1234567890",
                "propietarios": [1, 2, 3]
            },
        ]
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Endpoint: Crear un nuevo predio
        ---
        Body:
        {
            "nombre_direccion": "Calle principal 123",
            "tipo": "Casa",
            "numero_catastral": "1234567890",
            "numero_matricula": "ABC1234567890",
            "propietarios": [1, 2, 3]
        }
        ---
        Response:
        {
            "id": str,
            "nombre_direccion": "Calle principal 123",
            "tipo": "Casa",
            "numero_catastral": "1234567890",
            "numero_matricula": "ABC1234567890",
            "propietarios": [1, 2, 3]
        }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        """
        Endpoint: Actualizar detalles de un predio
        ---
        Body:
        {
            "nombre_direccion": "Calle principal 456",
            "tipo": "Apartamento",
            "numero_catastral": "0987654321",
            "numero_matricula": "ZYX0987654321",
            "propietarios": [2, 3, 4]
        }
        ---
        Response:
        {
            "id": str,
            "nombre_direccion": "Calle principal 456",
            "tipo": "Apartamento",
            "numero_catastral": "0987654321",
            "numero_matricula": "ZYX0987654321",
            "propietarios": [2, 3, 4]
        }
        """
        predio = self.get_object()
        if request.user.owner not in predio.propietarios.all():
            return Response({"detail": "No tienes permiso para editar este predio."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(predio, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Endpoint: Eliminar un predio
        ---
        Body: N/A
        ---
        Response:
        {
            "detail": "Predio eliminado con éxito."
        }
        """
        predio = self.get_object()
        if request.user.owner not in predio.propietarios.all():
            return Response({"detail": "No tienes permiso para eliminar este predio."},
                status=status.HTTP_403_FORBIDDEN
            )

        predio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
