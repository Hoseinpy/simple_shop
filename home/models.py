from django.db import models


class Items(models.Model):
    picture = models.ImageField(upload_to='img/', null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


