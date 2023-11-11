from django.contrib import admin
from .models import Discount

@admin.register(Discount)
class discount_list(admin.ModelAdmin):
    list_display=('id', 'name', 'type', 'description', 'banner', 'amount', 'start_date', 'end_date')