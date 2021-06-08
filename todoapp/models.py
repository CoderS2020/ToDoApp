from django.db import models
import datetime
import django.utils.timezone


# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200)
    # time=models.CharField(null=True,blank=True,max_length=100)
    time= models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title