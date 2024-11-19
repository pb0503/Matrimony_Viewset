from django.db import models

# Create your models here.
class CPPD(models.Model):
    looking_for=models.CharField(max_length=30)
    age_from=models.IntegerField()
    age_to=models.IntegerField()
    height_from=models.IntegerField()
    height_to=models.IntegerField()
    religon=models.CharField(max_length=30)
    caste=models.CharField(max_length=30)
    complexion=models.CharField(max_length=30)
    residency_status=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    education=models.CharField(max_length=30)
    occupation=models.CharField(max_length=30)
    partner_expectations=models.CharField(max_length=30)

