from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id=models.IntegerField(default=000)
    question=models.TextField(default='')
    result=models.CharField(default="not taking test yet",max_length=70)