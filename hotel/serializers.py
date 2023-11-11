from .models import Hotel
from rest_framework import serializers


class PropertyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name','car_parking','bike_parking', 'pool','pick_up','bed_breakfast','launch','party_area','hotel_type','latitude','longitude','check_in_time', 'check_out_time','images','video']
    
    def save(self):

        
        hotel = Hotel(
            hotel_name = self.validated_data['hotel_name'],
            car_parking = self.validated_data['car_parking'],
            bike_parking = self.validated_data['bike_parking'],
            pool = self.validated_data['pool'],
            pick_up = self.validated_data['pick_up'],
            bed_breakfast = self.validated_data['bed_breakfast'],
            launch = self.validated_data['launch'],
            party_area = self.validated_data['party_area'],
            hotel_type = self.validated_data['hotel_type'],
            latitude = self.validated_data['latitude'],
            longitude = self.validated_data['longitude'],
            check_in_time = self.validated_data['check_in_time'],
            check_out_time = self.validated_data['check_out_time'],
            images = self.validated_data['images'],
            video = self.validated_data['video'],
        )

        hotel.save()
        return hotel
    
    