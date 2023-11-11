from django.db import models



class Albumb(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    cover_photo = models.TextField()

    def __str__(self):
        return self.name

class Photo(models.Model):
    albumb = models.ForeignKey(Albumb, on_delete=models.CASCADE, related_name='photos')
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    location_taken = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.TextField()


    def __str__(self):
        return self.name