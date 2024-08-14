from rest_framework import serializers

from .models import Items, Slider


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['picture', 'name', 'description', 'price', 'is_active']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['picture']



class AddToCartSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class DeleteFromCartSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField()