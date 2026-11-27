from rest_framework import serializers

from animals.models import Animal

from .models import Vaccine


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'


class VaccineNextDoseQuerySerializer(serializers.Serializer):
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all())
