from rest_framework import serializers

from apps.property_management.models.predio import Predio


class PredioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predio
        fields = '__all__'
