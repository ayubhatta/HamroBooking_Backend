from django.db import models

from room.models import Room
from user.models import User
from discount.models import Discount


class Booking(models.Model):

    # status confirmed, cancelled, pending
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
    )

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(auto_now_add=False, blank=False, null=True)
    check_out_date = models.DateTimeField(auto_now_add=False, blank=False, null=True)
    total_price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=False, blank=False, null=True)
    status = models.CharField(blank=False, max_length=50, null = True, choices=STATUS_CHOICES)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.booking_id