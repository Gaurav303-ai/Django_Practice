from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=225)
    city=models.CharField(max_length=70)
    roll=models.IntegerField()
    status = models.CharField(max_length=70)

    # def __str__(self):
    #     return self.name

    # another way

    # def __str__(self):    use this is want to see integer value
    #     return str(self.roll)