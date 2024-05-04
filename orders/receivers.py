from django.db.models import signals, Avg
from django.dispatch import receiver
from .models import PurchaseOrder, COMPLETED
from vendors.models import Vendor
from django.utils import timezone


@receiver(signal=signals.post_save, sender=PurchaseOrder)
def calculate_performance_metrics(sender, instance, created, **kwargs):
    if not created:
        now = timezone.now()
        orders_count = PurchaseOrder.objects.filter(
            vendor_id=instance.vendor_id).count()
        completed_orders = PurchaseOrder.objects.filter(
            vendor_id=instance.vendor_id, status=COMPLETED)
        completed_orders_count = completed_orders.count()
        vendor_object = Vendor.objects.get(pk=instance.vendor_id)

        if instance.status == COMPLETED:
            on_time_completed_orders_count = completed_orders.filter(
                delivery_date__gte=now).count()
            vendor_object.on_time_delivery_rate = (
                on_time_completed_orders_count/completed_orders_count)

            if instance.quality_rating != 0.0:
                average_quality_rating = completed_orders.aggregate(
                    avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
                vendor_object.quality_rating_avg = average_quality_rating

        vendor_object.fulfillment_rate = (completed_orders_count/orders_count)
        vendor_object.save()
