from django.db import models

class Social_media(models.Model):
    name = models.CharField(max_length=255, blank=False)
    icon = models.TextField()
    link = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name