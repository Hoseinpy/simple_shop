from rest_framework import generics
from .serializers import ItemsSerializer, ItemsDetailSerializer
from .models import Items


class ItemList(generics.ListAPIView):
    serializer_class = ItemsSerializer
    queryset = Items.objects.filter(is_active=True)


class ItemDetail(generics.RetrieveAPIView):
    serializer_class = ItemsDetailSerializer
    queryset = Items.objects.filter(is_active=True)
    lookup_field = 'name'

