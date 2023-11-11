from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class booking_list(admin.ModelAdmin):
    list_display = ('id', 'room', 'customer', 'check_in_date', 'check_out_date', 'total_price', 'booking_date', 'status', 'discount')