from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=225)
    city=models.CharField(max_length=70)
    roll=models.IntegerField()
    status = models.CharField(max_length=70)