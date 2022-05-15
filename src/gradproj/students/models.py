from django.db import models

# Create your models here.
class user(models.Model):
    userid=models.IntegerField(primary_key=True,)
    userFirstName=models.TextField(max_length=10)
    userLastName=models.TextField(max_length=10)
    userResult=models.TextField(default="Not Taken The Test Yet")
    usersecresult=models.TextField(default="sec result")
    userthirdresult = models.TextField(default="third result")