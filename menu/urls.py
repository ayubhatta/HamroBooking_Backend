from django.urls import path
from .views import MenuItemList, MenuItemDetail

urlpatterns = [
    path('menu/', MenuItemList.as_view(), name='menu_list'),
    path('menu/<int:pk>/', MenuItemDetail.as_view(), name='menu_detail'),
]
