from django.db import models

# Create your models here.
class questions(models.Model):
    question_id=models.IntegerField(default=000)
    question=models.TextField(default='')
    result=models.DecimalField(decimal_places=2,max_digits=2,null=True,)