from django.db import models

# Create your models here.
class photo(models.Model):
    img = models.ImageField()

class Reviews(models.Model):
    

class BoothList(models.Model):
    BthName = models.CharField(max_lenght=200)
    picture = models.ManyToManyField()
    text = models.TextField(photo)
    #localtion = models
    review = models.ManyToManyField(Reviews)

    def __str__(self):
        return self.BthName