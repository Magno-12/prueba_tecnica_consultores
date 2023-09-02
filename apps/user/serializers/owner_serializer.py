from rest_framework import serializers

from apps.user.models.owner import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
