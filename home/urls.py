from django.urls import path
from . import views

urlpatterns = [
    path('items_list', views.ItemList.as_view(), name='item_list'),
    path('slider', views.SliderList.as_view(), name='slider'),
    path('add_to_cart', views.AddToCart.as_view(), name='add-to-cart'),
    path('delete_from_cart', views.DeleteFromCart.as_view(), name='delete-from-cart'),
]