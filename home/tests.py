from rest_framework.test import APITestCase
from django.urls import reverse


class TestHomeApp(APITestCase):

    def test_get_items_list(self):
        response = self.client.get(reverse('item_list'))

        self.assertEqual(response.status_code, 200)
