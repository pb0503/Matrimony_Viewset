from django.db import models

# Create your models here.
class Horoscope(models.Model):
    moon_sign=models.CharField(max_length=30)
    star=models.CharField(max_length=30)
    gotra=models.CharField(max_length=30)
    manglik=models.CharField(max_length=30)
    shani=models.CharField(max_length=30)
    horoscope_match=models.CharField(max_length=30)
    place_of_birth=models.CharField(max_length=30)
    place_of_country=models.CharField(max_length=30)
    hours=models.IntegerField()
    minutes=models.IntegerField()
    seconds=models.IntegerField()
    am_pm=models.CharField(max_length=30)
