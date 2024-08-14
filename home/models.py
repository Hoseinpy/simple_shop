from django.db import models
from django.contrib.auth.models import User


class Items(models.Model):
    picture = models.ImageField(upload_to='img/', null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Slider(models.Model):
    picture = models.ImageField(upload_to='img/', null=True)


class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    f_amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item.name}--{self.quantity}--{self.is_paid}'
