from django.contrib import admin
from .models import Landmark


admin.site.site_header = "Hamro Booking Admin"
admin.site.site_title = "Hamro Booking Admin"



# Register your models here.
@admin.register(Landmark)
class landmark(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'state', 'postal_code', 'street1', 'street2')