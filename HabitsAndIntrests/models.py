from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Habits(models.Model):
    sports=models.CharField(max_length=100)
    movie=models.CharField(max_length=100)
    books=models.CharField(max_length=100)
    travel=models.CharField(max_length=100)
    volenteerwork=models.CharField(max_length=100)
    cooking=models.CharField(max_length=100)
    music=models.CharField(max_length=100)
    writing=models.CharField(max_length=100)
   