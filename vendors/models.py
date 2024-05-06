from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contact_details = models.TextField(unique=True)
    address = models.TextField(unique=True)
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
