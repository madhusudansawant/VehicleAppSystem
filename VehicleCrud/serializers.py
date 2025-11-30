from rest_framework import serializers
from .models import VehicleModel

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['id', 'vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description', 'created_at']
        read_only_fields = ['id', 'created_at']  
