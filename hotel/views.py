from rest_framework import generics
from .models import Hotel
from .serializers import PropertyRegistrationSerializer

class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = PropertyRegistrationSerializer

class HotelRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = PropertyRegistrationSerializer


