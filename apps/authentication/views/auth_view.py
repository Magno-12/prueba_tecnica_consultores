from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotAuthenticated
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.exceptions import NotAuthenticated
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken,  OutstandingToken

from apps.authentication.serializers.auth_serializer import (
    LoginSerializer,
    LogoutSerializer,
    LoginResponseSerializer,
    LogoutResponseSerializer
)
from apps.user.models.user import User

import logging

logger = logging.getLogger(__name__)


class AuthViewSet(GenericViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        if self.action == 'logout':
            return LogoutSerializer

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """
        ...
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data

        try:
            user = User.objects.get(id=user_data['id'])
        except User.DoesNotExist:
            raise NotAuthenticated("User not found")

        refresh = RefreshToken.for_user(user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user_data,
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        """
        ...
        """
        token = request.data.get('access_token')

        if not token:
            return Response({"detail": "Token not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            AccessToken(token)
        except TokenError:
            return Response({"detail": "Token error during logout"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(status=status.HTTP_200_OK)
