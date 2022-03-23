from django.db import models

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length=25)
    address = models.TextField(default="/404")
    tag=models.CharField(max_length=10,null=True)

class link(models.Model):
    coursetitle=models.ForeignKey(course,on_delete=models.CASCADE)
    courseLink=models.TextField()

