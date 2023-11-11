from django.contrib import admin

from .models import MenuItem


@admin.register(MenuItem)
class menu(admin.ModelAdmin):
    list_display = ('item_name', 'description', 'price', 'ingredients', 'image')