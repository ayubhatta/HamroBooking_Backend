from django.db import models
from hotel.models import Hotel
from countries_plus.models import Country
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class Contact(models.Model):
    name = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField(unique=True, blank=False)
    address = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    state = models.CharField(max_length=255, blank=False)
    zipcode = models.CharField(max_length=10, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    operation_start_time = models.TimeField(default=datetime.time(4, 0))
    operation_end_time = models.TimeField(default=datetime.time(23, 0))

    def __int__(self):
        return self.name