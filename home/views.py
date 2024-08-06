from rest_framework import generics
from .serializers import ItemsSerializer, SliderSerializer
from .models import Items, Slider


class ItemList(generics.ListAPIView):
    serializer_class = ItemsSerializer
    queryset = Items.objects.filter(is_active=True)


class SliderList(generics.ListAPIView):
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()
