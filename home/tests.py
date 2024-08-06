from django.urls import reverse
from rest_framework.test import APITestCase


class TestHomeApp(APITestCase):

    def test_get_items_list(self):
        response = self.client.get(reverse('item_list'))

        self.assertEqual(response.status_code, 200)

    def test_get_slider_list(self):
        response = self.client.get(reverse('slider'))

        self.assertEqual(response.status_code, 200)
