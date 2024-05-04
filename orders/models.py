from django.db import models
from vendors.models import Vendor
# Create your models here.

PENDING = 'pending'
ACKNOWLEDGED = 'acknowledged'
COMPLETED = 'completed'
CANCELED = 'canceled'

STATUS_CHOICES = [
    (PENDING, 'Pending'),
    (ACKNOWLEDGED, 'Acknowledged'),
    (COMPLETED, 'Completed'),
    (CANCELED, 'Canceled'),
]


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)
