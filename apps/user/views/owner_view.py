from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from apps.user.models.owner import Owner
from apps.user.serializers.owner_serializer import OwnerSerializer
from apps.property_management.permissions import IsOwner


class OwnerViewSet(GenericViewSet):

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsOwner()]

    def list(self, request):
        """
        
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
