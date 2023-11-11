from enum import Enum

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    class users_type(Enum):
        DEFAULT = "DEFAULT"
        ADMIN = "ADMIN"
        EDITOR = "EDITOR"
    id = models.AutoField
    first_name = models.CharField(blank=False,null=False,max_length=100)
    last_name = models.CharField(blank=False,null=False,max_length=100)
    email = models.EmailField(blank=False,null=False,max_length=50, unique=True)
    password = models.CharField(blank=False,null=False, max_length=255)
    address = models.CharField(blank=False,null=False,max_length=50)
    phone = PhoneNumberField(unique=True, blank=False, null=False)
    user_type = models.CharField(choices=((x.value,x.name.title()) for x in users_type),null=False,max_length=50,blank=False)
    created_at =models.DateTimeField(auto_now_add=True,null=False)
    updated_at = models.DateTimeField(auto_now=True,null=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone']

    objects = CustomUserManager()



    

    # def if_exist(self):
    #     if User.objects.filter(email=self.email):
    #         return True

    #     return False



