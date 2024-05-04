from django.dispatch import receiver
from django.db.models import signals
from vendors.models import Vendor
from .models import HistoricalPerformance


@receiver(signals.post_save, sender=Vendor)
def create_historical_performance_model(sender, instance, created, **kwargs):
    if created:
        HistoricalPerformance.objects.create(vendor=instance,
                                             on_time_delivery_rate=instance.on_time_delivery_rate,
                                             quality_rating_avg=instance.quality_rating_avg,
                                             average_response_time=instance.average_response_time,
                                             fulfillment_rate=instance.fulfillment_rate)
    # when a model is updated
    else:
        # Fetch the existing instance from the database
        historical_performance_instance = HistoricalPerformance.objects.get(
            vendor__id=instance.id)

        # Update the attributes of the instance
        historical_performance_instance.on_time_delivery_rate = instance.on_time_delivery_rate
        historical_performance_instance.quality_rating_avg = instance.quality_rating_avg
        historical_performance_instance.average_response_time = instance.average_response_time
        historical_performance_instance.fulfillment_rate = instance.fulfillment_rate

        # Save the updated instance
        historical_performance_instance.save()
