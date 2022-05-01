from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id=models.IntegerField(default=000)
    question=models.TextField(default='')
    result=models.DecimalField(decimal_places=2,max_digits=2,null=True,)