from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import CartModel

from .serializers import ItemsSerializer, SliderSerializer, AddToCartSerializer, DeleteFromCartSerializer
from .models import Items, Slider


class ItemList(generics.ListAPIView):
    serializer_class = ItemsSerializer
    queryset = Items.objects.filter(is_active=True)


class SliderList(generics.ListAPIView):
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()


class AddToCart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)
        if serializer.is_valid():
            item_id = serializer.data.get('item_id')
            quantity = int(serializer.data.get('quantity'))

            item = Items.objects.filter(id=item_id).first()
            if item:
                user_card = CartModel.objects.filter(item=item).first()
                if user_card:
                    user_card.quantity += quantity
                    user_card.f_amount += item.price * quantity
                    user_card.save()

                    return Response({'status': 'success', 'message': 'successfully update quantity item'},
                                    status=status.HTTP_200_OK)

                else:
                    f_a = item.price * quantity
                    CartModel.objects.create(user=request.user, item=item, quantity=quantity, f_amount=f_a)

                    return Response({'status': 'success', 'message': 'Cart created successfully'},
                                    status=status.HTTP_201_CREATED)

            return Response({'status': 'failed', 'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteFromCart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeleteFromCartSerializer(data=request.data)
        if serializer.is_valid():
            cart = CartModel.objects.filter(id=serializer.data.get('cart_id')).first()
            if cart:
                if cart.quantity > 1:
                    cart.quantity -= 1
                    cart.f_amount -= cart.item.price

                    cart.save()

                    return Response({'status': 'success', 'message': 'successfully low cart item quantity number'},
                                    status=status.HTTP_200_OK)
                else:
                    cart.delete()
                    return Response({'status': 'success', 'message': 'successfully delete cart'},
                                    status=status.HTTP_204_NO_CONTENT)

            return Response({'status': 'failed', 'message': 'cart not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
