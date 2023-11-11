from django.contrib import admin
from .models import  Albumb, Photo


@admin.register(Albumb)
class Albumb_list(admin.ModelAdmin):
    list_display=('id', 'name', 'description', 'date_created', 'cover_photo')   

@admin.register(Photo)
class Photo_list(admin.ModelAdmin):
    list_display=('id', 'name', 'description','albumb', 'date_created', 'image')   