from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError

from rest_framework import serializers

from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','address','phone','user_type','password']

    def save(self):
        user = User(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email=self.validated_data['email'],
            address = self.validated_data['address'],
            phone = self.validated_data['phone'],
            user_type = "DEFAULT",
            password = self.validated_data['password'],
        )
        if user.phone == '':
            user.phone=None
        user.password = make_password(user.password)
        try:
            user.save()
        except IntegrityError as e:
            if 'Duplicate entry' in str(e) and 'user_user.phone' in str(e):
                raise serializers.ValidationError({'phone': 'Phone number already exists.'})
            else:
                raise e
        return user 

