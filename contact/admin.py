from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class contact_list(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'country', 'latitude', 'longitude', 'operation_start_time', 'operation_end_time')
