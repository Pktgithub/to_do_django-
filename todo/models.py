from django.db import models
from django.utils import timezone


class Todolist(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class signupdata(models.Model):

    Name=models.CharField(max_length=100)
    Email=models.EmailField() 
    Password=models.CharField(max_length=100)  
    class Meta:
        db_table="userdata"


# Create your models here.
