from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    question_id=models.IntegerField(default=000)
    question=models.TextField(default='')
    Programming=models.CharField(default="white",max_length=70)
    Theory = models.CharField(default="white", max_length=70)
    Mathematical = models.CharField(default="white", max_length=70)