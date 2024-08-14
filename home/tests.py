from django.urls import reverse
from rest_framework.test import APITestCase, force_authenticate, APIClient, APIRequestFactory
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Items, CartModel
from .views import AddToCart, DeleteFromCart


class TestHomeApp(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='Test123Password')
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.factor = APIRequestFactory()

        self.item = Items.objects.create(name='hjdf', description='iASHBDIASDeoifdjhe', price=10000)

    def test_get_items_list(self):
        response = self.client.get(reverse('item_list'))

        self.assertEqual(response.status_code, 200)

    def test_get_slider_list(self):
        response = self.client.get(reverse('slider'))

        self.assertEqual(response.status_code, 200)

    def test_create_cart(self):
        request = self.factor.post(reverse('add-to-cart'), {'item_id': self.item.id, 'quantity': 2})
        force_authenticate(request, self.user, self.token)
        response = AddToCart.as_view()(request)

        self.assertEqual(response.status_code, 201)

    def test_update_cart_item_quantity(self):
        CartModel.objects.create(user=self.user, item=self.item, quantity=1, f_amount=10000)

        request = self.factor.post(reverse('add-to-cart'), {'item_id': self.item.id, 'quantity': 2})
        force_authenticate(request, self.user, self.token)
        response = AddToCart.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_delete_cart(self):
        c = CartModel.objects.create(user=self.user, item=self.item, quantity=1, f_amount=10000)

        request = self.factor.post(reverse('delete-from-cart'), {'cart_id': c.id})
        force_authenticate(request, self.user, self.token)
        response = DeleteFromCart.as_view()(request)

        self.assertEqual(response.status_code, 204)

    def test_low_cart_item_quantity_number(self):
        c = CartModel.objects.create(user=self.user, item=self.item, quantity=2, f_amount=20000)

        request = self.factor.post(reverse('delete-from-cart'), {'cart_id': c.id})
        force_authenticate(request, self.user, self.token)
        response = DeleteFromCart.as_view()(request)

        self.assertEqual(response.status_code, 200)