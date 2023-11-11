from django.db import models

class MenuItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default='default.jpg')

    def __str__(self):
        return self.item_name
