from enum import Enum

from django.db import models

class Room(models.Model):
    class rooms_type(Enum):
        DELUXE = "DELUXE"
        LUXURY = "LUXURY"
    
    id = models.AutoField
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    room_type = models.CharField(choices=((x.value,x.name.title()) for x in rooms_type),null=False,max_length=50,blank=False)
    floor = models.CharField(blank=False, max_length=50, null = True)
    ac = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    attached_bathroom = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    furniture = models.BooleanField(default=False)
    smooking = models.BooleanField(default=False)
    room_service = models.BooleanField(default=False)
    king_size_bed_count = models.IntegerField(default=0)
    queen_size_bed_count = models.IntegerField(default=0)
    single_bed_count = models.IntegerField(default=0)      
    is_vacant = models.BooleanField(default=True)
    next_vacant_date = models.DateTimeField(auto_now_add=False, blank=False, null=True)
    
    
class RoomMaintenance(models.Model):
    class MaintenanceStatus(Enum):
        IN_PROGRESS = "In Progress"
        COMPLETED = "Completed"
        CANCELLED = "Cancelled"

    maintenance_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        choices=[(status.value, status.name) for status in MaintenanceStatus],
        default=MaintenanceStatus.IN_PROGRESS.value,
        max_length=20,
    )

    def __str__(self):
        return f"Room Maintenance ID: {self.maintenance_id}, Room ID: {self.room.id}"