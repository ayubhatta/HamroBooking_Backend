
from rest_framework import serializers
from .models import Booking
from user.models import User


class BookingCustomerSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = User
            fields = ("first_name", "last_name", "email", "phone","last_login")


class BookingSerializer(serializers.ModelSerializer):

    customer = BookingCustomerSerializer(read_only=True)

    


    def save(self, **kwargs):

        customer = User.objects.get(id=self.context['user_id'])
        Booking.objects.create(customer=customer, **self.validated_data)
        
        
    
        
    class Meta:
        model = Booking
        fields = "__all__"
