from django.db import models
from enum import Enum

class Hotel(models.Model):
    class hotels_type(Enum):
        GUESTHOUSE = "GUESTHOUSE"
        HOMESTAY = "HOMESTAY"
        RESORT = "RESORT"

    hotel_name = models.CharField(blank=False, max_length=100)
    car_parking = models.BooleanField(default=False)
    bike_parking = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    pick_up = models.BooleanField(default=False)
    bed_breakfast = models.BooleanField(default=False)
    launch = models.BooleanField(default=False)
    party_area = models.BooleanField(default=False)
    hotel_type = models.CharField(choices=((x.value,x.name.title()) for x in hotels_type),null=False,max_length=50,blank=False)
    latitude = models.DecimalField(blank=False, max_digits=10, decimal_places=7)
    longitude = models.DecimalField(blank=False, max_digits=10, decimal_places=7)
    check_in_time = models.TimeField(auto_now_add=False, blank=False)
    check_out_time = models.TimeField(auto_now_add=False, blank=False)
    images = models.TextField(blank=False, max_length=16383, null=True)
    video = models.TextField(blank=False, max_length=16383, null=True)

    def __str__(self):
        return self.hotel_name

        
