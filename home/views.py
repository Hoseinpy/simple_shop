from rest_framework import generics
from .serializers import ItemsSerializer
from .models import Items


class ItemList(generics.ListAPIView):
    serializer_class = ItemsSerializer
    queryset = Items.objects.filter(is_active=True)
