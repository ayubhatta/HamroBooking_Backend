from django.contrib import admin
from .models import Room, RoomMaintenance

@admin.register(Room)
class room_list(admin.ModelAdmin):
    list_display = ('id', 'price', 'room_type','floor', 'ac', 'wifi', 'attached_bathroom', 'wifi', 'tv', 'furniture', 'smooking', 'room_service', 'king_size_bed_count', 'queen_size_bed_count', 'single_bed_count', 'is_vacant', 'next_vacant_date')


@admin.register(RoomMaintenance)
class RoomMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('maintenance_id', 'room', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('maintenance_id', 'room__id')  
    date_hierarchy = 'start_date'

    readonly_fields = ('maintenance_id',)

    actions = ['mark_completed', 'mark_cancelled']

    def mark_completed(self, request, queryset):
        queryset.update(status=RoomMaintenance.MaintenanceStatus.COMPLETED.value)

    def mark_cancelled(self, request, queryset):
        queryset.update(status=RoomMaintenance.MaintenanceStatus.CANCELLED.value)

    mark_completed.short_description = 'Mark selected maintenance as completed'
    mark_cancelled.short_description = 'Mark selected maintenance as cancelled'