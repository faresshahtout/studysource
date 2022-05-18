from django.db import models

# Create your models here.
class rating(models.Model):
    user=models.CharField(max_length=100)
    star_rating = models.IntegerField(max_length=5,default=5)
    submission= models.CharField(max_length=500)