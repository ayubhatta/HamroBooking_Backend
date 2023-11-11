from django.urls import path
from .views import create_list_view, detail_update_delete_view, create_list_maintenance_view, detail_update_delete_maintenance_view

app_name = "room"

urlpatterns = [
    path('', create_list_view, name='create_room'),
    path('<int:pk>', detail_update_delete_view, name="get_room"),
    path('roommaintenance/', create_list_maintenance_view, name='create_room_maintenance'),
    path('roommaintenance/<int:pk>', detail_update_delete_maintenance_view, name="get_room_maintenance"),
]
