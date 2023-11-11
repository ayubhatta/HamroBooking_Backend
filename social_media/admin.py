from django.contrib import admin
from .models import Social_media

@admin.register(Social_media)
class Media_list(admin.ModelAdmin):
    list_display=('id', 'name', 'icon', 'link', 'description')