from .models import Booking
from .serializers import BookingSerializer

from rest_framework.viewsets import ModelViewSet
# Create your views here.

class BookingViewset(ModelViewSet):
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}


