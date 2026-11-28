from .models import Vaccination
from rest_framework import serializers

class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = '__all__'
        read_only_fields = ['applied_at']