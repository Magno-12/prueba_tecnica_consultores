from django.contrib.auth import authenticate

from rest_framework import serializers

from apps.user.models.user import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user is None or not user.is_active:
            raise serializers.ValidationError('Invalid email or password or user is not active')

        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }

class LogoutSerializer(serializers.Serializer):
    access_token = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        fields = ['refresh', 'access', 'user']

    def get_user(self, obj):
        try:
            user = User.objects.get(email=obj['email'])
            return {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

class LogoutResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(read_only=True)
