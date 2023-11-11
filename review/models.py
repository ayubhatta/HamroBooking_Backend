from enum import Enum

from django.db import models

from hotel.models import Hotel
from user.models import User


class Review(models.Model):
    class star(Enum):
        ONE = "1"
        TWO = "2"
        THREE = "3"
        FOUR = "4"
        FIVE = "5"
    user_id  = models.ForeignKey(User,blank=False, on_delete=models.CASCADE, null=True)
    star_count = models.CharField(choices=((x.value,x.name.title()) for x in star),null=False,max_length=50,blank=False)
    comment = models.CharField(max_length=255)
    hotel_id = models.ForeignKey(Hotel, blank=True, on_delete=models.CASCADE,  null=True)