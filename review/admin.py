from django.contrib import admin

from .models import Review


@admin.register(Review)
class review(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'star_count', 'comment', 'hotel_id')
    def user_id(self, obj):
        return obj.User.full_name