from django.contrib import admin

from .models import Items, Slider, CartModel

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']