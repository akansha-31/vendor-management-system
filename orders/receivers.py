from django.db.models import signals, Avg
from django.dispatch import receiver
from .models import PurchaseOrder, COMPLETED
from vendors.models import Vendor
from django.utils import timezone


@receiver(signal=signals.post_save, sender=PurchaseOrder)
def calculate_performance_metrics(sender, instance, created, **kwargs):
    """
    Calculate performance metrics for the vendor associated with the saved PurchaseOrder.

    This function is a signal receiver that is triggered after any change in PurchaseOrder status

    Args:
        sender: The model class that sent the signal (PurchaseOrder).
        instance: The instance of the saved PurchaseOrder.
        created: A boolean indicating whether the PurchaseOrder was created or updated.
        **kwargs: Additional keyword arguments.

    Raises:
        Vendor.DoesNotExist: If the vendor associated with the PurchaseOrder does not exist.

    """
    # If the PurchaseOrder is updated
    if not created:
        now = timezone.now()
        # Count total orders for the vendor
        orders_count = PurchaseOrder.objects.filter(
            vendor_id=instance.vendor_id).count()

        # Filter completed orders for the vendor
        completed_orders = PurchaseOrder.objects.filter(
            vendor_id=instance.vendor_id, status=COMPLETED)
        completed_orders_count = completed_orders.count()

        try:
            vendor_object = Vendor.objects.get(pk=instance.vendor_id)
        except Vendor.DoesNotExist:
            # Handle case where vendor does not exist
            raise Vendor.DoesNotExist(
                "Vendor with id {} does not exist.".format(instance.vendor_id))

        # If the PurchaseOrder status is completed
        if instance.status == COMPLETED:
            # Count on-time completed orders
            on_time_completed_orders_count = completed_orders.filter(
                delivery_date__gte=now).count()

            # Calculate on-time delivery rate
            vendor_object.on_time_delivery_rate = (
                on_time_completed_orders_count/completed_orders_count)

            # If quality rating is provided, calculate average quality rating
            if instance.quality_rating != 0.0:
                average_quality_rating = completed_orders.aggregate(
                    avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
                vendor_object.quality_rating_avg = average_quality_rating

        # Calculate fulfillment rate
        vendor_object.fulfillment_rate = (completed_orders_count/orders_count)
        vendor_object.save()
