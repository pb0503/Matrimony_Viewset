from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Education(models.Model):
    qualification=models.CharField(max_length=30)
    occupation=models.CharField(max_length=30)
    occupation_details=models.CharField(max_length=30)
    annual_income=models.IntegerField()
    employed_in=models.CharField(max_length=30)
    working_locations=models.TextField()