from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Items


class TestHomeApp(APITestCase):

    def test_get_items_list(self):
        response = self.client.get(reverse('item_list'))

        self.assertEqual(response.status_code, 200)

    def test_get_items_detail(self):
        new_obj = Items.objects.create(name='jhzsdfbcv', description='hkjdbfahjk', price=10000)
        response = self.client.get(reverse('item_detail', args=[new_obj.name]))

        self.assertEqual(response.status_code, 200)
