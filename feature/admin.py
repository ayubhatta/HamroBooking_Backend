from django.contrib import admin
from .models import  Feature


@admin.register(Feature)
class Albumb_list(admin.ModelAdmin):
    list_display=('id', 'title', 'description','type', 'cover_image', 'albumb')   

  