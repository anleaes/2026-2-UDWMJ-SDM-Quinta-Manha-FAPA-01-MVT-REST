from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
   age = serializers.IntegerField(read_only=True)

   class Meta:
        model = Animal