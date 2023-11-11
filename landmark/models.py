from django.db import models
from countries_plus.models import Country


# Create your models here.
class Landmark(models.Model):
    id = models.AutoField
    name = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=False, max_length=500)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(blank=False, max_length=50)
    postal_code = models.IntegerField(blank=False, default=0)
    street1 = models.CharField(blank=False,null=True, max_length=100)
    street2 = models.CharField(blank=False,null=True, max_length=100)

    def __str__(self):
        return self.name

