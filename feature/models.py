from django.db import models

from gallery.models import Albumb,Photo

class Feature(models.Model):
    TYPE_CHOICES = (
        ('amenities', 'Amenities'),
        ('services', 'Services'),
        ('activities', 'Activities'),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    cover_image = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True, null=True)
    albumb = models.ForeignKey(Albumb, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
