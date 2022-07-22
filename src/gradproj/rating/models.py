from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class rating(models.Model):
    feedbackid=models.IntegerField(default="000",primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,max_length=100,)
    star_rating = models.IntegerField(max_length=5,default=5)
    feedback= models.CharField(max_length=500,default="good")