from django.test import TestCase
from .models import Vendor
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.


class TestVendorViewSet(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Test Vendor')
        return super().setUp()

    def test_get_all_vendors(self):
        response = self.client.get('/api/vendors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_vendor(self):
        response = self.client.get(f'/api/vendors/{self.vendor.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vendor(self):
        data = {'name': 'new vendor', 'contact_details': 'test',
                'address': 'test', 'vendor_code': 'test'}
        response = self.client.post('/api/vendors/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_vendor(self):
        response = self.client.delete(f'/api/vendors/{self.vendor.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
