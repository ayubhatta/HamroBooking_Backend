from django.urls import path

from .views import registration_view, users_view, user_login, activate_account

app_name = "user"

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('delete/<int:id>', users_view, name="delete"),
    path('login/', user_login, name="login"),
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate'),
]
