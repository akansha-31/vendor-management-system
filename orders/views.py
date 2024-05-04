from rest_framework import viewsets
from rest_framework.response import Response
from .models import PurchaseOrder
from vendors.models import Vendor
from datetime import datetime
from django.utils import timezone
import pytz
from orders.models import ACKNOWLEDGED

from .serializers import PurchaseOrderSerializerForGet, PurchaseOrderSerializerForPost
# Create your views here.


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor_id = self.request.query_params.get('vendor')
        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PurchaseOrderSerializerForGet
        elif self.request.method == "POST" or "PUT":
            return PurchaseOrderSerializerForPost


class AcknowledgePurchaseOrderViewSet(viewsets.ViewSet):
    # average response time - Calculated each time a PO is acknowledged by the vendor.

    def calculate_average_response_time(self, vendor, order):
        issue_date = order.issue_date
        acknowledgment_date = order.acknowledgment_date
        time_difference = acknowledgment_date - issue_date
        total_seconds = time_difference.total_seconds()

        count = PurchaseOrder.objects.filter(
            vendor_id=order.vendor_id, status=ACKNOWLEDGED).count()
        count = count + 1

        return (vendor.average_response_time + total_seconds) / (count*3600)

    def create(self, request, pk=None):
        order_instance = PurchaseOrder.objects.get(pk=pk)
        vendor_instance = Vendor.objects.get(pk=order_instance.vendor_id)

        if order_instance.status == ACKNOWLEDGED:
            return Response("Order is already Acknowledged.")
        else:
            order_instance.status = ACKNOWLEDGED

        tz = pytz.timezone('UTC')
        order_instance.acknowledgment_date = datetime.now(tz=tz)

        average_response_time = self.calculate_average_response_time(
            vendor_instance, order_instance)
        vendor_instance.average_response_time = average_response_time

        order_instance.save()
        vendor_instance.save()

        return Response("Order Acknowledged")
