from django.test import TestCase
from .models import PurchaseOrder, STATUS_CHOICES
from vendors.models import Vendor
from rest_framework import status
from rest_framework.test import APIClient
from django.utils import timezone

# Create your tests here.


class TestPurchaseOrderViewSet(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Test Vendor')
        now = timezone.now()
        self.purchase_order = PurchaseOrder.objects.create(po_number='123', delivery_date=now, items={
                                                           "1": "one"}, quantity=2, issue_date=now, vendor=self.vendor)
        return super().setUp()

    def test_get_all_orders(self):
        response = self.client.get('/api/purchase_orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_order(self):
        response = self.client.get(
            f'/api/purchase_orders/{self.purchase_order.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        payload = {
            'po_number': '123',
            'vendor': self.vendor.id,
            'delivery_date': '2024-05-15T10:00:00Z',
            'items': {"item1": "description1"},
            'quantity': 1,
            'status': STATUS_CHOICES[0][0],
            'issue_date': '2024-05-10T10:00:00Z',
        }
        response = self.client.post(
            '/api/purchase_orders/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_order(self):
        response = self.client.delete(
            f'/api/purchase_orders/{self.vendor.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_acknowledge_order(self):
        response = self.client.post(
            f'/api/purchase_orders/{self.purchase_order.id}/acknowledge/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
