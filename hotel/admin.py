from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class hotel_list(admin.ModelAdmin):

    list_display = ('id', 'hotel_name','hotel_type', 'car_parking', 'bike_parking', 'pool', 'pick_up', 'bed_breakfast', 'launch', 'party_area','latitude', 'longitude', 'check_in_time', 'check_out_time','images','video')
