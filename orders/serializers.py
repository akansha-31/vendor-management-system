from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializerForGet(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = [
            'po_number',
            'vendor',
            'order_date',
            'delivery_date',
            'items',
            'quantity',
            'status',
            'quality_rating',
            'issue_date',
            'acknowledgment_date',
        ]


class PurchaseOrderSerializerForPost(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = [
            'po_number',
            'vendor',
            'delivery_date',
            'items',
            'quantity',
            'quality_rating',
            'status',
            'issue_date',
        ]
