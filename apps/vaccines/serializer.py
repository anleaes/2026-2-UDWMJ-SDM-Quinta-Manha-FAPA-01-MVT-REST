from rest_framework import serializers
from .models import Vaccine


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
