from rest_framework import serializers
from .models import Room, RoomMaintenance

class RoomMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMaintenance
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    maintenance = RoomMaintenanceSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'


    