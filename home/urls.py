from django.urls import path
from . import views

urlpatterns = [
    path('items_list', views.ItemList.as_view(), name='item_list'),
    path('items_list/<str:name>', views.ItemDetail.as_view(), name='item_detail'),
]