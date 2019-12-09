from django.db import models
from django.urls import reverse

# Create your models here.


class brand(models.Model):
    brand = models.CharField(max_length=250)


    def get_absolute_url(self):
        return reverse('Music:details',kwargs={'pk': self.pk})
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class type(models.Model):
    brand_name = models.ForeignKey(brand, on_delete=models.CASCADE)
    brand_type = models.CharField(max_length=10)
    brand_in_ml = models.CharField(max_length=250)
    brand_price = models.CharField(max_length=150)
    brand_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title