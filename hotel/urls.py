from django.urls import path
from .views import HotelListCreateView, HotelRetrieveUpdateDeleteView

app_name = 'hotel'

urlpatterns = [
    path('hotel/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotel/<int:pk>/', HotelRetrieveUpdateDeleteView.as_view(), name='hotel-retrieve-update-delete'),
]
