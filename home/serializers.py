from rest_framework import serializers
from .models import Items


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['picture', 'name', 'description', 'price', 'is_active']