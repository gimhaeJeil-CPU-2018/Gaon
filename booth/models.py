from django.db import models

# Create your models here.
class photo(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField()
    def __str__(self):
        return self.name

class Reviews(models.Model):
    auther = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    star = models.PositiveSmallIntegerField()
    text = models.TextField()
    def __str__(self):
        return self.auther

class BoothList(models.Model):
    auther = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    BthName = models.CharField(max_length=50)
    picture = models.ManyToManyField('photo',related_name='aa',blank=True)
    stxt = models.CharField(max_length=200)
    text = models.TextField()
    floor = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=30)
    review = models.ManyToManyField(Reviews,blank=True)

    def __str__(self):
        return self.BthName