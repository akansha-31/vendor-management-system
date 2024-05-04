from django.test import TestCase
from .models import Vendor
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.


class TestVendorPerformanceViewse(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Test Vendor')
        return super().setUp()

    def test_get_all_vendors(self):
        response = self.client.get(
            f'/api/vendors/{self.vendor.id}/performance/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
