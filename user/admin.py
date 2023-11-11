from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserManager

from .models import User


class UserAdmin(BaseUserManager):
    ordering=['id']
    list_display = ['id','first_name','last_name', 'email', 'password', 'address', 'phone', 'user_type', 'created_at', 'updated_at', 'is_active','is_staff', 'is_admin', 'is_superuser',]
    add_fieldsets = ((None, {"fields":('first_name','last_name','email','password1','password2', 'address', 'phone', 'user_type',)}),)
    search_fields =('email',)

admin.site.register(User, UserAdmin)